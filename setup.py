
from setuptools import setup, find_packages
from tank.core.version import get_version
import tank

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

requires = [
    'cement==3.0.4',
    'ansible==2.8.0',
    'jinja2',
    'pyyaml',
    'colorlog',
    'tinydb',
    'sh==1.12.13'
 ]

setup_options = dict(
    name='tank-polkadot',
    version=VERSION,
    description='Bench toolkit for blockchain',
    long_description='Long Description',
    long_description_content_type='text/markdown',
    author='Andrey Levkin',
    author_email='alevkin@gmail.com',
    url='https://github.com/mixbytes/tank/',
    license='Apache-2.0',
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Benchmark",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Clustering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    keywords='bench blockchain',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'tank': ['templates/*']},
    include_package_data=True,
    install_requires=requires,
    python_requires='>=3',
    entry_points="""
        [console_scripts]
        tank = tank.main:main
    """,
)

setup(**setup_options)
