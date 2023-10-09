import yaml


def read_yaml(file_path: str) -> dict:
    with open(file_path, encoding="utf-8") as yaml_file:
        data = yaml.safe_load(yaml_file)
    return data
