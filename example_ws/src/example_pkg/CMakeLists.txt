cmake_minimum_required(VERSION 2.8.3)
project(example_pkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

###################################
## catkin specific configuration ##
###################################

if (CATKIN_ENABLE_TESTING AND ENABLE_COVERAGE_TESTING)
  find_package(code_coverage REQUIRED)
  APPEND_COVERAGE_COMPILER_FLAGS()
endif()

#############
## Testing ##
#############

if (CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)

  # This will run all NON-executable .py files in test folder
  catkin_add_nosetests(test)

  # Integration tests
  add_rostest(test/sample_rostest.test ARGS coverage:=ENABLE_COVERAGE_TESTING)

  if (ENABLE_COVERAGE_TESTING)
    set(COVERAGE_EXCLUDES "*/${PROJECT_NAME}/test*")
    add_code_coverage(
      NAME ${PROJECT_NAME}_coverage_report
      DEPENDENCIES tests
    )
  endif()

endif()
