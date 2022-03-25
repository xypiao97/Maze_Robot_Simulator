import ctypes
from typing import List

from .sensor import IR_Sensor


class _Interface:
    def __init__(self, user_code_path: str) -> None:
        self.lib = ctypes.CDLL( user_code_path )

    def __call__(self, sensors: List[IR_Sensor]):
        return 0, 0, self.lib.algorithm(1, 3)



