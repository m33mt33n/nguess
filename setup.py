
from setuptools import setup

setup(
  name='nguess',
  version='1.0',
  description='A number guess game',
  long_description=open('README.md').read(),
  author='m33mt33n',
  author_email='m.3@gmx.com',
  url='https://github.com/m33mt33n/nguess',
  license='GPLv3+',
  packages=['nguess'],
  package_dir={'nguess': 'src'},
  install_requires=['colored', 'tabulate'],
  entry_points={
    'console_scripts': ['nguess = nguess.cli:main'],
  },
  classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Topic :: Games/Entertainment :: Simulation',
    'Environment :: Console',
    'License :: OSI Approved :: GPLv3+ License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python',
    'Development Status :: 5 - Production/Stable',
  ],
)
