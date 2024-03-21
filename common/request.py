import requests
from config.environment import get_domain
from config import environment


class Request(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.domain = get_domain()[environment.global_environment]["domain"]
        self.session = requests.Session()

    def post(self, api_url: str, header: dict = None, body: dict = None):
        return self.request(api_url=api_url, method="POST", header=header, body=body)

    def get(self, api_url: str, header: dict = None):
        return self.request(api_url=api_url, method="GET", header=header, body=None)

    def request(self, api_url: str, method: str, header: dict, body: dict = None):
        url = f"{self.domain}{api_url}"
        if method == "POST":
            return self.session.post(url=url, headers=header, json=body, timeout=3)
        else:
            return self.session.get(url=url, headers=header, timeout=3)


if __name__ == '__main__':
    test = Request()
    print(test.post(api_url="/asda", header={"asd": "asd"}, body={"asd": "asd"}))
