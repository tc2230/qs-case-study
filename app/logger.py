import os
# import dotenv
import request
from google.cloud import logging

dotenv.loads('.env')

measurement_id = os.environ['MEASUREMENT_ID']
api_secret = os.environ['API_SECRET']


def setup_logger():
    client = logging.Client.from_service_account_json('app/gcp_logging_key.json')
    client.setup_logging()
    logger = client.logger('flask-app-logger')
    
    return logger

def send_ga_record(payload):
    # measurement_id = os.environ['MEASUREMENT_ID']
    # api_secret = os.environ['API_SECRET']

    url = f'https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}'

    response = requests.post(url, data=json.dumps(payload), verify=True)

    return response