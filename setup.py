#  gotbase kenbot
#  Copyright (c) gotbase, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import os
from setuptools import dist

dist.Distribution().fetch_build_eggs(['Cython==0.29.23'])

try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    # create closure for deferred import
    def cythonize(*args, **kwargs):
        from Cython.Build import cythonize
        return cythonize(*args, **kwargs)


    def build_ext(*args, **kwargs):
        from Cython.Distutils import build_ext
        return build_ext(*args, **kwargs)

from setuptools import find_packages
from setuptools import setup, Extension
from kenbot.constants import PROJECT_NAME, VERSION

PACKAGES = find_packages(exclude=["tentacles*"])

packages_list = [
    "kenbot.configuration_manager",
    "kenbot.kenbot_backtesting_factory",
    "kenbot.kenbot_api",
    "kenbot.task_manager",
    "kenbot.kenbot_channel_consumer",
    "kenbot.initializer",
    "kenbot.kenbot",
    "kenbot.backtesting.independent_backtesting",
    "kenbot.backtesting.abstract_backtesting_test",
    "kenbot.backtesting.kenbot_backtesting",
    "kenbot.channels.kenbot_channel",
    "kenbot.strategy_optimizer.strategy_test_suite",
    "kenbot.strategy_optimizer.test_suite_result",
    "kenbot.strategy_optimizer.strategy_optimizer",
    "kenbot.producers.interface_producer",
    "kenbot.producers.service_feed_producer",
    "kenbot.producers.evaluator_producer",
    "kenbot.producers.exchange_producer",
    "kenbot.updater.binary_updater",
    "kenbot.updater.python_updater",
    "kenbot.updater.updater",
    "kenbot.updater.updater_factory",
]

ext_modules = [
    Extension(package, [f"{package.replace('.', '/')}.py"])
    for package in packages_list]

# long description from README file
with open('README.md', encoding='utf-8') as f:
    DESCRIPTION = f.read()


def ignore_git_requirements(requirements):
    return [requirement for requirement in requirements if "git+" not in requirement]


REQUIRED = ignore_git_requirements(open('requirements.txt').readlines())
REQUIRES_PYTHON = '>=3.8'
CYTHON_DEBUG = False if not os.getenv('CYTHON_DEBUG') else os.getenv('CYTHON_DEBUG')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    url='https://github.com/gotbase/kenbot',
    license='LGPL-3.0',
    author='gotbase',
    author_email='gotbase@protonmail.com',
    description='Cryptocurrencies alert / trading bot',
    py_modules=['start'],
    packages=PACKAGES,
    package_data={
        "": ["config/*", "strategy_optimizer/optimizer_data_files/*"],
    },
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    cmdclass={'build_ext': build_ext},
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    setup_requires=REQUIRED if not CYTHON_DEBUG else [],
    install_requires=REQUIRED,
    ext_modules=cythonize(ext_modules, gdb_debug=CYTHON_DEBUG),
    python_requires=REQUIRES_PYTHON,
    entry_points={
        'console_scripts': [
            PROJECT_NAME + ' = kenbot.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Cython'
    ],
)
