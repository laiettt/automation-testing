from common import request as request_package

request = request_package.Request()


def mock_login_step1_api(header: dict, body: dict):
    api_url = "/mock/login_step1_api"
    return request.post(api_url=api_url, header=header, body=body)


def mock_login_step2_api(header: dict):
    api_url = "/mock/login_step2_api"
    return request.get(api_url=api_url, header=header)
