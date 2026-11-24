# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.eam.issue



class AgentIssue(pyVmomi.eam.issue.AgencyIssue):
   agent: pyVmomi.eam.Agent
   cluster: _typing.Optional[pyVmomi.vim.ComputeResource] = None

class CertificateNotTrusted(VmNotDeployed):
   url: str

class HostInMaintenanceMode(VmIssue):
   pass

class HostInPartialMaintenanceMode(VmIssue):
   pass

class InsufficientClusterResources(VmPoweredOff):
   pass

class InsufficientClusterSpace(VmNotDeployed):
   pass

class InvalidConfig(VmIssue):
   error: object


class MissingClusterVmDatastore(VmNotDeployed):
   missingDatastores: list[pyVmomi.vim.Datastore] = []


class MissingClusterVmNetwork(VmNotDeployed):
   missingNetworks: list[pyVmomi.vim.Network] = []
   networkNames: list[str] = []


class OvfInvalidProperty(AgentIssue):
   error: list[pyVmomi.vmodl.MethodFault] = []

class TransitionFailed(AgentIssue):
   pass

class VmHookFailed(VmIssue):
   pass

class VmHookTimedout(VmIssue):
   pass

class VmInaccessible(VmIssue):
   pass


class VmIssue(AgentIssue):
   vm: pyVmomi.vim.VirtualMachine

class VmNotDeployed(AgentIssue):
   pass

class VmNotRemoved(VmIssue):
   pass

class VmPoweredOff(VmIssue):
   pass

class VmPoweredOn(VmIssue):
   pass

class VmProtected(VmIssue):
   pass

class VmSuspended(VmIssue):
   pass
