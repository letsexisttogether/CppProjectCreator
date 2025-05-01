import os
import argparse

parser = argparse.ArgumentParser(description='Create a C++ project structure.')
parser.add_argument('project_name', nargs='?', default='NewCppProject', help='The name of the project')

# Parse the arguments
args = parser.parse_args()
projectName = args.project_name

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
    cmakelistsContent = f'''set(OUT_FILE_NAME {projectName})

set(SOURCES Main.cpp)

add_executable(${{OUT_FILE_NAME}})

target_sources(${{OUT_FILE_NAME}}
    PRIVATE ${{SOURCES}})

target_include_directories(${{OUT_FILE_NAME}}
    PRIVATE ${{CMAKE_CURRENT_SOURCE_DIR}})
    '''
    CreateFile(f'{projectName}/Source/CMakeLists.txt', cmakelistsContent)

    mainFileContent = f'''#include <iostream>
    
std::int32_t main(std::int32_t argc, char** argv)
{{
    std::cout << "Hello, {projectName}" << std::endl;

    return EXIT_SUCCESS;
}}
    '''
    CreateFile(f'{projectName}/Source/Main.cpp', mainFileContent)

def CreateAndFillTest():
    CreateFolder(f'{projectName}/Test')

    cmakelistsContent = f'''set(OUT_FILE_NAME {projectName}_TEST)
set(SOURCES Main.cpp)

add_executable(${{OUT_FILE_NAME}})

target_sources(${{OUT_FILE_NAME}}
    PRIVATE ${{SOURCES}})

target_include_directories(${{OUT_FILE_NAME}}
    PRIVATE ${{CMAKE_CURRENT_SOURCE_DIR}}
    PRIVATE ${{CMAKE_SOURCE_DIR}}/Source
)
'''
    CreateFile(f'{projectName}/Test/CMakeLists.txt', cmakelistsContent)

    mainFileContent = f'''#include <iostream>
    
std::int32_t main(std::int32_t argc, char** argv)
{{
    std::cout << "Hello, {projectName} Test" << std::endl;

    return EXIT_SUCCESS;
}}
    '''
    CreateFile(f'{projectName}/Test/Main.cpp', mainFileContent)

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
