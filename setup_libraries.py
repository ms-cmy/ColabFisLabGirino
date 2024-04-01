import os


def requirements_libraries():
    with open('requirements.txt') as f:
        libraries = f.read().splitlines()
    return libraries

def test_requirements_libraries():
    assert len(requirements_libraries()) > 0

print(requirements_libraries())