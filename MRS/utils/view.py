from typing import List

from .types import (
    robot_pos,
    blocked,
    non_blocked
)

expr_design = {
    'robot':        '⚉',
    'detected':     '.',
    'obstacle':     '🁢',
}


class _Representation:
    @classmethod
    def show_value(cls, epoch:int, near_map: List):
        print("-" * 10, f"[Epoch: {epoch+1}]", "-" * 10)
        for col in near_map:
            print(col)
        print("-" * 32)


class Representation_Map(_Representation):
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def show(cls, epoch:int, near_map: List):
        print("-" * 10, f"[Epoch: {epoch+1}]", "-" * 10)
        for col in near_map:
            for blk in col:
                if blk == robot_pos:
                    print(expr_design['robot'], end="")
                elif blk == blocked:
                    print(expr_design['obstacle'], end="")
                else:
                    print(expr_design['detected'], end="")
            print()
        print("-" * 32)