from setuptools import setup
from act_dr6_lenslike import __author__, __version__
import os

file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(file_dir)

setup(name="act_dr6_lenslike",
      version=__version__,
      author=__author__,
      license='BSD 2-Clause',
      description='Likelihood software for ACT DR6 CMB lensing',
      # zip_safe=False,  # set to false if you want to easily access bundled package data files
      packages=['act_dr6_lenslike'],#, 'act_dr6_lenslike.tests'],
      # package_data={'act_dr6_lenslike': ['*.yaml', '*.bibtex', 'data/*', 'data/**/*']},
      test_suite='act_dr6_lenslike.tests',
      # tests_require=['camb>=1.0.5']
      )
