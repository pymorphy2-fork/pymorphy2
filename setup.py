#!/usr/bin/env python
import platform

from setuptools import setup


# from Cython.Build import cythonize


def get_version():
    with open("pymorphy2/version.py", "rt") as f:
        return f.readline().split("=")[1].strip(' "\n')


# TODO: use environment markers instead of Python code in order to
# allow building proper wheels. Markers are not enabled right now because
# of setuptools/wheel incompatibilities and the 'pip >= 6.0' requirement.

# extras_require = {
#     'fast:platform_python_implementation==CPython': ["DAWG>=0.7.7"],
# }

is_cpython = platform.python_implementation() == 'CPython'


install_requires = [
    'dawg2-python >= 0.8.0',
    'pymorphy2-dicts-ru >=2.4, <3.0',
    'docopt-ng >= 0.6',
]

extras_require = {'fast': []}
if is_cpython:
    extras_require['fast'].append("DAWG2 >= 0.9.0, < 1.0.0")

setup(
    name='pymorphy2',
    version=get_version(),
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    url='https://github.com/kmike/pymorphy2/',

    description='Morphological analyzer (POS tagger + inflection engine) for Russian language.',
    long_description=open('README.rst').read(),

    license='MIT license',
    packages=[
        'pymorphy2',
        'pymorphy2.units',
        'pymorphy2.lang',
        'pymorphy2.lang.ru',
        'pymorphy2.lang.uk',
        'pymorphy2.opencorpora_dict',
    ],
    entry_points={
        'console_scripts': ['pymorphy = pymorphy2.cli:main']
    },
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,

    # ext_modules=cythonize([
    #     'pymorphy2/*.py',
    #     'pymorphy2/units/*.py',
    #     'pymorphy2/opencorpora_dict/*.py',
    # ], annotate=True, profile=True),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
