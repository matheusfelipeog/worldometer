import os

from setuptools import find_packages, setup

import worldometer


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), mode='r', encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='worldometer',
    version=worldometer.__version__,
    description='Get live, population, geography, projected, and historical data from around the world.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author=worldometer.__author__,
    author_email='matheusfelipeog@protonmail.com',
    url='https://github.com/matheusfelipeog/worldometer',
    packages=find_packages(),
    install_requires=[
        'requests-html',
        'pandas',
        'html5lib'
    ],
    zip_safe=False,
    python_requires='>=3.8',
    project_urls={
        "Bug Tracker": "https://github.com/matheusfelipeog/worldometer/issues",
        "Documentation": "https://worldometer.readthedocs.io",
        "Source Code": "https://github.com/matheusfelipeog/worldometer",
    },
    keywords=[
        'worldometer', 'worldometers', 'worldometer-api', 'worldometer-scraping',
        'world-data', 'world-metrics', 'metrics', 'real-time-data', 'real-time-metrics',
        'api', 'scraping', 'requests-html'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
