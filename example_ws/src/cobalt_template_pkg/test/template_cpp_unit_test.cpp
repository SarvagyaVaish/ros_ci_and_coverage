#include <gtest/gtest.h>

TEST(TemplateCppUT, smoke_test)
{
    EXPECT_TRUE(true) << "A simple smoke test.";
}

// Run all the tests that were declared with TEST()
int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
