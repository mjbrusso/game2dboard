from setuptools import setup, find_packages
from game2dboard import __name__, __package__, __version__

__author__ = "Marcos Brusso"
__author_email__="mjbrusso@gmail.com"
__license__ ="MIT License"
__desc__ = "Python GUI library for creating 2D arrays based board games"
__python_requires__ = ">=3"
__keywords__ = [
    "GUI",
    __name__,
    "2D",
    "Matrices",
    "array"
]
__url__ = "https://github.com/mjbrusso/game2dboard"

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Topic :: Education",
    "Topic :: Software Development :: User Interfaces",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
]

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__desc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=__license__,
    keywords=__keywords__,
    url=__url__,
    packages=find_packages(),
    classifiers=__classifiers__,
    install_requires=[],
    # extras_require=[],
    python_requires=__python_requires__,
)
