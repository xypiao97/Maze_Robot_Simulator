from typing import Any, List, Optional

from .utils import ConfigParser
from .simul_map import Simul_Map, Representation_Map
from .robot import Robot

class Simulator:
    def __init__(
        self,
        config_path: str,
        user_code_path: str = None
    ) -> None:
        '''
            Configuration of toml file
            ---
                [obstacle]
                    x=[2,5,1]
                    y=[1,2,3]
                [size]
                    x=10
                    y=10
                [robot]
                    x=0
                    y=0
        '''
        self.user_code_path = user_code_path

        self.config = ConfigParser.parse(config_path)
        obs_position = []
        for x, y in zip(self.config.data.obstacle.x, self.config.data.obstacle.y):
            obs_position.append( (x, y) )

        self.simul_map = Simul_Map( self.config.data.size.x, self.config.data.size.y, obs_position )
        self.robot = Robot( self.config.data.robot.x, self.config.data.robot.y, self.config.data.robot.num_sensor )
        self.epochs = self.config.data.sim.epoch

    def simulation(self):
        for e in range(self.epochs):
            self._epoch_simulation()

    def _epoch_simulation(self):
        current_map = self.simul_map.get_map_info(self.robot)
        Representation_Map.show( current_map )
        # new_x, new_y = self.robot.run(current_map)
        # self.simul_map.update( new_x, new_y )

