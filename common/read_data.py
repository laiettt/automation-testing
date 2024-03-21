import yaml
from common.logger import logger


def read_yaml(file_path: str) -> dict:
    try:
        logger.info(f'---File Path: {file_path}---')
        with open(file_path, encoding="utf-8") as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f'---Read Yaml Result: {data}---')
        return data
    except Exception as e:
        logger.error(f'{e}')
        raise Exception
