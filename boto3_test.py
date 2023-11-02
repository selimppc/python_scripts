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
API_ENDPOINT = 'https://api.bongo-solutions.com/agency/v1/activate/package'
HEADERS = {
    'Access-Code': 'QkQ%3D',
    'Content-Type': 'application/json',
    # prod =>
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJBTlRNQU4iLCJpYXQiOjE2OTIxNjcyMjQuMjE2NzkyOCwiZXhwIjoxOTA4MTY3MjI0LjIxNjc5MjgsImNsaWVudF9pZCI6IjJkZjA0NDZmMzViOTQ1Zjc4ZTQ5YzdhOWY0NGFiYjVhIiwiY2xpZW50X3R5cGUiOiJpbnRlcm5hbF9jbGllbnRfZmFjaW5nX2FwcCIsInNjb3BlIjoiZGlnaWFjeS5wYWNrYWdlLmxpc3QsZGlnaWFjeS5wYWNrYWdlLmFjdGl2YXRlIiwiZGF0YSI6e319.YyyeLVoCYglnRHLv7Lj5O8JksKuutPbt-Hxs2snie0zIb7Qs_HIDge6ZEZQBGLkcpHmD8kpqGWupraRlLYLqCCEgwfvoSzakt5tUNQERWr7Dtb40wys7V5leK-QCD9R9v7Rfgn1anxyb4IzgoHb4ydLw6I9ABqOXMRuXhML_t3O3DHxku6fzaq-9usE1Qi_s_wMs2gJvcV3HTwTtkFi9OGXy5XAUyganxUcSG9p5vi1965aqikyVrs_xvwi0q9LPpWCQKiWKhA6cpcIvjzMFULp1eW_wE1p5RqIKrM7kUIo0U4k6Nx2iBKMT3ggR8I3JdYYvLfuvUtpU-iU64OkVJg',  # noqa
    # Stage =>
    #'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJBTlRNQU4iLCJpYXQiOjE2OTc5NTc4NDcuMjM0NjIwNiwiZXhwIjoxOTEzOTU3ODQ3LjIzNDYyMDYsImNsaWVudF9pZCI6ImE4ZGI2M2UxMmZjOTRjNWJiZDQ5MjVmZTMwNmE2ZjI0IiwiY2xpZW50X3R5cGUiOiJpbnRlcm5hbF9jbGllbnRfZmFjaW5nX2FwcCIsInNjb3BlIjoiZGlnaWFjeS5wYWNrYWdlLmxpc3QsZGlnaWFjeS5wYWNrYWdlLmFjdGl2YXRlIiwiZGF0YSI6e319.WtMd89GRJwf1uVRnIeDJDC7R6_ajKIkp0ikDkezWoV5Aacv8TVu3aZIztJHqdrnHKC3HIk7ph-OU8F9pex_TAJXQQxs5z9VdYNbAyw_39zUIsAJU_R75J1P7Ss3qvdXVKTh9f4zo3t1_Q8ryJYOo0oKYxawOleHWgO-S7BHTVgCWRTlc81pq_116eiC1wKAe5o-L_gHFcVoKjXMi9AUITm-BmnaauBuLVTwNhC-ZiabJS_vXGfknP3dAl3h7LlDB11ZNvyIO1cZwYyp1j1ytoLPRjD1QnqJKqeksdqGPPUVdVF6KaB36dympxZKoShT2T6EajzP9DoCXkZBo2aO4zQ',  # noqa
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
