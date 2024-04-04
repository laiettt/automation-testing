from enum import Enum


class Code(Enum):
    Success = "0000"
    Error = "1000"


class Message(Enum):
    Success = "成功"
    Error = "失敗"
    Timeout = "timeout"
