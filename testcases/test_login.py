from operation.mock_login import MockLogin
from common.basic_enum import Code, Message
import pytest
import allure
from testcases.conftest import get_testdata


@allure.feature("登入")
class TestLogin(object):
    login_data = get_testdata("login_data.yaml")

    @classmethod
    def setup_class(cls):
        cls.header = {}

    @allure.title("驗證Api Response")
    @pytest.mark.parametrize("account, password", login_data["user"])
    def test_login(self, account, password):
        login = MockLogin()
        response = login.login()
        # verify some result
        assert response["code"] == password
        assert response["code"] == account
        assert response["code"] == Code.Success.value
        assert response["massage"] == Message.Success.value
