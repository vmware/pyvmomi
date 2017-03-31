#!/usr/bin/python
# William Lam
# www.virtuallyghetto.com

"""
vSphere Python SDK program for demonstrating vSphere perfManager API based on Rbvmomi sample https://gist.github.com/toobulkeh/6124975
"""

from optparse import OptionParser, make_option
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vmodl
from pyVmomi import vim
from datetime import timedelta

import argparse
import atexit
import sys
import datetime

def GetArgs():
    """
   Supports the command-line arguments listed below.
   """
    parser = argparse.ArgumentParser(description='Process args for retrieving all the Virtual Machines')
    parser.add_argument('-s', '--host', required=True, action='store', help='Remote host to connect to')
    parser.add_argument('-o', '--port', type=int, default=443, action='store', help='Port to connect on')
    parser.add_argument('-u', '--user', required=True, action='store', help='User name to use when connecting to host')
    parser.add_argument('-p', '--password', required=True, action='store', help='Password to use when connecting to host')
    parser.add_argument('-x', '--vihost', required=True, action='store', help='Name of ESXi host as seen in vCenter Server')
    args = parser.parse_args()
    return args

def main():
    """
   Simple command-line program demonstrating vSphere perfManager API
   """

    args = GetArgs()
    try:
        si = None
        try:
            si = SmartConnect(host=args.host,
                              user=args.user,
                              pwd=args.password,
                              port=int(args.port))
        except IOError, e:
            pass
        if not si:
            print "Could not connect to the specified host using specified username and password"
            return -1

        atexit.register(Disconnect, si)

        content = si.RetrieveContent()

        searchIndex = content.searchIndex
        # quick/dirty way to find an ESXi host
        host = searchIndex.FindByDnsName(dnsName=args.vihost, vmSearch=False)

        perfManager = content.perfManager
        metricId = vim.PerformanceManager.MetricId(counterId=6, instance="*")
        startTime = datetime.datetime.now()-datetime.timedelta(hours=1)
        endTime = datetime.datetime.now()
        query = vim.PerformanceManager.QuerySpec(maxSample=1, entity=host, metricId=[metricId], startTime=startTime, endTime=endTime)
        perfResults = perfManager.QueryPerf(querySpec=[query])
        print perfResults

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