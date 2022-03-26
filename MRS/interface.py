import ctypes
from typing import List

from .sensor import IR_Sensor
from .cls import _Robot_Unit


class Interface:
    def __init__(self, user_code_path: str) -> None:
        self.lib = ctypes.CDLL( user_code_path )

    def __call__(
        self,
        robot: _Robot_Unit,
        sensors: List[IR_Sensor],
        viewer: bool = False
    ):
        '''
            Transfer data(robot, sensor) to user C++ code.
            ---
                Transfer data to C++ code
                    - 6 inputs
                    - current_pos (x, y), target_pos (x, y), robot_head (int), sensor data
                    - sensor data = sensor[0] * 100 + sensor[1] * 10 + sensor[2]

                Returns from C++ code
                    - 1 output
                    - Integer type
                    - robot_head(int), robot_new_x(int), robot_new_y(int)
                    - robot_head * 100 + robot_new_x * 10 + robot_new_y
        '''
        # Compose the current values.
        cur_pos = robot.cur_pos
        tar_pos = robot.tar_pos

        sensor_data = 0
        for i, sensor in enumerate(sensors):
            sensor_data += sensor.is_detect * ( 10 ** i )

        if viewer:
            print(
                f"[Send] head: {robot.head}, sensor: {sensor_data}, current: {cur_pos}, target: {tar_pos}"
            )

        # Computation in C++ code.
        rtn = self.lib.algorithm(
            cur_pos.x, cur_pos.y,
            tar_pos.x, tar_pos.y,
            robot.head, sensor_data
        )

        # Analyze the value of C++ code return.
        _head = rtn - (rtn % 100)
        head = int(_head / 100)
        _robot_x = (rtn - head * 100) - ((rtn - head * 100) % 10)
        robot_x = int(_robot_x / 10)
        robot_y = (rtn - head * 100 - robot_x * 10)

        # Return to simulator.
        return head, robot_x, robot_y



