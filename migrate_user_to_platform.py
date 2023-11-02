"""
User migration from CSV to Digital Agency
"""
import csv
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

# Setup logging
logging.basicConfig(filename='api_requests.log', level=logging.INFO)
logger = logging.getLogger()

# API endpoint and headers
API_ENDPOINT = 'https://api.dev.bongo-solutions.com/agency/v1/activate/package'
HEADERS = {
    'Access-Code': 'QkQ%3D',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <TOKEN>',  # noqa
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}
CSV_FILE = 'csv/error_oct_24_2023.csv'


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


def send_request(user_msisdn, package_code, expiry):
    data = {
        "agent_id": "",
        "agent_msisdn": "",
        "code": package_code,
        "user_msisdn": user_msisdn,
        "platform": "bioscope",
        "is_recurring": False,
        "source": "gp",
        "expiry": expiry,
    }

    try:
        response = requests.post(
            API_ENDPOINT,
            headers=HEADERS,
            json=data,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        logger.error(f'TIMEOUT_ERROR:: for {user_msisdn}-{package_code}-{expiry}')
    except requests.HTTPError as http_err:
        logger.error(f'HTTP_ERROR:: for {user_msisdn}-{package_code}-{expiry}: {http_err}')
    except Exception as err:
        logger.error(f'ERROR:: for {user_msisdn}-{package_code}-{expiry}: {err}')


def main():
    for row in read_csv(CSV_FILE):
        user_msisdn = row.get('user_msisdn')
        package_code = row.get('package_code')
        expiry = row.get('end_date')
        if user_msisdn and package_code and expiry:
            response = send_request(
                user_msisdn=user_msisdn, package_code=package_code, expiry=expiry
            )
            if response:
                logger.info(
                    f"SUCCESS:: {user_msisdn}::{package_code}::{expiry}"
                )
            else:
                logger.warning(
                    f"FAILED:: {user_msisdn}::{package_code}::{expiry}"
                )
        else:
            logger.warning(
                f"MISSING_DATA:: in row: {row}"
            )


if __name__ == '__main__':
    main()
