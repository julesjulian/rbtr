class Table():
    def __init__(self, x_dimension, y_dimension):
        self._x_dimension = x_dimension
        self._y_dimension = y_dimension

    def is_safe(self, x_coordinate, y_coordinate):
        if 0 <= x_coordinate < self._x_dimension and 0 <= y_coordinate < self._y_dimension:
            return True
        return False
