# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

from worldometer.__about__ import __version__, __author__, __email__


NAME = 'worldometer'
URL = 'https://github.com/matheusfelipeog/worldometer'
DESCRIPTION = 'Worldometer Scraping & API - Get world metrics from worldometers.info'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), mode='r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=NAME,
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author=__author__,
    author_email=__email__,
    url=URL,
    packages=find_packages(),
    install_requires=[
        'requests-html'
    ],
    zip_safe=False,
    python_requires='>=3.6',
    project_urls={
        "Bug Tracker": "https://github.com/matheusfelipeog/worldometer/issues",
        "Documentation": "https://github.com/matheusfelipeog/worldometer/blob/master/doc/README.md",
        "Source Code": "https://github.com/matheusfelipeog/worldometer",
    },
    keywords=[
        'worldometer', 'worldometers', 'worldometer-api', 'worldometer-scraping',
        'world-data', 'world-metrics', 'metrics', 'real-time-data', 'real-time-metrics',
        'api', 'scraping', 'requests-html'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
