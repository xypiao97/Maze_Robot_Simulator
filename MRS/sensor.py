from typing import List

from .cls import _Robot_Unit
from .utils.types import (
    RIGHT,
    FORWARD,
    blocked,
    detected,
    non_detected
)


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
        self.is_detect = detected if simul_map[pos[1]][pos[0]] == blocked else non_detected

