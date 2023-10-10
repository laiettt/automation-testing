from common.read_data import read_yaml
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_testdata(yaml_file_name: str):
    data = read_yaml(file_path=f"{BASE_PATH}/testdata/{yaml_file_name}")
    return data
