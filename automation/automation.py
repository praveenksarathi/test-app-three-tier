import requests
import time
import logging
import os

logging.basicConfig(level=logging.INFO)

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000")
DATA_ENDPOINT = f"{BACKEND_URL}/data"

def write_data():
    payload = {"name": "test", "value": "123"}
    try:
        response = requests.post(DATA_ENDPOINT, json=payload)
        logging.info(f"Write: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Write failed: {e}")

def read_data():
    try:
        response = requests.get(DATA_ENDPOINT)
        logging.info(f"Read: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Read failed: {e}")

def delete_data():
    try:
        response = requests.delete(DATA_ENDPOINT)
        logging.info(f"Delete: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Delete failed: {e}")

if __name__ == "__main__":
    while True:
        write_data()
        time.sleep(2)
        read_data()
        time.sleep(2)
        delete_data()
        time.sleep(5)
