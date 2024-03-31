from common.read_data import read_yaml
import os
from common.logger import logger


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_testdata(yaml_file_name: str):
    logger.info(f'---Ready To Get Testdata---')
    data = read_yaml(file_path=f"{BASE_PATH}/testdata/{yaml_file_name}")
    return data
