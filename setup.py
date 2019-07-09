#!/usr/bin/env python3

import io
import os
import sys

from setuptools import find_packages, setup, Command
from setuptools.command.install import install
import subprocess
import os

NAME = 'pifan'

class CustomInstallCommand(install):
  def run(self):
    install.run(self)
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    create_service_script_path = os.path.join(current_dir_path, 'create_service.sh')
    subprocess.check_output([create_service_script_path])


setup(
    name=NAME,
    version='0.1.0',
    description='Simple raspberry pi fan control',
    long_description_content_type='text/markdown',
    author='element54',
    author_email='element54@posteo.de',
    python_requires='>=3.7.0',
    url='https://github.com/element54/pifan',
    install_requires=['RPi.GPIO', ],
    include_package_data=True,
    license='MIT',
    scripts=['bin/pifan', ],
    cmdclass={'install': CustomInstallCommand},
)
