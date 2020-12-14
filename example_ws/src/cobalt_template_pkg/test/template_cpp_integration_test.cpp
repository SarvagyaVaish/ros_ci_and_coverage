#include <gtest/gtest.h>
#include <ros/ros.h>
#include <std_msgs/String.h>

// Based off of:
// - https://szobov.github.io/2019/02/08/ros-cpp-writing-tests/
// - https://github.com/ros-planning/navigation/blob/c7bcd005fde62d3eaa2069b96f33ba4c472eadb8/map_server/test/rtest.cpp

class TemplateCppIntegrationTest : public ::testing::Test
{
public:
    TemplateCppIntegrationTest() : spinner(0){};
    ~TemplateCppIntegrationTest(){};

    ros::NodeHandle *node;
    ros::AsyncSpinner *spinner;

    void SetUp() override
    {
        ::testing::Test::SetUp();
        this->node = new ros::NodeHandle("/");
        this->spinner = new ros::AsyncSpinner(0);
        this->spinner->start();
    };

    void TearDown() override
    {
        ros::shutdown();
        delete this->spinner;
        delete this->node;
        ::testing::Test::TearDown();
    }

    // Topic callback for receiving messages.
    void chatter_callback(const std_msgs::String::ConstPtr &msg)
    {
        chatter_msg = msg.get();
        msg_received = true;
    }

    // Member variable to hold state
    const std_msgs::String *chatter_msg = nullptr;
    bool msg_received = false;
};

TEST_F(TemplateCppIntegrationTest, test_chatter)
{
    ros::Subscriber sub =
        node->subscribe<std_msgs::String>("chatter", 1, boost::bind(&TemplateCppIntegrationTest::chatter_callback, this, _1));

    ros::Duration d = ros::Duration().fromSec(0.25);

    while (!msg_received)
    {
        ros::spinOnce();
        d.sleep();
    }

    // We now have a chatter message.

    // If this was a real test, we would do something useful here.
    EXPECT_TRUE(msg_received);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "template_cpp_integration_test");

    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
