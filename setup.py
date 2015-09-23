#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import magiccontent

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = magiccontent.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-magic-content',
    version=version,
    description="""A flexible content application""",
    long_description=readme + '\n\n' + history,
    author='Djenie BR Team',
    author_email='dev-br@djenie.com',
    url='https://github.com/DjenieLabs/django-magic-content',
    packages=[
        'magiccontent',
    ],
    include_package_data=True,
    install_requires=[
        'django-multisites-utils',
        'django-magic-gallery',
    ],
    dependency_links=[
        "git+http://github.com/DjenieLabs/django-multisites-utils.git#egg=django-multisites-utils",
        "git+http://github.com/DjenieLabs/django-magic-gallery.git#egg=django-magic-gallery"
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-magic-content',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
