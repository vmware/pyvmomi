"""
Written By: Mohammadali Bazyar <m.ali.bazyar@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


    Usage:
      This module allows you to retrive all the information of VMs already spun up in vSphere.

    Use Case:
      from Vcenter import Vcenter
      vcenter = Vcenter("vcenter-host-url", "username", "password", 443) #443 in the case of https
      for serializedVM in vcenter.retrieveVMs():
         print(serializedVM)
"""


from __future__ import print_function

from pyVmomi import vim

from pyVim.connect import SmartConnectNoSSL, SmartConnect,Disconnect

import argparse
import atexit
import json
import ssl
import requests



class Vcenter():
    def __init__(self, host, user, pwd, port):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        if hasattr(ssl, '_create_unverified_context'):
            context = ssl._create_unverified_context()
        si = SmartConnect(host = self.host,
                      user = self.user,
                      pwd = self.pwd,
                      port = int(self.port),
                      sslContext = context)
        if not si:
            print("Could not connect to the specified host using specified "
                  "username and password")
            return -1
        self.si = si
        atexit.register(Disconnect, self.si)
        self.content = self.si.RetrieveContent()
        self.children = self.content.rootFolder.childEntity
    def retrieveContent(self):
        return self.content
    def retrieveChildren(self):
        return self.children
    
    
    
    def getNICs(self, summary, guest):
        nics = {}
        for nic in guest.net:
            if nic.network:  # Only return adapter backed interfaces
                if nic.ipConfig is not None and nic.ipConfig.ipAddress is not None:
                    nics[nic.macAddress] = {}  # Use mac as uniq ID for nic
                    nics[nic.macAddress]['netlabel'] = nic.network
                    ipconf = nic.ipConfig.ipAddress
                    for ip in ipconf:
                        if ":" not in ip.ipAddress:  # Only grab ipv4 addresses
                            nics[nic.macAddress]['ip'] = ip.ipAddress
                            nics[nic.macAddress]['prefix'] = ip.prefixLength
                            nics[nic.macAddress]['connected'] = nic.connected
        return nics
    
    
    def diskInfo(self, summary):
        if not hasattr(summary, 'storage'):
            return "0"
        elif not hasattr(summary.storage, "committed"):
            return "0"
        return int(summary.storage.committed / 1024**3)   
    
    def vmsummary(self, summary, guest):
        
        vmsum = {}
        config = summary.config
        net = self.getNICs(summary, guest)
        vmsum['mem'] = str(config.memorySizeMB)
        vmsum['diskGB'] = str(self.diskInfo(summary))
        vmsum['cpu'] = str(config.numCpu)
        vmsum['path'] = config.vmPathName
        vmsum['ostype'] = config.guestFullName
        vmsum['state'] = summary.runtime.powerState
        vmsum['annotation'] = config.annotation if config.annotation else ''
        vmsum['net'] = net
        return vmsum
    
    def retrieveVMs(self):
        for child in self.children:  # Iterate though DataCenters
            dc = child
            clusters = dc.hostFolder.childEntity
            for cluster in clusters:  # Iterate through the clusters in the DC
                if hasattr(cluster, 'host'):  # Variable to make pep8 compliance
                    hosts = cluster.host
                else:
                    continue
                for host in hosts:  # Iterate through Hosts in the Cluster
                    hostname = host.summary.config.name
                    # Retrieves all the VMs
                    vms = host.vm
                    for vm in vms:  # Iterate through each VM on the host
                        vmname = vm.summary.config.name
                        summary = self.vmsummary(vm.summary, vm.guest)
                        vcpus = summary['cpu']
                        memory = summary['mem']
                        network = summary['net']
                        os = summary['ostype']
                        path = summary['path']
                        annotation = summary['annotation']
                        state = summary['state']
                        disk = summary['diskGB']
                        clustername = cluster.name
                                                
                        vmSerializedData = {"name": vmname, "vcpus": vcpus, "memory": memory, "network": network, "os": os,
                                          "path": path, "comment": annotation, "state": state, "disk": disk, 
                                          "hostname": hostname, "cluster": clustername, "DC": dc.name}
                        yield vmSerializedData  
                        


