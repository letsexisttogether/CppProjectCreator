cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)

project(NewCppProject
    VERSION 0.1 LANGUAGES CXX)

add_subdirectory(Source)
add_subdirectory(Test)
    