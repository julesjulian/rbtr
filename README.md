# RBTR
[![Build Status](https://travis-ci.org/julesjulian/rbtr.svg?branch=master)](https://travis-ci.org/julesjulian/rbtr)

Simulate a robot moving along a tabletop.

## Features
* Robot can be placed on any field on the table, facing in any direction.
* Turn left and right.
* Move forward.
* Built-in disaster prevention.

## Installation and Usage
Navigate to the repository and type
```sh
$ python setup.py develop
```
to install the program. To run it, type
```sh
$ rbtr
```

##Developer Information
Testing is done with py.test. Run the test suite by navigating to the repository and typing
```sh
$ py.test
```
