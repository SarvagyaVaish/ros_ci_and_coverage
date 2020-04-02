TravisCI: [![Build Status](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage.svg?branch=master)](https://travis-ci.org/SarvagyaVaish/ros_ci_and_coverage)

Codecov: [![codecov](https://codecov.io/gh/SarvagyaVaish/ros_ci_and_coverage/branch/master/graph/badge.svg)](https://codecov.io/gh/SarvagyaVaish/ros_ci_and_coverage)


## How to add ci and coverage to your repo

- Look at the .travis.yml in this repo and add elements to your own .travis.yml. TODO: add more details

- Add code_coverage dependency to the package.xml of your ROS package

`<test_depend>code_coverage</test_depend>`

- Add elements from the example_pkg/CMakeLists.txt file to your package's CMakeLists.txt file. TODO: add more details

- Add the .coverage.sh and .codecov.sh files to your repo.


## Running coverage on tests (locally)

See the [code_coverage](https://github.com/mikeferguson/code_coverage) repo for how to add coverage targets for your tests.

Install ros dependencies:

`rosdep install --from-paths src --ignore-src -r -y`

Run tests with coverage on. This creates several .coverage files in the ~/.ros folder, one for each test.

`catkin_make run_tests -DENABLE_COVERAGE_TESTING=ON`

`catkin_make run_tests_example_pkg -DENABLE_COVERAGE_TESTING=ON`

Create a coverage report in the current directory by combining the the .coverage files.

`python-coverage combine ~/.ros`

Render the coverage report:

in_terminal: `python-coverage report`
html: `python-coverage html -d .coverage.html`


Protip #1: View the html report in a browset directly from the commandline

`google-chrome .coverage.html/index.html `

Protip #2: You can specify the --omit or --include flag while generating any of the above reports. This is handy for filtering files in the report. Check the python-coverage [docs](https://coverage.readthedocs.io/en/coverage-4.5.4/) for more options.

`python-coverage report --omit="/opt/*,/usr/*"`

`python-coverage report --include="*/example_pkg/*"`
