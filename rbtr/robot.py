import numpy as np

_DIRECTION_VECTORS = {
    'NORTH': np.array([0, 1]),
    'EAST': np.array([1, 0]),
    'SOUTH': np.array([0, -1]),
    'WEST': np.array([-1, 0])
}
_ROTATION_MATRIX_90DEG_LEFT = np.array([[0, -1], [1, 0]])
_ROTATION_MATRIX_90DEG_RIGHT = np.array([[0, 1], [-1, 0]])


class Robot():
    def __init__(self, table):
        self._table = table
        self._current_position = np.array([None, None])
        self._current_facing = None

    @property
    def current_x(self):
        return self._current_position[0]

    @property
    def current_y(self):
        return self._current_position[1]

    @property
    def current_facing(self):
        return _direction_string(self._current_facing)

    def place(self, x_coordinate, y_coordinate, facing):
        if self._table.is_safe(x_coordinate=x_coordinate, y_coordinate=y_coordinate):
            self._current_position = np.array([x_coordinate, y_coordinate])
            self._current_facing = _DIRECTION_VECTORS[facing]

    def report(self):
        return "X: {}, Y: {}, F: {}".format(
            self._current_position[0],
            self._current_position[1],
            _direction_string(self._current_facing)
        )

    def move(self):
        self._refuse_before_placement()
        prospective_position = self._current_position + self._current_facing
        if self._table.is_safe(x_coordinate=prospective_position[0],
                               y_coordinate=prospective_position[1]):
            self._current_position = prospective_position
        else:
            print('Prospective position (X: {}, Y: {}) is unsafe. Refusing to move.'.format(
                  prospective_position[0], prospective_position[1]))

    def left(self):
        self._refuse_before_placement()
        self._current_facing = np.dot(_ROTATION_MATRIX_90DEG_LEFT, self._current_facing)

    def right(self):
        self._refuse_before_placement()
        self._current_facing = np.dot(_ROTATION_MATRIX_90DEG_RIGHT, self._current_facing)

    def _refuse_before_placement(self):
        if (self._current_facing is None):
            raise ValueError("Must receive 'PLACE' command before other commands can be accepted.")


def _direction_string(direction_vector):
    if direction_vector is None:
        return None
    for k in _DIRECTION_VECTORS:
        if (_DIRECTION_VECTORS[k] == direction_vector).all():
            return k
