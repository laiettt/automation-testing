import logging
import os
from functools import wraps
from datetime import datetime
import inspect

BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')


class Logger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger('logger')
        self.level = logging.INFO
        self.logger.setLevel(level=self.level)
        self.formatter = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s', datefmt="%Y-%m-%d %H:%M:%S")

    @staticmethod
    def log_file_handler_check(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):  # 類別裡的裝飾器要多self參數來放
            current_time = datetime.now()
            log_name = current_time.strftime("%H00")
            folder_name = current_time.strftime("%Y-%m-%d")
            folder_path = os.path.join(BASE_PATH, folder_name)
            log_path = f"{folder_path}/{log_name}.log"
            os.makedirs(folder_path, exist_ok=True)  # 若不存在就建立
            if self.logger.handlers:  # 若為初始化 handlers.list為空則不remove
                self.logger.removeHandler(self.logger.handlers[0])
            self.file_handler = logging.FileHandler(log_path, encoding='utf-8')
            self.file_handler.setLevel(level=self.level)
            self.file_handler.setFormatter(fmt=self.formatter)
            self.logger.addHandler(self.file_handler)
            func(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def get_caller(func):
        def wrapper(*args):
            frame = inspect.currentframe().f_back  # 找回誰Call這支function
            file_path = frame.f_code.co_filename
            file_name = os.path.basename(file_path)
            lineno = frame.f_lineno
            args = list(args)
            args.append(f'{file_name}:{lineno}')
            func(*args)
        return wrapper

    @get_caller
    @log_file_handler_check
    def info(self, message: str, caller='') -> None:
        self.logger.info(f'[{caller}] {message}')

    @get_caller
    @log_file_handler_check
    def error(self, message: str, caller='') -> None:
        self.logger.error(f'[{caller}] {message}')


logger = Logger()
