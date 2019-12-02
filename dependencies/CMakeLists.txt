
add_subdirectory(dependencies/date)
add_subdirectory(dependencies/armadillo-code)

if(WITH_TESTS)
    add_subdirectory(dependencies/googletest)
endif()
