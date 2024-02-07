# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='aiofiles',
    version='23.2.1',
    description='File support for asyncio.',
    author_email='Tin Tvrtkovic <tinchester@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=[
        'aiofiles',
        'aiofiles.tempfile',
        'aiofiles.threadpool',
    ],
    package_dir={'': 'src'},
)
