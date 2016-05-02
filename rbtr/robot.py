import numpy as np


class Robot():
    def __init__(self, table):
        self._table = table

    def place(self, x_coordinate, y_coordinate, facing):
        if self._table.is_safe(x_coordinate=x_coordinate, y_coordinate=y_coordinate):
            self._current_position = np.array([x_coordinate, y_coordinate])
            self._current_facing = facing

    def report(self):
        return "X: {}, Y: {}, F: {}".format(
            self._current_position[0], self._current_position[1], self._current_facing
        )

    def move(self):
        prospective_position = self._current_position + _direction_vectors[self._current_facing]
        if self._table.is_safe(x_coordinate=prospective_position[0],
                               y_coordinate=prospective_position[1]):
            self._current_position = prospective_position
        else:
            print('Prospective position (X: {}, Y: {}) is unsafe. Refusing to move.'.format(
                  prospective_position[0], prospective_position[1]))


_direction_vectors = {
    'NORTH': np.array([0, 1]),
    'EAST': np.array([1, 0]),
    'SOUTH': np.array([0, -1]),
    'WEST': np.array([-1, 0])
}
