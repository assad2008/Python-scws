#!/usr/bin/env python

from distutils.core import setup, Extension

scws_module = Extension(name='_scws', 
        sources = ['scws.c'], 
        language='c', 
        include_dirs=['/usr/include/python2.6', 'include/scws'], 
        library_dirs=['.'],
        libraries=['scws'], 
        extra_compile_args=[])


setup (
    name = 'scws',
    version = '0.0.1',
    url = 'xxx',
    description = 'a python package for scws',
    author_email = 'xxx',
    ext_modules = [scws_module]
)


