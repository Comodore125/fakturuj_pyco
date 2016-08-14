#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='fakturuj_pyco',
    version='1.1.0',
    description="Generator faktur.",
    long_description='Generuje faktury z jsonu, pyco.',
    author="Visgean Skeloru",
    author_email='visgean@gmail.com',
    url='https://github.com/visgean/fakturuj_pyco',
    packages=[
        'fakturuj',
    ],
    package_dir={'fakturuj': 'fakturuj'},
    include_package_data=True,
    license="MIT",
    keywords='urljects',
    classifiers=[
        'Intended Audience :: Moje mama',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Czech',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'ares_util',
        'python-dateutil',
        'jinja2',
        'pdfkit',
    ],
    entry_points={
        'console_scripts': [
            'fakturuj = fakturuj.fakturuj:main'
        ]
    },
    package_data={
        'fakturuj': ['templates/*.html']
    },
)
