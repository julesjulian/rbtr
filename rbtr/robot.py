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
    """
    A simulated robot that moves on a 2D tabletop.

    Parameters:
    * table: an instance of the class rbtr.table.Table
    """

    def __init__(self, table):
        self._table = table
        self._current_position = np.array([None, None])
        self._current_facing = None
        self._placed = False

    @property
    def current_x(self):
        """The current x coordinate."""
        return self._current_position[0]

    @property
    def current_y(self):
        """The current y coordinate."""
        return self._current_position[1]

    @property
    def current_facing(self):
        """The direction in which the robot is currently facing."""
        return _direction_string(self._current_facing)

    def place(self, x_coordinate, y_coordinate, facing):
        """
        Place the robot on the tabletop.

        Parameters:
        * x_coordinate: the x coordinate at which the robot should be placed.
        * y_coordinate: the y coordinate at which the robot should be placed.
        * facing: the direction in which the robot should be facing;
            one of 'NORTH', 'EAST', 'SOUTH', or 'WEST'
        """
        if self._table.is_safe(x_coordinate=x_coordinate, y_coordinate=y_coordinate):
            self._current_position = np.array([x_coordinate, y_coordinate])
            self._current_facing = _DIRECTION_VECTORS[facing]
            self._placed = True

    def report(self):
        """Return a report containing the position the direction of the robot."""
        return "{},{},{}".format(
            self._current_position[0],
            self._current_position[1],
            _direction_string(self._current_facing)
        )

    def move(self):
        """Move the robot one square in the direction in which it is currently facing."""
        if not self._placed:
            print("Must place the robot before moving.")
            return
        prospective_position = self._current_position + self._current_facing
        if self._table.is_safe(x_coordinate=prospective_position[0],
                               y_coordinate=prospective_position[1]):
            self._current_position = prospective_position
        else:
            msg = "Prospective position (X: {}, Y: {}) is unsafe. Refusing to move."
            print(msg.format(prospective_position[0], prospective_position[1]))

    def left(self):
        """Turn the robot towards its left by 90 degrees."""
        if not self._placed:
            print("Must place the robot before turning.")
            return
        self._current_facing = np.dot(_ROTATION_MATRIX_90DEG_LEFT, self._current_facing)

    def right(self):
        """Turn the robot towards its right by 90 degrees."""
        if not self._placed:
            print("Must place the robot before turning.")
            return
        self._current_facing = np.dot(_ROTATION_MATRIX_90DEG_RIGHT, self._current_facing)


def _direction_string(direction_vector):
    if direction_vector is None:
        return None
    for k in _DIRECTION_VECTORS:
        if (_DIRECTION_VECTORS[k] == direction_vector).all():
            return k
