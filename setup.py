#!/usr/bin/env python
from setuptools import setup, find_packages

def install():
    desc = 'A Python client library for nyaa.se!'
    setup(
        name='nyaa',
        version='1.3',
        description=desc,
        long_description=desc,
        author='SuHun Han',
        author_email='ssut@ssut.me',
        url='https://github.com/ssut/py-nyaa',
        classifiers = ['Development Status :: 5 - Production/Stable',
            'Intended Audience :: Education',
            'Intended Audience :: End Users/Desktop',
            'License :: Freeware',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: MacOS :: MacOS X',
            'Topic :: Education',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4'],
        packages=find_packages(),
        install_requires=[
            'requests',
            'xmltodict',
        ],
    )

if __name__ == "__main__":
    install()