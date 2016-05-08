"""Main module for parameter setup and command line interface."""

from .robot import Robot
from .table import Table

X_DIMENSION = 5
Y_DIMENSION = 5
WELCOME_MESSAGE = """
Welcome to RBTR. You can type the following commands:

PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
EXIT
"""
FAREWELL_MESSAGE = "Goodbye."
UNKNOWN_COMMAND_MESSAGE = "Unknown command {}. Please try again."


def run_from_command_line():
    """Receive input from stdin to control the robot."""
    robot = Robot(table=Table(x_dimension=X_DIMENSION, y_dimension=Y_DIMENSION))
    print(WELCOME_MESSAGE)
    while True:
        command = input('Enter command: ')
        if command[:len('PLACE')] == 'PLACE':
            [x_coord, y_coord, facing] = command[len('PLACE') + 1:].split(',')
            robot.place(x_coordinate=int(x_coord), y_coordinate=int(y_coord), facing=facing)
        elif command == 'MOVE':
            robot.move()
        elif command == 'LEFT':
            robot.left()
        elif command == 'RIGHT':
            robot.right()
        elif command == 'REPORT':
            print(robot.report())
        elif command == 'EXIT':
            print(FAREWELL_MESSAGE)
            return
        else:
            print(UNKNOWN_COMMAND_MESSAGE.format(command))
