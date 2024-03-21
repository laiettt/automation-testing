import pytest
from config import environment
from common.logger import logger
from common.request import Request


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
        Request()
        logger.info(f'---Create Request Session Success---')
    except Exception as e:
        logger.error(f'{e}')
        raise Exception


