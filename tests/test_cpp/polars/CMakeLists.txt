set(TEST_CPP_SOURCE_DIR "tests/test_cpp/polars")

add_executable(
        polars_cpp_test
        ${TEST_CPP_SOURCE_DIR}/test_numc.cpp
        ${TEST_CPP_SOURCE_DIR}/TestSeries.cpp
        ${TEST_CPP_SOURCE_DIR}/TestSeriesMask.cpp
        ${TEST_CPP_SOURCE_DIR}/TestTimeSeries.cpp
        ${TEST_CPP_SOURCE_DIR}/TestTimeSeriesMask.cpp
        ${TEST_CPP_SOURCE_DIR}/TestWindowProcessor.cpp
)

if(BUILD_WITH_CONAN)
    target_link_libraries(polars_cpp_test polars_cpp CONAN_PKG::gtest)
else()
    target_link_libraries(polars_cpp_test polars_cpp gtest_main)
endif()
