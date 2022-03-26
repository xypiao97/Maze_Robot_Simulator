class _Position:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class _Robot_Unit:
    head: int
    cur_pos: _Position
    tar_pos: _Position

    def __init__(
        self,
        x: int, y: int,
        target_x: int, target_y: int,
        head: int
    ) -> None:
        self.cur_pos = _Position( x, y )
        self.tar_pos = _Position( target_x, target_y )
        self.head = head