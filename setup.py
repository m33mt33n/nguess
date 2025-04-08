
from setuptools import setup

with open('requirements.txt') as f:
  install_requires = [d.strip() for d in f.read().strip().splitlines()]

setup(
  name='nguess',
  version='1.0',
  description='Simulation of a schooltime number guess game',
  long_description=open('README.md').read(),
  author='m33mt33n',
  author_email='m.3@gmx.com',
  url='https://github.com/m33mt33n/nguess',
  license='GPLv3+',
  packages=['nguess'],
  package_dir={'nguess': 'src'},
  python_requires=">=3.7",
  install_requires=install_requires,
  entry_points={
    'console_scripts': ['nguess = nguess.cli:main'],
  },
  classifiers=[  # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Topic :: Games/Entertainment :: Simulation',
    'Environment :: Console',
    'License :: GPLv3+ License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Development Status :: 5 - Production/Stable',
  ],
)
