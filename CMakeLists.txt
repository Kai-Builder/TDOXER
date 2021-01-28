cmake_minimum_required(VERSION 3.17)
project(TdDoxer C CXX)

set(CMAKE_C_STANDARD 11)

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "../bin/")

add_executable(gen
        c/run.cpp)

add_executable(support
        c/build.cpp)