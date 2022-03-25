from typing import Any, List, Optional


class _Environment:
    map_x: int
    map_y: int

    sim_map: List
    
    def __init__(
        self,
        x_axis: Optional[int] = None,
        y_axis: Optional[int] = None,
        map_config: Optional[Any] = None
    ) -> None:
        if x_axis == None or y_axis == None:
            raise ValueError(
                "[MAP ERROR] Check the size of virtual environment map for simulation your c++ code!!"
                )

        self.map_x = x_axis
        self.map_y = y_axis

        if map_config == None:
            self._config_random_map()
        else:
            self._config_map( map_config )

    def _config_random_map():
        
        pass

    def _config_map( map_config: Any ):
        pass

