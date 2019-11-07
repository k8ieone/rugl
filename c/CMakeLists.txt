cmake_minimum_required(VERSION 2.6)
SET(PROJ_NAME "test")
project(${PROJ_NAME})

add_executable(HelloWorld.out starting_with_c/hello_world.c)
add_executable(DrawShape.out starting_with_c/draw_shape.c)
add_executable(HelloWorldCPP.out starting_with_cpp/hello_world.cpp)
add_executable(Test.out starting_with_cpp/test.cpp)
add_executable(Test2.out starting_with_cpp/test2.cpp)