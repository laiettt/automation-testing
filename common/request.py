import requests
from config.environment import get_domain
from config import environment
from common.logger import logger
import json

global global_request


class Request(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.domain = get_domain()[environment.global_environment]["domain"]
        self.session = requests.Session()

    def post(self, api_url: str, header: dict = None, body: dict = None):
        return self.request(api_url=api_url, method="POST", header=header, body=body)

    def get(self, api_url: str, header: dict = None):
        return self.request(api_url=api_url, method="GET", header=header, body=None)

    def request(self, api_url: str, method: str, header: dict, body: dict = None):
        try:
            url = f"{self.domain}{api_url}"
            if method == "POST":
                request_log(api_url=api_url, url=url, method="POST", header=header, body=body)
                response = self.session.post(url=url, headers=header, json=body, timeout=3)
            else:
                request_log(url=url, method="GET", header=header, body=body)
                response = self.session.get(url=url, headers=header, timeout=3)
            logger.info(f'Response: {response}')
            return response

        except Exception as e:
            logger.error(f'{e}')
            raise Exception


def request_log(**kwargs):
    logger.info(json.dumps(kwargs, indent=4))

