from setuptools import setup

setup(name='address_parser',
      version='0.1',
      description='Address Parser REST API',
      url='',
      author='George the Silent',
      author_email='george.the.silent@gmail.com',
      license='MIT',
      zip_safe=False,
      packages=['app'],
      install_requires=['torch', 'deepparse', 'flask', 'flask_restful', 'jsonpickle'],
      entry_points = {
          'console_scripts': ['address_parser=app.app:main'],
      })