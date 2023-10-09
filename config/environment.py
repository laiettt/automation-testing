import os
from common.read_data import read_yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_domain(yaml_path: str = "/config/environment.yaml") -> dict:
    domain = read_yaml(file_path=f"{BASE_PATH}{yaml_path}")
    return domain


if __name__ == '__main__':
    print(get_domain())
