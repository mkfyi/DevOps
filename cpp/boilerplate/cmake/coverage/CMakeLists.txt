# Project
# ├── contrib
# │   └── catchorg
# │       └── Catch2
# │           └── include
# │               └── Catch2
# │                   └── catch.hpp
# ├── include
# ├── src
# ├── tests
# │   ├── CMakeLists.txt (this file)
# │   ├── main.cpp
# │   └── component
# │       ├── test1.cpp
# │       └── test2.cpp
# └── CMakeLists.txt (base project)
set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)

cmake_minimum_required(VERSION 3.1)
project("boilerplate-name")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++20 -fprofile-instr-generate -fcoverage-mapping")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fprofile-instr-generate")

set(LDFLAGS "${LDFLAGS} -fprofile-instr-generate")
set(EXECUTABLE_OUTPUT_PATH ${dir})

include_directories(
  "../include"
  "../contrib/catchorg/Catch2/include"
)

file(
  GLOB SOURCES
  "main.cpp"
  "**/*.cpp"
  "../src/*.cpp"
  "../src/**/*.cpp"
)

# your project usually contains a main.cpp, we'll exclude this file
list(FILTER SOURCES EXCLUDE REGEX "*src\/main.cpp$")

# optional add necessary libraries
set(PROJECT_LINK_LIBS pthread)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCES})
target_link_libraries(${CMAKE_PROJECT_NAME} ${PROJECT_LINK_LIBS})
