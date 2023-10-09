from api.mock_step_api import mock_login_step1_api, mock_login_step2_api
from pydantic import BaseModel


class MockLogin(BaseModel):
    mock_step1_header: dict = None
    mock_step1_body: dict = None
    mock_step2_header: dict = None

    def set_data(self, mock_step1_header: dict, mock_step1_body: dict, mock_step2_header: dict):
        self.mock_step1_header = mock_step1_header
        self.mock_step1_body = mock_step1_body
        self.mock_step2_header = mock_step2_header

    def login(self):
        # step1_response = mock_login_step1_api(header=self.mock_step1_header, body=self.mock_step1_body)
        # step1_response = "Maybe had some data need to insert  step2's header"
        # step2_response = mock_login_step2_api(header=self.mock_step2_header)
        # return step2_response
        return {"code": "0000", "message": "成功"}
