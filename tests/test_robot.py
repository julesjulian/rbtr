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
