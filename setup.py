from setuptools import setup, find_packages

setup(name='cheapFlights',
      version='0.1',
      author='Rahul Bhattacharyya',
      author_email='rahul.bhattacharyya18@gmail.com'
      description='A Python package that aggegates flight data from Kayak, Kiwi, \
                  FlightHub, etc. to find the cheapest flight'
      url='https://github.com/brahul90/cheapflights/cheapflights'
      license='Apache 2.0',
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=['lxml==3.7.3', 'requests==2.13.0'],
      test_suite='tests',
      entry_points=('console_scripts':['cheapFlights = cheapFlights.py:run']),
      package_data={
            'aiportCodes': ['airportCodes.dat']
          }
      data_files=None
      )
