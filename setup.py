"""Test Bot.
Author: Tom Bennett -- <thomas.bennett@sky.uk>
License: MIT License (c) 2016
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='testbot',
    description='Toms first twitter bot',
    entry_points={
        'console_scripts': [
            'artbot = artbot.console:main',
        ]
    },
    long_description=open('README.md').read(),
    version='1.0.1',
    packages=['artbot'],
    scripts=[],
    author='Tom Bennett',
    author_email='thomas.bennett@sky.uk',
    url='',
    download_url='',
    install_requires=['requests'],
)
