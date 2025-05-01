import os


projectName = "NewCppProject"

def CheckException(function, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except Exception as e:
        print(f'An exception occurred: {type(e).__name__}: {e}')
        raise Exception('CppProjectCreator Termination...')

def CreateFolder(folder: str):
    CheckException(os.makedirs, folder, exist_ok=True)

def CreateFile(path: str, content: str):
    def subFunction(path: str, content: str):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

    CheckException(subFunction, path, content)

def CreateAndFillProject():
    # Create the main project folder
    CreateFolder(projectName)

    # Content for CMakeLists.txt
    cmakelistsContent = f'''cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 17)

project({projectName}
    VERSION 0.1 LANGUAGES CXX)

add_subdirectory(Source)
add_subdirectory(Test)
    '''
    
    # Create CMakeLists.txt in the project root
    CreateFile(f'{projectName}/CMakeLists.txt', cmakelistsContent)

    # Create the Source and Test folders and their contents
    CreateAndFillSource()
    CreateAndFillTest()

    # Create the .gitignore file
    LoadGitignore()

def CreateAndFillSource():
    # Create Source folder
    CreateFolder(f'{projectName}/Source')

    # Content for CMakeLists.txt inside Source
    cmakelistsContent = '''set(PROJECT_SOURCES
    Main.cpp)

target_sources(${PROJECT_NAME}
    PRIVATE ${PROJECT_SOURCES})

target_include_directories(${PROJECT_NAME}
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
    '''
    CreateFile(f'{projectName}/Source/CMakeLists.txt', cmakelistsContent)

    # Content for Main.cpp
    mainFileContent = f'''#include <iostream>
    
std::int32_t main(int argc, char** argv)
{{
    std::cout << "Hello, {projectName}" << std::endl;

    return EXIT_SUCCESS;
}}
    '''
    CreateFile(f'{projectName}/Source/Main.cpp', mainFileContent)

def CreateAndFillTest():
    CreateFolder(f'{projectName}/Test')

    cmakelistsContent = '''# Include your tests here'''

    CreateFile(f'{projectName}/Test/CMakeLists.txt', cmakelistsContent)

def LoadGitignore():
    gitignoreContent = '''# Ignore build directories
build/
bin/
obj/

# Ignore CMake files
CMakeCache.txt
CMakeFiles/
    '''

    CreateFile(f'{projectName}/.gitignore', gitignoreContent)


if __name__ == '__main__':
    CreateAndFillProject()
