from setuptools import setup, find_packages

def readfile(filename):
    with open(filename) as f:
        return f.read()

setup(
    name="22too",
    version="0.1.0dev",
    packages=find_packages(),
    install_requires = readfile("requirements.txt")

)