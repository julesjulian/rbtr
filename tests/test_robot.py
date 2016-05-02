from unittest.mock import Mock

import pytest

from rbtr.robot import Robot
from rbtr.table import Table


@pytest.fixture
def robot_on_mock_table():
    return Robot(table=Mock())


@pytest.fixture
def robot_on_5_by_5_table():
    return Robot(table=Table(x_dimension=5, y_dimension=5))


def test_robot_can_be_initialized():
    Robot(table=Mock())


@pytest.mark.parametrize('x,y,f', [(1, 3, 'SOUTH'), (3, 2, 'NORTH'), (4, 4, 'WEST')])
def test_robot_can_be_placed(robot_on_mock_table, x, y, f):
    robot_on_mock_table.place(x_coordinate=x, y_coordinate=y, facing=f)


@pytest.mark.parametrize('x,y,f', [(1, 3, 'SOUTH'), (3, 2, 'NORTH'), (4, 4, 'WEST')])
def test_robot_communicates_correct_coordinates_and_direction(robot_on_mock_table, x, y, f):
    robot_on_mock_table.place(x_coordinate=x, y_coordinate=y, facing=f)
    assert robot_on_mock_table.current_x == x
    assert robot_on_mock_table.current_y == y
    assert robot_on_mock_table.current_facing == f


@pytest.mark.parametrize('x,y,f', [(-1, 3, 'SOUTH'), (3, 5, 'NORTH'), (4, -4, 'WEST')])
def test_robot_cannot_be_placed_off_the_table(robot_on_5_by_5_table, x, y, f):
    robot_on_5_by_5_table.place(x_coordinate=x, y_coordinate=y, facing=f)
    assert robot_on_5_by_5_table.report() == "X: None, Y: None, F: None"


def test_robot_reports_correct_position(robot_on_mock_table):
    robot_on_mock_table.place(x_coordinate=3, y_coordinate=2, facing='EAST')
    assert robot_on_mock_table.report() == "X: 3, Y: 2, F: EAST"


def test_robot_does_not_move_when_things_become_unsafe(robot_on_5_by_5_table):
    robot_on_5_by_5_table.place(0, 0, 'SOUTH')
    robot_on_5_by_5_table.move()


def test_robot_does_not_move_before_being_placed(robot_on_5_by_5_table):
    robot_on_5_by_5_table.move()


@pytest.mark.parametrize('x,y,f,x_final,y_final', [(1, 1, 'NORTH', 1, 2),
                                                   (3, 4, 'WEST', 2, 4),
                                                   (2, 6, 'SOUTH', 2, 5)])
def test_robot_moves_correctly(robot_on_mock_table, x, y, f, x_final, y_final):
    robot_on_mock_table.place(x, y, f)
    robot_on_mock_table.move()
    assert robot_on_mock_table.current_x == x_final
    assert robot_on_mock_table.current_y == y_final
