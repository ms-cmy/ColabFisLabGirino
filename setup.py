from setuptools import setup, find_packages

from setup_libraries import requirements_libraries

setup(
    name='FisLab',
    version='0.0.1',
    packages=find_packages(exclude=['tests'],
                           include=['FisLab']),
    install_requires=requirements_libraries('requirements.txt'),
    extras_require={
        'gpu': requirements_libraries('requirements.gpu.txt'),
        'test': [
        'pytest',
        'pytest-cov',
    ]},
)
