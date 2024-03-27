from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A simple library for working with quaternions and vectors.'
LONG_DESCRIPTION = 'This library is written by Geir Istad, aimed for working with vectors and quaternions obtained from IMU and DMP modules. I have simply made it available on PyPI.'

# Setting up
setup(
    name="quat",
    version=VERSION,
    author="Majid Alekasir",
    author_email="<majid.alekasir@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'quaternion', 'vector', 'XYZVector', 'IMU', 'DMP'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)