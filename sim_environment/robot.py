from math import inf
from typing import List

from interface import _Interface


detected: int = inf
non_detected: int = 0

FORWARD = 0
LEFT = 1
RIGHT = 2
BACKWARD = 3


class _Robot_Unit:
    x: int
    y: int
    head: int


class IR_Sensor:
    '''
        IR Sensor
        ---

            if FORWARD or LEFT:
                F(0,-1)<-[-1,-1]<-R(1,0)
                    |               ^
                    v               |
                [-1,+1]          [1,-1]
                    |               ^
                    v               |
                L(-1,0)->[1,1]->B(0,1)

            else if RIGHT:
                F(0,-1)->[1,1]->R(1,0)
                    ^               |
                    |               V
                [+1,-1]          [+1,1]
                    ^               |
                    |               V
                L(-1,0)<-[-1,-1]<-B(0,1)
    '''
    is_detect: int 
    direction: int

    _fw = (0, -1)
    _bw = (0, +1)
    _le = (-1, 0)
    _ri = (+1, 0)
    _dir_values = [ _fw, _le, _ri, _bw ]
    _dir_factor = [
        [-1,+1],
        [+1,+1],
        [+1,-1],
        [-1,-1]
    ]

    def __init__(self, dir: int) -> None:
        self.direction = dir
        if dir == RIGHT:
            for i, factor in enumerate(self._dir_factor):
                self._dir_factor[i] = [ factor[0] * -1, factor[1] * -1 ]

    def __call__(self, robot: _Robot_Unit, simul_map: List):
        _dir_value = self._dir_values[robot.head]
        if self.direction != FORWARD:
            _dir_factor = self._dir_factor[self.direction]
        else:
            _dir_factor = [0, 0]

        pos = [ (_dir_factor[0] + _dir_value[0]), (_dir_factor[1] + _dir_value[1]) ]
        self.is_detect = simul_map[pos[1]][pos[0]]


class Robot(_Robot_Unit):
    num_sensor: int
    sensors: List[IR_Sensor]
    interfacing: _Interface

    def __init__(self, x: int, y: int, num_sensor: int = 3) -> None:
        super().__init__()
        self.x = x
        self.y = y

        self.sensors = [ IR_Sensor(dir) for dir in range(num_sensor) ]
        self.num_sensor = num_sensor

        self.head = FORWARD
        self.interfacing = _Interface()

    def run(self, near_map: List):
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
            sensor(self.head, near_map)

        # Communication C++ code
        _new_robot_head, _new_robot_x, _new_robot_y = self.interfacing()
        self.head = _new_robot_head

        return _new_robot_x, _new_robot_y