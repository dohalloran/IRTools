#!/usr/bin/env python
# Time-stamp: <2015-11-02 22:56:22 Zhouhao Zeng>

"""Description

Setup script for IRTools -- a powerful toolset for intron retention detection

Copyright (c) 2015 Zhouhao Zeng <zzhlbj23@gwmail.gwu.edu>

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file COPYING included with
the distribution).

@status:  beta
@version: $Revision$
@author:  Zhouhao Zeng
@contact: zzhlbj23@gwmail.gwu.edu
"""

import os
import sys
from setuptools import setup

try:
        import HTSeq
except: 
        sys.stderr.write("CRITICAL:HTSeq must be installed!\n")
        sys.exit(1)

try:
        import pysam
except: 
        sys.stderr.write("CRITICAL:pysam must be installed!\n")
        sys.exit(1)

try:
        import pandas
except: 
        sys.stderr.write("CRITICAL:pandas must be installed!\n")
        sys.exit(1)

try:
        import networkx
except: 
        sys.stderr.write("CRITICAL:networkx must be installed!\n")
        sys.exit(1)

def main():
        if float(sys.version[:3])<2.7 or float(sys.version[:3])>=2.8:
                sys.stderr.write("CRITICAL: Python version must be 2.7!\n")
                sys.exit(1)

        setup(name="IRTools",
              version="1.1.0",
              description="a powerful toolset for intron retention detection",
              author='Zhouhao Zeng',
              author_email='zzhlbj23@gwmail.gwu.edu',
              url='https://github.com/zhouhaozeng/IRTools/',
              package_dir={'IRTools' : 'IRTools'},
              packages=['IRTools'],   
              package_data={'IRTools': ['data/*.gtf']},
              scripts=['bin/IRTools',
                       ],
              classifiers=[
                      'Development Status :: 4 - Beta',
                      'Environment :: Console',
                      'Intended Audience :: Developers',
                      'Intended Audience :: Science/Research',              
                      'License :: OSI Approved :: BSD License',
                      'Operating System :: MacOS :: MacOS X',
                      'Operating System :: POSIX',
                      'Topic :: Scientific/Engineering :: Bio-Informatics',
                      'Programming Language :: Python',
                      ],
              install_requires=[
                      'HTSeq',
                      'pysam',
                      'pandas',
                      'networkx'
                      ],
              )

if __name__ == '__main__':
        main()
