class Table():
    """
    A model of a 2D tabletop.

    Parameters:
    * x_dimension: The number of squares in east-west direction.
    * y_dimension: The number of squares in north-south direction.
    """
    def __init__(self, x_dimension, y_dimension):
        self._x_dimension = x_dimension
        self._y_dimension = y_dimension

    def is_safe(self, x_coordinate, y_coordinate):
        """Given x and y coordinates, return whether the position is safe, i.e. on the table."""
        if 0 <= x_coordinate < self._x_dimension and 0 <= y_coordinate < self._y_dimension:
            return True
        return False
