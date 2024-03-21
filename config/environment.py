import os
from common.read_data import read_yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
global global_environment


def get_domain(yaml_path: str = "/config/environment.yaml") -> dict:
    domain = read_yaml(file_path=f"{BASE_PATH}{yaml_path}")
    return domain
