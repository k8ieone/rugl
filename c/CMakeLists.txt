cmake_minimum_required(VERSION 2.6)
SET(PROJ_NAME "test")
project(${PROJ_NAME})

add_executable(HelloWorld starting_with_c/hello_world.c)
add_executable(DrawShape starting_with_c/draw_shape.c)
add_executable(HelloWorldCPP starting_with_cpp/hello_world.cpp)
add_executable(Test starting_with_cpp/test.cpp)
add_executable(Test2 starting_with_cpp/test2.cpp)