from math import inf
from typing import List

from .interface import Interface
from .utils.types import *
from .sensor import IR_Sensor
from .cls import _Robot_Unit


class Robot(_Robot_Unit):
    num_sensor: int
    sensors: List[IR_Sensor]
    interfacing: Interface

    def __init__(
        self,
        x: int, y: int,
        target_x: int, target_y: int,
        num_sensor: int = 3, user_code_path: str = None
    ) -> None:
        super().__init__(x, y, target_x, target_y, RIGHT)
        self.sensors = [ IR_Sensor(dir) for dir in range(num_sensor) ]
        self.num_sensor = num_sensor
        self.interfacing = Interface(user_code_path)

    def run(self, near_map: List, viewer: bool = False):
        '''
            Near map size: (3 by 3) or (3 by 2) or (2 by 2)
            ---
                +-----+-----+-----+
                |  0  | inf | inf |
                +-----+-----+-----+
                |  0  | xf  |  0  |
                +-----+-----+-----+
                | inf |  0  | inf |
                +-----+-----+-----+
        '''

        # Update sensor data
        for sensor in self.sensors:
            sensor(self, near_map)

        # Communication C++ code
        _new_robot_head, _new_robot_x, _new_robot_y = self.interfacing( self, self.sensors, viewer )
        if viewer:
            print( f"[Recv] head: {_new_robot_head}, new robot pos: ({_new_robot_x}, {_new_robot_y})" )
        self.head = _new_robot_head

        return _new_robot_x, _new_robot_y