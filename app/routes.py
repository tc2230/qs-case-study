import io
import json
import random
import datetime
import traceback
from PIL import Image
from app.forms import ImageDimension
from app.logger import setup_logger, send_ga_record
from flask import Blueprint, send_file, request, abort, Response

routes = Blueprint('routes', __name__)
logger = setup_logger()

@routes.after_request
def log_expected_response(response):
    log_entry = {
        'severity': 'INFO',
        'remote_addr': request.remote_addr, 
        'protocol': request.scheme, 
        'request': {
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
            'method': request.method, 
            'path': request.path, 
            'url': request.url, 
            'headers': dict(request.headers), 
            'body': request.get_data().decode('utf-8'),
        }, 
        'response': {
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
            'status_code': response.status_code,
            'content_length': response.content_length, 
            'content_type': response.content_type, 
        }
    }
    # google cloud logginf
    logger.log_struct(log_entry)
    
    # GA measurement protocol
    payload = {
        "client_id": "taylor.fu.dev",
        "events": [
            {
                "name": "test-event",
                "params": {
                    "event_id": "google_1234",
                    "campaign": "Summer_fun",
                    "source": "dev",
                    "term": "api+png",
                    "content": "image",
                    "session_id": "123",
                }
            },
        ]
    }

    ga_response = send_ga_record(payload)
    if ga_response.status_code != 200:
        log_entry = {
            'severity': 'WARNING',
            'ga_response': {
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                'status_code': ga_response.status_code,
            }
        }
        logger.log_struct(log_entry)
    return response

@routes.route('/generate_png', methods=['GET'])
def generate_png():
    # data validation
    data = ImageDimension(request.args, meta={'csrf': False})
    if data.validate():
        width = data.width.data
        height = data.height.data
    else:
        dict_error = {}
        for field, errors in data.errors.items():
            for error in errors:
                dict_error.update({field: error})
        abort(Response(json.dumps(dict_error), 400))
        
    # create random-colored image
    try:
        img = Image.new('RGB', (width, height), tuple(random.choices(range(256), k=4)))
        img_io = io.BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        logger.log_struct({
            'severity': 'ERROR', 
            "detail": ''.join(traceback.format_exception(type(e), e, e.__traceback__))
            })
        abort(Response('internal server error', 500))