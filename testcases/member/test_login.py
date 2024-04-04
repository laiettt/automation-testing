from operation.mock_login import Login
from common.basic_enum import Code, Message
import pytest
import allure
from common.logger import logger
from common.read_testdata import get_testdata
from common import testcase_id
from pytest_mock import MockFixture


@allure.epic("Member ")
@allure.feature("登入")
class TestLogin(object):
    login_data = get_testdata("login_data.yaml")
    story_id = testcase_id.get_story_id()

    # @classmethod
    # def setup_class(cls):
    #     logger.info("setup_class 開始。。。")
    #
    # @classmethod
    # def setup_method(cls):
    #     logger.info("setup_method 開始。。。")
    #
    # @classmethod
    # def teardown_method(cls):
    #     logger.info("setup_method 結束。。。")
    #
    # @classmethod
    # def teardown_class(cls):
    #     logger.info("teardown_class 結束。。。")

    @allure.story(f'{next(story_id)}使用者登入成功')
    @allure.title('{title}')
    @pytest.mark.parametrize("account, password, title", login_data["user_success"])
    def test_login_success(self, account, password, title):
        login = Login(account=account, password=password)
        response = login.login()
        assert response["code"] == Code.Success.value
        assert response["message"] == Message.Success.value

    @allure.story(f'{next(story_id)}登入Timeout(Mock)')
    @allure.title('{title}')
    @pytest.mark.parametrize("account, password, title", login_data["user_success"])
    def test_timeout_mock(self, account, password, title, mocker: MockFixture):
        login = Login(account=account, password=password)
        mock_response = {"code": '0000', "message": 'timeout'}
        mocker.patch(target='operation.mock_login.Login.login',
                     return_value=mock_response)
        response = login.login()
        assert response["code"] == Code.Success.value
        assert response["message"] == Message.Timeout.value

    @allure.story(f'{next(story_id)}使用者登入失敗')
    @allure.title('{title}')
    @pytest.mark.parametrize("account, password, title", login_data["user_failed"])
    def test_login_failed(self, account, password, title):
        assert 1 == 1
