import pytest
from config import environment
from common.logger import logger
from common import request as request_module
from api import mock_step_api


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="sit",
        choices=["sit", "uat"],
        help="test environment, choice is sit and uat, default is sit"
    )


@pytest.fixture(scope="session", autouse=True)
def init():
    logger.info(f'------Test Start------')
    yield
    logger.info(f'------Test End------')


@pytest.fixture(scope='session', autouse=True)
def get_environment(init, request) -> str:
    try:
        environment_parameter = request.config.getoption("--env")
        environment.global_environment = environment_parameter
        logger.info(f'---Set Test Environment: {environment_parameter}---')
        return environment_parameter
    except Exception as e:
        logger.error(f'{e}')
        raise Exception


# @pytest.fixture(scope="class")
# def setup_headers():
#     logger.info(f'取得token並回塞header--------')
    # yield
    # logger.info(f'結束etup_token')


@pytest.fixture(scope="session", autouse=True)
def request_fixture():
    try:
        logger.info(f'---Create Request Session---')
        request_module.global_request = request_module.Request()
        mock_step_api.request = request_module.global_request
        logger.info(f'---Create Request Session Success---')
    except Exception as e:
        logger.error(f'{e}')
        raise Exception


# @pytest.fixture(scope="function", autouse=True)
# def say_hiiiii():
#     logger.error(f'開始-最外層的conftest--------')
#     yield
#     logger.error(f'結束-最外層的conftest')
