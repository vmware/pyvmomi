# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.eam.issue



class AgentIssue(pyVmomi.eam.issue.AgencyIssue):
   """
   Base class for all cluster bound agents.
   
   Attributes:
       agent: The agent that has this issue.
       cluster: The cluster for which this issue is raised.
           
           Might be null if the cluster
           is missing in vCenter Server inventory.
   """
   agent: pyVmomi.eam.Agent
   cluster: _typing.Optional[pyVmomi.vim.ComputeResource] = None

class VmNotDeployed(AgentIssue):
   """
   A cluster agent Virtual Machine is expected to be deployed on a cluster, but
   the cluster agent Virtual Machine has not been deployed or has been explicitly
   deleted from the cluster.
   
   Typically more specific issue (a subclass of this
   issue) indicates the particular reason why vSphere ESX Agent Manager was
   unable to deploy the cluster agent Virtual Machine.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   redeploys the cluster agent Virtual Machine.
   """
   pass

class CertificateNotTrusted(VmNotDeployed):
   """
   The cluster agent Virtual Machine cannot be deployed, because vSphere ESX
   Agent Manager is not able to make successful SSL trust verification of the
   server's certificate, when establishing connection to the provided
   `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl`.
   
   Reasons for this might be that the
   certificate provided via the API `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust` or via
   the script /usr/lib/vmware-eam/bin/eam-utility.py
   - is invalid.
   - does not match the server's certificate.
     
   If there is no provided certificate, the issue is raised when the server's
   certificate is not trusted by the system or invalid - @see
   `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust`.
   To remediate the cluster agent Virtual Machine deployment 1) provide a valid
   certificate used by the server hosting the
   `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl` or 2) ensure the server's certificate
   is signed by a CA trusted by the system. Then resolve this issue, vSphere ESX
   Agent Manager will retry the SSL trust verification and proceed with reaching
   the desired state.
   
   Attributes:
       url: The URL that failed the SSL trust verification.
   
   Since: vEAM API 8.2
   """
   url: str


class VmIssue(AgentIssue):
   """
   Base class for all cluster bound Virtual Machines.
   
   Attributes:
       vm: The Virtual Machine to which this issue is related.
   """
   vm: pyVmomi.vim.VirtualMachine

class HostInMaintenanceMode(VmIssue):
   """
   An agent virtual machine operation cannot be executed on host, because the
   host is in maintenance mode that blocks the virtual machine operation.
   
   This is not a remediable issue. To remediate, take the host ouf of
   maintenance mode.
   
   Since: vEAM API 8.3
   """
   pass

class HostInPartialMaintenanceMode(VmIssue):
   """
   An agent virtual machine operation cannot be executed on host, because the
   host is in partial maintenance mode that blocks the virtual machine
   operation.
   
   This is not a remediable issue. To remediate, take the host ouf of partial
   maintenance mode.
   
   Since: vEAM API 8.3
   """
   pass

class VmPoweredOff(VmIssue):
   """
   A cluster agent Virtual Machine is expected to be powered on, but the agent
   Virtual Machine is powered off.
   
   Typically more specific issue (a subclass of
   this issue) indicates the particular reason why vSphere ESX Agent Manager was
   unable to power on the cluster agent Virtual Machine.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers on the cluster agent Virtual Machine.
   """
   pass

class InsufficientClusterResources(VmPoweredOff):
   """
   The cluster agent Virtual Machine could not be powered-on, because the
   cluster does not have enough CPU or memory resources.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers on the agent Virtual Machine. However, the problem is likely to
   persist until enough CPU and memory resources are made available.
   """
   pass

class InsufficientClusterSpace(VmNotDeployed):
   """
   The cluster agent Virtual Machine cannot be deployed, because any of the
   configured datastores does not have enough disk space.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   redeploys the agent Virtual Machine. However, the problem is likely to
   persist until enough disk space is freed up on the cluster datastore.
   """
   pass

class InvalidConfig(VmIssue):
   """
   Invalid configuration is preventing a cluster agent virtual machine
   operation.
   
   Typically the attached error indicates the particular reason why
   vSphere ESX Agent Manager is unable to power on or reconfigure the agent
   virtual machine.
   
   This is a passive remediable issue. To remediate update the virtual machine
   configuration.
   
   Attributes:
       error: The error, that caused this issue.
           
           It must be either MethodFault or
           RuntimeFault.
   """
   error: object


class MissingClusterVmDatastore(VmNotDeployed):
   """
   The cluster agent Virtual Machine cannot be deployed, because any of the
   configured datastores does not exist on the cluster.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   redeploys the agent Virtual Machine. However, the problem is likely to
   persist until required Virtual Machine datastores are configured on the
   cluster.
   
   Attributes:
       missingDatastores: A non-empty array of cluster agent VM datastores that are missing on the
           cluster.
   """
   missingDatastores: list[pyVmomi.vim.Datastore] = []


class MissingClusterVmNetwork(VmNotDeployed):
   """
   The cluster agent Virtual Machine cannot be deployed, because the configured
   networks do not exist on the cluster.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   redeploys the agent Virtual Machine. However, the problem is likely to
   persist until required Virtual Machine networks are configured on the
   cluster.
   
   Attributes:
       missingNetworks: A non-empty array of cluster agent VM networks that are required on the
           cluster.
       networkNames: The names of the cluster agent VM networks.
   """
   missingNetworks: list[pyVmomi.vim.Network] = []
   networkNames: list[str] = []


class OvfInvalidProperty(AgentIssue):
   """
   A cluster agent virtual machine needs to be provisioned, but an OVF property
   is either missing or has an invalid value.
   
   This is a passive remediable issue. To remediate, update the OVF environment
   in the agent configuration used to provision the agent virtual machine.
   
   Attributes:
       error: An optional list of errors that caused this issue.
           
           These errors are
           generated by the vCenter server.
   """
   error: list[pyVmomi.vmodl.MethodFault] = []

class TransitionFailed(AgentIssue):
   """
   A cluster agent failed to be transitioned to a LCCM Solution.
   
   This is an active remediable issue. To remediate, resolve the issue via vLCM
   System VMs API
   
   Since: vEAM API 9.0
   """
   pass

class VmHookFailed(VmIssue):
   """
   The VM hook remediation failed.
   
   In order to remediate the issue:
   Resolve the issue via apply API and process the hook within the
   timeout configured for the System VM Solution this issue's VM belongs to.
   
   Since: vEAM API 9.0
   """
   pass

class VmHookTimedout(VmIssue):
   """
   The VM hook remediation timed out.
   
   In order to remediate the issue:
   Resolve the issue via apply API and process the hook within the
   timeout configured for the System VM Solution this issue's VM belongs to.
   
   Since: vEAM API 9.0
   """
   pass

class VmInaccessible(VmIssue):
   """
   The connection state of the cluster agent Virtual Machine is
   `inaccessible`.
   
   In order to remediate the issue:
   - Mark the VM for removal using the `pyVmomi.eam.EsxAgentManager.markForRemoval`
     API.
   - Do the necessary changes to ensure that the connection state of the VM is
     `connected`.
     
   NOTE: When the HA is enabled on the cluster these issues may be transient and
   automatically remediated.
   
   Since: vEAM API 8.3
   """
   pass

class VmNotRemoved(VmIssue):
   """
   The cluster agent Virtual Machine can not be removed from a cluster.
   
   Typically the description indicates the particular reason why vSphere ESX
   Agent Manager was unable to remove the cluster agent Virtual Machine.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   removes the cluster agent Virtual Machine.
   """
   pass

class VmPoweredOn(VmIssue):
   """
   A cluster agent virtual machine is expected to be powered off, but the agent
   virtual machine is powered on.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers off the agent virtual machine.
   """
   pass

class VmProtected(VmIssue):
   """
   An agent virtual machine is protected from modifications
   (example: HA recovery).
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   modifies the virtual machine.
   
   Since: vEAM API 9.0
   """
   pass

class VmSuspended(VmIssue):
   """
   A cluster agent Virtual Machine is expected to be powered on, but the agent
   Virtual Machine is suspended.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers on the cluster agent Virtual Machine.
   """
   pass
