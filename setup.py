from setuptools import setup, find_packages

setup(
    name='FisLab',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ]
)
