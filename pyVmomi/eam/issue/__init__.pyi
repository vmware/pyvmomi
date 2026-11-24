# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl


class AgencyDisabled(AgencyIssue):
   pass


class AgencyIssue(Issue):
   agency: pyVmomi.eam.Agency
   agencyName: str
   solutionId: str
   solutionName: str


class AgentIssue(AgencyIssue):
   agent: pyVmomi.eam.Agent
   agentName: str
   host: pyVmomi.vim.HostSystem
   hostName: str

class CannotAccessAgentOVF(VmNotDeployed):
   downloadUrl: str

class CannotAccessAgentVib(VibNotInstalled):
   downloadUrl: str

class CertificateNotTrusted(AgentIssue):
   url: str


class ExtensibleIssue(Issue):
   typeId: str
   argument: list[pyVmomi.vmodl.KeyAnyValue] = []
   target: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   agent: _typing.Optional[pyVmomi.eam.Agent] = None
   agency: _typing.Optional[pyVmomi.eam.Agency] = None

class HostInMaintenanceMode(VmDeployed):
   pass


class HostInPartialMaintenanceMode(AgentIssue):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None

class HostInStandbyMode(VmDeployed):
   pass


class HostIssue(Issue):
   host: pyVmomi.vim.HostSystem

class HostNotReachable(AgentIssue):
   pass

class HostPoweredOff(VmDeployed):
   pass

class ImmediateHostRebootRequired(VibIssue):
   pass

class IncompatibleHostVersion(VmNotDeployed):
   pass


class InsufficientIpAddresses(VmPoweredOff):
   network: pyVmomi.vim.Network

class InsufficientResources(VmNotDeployed):
   pass

class InsufficientSpace(VmNotDeployed):
   pass

class InvalidConfig(VmIssue):
   error: object


class Issue(pyVmomi.vmodl.DynamicData):
   key: int
   description: str
   time: _datetime.datetime


class MissingAgentIpPool(VmPoweredOff):
   network: pyVmomi.vim.Network

class MissingDvFilterSwitch(AgentIssue):
   pass

class NoAgentVmDatastore(VmNotDeployed):
   pass

class NoAgentVmNetwork(VmNotDeployed):
   pass


class NoCustomAgentVmDatastore(NoAgentVmDatastore):
   customAgentVmDatastore: list[pyVmomi.vim.Datastore] = []
   customAgentVmDatastoreName: list[str] = []


class NoCustomAgentVmNetwork(NoAgentVmNetwork):
   customAgentVmNetwork: list[pyVmomi.vim.Network] = []
   customAgentVmNetworkName: list[str] = []

class NoDiscoverableAgentVmDatastore(VmNotDeployed):
   pass

class NoDiscoverableAgentVmNetwork(VmNotDeployed):
   pass

class OrphanedAgency(AgencyIssue):
   pass

class OrphanedDvFilterSwitch(HostIssue):
   pass


class OvfInvalidFormat(VmNotDeployed):
   error: list[pyVmomi.vmodl.MethodFault] = []


class OvfInvalidProperty(AgentIssue):
   error: list[pyVmomi.vmodl.MethodFault] = []

class TransitionFailed(AgentIssue):
   pass


class UnknownAgentVm(HostIssue):
   vm: pyVmomi.vim.VirtualMachine

class VibCannotPutHostInMaintenanceMode(VibIssue):
   pass

class VibCannotPutHostOutOfMaintenanceMode(VibIssue):
   pass

class VibDependenciesNotMetByHost(VibNotInstalled):
   pass

class VibInvalidFormat(VibNotInstalled):
   pass

class VibIssue(AgentIssue):
   pass

class VibNotInstalled(VibIssue):
   pass

class VibRequirementsNotMetByHost(VibNotInstalled):
   pass

class VibRequiresHostInMaintenanceMode(VibIssue):
   pass

class VibRequiresHostReboot(VibIssue):
   pass

class VibRequiresManualInstallation(VibIssue):
   bulletin: list[str] = []

class VibRequiresManualUninstallation(VibIssue):
   bulletin: list[str] = []


class VmCorrupted(VmIssue):
   missingFile: _typing.Optional[str] = None

class VmDeployed(VmIssue):
   pass

class VmHookFailed(VmIssue):
   pass

class VmHookTimedout(VmIssue):
   pass

class VmInaccessible(VmIssue):
   pass


class VmIssue(AgentIssue):
   vm: pyVmomi.vim.VirtualMachine

class VmMarkedAsTemplate(VmIssue):
   pass

class VmNotDeployed(AgentIssue):
   pass

class VmOrphaned(VmIssue):
   pass

class VmPoweredOff(VmIssue):
   pass

class VmPoweredOn(VmIssue):
   pass

class VmProtected(VmIssue):
   pass

class VmRequiresHostOutOfMaintenanceMode(VmNotDeployed):
   pass

class VmSuspended(VmIssue):
   pass


class VmWrongFolder(VmIssue):
   currentFolder: pyVmomi.vim.Folder
   requiredFolder: pyVmomi.vim.Folder


class VmWrongResourcePool(VmIssue):
   currentResourcePool: pyVmomi.vim.ResourcePool
   requiredResourcePool: pyVmomi.vim.ResourcePool
