# -*- coding: utf8 -*-
"""A ``setuptools`` based setup module for webstr project.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='webstr',
    # See https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.4.dev1',
    description='Web testing framework based on Selenium.',
    long_description=long_description,
    url='TODO',
    author='TODO',
    author_email='TODO',
    license='Apache 2.0',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    packages=find_packages(exclude=['doc', 'tests']),
    include_package_data=True,
    install_requires=['selenium'],
    # http://docs.pytest.org/en/latest/goodpractices.html
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    )
