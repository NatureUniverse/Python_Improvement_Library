from setuptools import setup, find_packages

setup(
  name='natu',
  version='0.0.1',
  description='Make python more eazy',
  url='https://github.com/NatureUniverse/Python_Improvement_Library',
  author='NatureUniverse',
  author_email='pinokio082722@gmail.com',
  license='MIT',
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires=[],
  entry_points={},
)
