from setuptools import setup, find_packages
from datetime import datetime


def version():
    now = datetime.now()
    return f'{now.year}.{now.month}.{now.day}'


setup(
    name='stockprice',
    version=version(),
    packages=find_packages(),
    entry_points={
        'console_scripts': 'stockprice=stockprice.cli.main:main'
    },
    install_requires=[
        'click',
        'requests',
    ],
)
