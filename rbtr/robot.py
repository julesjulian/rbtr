class Robot():
    def __init__(self, table):
        self._table = table

    def place(self, x_coordinate, y_coordinate, facing):
        if self._table.is_safe(x_coordinate=x_coordinate, y_coordinate=y_coordinate):
            self._current_x = x_coordinate
            self._current_y = y_coordinate
            self._current_facing = facing

    def report(self):
        return "X: {}, Y: {}, F: {}".format(self._current_x, self._current_y, self._current_facing)
