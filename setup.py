from setuptools import setup, find_packages

from setup_libraries import requirements_libraries

setup(
    name='FisLab',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements_libraries(),
    tests_require=[
        'pytest',
        'pytest-cov',
    ]
)
