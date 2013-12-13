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

from optparse import OptionParser, make_option
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vmodl
import sys
import atexit

def GetOptions():
   """
   Supports the command-line arguments listed below.
   """

   _CMD_OPTIONS_LIST = [
      make_option("-h", "--host",
                  help="remote host to connect to"),
      make_option("-o", "--port",
                  default=443,
                  help="Port"),
      make_option("-u", "--user",
                  default="root",
                  help="User name to use when connecting to host"),
      make_option("-p", "--password",
                  help="Password to use when connecting to host"),
      make_option("-?", "--help", action="store_true",
                  help="Help"),
   ]
   _STR_USAGE = "%prog [options]"

   parser = OptionParser(option_list=_CMD_OPTIONS_LIST,
                         usage=_STR_USAGE,
                         add_help_option=False)
   (options, _) = parser.parse_args()

   return options

def PrintVmInfo(vm):
   """
   Print information for a particular virtual machine.
   """

   summary = vm.summary
   print "Name       : ", summary.config.name
   print "Path       : ", summary.config.vmPathName
   print "Guest      : ", summary.config.guestFullName
   annotation = summary.config.annotation
   if annotation != None and annotation != "":
      print "Annotation : ", annotation
   print "State      : ", summary.runtime.powerState
   if summary.guest != None:
      ip = summary.guest.ipAddress
      if ip != None and ip != "":
         print "IP         : ", ip
   if summary.runtime.question != None:
      print "Question  : ", summary.runtime.question.text
   print ""

def main():
   """
   Simple command-line program for listing the virtual machines on a system.
   """

   options = GetOptions()
   try:
      si = SmartConnect(host=options.host,
                user=options.user,
                pwd=options.password,
                port=int(options.port))
      if not si:
         print "Could not connect to the specified host"
         return -1

      atexit.register(Disconnect, si)

      content = si.RetrieveContent()
      datacenter = content.rootFolder.childEntity[0]
      vmFolder = datacenter.vmFolder
      vmList = vmFolder.childEntity
      for vm in vmList:
         PrintVmInfo(vm)
   except vmodl.MethodFault, e:
      print "Caught vmodl fault : " + e.msg
      return -1
   except Exception, e:
      print "Caught exception : " + str(e)
      return -1

   return 0

# Start program
if __name__ == "__main__":
   main()
