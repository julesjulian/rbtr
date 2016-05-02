from unittest.mock import Mock

import pytest

from rbtr.robot import Robot


@pytest.fixture
def robot():
    return Robot(table=Mock())


def test_robot_can_be_initialized():
    Robot(table=Mock())


@pytest.mark.parametrize('x,y,f', [(1, 3, 'SOUTH'), (3, 2, 'NORTH'), (4, 4, 'WEST')])
def test_robot_can_be_placed(robot, x, y, f):
    robot.place(x_coordinate=x, y_coordinate=y, facing=f)


def test_robot_reports_correct_position(robot):
    robot.place(x_coordinate=3, y_coordinate=2, facing='EAST')
    assert robot.report() == "X: 3, Y: 2, F: EAST"
