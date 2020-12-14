cmake_minimum_required(VERSION 2.8.3)
project(cobalt_template_pkg)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs
)

catkin_python_setup()

###################################
## catkin specific configuration ##
###################################

catkin_package(
    INCLUDE_DIRS
        include
    LIBRARIES
        cobalt_template_pkg
    CATKIN_DEPENDS
        roscpp
        rospy
        std_msgs
)

if (CATKIN_ENABLE_TESTING AND ENABLE_COVERAGE_TESTING)
    find_package(code_coverage REQUIRED)
    APPEND_COVERAGE_COMPILER_FLAGS()
endif()

###########
## Build ##
###########

## Specify additional locations of header files
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)

# Declare a C++ executable
add_executable(template_cpp_node
    nodes/template_cpp_node.cpp
)
add_dependencies(template_cpp_node
    ${${PROJECT_NAME}_EXPORTED_TARGETS}
    ${catkin_EXPORTED_TARGETS}
)
target_link_libraries(template_cpp_node
    ${catkin_LIBRARIES}
)

#############
## Install ##
#############

install(
    PROGRAMS
        nodes/template_python_node.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
    TARGETS template_cpp_node
    ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Testing ##
#############

if (CATKIN_ENABLE_TESTING)

    find_package(rostest REQUIRED)

    # A C++ unit test
    catkin_add_gtest(template_cpp_unit_test
        test/template_cpp_unit_test.cpp
    )
    target_link_libraries(template_cpp_unit_test
        ${Boost_LIBRARIES}
        ${catkin_LIBRARIES}
    )

    # A C++ node test
    add_rostest_gtest(template_cpp_integration_test
        test/template_cpp_integration_test.launch
        test/template_cpp_integration_test.cpp
    )
    target_link_libraries(template_cpp_integration_test
        ${Boost_LIBRARIES}
        ${catkin_LIBRARIES}
    )

    # Python unit tests. This runs all NON-executable .py files in test folder.
    catkin_add_nosetests(test)

    # A python node test
    add_rostest(test/template_python_integration_test.launch ARGS coverage:=ENABLE_COVERAGE_TESTING)

    if (ENABLE_COVERAGE_TESTING)
        set(COVERAGE_EXCLUDES "*/${PROJECT_NAME}/test*")  # applies to c++ coverage report only
        add_code_coverage(
            NAME ${PROJECT_NAME}_coverage_report
            DEPENDENCIES tests
        )
    endif()

endif()
