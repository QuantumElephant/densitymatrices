#!/usr/bin/env python3

from setuptools import setup

setup(name = 'var2DM',
      version = '1.0',
      description = 'Density Matrices Optimiser',
      author = 'Xiaomin Huang, Jen Garner, Fanwang Meng, Ali Teh',
      author_email = 'ayers-lab@googlegroups.com',
      url = 'https://github.com/QuantumElephant/densitymatrices',
      packages = ['var2DM', 'var2DM.test'],
      package_dir = {'var2DM': 'var2DM'},
      include_package_data = True,
      requires = ['numpy'],
     )
