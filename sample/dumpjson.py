#!/usr/bin/env python
# VMware vSphere Python SDK
# Copyright (c) 2008-2018 VMware, Inc. All Rights Reserved.
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

"""
Python program for dumping JSON of any object given the type and MOID
"""

from __future__ import print_function

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, VmomiSupport

import argparse
import atexit
import getpass
import json
import ssl

def GetArgs():
   """
   Supports the command-line arguments listed below.
   """
   parser = argparse.ArgumentParser(
       description='Process args for extracting JSON from a Managed Object')
   parser.add_argument('-s', '--host', required=True, action='store',
                       help='Remote host to connect to')
   parser.add_argument('-o', '--port', type=int, default=443, action='store',
                       help='Port to connect on')
   parser.add_argument('-u', '--user', required=True, action='store',
                       help='User name to use when connecting to host')
   parser.add_argument('-p', '--password', required=False, action='store',
                       help='Password to use when connecting to host')
   parser.add_argument('-t', '--type', required=True, action='store',
                       help='The vim type lookup, ex: "VirtualMachine"')
   parser.add_argument('-i', '--id', required=True, action='store',
                       help='The MOID to lookup, ex: "vm-42"')
   args = parser.parse_args()
   return args

def main():
   """
   Simple command-line program for dumping the contents of any managed object.
   """

   args = GetArgs()
   if args.password:
      password = args.password
   else:
      password = getpass.getpass(prompt='Enter password for host %s and '
                                        'user %s: ' % (args.host,args.user))

   context = None
   if hasattr(ssl, '_create_unverified_context'):
      context = ssl._create_unverified_context()
   si = SmartConnect(host=args.host,
                     user=args.user,
                     pwd=password,
                     port=int(args.port),
                     sslContext=context)
   if not si:
       print("Could not connect to the specified host using specified "
             "username and password")
       return -1

   atexit.register(Disconnect, si)

   obj = VmomiSupport.templateOf(args.type)(args.id, si._stub)
   print(json.dumps(obj, cls=VmomiSupport.VmomiJSONEncoder,
                    sort_keys=True, indent=4))

# Start program
if __name__ == "__main__":
   main()
