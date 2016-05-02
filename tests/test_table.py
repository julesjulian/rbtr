import pytest

from rbtr.table import Table


@pytest.fixture
def table():
    return Table(x_dimension=5, y_dimension=5)


def test_table_can_be_initialized_with_x_and_y_dimesions():
    Table(x_dimension=5, y_dimension=5)


@pytest.mark.parametrize('x_coord, y_coord', [(0, 0), (0, 4), (4, 0), (4, 4), (2, 3)])
def test_fields_on_table_are_considered_safe(table, x_coord, y_coord):
    assert table.is_safe(x_coordinate=x_coord, y_coordinate=y_coord)


@pytest.mark.parametrize('x_coord, y_coord', [(-1, 0), (0, 5), (4, -1), (5, 4)])
def test_fields_off_table_are_considered_unsafe(table, x_coord, y_coord):
    assert not table.is_safe(x_coordinate=x_coord, y_coordinate=y_coord)
