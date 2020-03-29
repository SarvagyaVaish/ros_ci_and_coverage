TravisCI: [![Build Status](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage.svg?branch=master)](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage)

Codecov: [![codecov](https://codecov.io/gh/SarvagyaVaish/ros_ci_and_coverage/branch/master/graph/badge.svg)](https://codecov.io/gh/SarvagyaVaish/ros_ci_and_coverage)



`export COVERAGE_PROCESS_START=.coveragerc`

`export COVERAGE_RCFILE=/home/turtlebot/ros_ci_and_coverage/.coveragerc`

`export CODECOV_TOKEN="..."  # codecov.io`

`coverage combine ~/.ros/`

`coverage xml`

`bash <(curl -s https://codecov.io/bash)`
