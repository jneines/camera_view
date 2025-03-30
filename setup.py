#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/camera_view.svg
        :target: https://pypi.python.org/pypi/camera_view
.. image:: https://img.shields.io/travis/jneines/camera_view.svg
        :target: https://travis-ci.org/jneines/camera_view

A simple application to display camera streams on the desktop


Links:
---------
* `Github <https://github.com/jneines/camera_view>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', 'qtpy', 'loguru']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jens Nie",
    author_email='jneines@web.de',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A simple application to display camera streams on the desktop",
    entry_points={
        'console_scripts': [
            'camera_view=camera_view.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='camera_view',
    name='camera_view',
    packages=find_packages(include=['camera_view']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jneines/camera_view',
    version='0.1.0',
    zip_safe=False,
)
