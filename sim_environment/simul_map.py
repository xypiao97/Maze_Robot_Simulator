from math import inf
from turtle import pos
from typing import Any, List, Optional
import random

from .robot import Robot


blocked: int = inf
non_blocked: int = 0
robot_pos: int = 82


class _Map:
    x_size: int
    y_size: int
    blocks: List[List[int]]
    total_blocks: int
    obstacles: int

    user: Robot

    def __init__(
        self,
        x_axis: int = 10, y_axis: int = 10,
        config_file: Optional[List] = None
    ) -> None:
        self.x_size = x_axis
        self.y_size = y_axis
        self.total_blocks = x_axis * y_axis
        self.blocks = []

        _pos_x = [ i for i in range(self.x_size) ]
        _pos_y = [ i for i in range(self.y_size) ]
        if config_file == None:
            self._apply_random(_pos_x, _pos_y)
        else:
            self.obstacles = len(config_file)
            self._apply_config(config_file)

    def _apply_random(self, pos_x: List, pos_y: List):
        self.obstacles = random.randrange( 
            start=int(self.total_blocks / 10),
            stop=int(self.total_blocks / 4)
        )
        _obstacles_pos = []
        # To avoid the position of obstacle and user's robot being the same. 
        del pos_x[0]
        del pos_y[0]

        # Create new position of obstacles.
        for _ in range(self.obstacles):
            _obs_x = random.choice(pos_x)
            _obs_y = random.choice(pos_y)
            while (_obs_x, _obs_y) in _obstacles_pos:
                _obs_x = random.choice(pos_x)
                _obs_y = random.choice(pos_y)
            _obstacles_pos.append( (_obs_x, _obs_y) )

        # Create simulation map.
        for y in range(self.y_size):
            self.blocks.append( [] )
            for x in range(self.x_size):
                if (x, y) in _obstacles_pos:
                    _new_blocks = blocked
                else:
                    _new_blocks = non_blocked
                self.blocks[y].append( _new_blocks )

    def _apply_config(self, obs_position: List):
        for y in range(self.y_size):
            self.blocks.append( [] )
            for x in range(self.x_size):
                if (x, y) in obs_position:
                    _new_blocks = blocked
                else:
                    _new_blocks = non_blocked
                self.blocks[y].append( _new_blocks )


class Simul_Map(_Map):
    pre_robot_x: int
    pre_robot_y: int

    def __init__(self, x_axis, y_axis, obs_pos) -> None:
        super().__init__(x_axis, y_axis, obs_pos)

    def init_update(self, robot: Robot):
        self.blocks[robot.y][robot.x] = robot_pos

    def get_map_info(self, robot: Robot):
        self.pre_robot_x = robot.x
        self.pre_robot_y = robot.y
        near_map = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

        for y in range(3):
            _y = y - 1
            for x in range(3):
                _x = x - 1
                try:
                    near_map[y][x] = self.blocks[robot.y + _y][robot.x + _x]
                    if robot.x + _x < 0:
                        near_map[y][x] = blocked
                    elif robot.y + _y < 0:
                        near_map[y][x] = blocked
                except IndexError:
                    near_map[y][x] = blocked
        return near_map

    def update(self, new_robot_x: int, new_robot_y: int):
        self.blocks[self.pre_robot_y][self.pre_robot_x] = non_blocked
        self.blocks[new_robot_y][new_robot_x] = robot_pos

