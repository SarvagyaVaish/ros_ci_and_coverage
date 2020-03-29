TravisCI: [![Build Status](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage.svg?branch=master)](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage)

## Export the following

export COVERAGE_PROCESS_START=.coveragerc
export COVERAGE_RCFILE=/home/turtlebot/ros_ci_and_coverage/example_ws/.coveragerc
export CODECOV_TOKEN="..."  # codecov.io

## Python virtual env setup

Even though ROS runs against python2, we want to setup the virtual environment with python3 so that we can use black and flake8 formatters and linters.

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
