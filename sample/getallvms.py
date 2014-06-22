#!/usr/bin/python
# VMware vSphere Python SDK
# Copyright (c) 2008-2013 VMware, Inc. All Rights Reserved.
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
Python program for listing the vms on an ESX / vCenter host
"""

from __future__ import print_function

import pyVmomi

from pyVmomi import vim
from pyVmomi import vmodl

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vmodl

import argparse
import atexit
import getpass


def GetArgs():
   """
   Supports the command-line arguments listed below.
   """
   parser = argparse.ArgumentParser(
       description='Process args for retrieving all the Virtual Machines')
   parser.add_argument('-s', '--host', required=True, action='store',
                       help='Remote host to connect to')
   parser.add_argument('-o', '--port', type=int, default=443, action='store',
                       help='Port to connect on')
   parser.add_argument('-u', '--user', required=True, action='store',
                       help='User name to use when connecting to host')
   parser.add_argument('-p', '--password', required=False, action='store',
                       help='Password to use when connecting to host')
   args = parser.parse_args()
   return args


def PrintVmInfo(vm, depth=1):
   """
   Print information for a particular virtual machine or recurse into a folder
    with depth protection
   """
   maxdepth = 10

   # if this is a group it will have children. if it does, recurse into them
   # and then return
   if hasattr(vm, 'childEntity'):
      if depth > maxdepth:
         return
      vmList = vm.childEntity
      for c in vmList:
         PrintVmInfo(c, depth+1)
      return

   summary = vm.summary
   print("Name       : ", summary.config.name)
   print("Path       : ", summary.config.vmPathName)
   print("Guest      : ", summary.config.guestFullName)
   annotation = summary.config.annotation
   if annotation != None and annotation != "":
      print("Annotation : ", annotation)
   print("State      : ", summary.runtime.powerState)
   if summary.guest != None:
      ip = summary.guest.ipAddress
      if ip != None and ip != "":
         print("IP         : ", ip)
   if summary.runtime.question != None:
      print("Question  : ", summary.runtime.question.text)
   print("")

def main():
   """
   Simple command-line program for listing the virtual machines on a system.
   """

   args = GetArgs()
   if args.password:
      password = args.password
   else:
      password = getpass.getpass(prompt='Enter password for host %s and '
                                        'user %s: ' % (args.host,args.user))

   si = SmartConnect(host=args.host,
                     user=args.user,
                     pwd=password,
                     port=int(args.port))
   if not si:
       print("Could not connect to the specified host using specified "
             "username and password")
       return -1

   atexit.register(Disconnect, si)

   content = si.RetrieveContent()
   for child in content.rootFolder.childEntity:
      if hasattr(child, 'vmFolder'):
         datacenter = child
         vmFolder = datacenter.vmFolder
         vmList = vmFolder.childEntity
         for vm in vmList:
            PrintVmInfo(vm)
   return 0

# Start program
if __name__ == "__main__":
   main()
