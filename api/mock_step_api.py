from common.logger import logger

global request


def mock_login_step1_api(header: dict, body: dict):
    try:
        api_url = "/qa/api/member/login"
        return request.post(api_url=api_url, header=header, body=body)
    except Exception as e:
        logger.error(f'{e}')
        raise Exception

