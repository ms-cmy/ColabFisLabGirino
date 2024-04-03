import os


def requirements_libraries(file_name: str):
    with open(file_name, "r") as f:
        libraries = f.read().splitlines()
    return libraries

def test_requirements_libraries():
    assert len(requirements_libraries('requirements.txt')) > 0
    assert isinstance(requirements_libraries(), list)
