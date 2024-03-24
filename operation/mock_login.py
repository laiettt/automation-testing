from api.mock_step_api import mock_login_step1_api
from dataclasses import dataclass
from common.logger import logger


@dataclass
class Login(object):
    account: str
    password: int

    def __post_init__(self) -> None:
        self.header = {}
        self.body = {'account': self.account,
                     'password': self.password,
                     }

    def login(self) -> dict:
        response = mock_login_step1_api(header=self.header, body=self.body).json()
        logger.info(f'Response: {response}')
        return response
