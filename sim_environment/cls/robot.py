from math import inf
from typing import List

detected: int = inf
non_detected: int = 0

FORWARD = 0
LEFT = 1
RIGHT = 2
BACKWARD = 3


class _Interface:
    def __init__(self) -> None:
        pass


class IR_Sensor:
    is_detect: int 
    direction: int

    def __init__(self, dir: int) -> None:
        self.direction = dir

    def __call__(self, robot, simul_map: List):
        if robot.head == self.direction:
            x_pos = 
        self.is_detect = simul_map[y_pos][x_pos]


class Robot:
    x: int
    y: int
    num_sensor: int
    sensors: List[IR_Sensor]
    head: int
    interfacing: _Interface

    def __init__(self, x: int, y: int, num_sensor: int = 3) -> None:
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