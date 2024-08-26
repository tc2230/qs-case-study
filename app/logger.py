from google.cloud import logging

def setup_logger():
    client = logging.Client.from_service_account_json('app/gcp_logging_key.json')
    client.setup_logging()
    logger = client.logger('flask-app-logger')
    
    return logger