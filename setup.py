#!/usr/bin/env python2

from distutils.core import setup

setup(name='var2DM',
      version='1.0',
      description='Density Matrices Optimiser',
      author='Xiaomin Huang, Jen Garner, Fanwang Meng, Ali Teh',
      author_email='ayers-lab@googlegroups.com',
      url='https://github.com/QuantumElephant/densitymatrices',
      packages=['var2DM'],
      package_dir = {'var2DM': 'var2DM'},
      package_data = {'var2DM': ['data/test/*.xyz']},
      requires = ['numpy'],
     )
