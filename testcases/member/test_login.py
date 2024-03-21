from operation.mock_login import MockLogin
from common.basic_enum import Code, Message
import pytest
import allure
from common.logger import logger
from common.read_testdata import get_testdata


@allure.epic("Member ")
@allure.feature("登入")
class TestLogin(object):
    login_data = get_testdata("login_data.yaml")

    @classmethod
    def setup_class(cls):
        # datas =
        cls.header = {}

    @allure.story('0001-一般使用者登入成功')
    @allure.title("驗證Api Response")
    @pytest.mark.parametrize("account, password", login_data["user"])
    def test_login(self, account, password):
        login = MockLogin()
        response = login.login()
        logger.info(f'asdadasasdfaddad{Message.Success.value}')
        # verify some result
        assert response["code"] == password
        assert response["code"] == account
        assert response["code"] == Code.Success.value
        assert response["massage"] == Message.Success.value

    @allure.story('0002-一般使用者登入失敗')
    @allure.title("驗dddd證Api Response")
    def test_loginssnm(self):
        from config.environment import global_environment
        # from dataclasses import asdict
        assert "1" == global_environment
