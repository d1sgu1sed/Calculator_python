from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.2'
__author__ = 'Ivan Kichigin'
__email__ = 'ivan.kichigin977@gmail.com'


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ionex',

    description='',
    long_description=long_description,

    version=__version__,

    url='https://github.com/gnss-lab/ionex',

    author=__author__,
    author_email=__email__,

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',

        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='ionosphere gnss tec development',

    packages=find_packages(exclude=['docs', 'tests']),

    include_package_data=True,

    install_requires=[],

    python_requires='>=3',

    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
