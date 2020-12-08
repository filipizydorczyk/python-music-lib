from setuptools import setup

setup(
    name='musiclib',
    version='1.0',
    description='Library provideing music structures',
    author='Filip Izydorczyk',
    author_email='filip.izydorczyk@protonmail.com',
    packages=['musiclib'],  # same as name
    install_requires=['pytest'],  # external packages as dependencies
)
