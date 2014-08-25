# VMware vSphere Python SDK
# Copyright (c) 2009-2014 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('test-requirements.txt') as f:
    required_for_tests = f.read().splitlines()

setup(
   name='pyvmomi',
   version='5.5.0-2014.1.1',
   description='VMware vSphere Python SDK',
   author='VMware, Inc.',
   author_email='jhu@vmware.com',
   url='https://github.com/vmware/pyvmomi',
   packages=['pyVmomi', 'pyVim'],
   install_requires=required,
   license='License :: OSI Approved :: Apache Software License',
   data_files = [("", ["LICENSE.txt", "NOTICE.txt", "MANIFEST.in",
                       "setup.py", "tox.ini"])],
   # NOTE: pypi prefers the use of RST to render docs
   long_description=read('README.rst'),
   classifiers=[
      "License :: OSI Approved :: Apache Software License",
      "Development Status :: 5 - Production/Stable",
      "Environment :: No Input/Output (Daemon)",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Intended Audience :: Information Technology",
      "Intended Audience :: System Administrators",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Topic :: System :: Distributed Computing",
      "Operating System :: Microsoft :: Windows",
      "Operating System :: POSIX",
      "Operating System :: Unix",
      "Operating System :: MacOS",
   ],
   platforms = ["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
   test_suite='tests',
   tests_require= required_for_tests,
   zip_safe=True
)
