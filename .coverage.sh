#!/bin/bash

source "${ICI_SRC_PATH}/workspace.sh"
source "${ICI_SRC_PATH}/util.sh"

for pkg in $COVERAGE_PKGS; do

    echo "Generating coverage for $pkg"

    ws=~/target_ws
    extend="/opt/ros/$ROS_DISTRO"
    ici_exec_in_workspace "$extend" "$ws" catkin build $pkg -v --no-deps --catkin-make-args ${pkg}_coverage_report

    echo "Uploading coverage results to codecov.io"

    # Codecov will merge all these reports
    bash <(curl -s https://codecov.io/bash) -s /root/.ros

done
