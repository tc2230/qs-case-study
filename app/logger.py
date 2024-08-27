import os
import json
import requests
from google.cloud import logging

measurement_id = os.environ['MEASUREMENT_ID']
api_secret = os.environ['API_SECRET']

def setup_logger():
    client = logging.Client.from_service_account_json('gcp_logging_key.json')
    client.setup_logging()
    logger = client.logger('flask-app-logger')
    
    return logger

def send_ga_record(payload):
    url = f'https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}'

    response = requests.post(url, data=json.dumps(payload), verify=True)

    return response