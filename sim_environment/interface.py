import ctypes
from typing import List

from .sensor import IR_Sensor


class Interface:
    def __init__(self, user_code_path: str) -> None:
        self.lib = ctypes.CDLL( user_code_path )

    def __call__(self, sensors: List[IR_Sensor]):
        rtn = self.lib.algorithm(1, 3)
        _head = rtn - (rtn % 100)
        head = int(_head / 100)
        _robot_x = (rtn - head * 100) - ((rtn - head * 100) % 10)
        robot_x = int(_robot_x / 10)
        robot_y = (rtn - head * 100 - robot_x * 10)
        return head, robot_x, robot_y



