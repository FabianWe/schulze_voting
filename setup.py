import os
from setuptools import setup, find_packages
from schulze_voting import __version__


setup(
    name='schulze_voting',
    version=__version__,
    description=' A python implementation for Schulze votings with the possibility to have weighted votes.',
    url='https://github.com/FabianWe/schulze_voting',
    author='Fabian Wenzelmann',
    author_email='fabianwen@posteo.eu',
    license='MIT',
    keywords='voting schulze',
    packages=find_packages(exclude=('docs', 'tests', 'env')),
    include_package_data=True,
    install_requires=['pytest'],
)
