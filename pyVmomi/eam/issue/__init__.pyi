# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl



class Issue(pyVmomi.vmodl.DynamicData):
   """
   An issue represents a problem encountered while deploying and configuring agents
   in a vCenter installation.
   
   An issue conveys the type of problem and the
   entity on which the problem has been encountered. Most issues are related to agents,
   but they can also relate to an agency or a host.
   
   The set of issues provided by the vSphere ESX Agent Manager describes the discrepancy between
   the desired agent deployment state, as defined by the agency configurations,
   and the actual deployment. The (@link EamObject.RuntimeInfo.Status.status)
   of an agency or agent is green if it has reached its goal state. It is
   marked as yellow if the vSphere ESX Agent Manager is actively working to bring the object
   to its goal state. It is red if there is a discrepancy between the current state and
   the desired state. In the red state, a set of issues are filed on the object that
   describe the reason for the discrepancy between the desired and actual states.
   
   Issues are characterized as either active or passive remediable issues. For an active
   remediable issue, the vSphere ESX Agent Manager can actively try to solve the issue. For
   example, by deploying a new agent, removing an agent, changing its power state, and so
   on. For a passive remediable issue, the vSphere ESX Agent Manager is not able to solve the
   problem directly, and can only report the problem. For example, this could be
   caused by an incomplete host configuration.
   
   When `resolve` is called for an active remediable issue, the vSphere ESX Agent Manager
   starts performing the appropriate remediation steps for the particular issue. For a passive
   remediable issue, the EAM manager simply checks if the condition
   still exists, and if not it removes the issue.
   
   The vSphere ESX Agent Manager actively monitors most conditions relating to both
   active and passive issues. Thus, it often automatically discovers when an
   issue has been remediated and removes the issue without needing to explicitly
   call `resolve` on an issue.
   
   The complete Issue hierarchy is shown below:
   - `pyVmomi.eam.issue.Issue`
     - `pyVmomi.eam.issue.AgencyIssue`
       - `pyVmomi.eam.issue.AgentIssue`
       - `pyVmomi.eam.issue.HostNotReachable`
         - `pyVmomi.eam.issue.VmNotDeployed`
           - `pyVmomi.eam.issue.CannotAccessAgentOVF`
           - `pyVmomi.eam.issue.IncompatibleHostVersion`
           - `pyVmomi.eam.issue.InsufficientResources`
           - `pyVmomi.eam.issue.InsufficientSpace`
           - `pyVmomi.eam.issue.OvfInvalidFormat`
           - `pyVmomi.eam.issue.NoAgentVmDatastore`
           - `pyVmomi.eam.issue.NoAgentVmNetwork`
         - `pyVmomi.eam.issue.VmIssue`
           - `pyVmomi.eam.issue.OvfInvalidProperty`
           - `pyVmomi.eam.issue.VmDeployed`
             - `pyVmomi.eam.issue.HostInMaintenanceMode`
             - `pyVmomi.eam.issue.HostInStandbyMode`
           - `pyVmomi.eam.issue.VmCorrupted`
           - `pyVmomi.eam.issue.VmOrphaned`
           - `pyVmomi.eam.issue.VmPoweredOff`
             - `pyVmomi.eam.issue.InsufficientIpAddresses`
             - `pyVmomi.eam.issue.MissingAgentIpPool`
           - `pyVmomi.eam.issue.VmPoweredOn`
           - `pyVmomi.eam.issue.VmSuspended`
         - `pyVmomi.eam.issue.VibIssue`
           - `pyVmomi.eam.issue.VibCannotPutHostInMaintenanceMode`
           - `pyVmomi.eam.issue.VibNotInstalled`
             - `pyVmomi.eam.issue.CannotAccessAgentVib`
             - `pyVmomi.eam.issue.VibDependenciesNotMetByHost`
             - `pyVmomi.eam.issue.VibInvalidFormat`
             - `pyVmomi.eam.issue.VibRequirementsNotMetByHost`
           - `pyVmomi.eam.issue.VibRequiresHostInMaintenanceMode`
           - `pyVmomi.eam.issue.VibRequiresHostReboot`
           - `pyVmomi.eam.issue.VibRequiresManualInstallation`
           - `pyVmomi.eam.issue.VibRequiresManualUninstallation`
           - `pyVmomi.eam.issue.ImmediateHostRebootRequired`
       - `pyVmomi.eam.issue.OrphanedAgency`
       - `pyVmomi.eam.issue.integrity.agency.VUMIssue`
         - `pyVmomi.eam.issue.integrity.agency.VUMUnavailable`
         - `pyVmomi.eam.issue.integrity.agency.CannotStageSoftware`
         - `pyVmomi.eam.issue.integrity.agency.CannotDeleteSoftware`
       - `pyVmomi.eam.issue.cluster.agent.AgentIssue`
         - `pyVmomi.eam.issue.cluster.agent.VmIssue`
           - `pyVmomi.eam.issue.cluster.agent.VmNotRemoved`
           - `pyVmomi.eam.issue.cluster.agent.VmPoweredOff`
             - `pyVmomi.eam.issue.cluster.agent.InsufficientClusterResources`
         - `pyVmomi.eam.issue.cluster.agent.VmNotDeployed`
           - `pyVmomi.eam.issue.cluster.agent.InsufficientClusterSpace`
           - `pyVmomi.eam.issue.cluster.agent.MissingClusterVmDatastore`
           - `pyVmomi.eam.issue.cluster.agent.MissingClusterVmNetwork`
             
   See Also: `pyVmomi.eam.EamObject.resolve`, `pyVmomi.eam.EamObject.resolveAll`
   
   Attributes:
       key: A unique identifier per `Issue` instance.
       description: A localized message describing the issue.
       time: The point in time when this issue was generated.
           
           Note that issues can be
           regenerated periodically, so this time does not necessarily reflect the
           first time the issue was detected.
   """
   key: int
   description: str
   time: _datetime.datetime


class AgencyIssue(Issue):
   """
   Base class for all agency issues.
   
   Attributes:
       agency: The agency to which this issue belongs.
       agencyName: The name of the agency.
       solutionId: The ID of the solution to which this issue belongs.
       solutionName: The name of the solution to which this issue belongs.
   """
   agency: pyVmomi.eam.Agency
   agencyName: str
   solutionId: str
   solutionName: str

class AgencyDisabled(AgencyIssue):
   """
   Agency is disabled - one or more ClusterComputeResources from it's scope are
   disabled.
   
   This is not a remediable issue. To remediate, re-enable the cluster.
   
   Since: vEAM API 7.6
   """
   pass


class AgentIssue(AgencyIssue):
   """
   Base class for all agent issues.
   
   Attributes:
       agent: The agent that has this issue.
       agentName: The name of the agent.
       host: The managed object reference to the host on which this agent is located.
       hostName: The name of the host on which this agent is located.
   """
   agent: pyVmomi.eam.Agent
   agentName: str
   host: pyVmomi.vim.HostSystem
   hostName: str

class VmNotDeployed(AgentIssue):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent virtual machine has not
   been deployed.
   
   Typically, a more specific issue (a subclass of this issue)
   indicates the particular reason why vSphere ESX Agent Manager was unable to deploy the
   agent, such as being unable to access the OVF package for the agent or a missing host
   configuration. This issue can also happen if the agent virtual machine is explicitly deleted
   from the host.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeploys the agent virtual machine.
   """
   pass

class CannotAccessAgentOVF(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent virtual machine
   cannot be deployed because the vSphere ESX Agent Manager is unable to access the OVF
   package for the agent.
   
   This typically happens because the Web server providing the
   OVF package is down. The Web server is often internal to the solution
   that created the Agency.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeploys the agent.
   
   Attributes:
       downloadUrl: The URL from which the OVF could not be downloaded.
   """
   downloadUrl: str

class VibIssue(AgentIssue):
   """Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Base class for all issues related to the VIB modules that belong to an agent."""
   pass

class VibNotInstalled(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module is expected to be installed/removed on a host, but it has not
   been installed/removed.
   
   Typically, a more specific issue (a subclass of this
   issue) indicates the particular reason why the VIB module operation failed.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   attempts the VIB operation again.
   In case of unreachable host vSphere ESX Agent Manager will remediate the
   issue automatically when the host becomes reachable.
   """
   pass

class CannotAccessAgentVib(VibNotInstalled):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.An agent VIB module is expected to be deployed on a host, but the VIM module
   cannot be deployed because the vSphere ESX Agent Manager is unable to access the VIB
   package for the agent.
   
   This typically happens because the Web server providing the
   VIB package is down. The Web server is often internal to the solution
   that created the Agency.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager reinstalls the VIB module.
   
   Attributes:
       downloadUrl: The URL from which the VIB package could not be downloaded.
   """
   downloadUrl: str

class CertificateNotTrusted(AgentIssue):
   """
   The agent Virtual Machine deployment or agent VIB module installation cannot
   be done, because vSphere ESX Agent Manager is not able to make successful SSL
   trust verification of the server's certificate, when establishing connection
   to the provided `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl` or
   `pyVmomi.eam.Agent.ConfigInfo.vibUrl`.
   
   Reasons for this might be that the
   certificate provided via the API `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust` and
   `pyVmomi.eam.Agent.ConfigInfo.vibSslTrust` or via the script
   /usr/lib/vmware-eam/bin/eam-utility.py
   - is invalid.
   - does not match the server's certificate.
     
   If there is no provided certificate, the issue is raised when the server's
   certificate is not trusted by the system or is invalid - @see
   `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust` and
   `pyVmomi.eam.Agent.ConfigInfo.vibSslTrust`.
   To remediate the agent Virtual Machine deployment or agent VIB module
   installation 1) provide a valid certificate used by the server hosting the
   `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl` or `pyVmomi.eam.Agent.ConfigInfo.vibUrl` or
   2\\) ensure the server's certificate is signed by a CA trusted by the system.
   Then resolve this issue, vSphere ESX Agent Manager will retry the SSL trust
   verification and proceed with reaching the desired state.
   
   Attributes:
       url: The URL that failed the SSL trust verification.
   
   Since: vEAM API 8.2
   """
   url: str


class ExtensibleIssue(Issue):
   """
   Deprecated: as of vSphere 9.0. No longer in use since vSphee 6.5.Extensible issue class used by solutions to add custom issues to agents.
   
   When resolved, the issue is removed from the agent and an event is generated.
   
   Attributes:
       typeId: Unique string for this type of issue.
           
           The type must match an event registered
           by the solution as part of its extension.
       argument: Arguments associated with the typeId.
       target: A managed object reference to the object this issue is related to.
       agent: An optional agent this issue pertains
       agency: An optional agency this issue pertains
   """
   typeId: str
   argument: list[pyVmomi.vmodl.KeyAnyValue] = []
   target: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   agent: _typing.Optional[pyVmomi.eam.Agent] = None
   agency: _typing.Optional[pyVmomi.eam.Agency] = None


class VmIssue(AgentIssue):
   """
   Base class for all issues related to the deployed virtual machine for a
   particular agent.
   
   Attributes:
       vm: The virtual machine to which this issue is related.
   """
   vm: pyVmomi.vim.VirtualMachine

class VmDeployed(VmIssue):
   """
   An agent virtual machine is expected to be removed from a host, but the agent virtual machine has not
   been removed.
   
   Typically, a more specific issue (a subclass of this issue)
   indicates the particular reason why vSphere ESX Agent Manager was unable to remove the
   agent virtual machine, such as the host is in maintenance mode, powered off or in standby
   mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeploys the agent.
   """
   pass

class HostInMaintenanceMode(VmDeployed):
   """
   An agent virtual machine operation is expected to be initiated on host, but
   the agent virtual machine operation has not been initiated.
   
   The reason is
   that the host is in maintenance mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   takes the host out of maintenance mode and initiates the agent virtual
   machine operation.
   
   Resolving this issue in vSphere Lifecycle Manager environment will be no-op.
   In those cases user must take the host out of Maintenance Mode manually or
   wait vSphere Lifecycle Manager cluster remediation to complete (if any).
   """
   pass


class HostInPartialMaintenanceMode(AgentIssue):
   """
   An agent virtual machine operation cannot be executed on host, because the
   host is in partial maintenance mode that blocks the virtual machine
   operation.
   
   This is not a remediable issue. To remediate, take the host ouf of partial
   maintenance mode.
   
   Attributes:
       vm: The virtual machine to which this issue is related.
           
           Unset if the
           operation that is blocked by partial maintenance mode is preventing the
           virtual machine deployment.
   
   Since: vEAM API 8.3
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None

class HostInStandbyMode(VmDeployed):
   """
   An agent virtual machine is expected to be removed from a host, but the agent virtual machine has not
   been removed.
   
   The reason is that the host is in standby mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager puts the host in standby mode
   and removes the agent virtual machine.
   """
   pass


class HostIssue(Issue):
   """
   Deprecated: All host issues were removed.Base class for all host issues.
   
   Attributes:
       host: The host to which the issue is related.
   """
   host: pyVmomi.vim.HostSystem

class HostNotReachable(AgentIssue):
   """
   Managed ESXi Server is unreachable from vCenter Server or vSphere ESX Agent
   Manager.
   
   Currently all operations on the affected host are impossible. Reasons
   for this might be :
   - ESXi Server is not connected from vCenter Server
   - ESXi Server powered off
     
   This is not a remediable issue. To remediate, connect, power on or reboot the
   host.
   """
   pass

class HostPoweredOff(VmDeployed):
   """
   Deprecated: HostPoweredOff will no longer be used, instead
   `pyVmomi.eam.issue.HostNotReachable` will be raised.An agent virtual machine is expected to be removed from a host, but the agent
   virtual machine has not been removed.
   
   The reason is that the host is powered
   off.
   
   This is not a remediable issue. To remediate, power on the host.
   """
   pass

class ImmediateHostRebootRequired(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Live VIB operation failed.
   
   An immediate reboot is required to clear live VIB
   operation failure.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   puts the host into maintenance mode and reboots it.
   """
   pass

class IncompatibleHostVersion(VmNotDeployed):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An agent virtual machine is expected to be deployed on a host, but the agent could not be
   deployed because it was incompatible with the host.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeployes the agent. However,
   the problem is likely to persist until either the host or the solution has been
   upgraded, so that the agent will become compatible with the host.
   """
   pass

class VmPoweredOff(VmIssue):
   """
   An agent virtual machine is expected to be powered on, but the agent virtual machine is powered off.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers on the agent virtual machine.
   """
   pass


class InsufficientIpAddresses(VmPoweredOff):
   """
   Deprecated: This issue is no longer raised by EAM. It is replaced by
   `pyVmomi.eam.issue.InvalidConfig`.An agent virtual machine is expected to be powered on, but there are no free IP addresses in the
   agent's pool of virtual machine IP addresses.
   
   To remediate, free some IP addresses or add some more to the IP pool and invoke
   `resolve`.
   
   Attributes:
       network: The agent virtual machine network.
   """
   network: pyVmomi.vim.Network

class InsufficientResources(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent virtual machine could not be
   deployed because the host does not have enough free CPU or memory resources.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeploys the agent virtual machine. However,
   the problem is likely to persist until enough CPU and memory resources are made available.
   """
   pass

class InsufficientSpace(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent virtual machine could not be
   deployed because the host's agent datastore did not have enough free space.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager redeploys the agent virtual machine. However,
   the problem is likely to persist until either space is freed up on the host's agent
   virtual machine datastore or a new agent virtual machine datastore with enough free space is configured.
   """
   pass

class InvalidConfig(VmIssue):
   """
   Invalid configuration is preventing a virtual machine operation.
   
   Typically
   the attached error indicates the particular reason why vSphere ESX Agent
   Manager is unable to power on or reconfigure the agent virtual machine.
   
   This is a passive remediable issue. To remediate update the virtual machine
   configuration.
   
   Attributes:
       error: The error, that caused this issue.
           
           It must be either MethodFault or
           RuntimeFault.
   """
   error: object


class MissingAgentIpPool(VmPoweredOff):
   """
   Deprecated: This issue is no longer raised by EAM. It is replaced by
   `pyVmomi.eam.issue.InvalidConfig`.An agent virtual machine is expected to be powered on, but the agent virtual machine is powered off because
   there there are no IP addresses defined on the agent's virtual machine network.
   
   To remediate, create an IP pool on the agent's virtual machine network and invoke `resolve`.
   
   Attributes:
       network: The agent virtual machine network.
   """
   network: pyVmomi.vim.Network

class MissingDvFilterSwitch(AgentIssue):
   """
   Deprecated: DvFilters are no longer supported by EAM.The agent is using the dvFilter API on the ESX host, but no dvFilter switch
   has been configured on the host.
   
   This can happen due to host communication
   failures or if the dvSwitch was (presumably accidentally) deleted from the
   host configuration.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   recreates the dvFilter switch.
   """
   pass

class NoAgentVmDatastore(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent cannot be
   deployed because the agent datastore has not been configured on the host.
   
   This is a passive remediable issue. The administrator must configure
   the agent virtual machine datastore on the host.
   """
   pass

class NoAgentVmNetwork(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent cannot be
   deployed because the agent network has not been configured on the host.
   
   This is a passive remediable issue. The administrator must configure
   the agent virtual machine network on the host.
   """
   pass


class NoCustomAgentVmDatastore(NoAgentVmDatastore):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent cannot be
   deployed because the agent datastore has not been configured on the host.
   
   The host
   needs to be added to one of the datastores listed in customAgentVmDatastore.
   
   This is a passive remediable issue. The administrator must add one of the datastores
   customAgentVmDatastore to the host.
   
   Attributes:
       customAgentVmDatastore: A non-empty array of agent VM datastores that is required on the host.
       customAgentVmDatastoreName: The names of the agent VM datastores.
   """
   customAgentVmDatastore: list[pyVmomi.vim.Datastore] = []
   customAgentVmDatastoreName: list[str] = []


class NoCustomAgentVmNetwork(NoAgentVmNetwork):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent cannot be
   deployed because the agent network has not been configured on the host.
   
   The host
   needs to be added to one of the networks listed in customAgentVmNetwork.
   
   This is a passive remediable issue. The administrator must add one of the networks
   customAgentVmNetwork to the host.
   
   Attributes:
       customAgentVmNetwork: A non-empty array of agent VM networks that is required on the host.
       customAgentVmNetworkName: The names of the agent VM networks.
   """
   customAgentVmNetwork: list[pyVmomi.vim.Network] = []
   customAgentVmNetworkName: list[str] = []

class NoDiscoverableAgentVmDatastore(VmNotDeployed):
   """
   Deprecated: as of vSphere 9.0. No longer in use since vCLS 2.0.An agent virtual machine is expected to be deployed on a host, but the
   agent cannot be deployed because the agent VM datastore could not be
   discovered, as per defined selection policy, on the host.
   
   This issue can be remediated passively if the administrator configures
   new datastores on the host.
   """
   pass

class NoDiscoverableAgentVmNetwork(VmNotDeployed):
   """
   Deprecated: as of vSphere 9.0. No longer in use since vCLS 2.0.An agent virtual machine is expected to be deployed on a host, but the
   agent cannot be deployed because the agent VM network could not be
   discovered, as per defined selection policy, on the host.
   
   This issue can be remediated passively if the administrator configures
   new networks on the host.
   """
   pass

class OrphanedAgency(AgencyIssue):
   """
   Deprecated: EAM no longer raises this issue. If agecny is getting orphaned
   EAM simply destroys it.The solution that created the agency is no longer registered with the vCenter
   server.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   undeploys and removes the agency.
   """
   pass

class OrphanedDvFilterSwitch(HostIssue):
   """
   Deprecated: DvFilters are no longer supported by EAM.A dvFilter switch exists on a host but no agents on the host depend on
   dvFilter.
   
   This typically happens if a host is disconnected when an agency
   configuration changed.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   removes the dvFilterSwitch.
   """
   pass


class OvfInvalidFormat(VmNotDeployed):
   """
   An Agent virtual machine is expected to be provisioned on a host, but it failed to do so
   because the provisioning of the OVF package failed.
   
   The provisioning is unlikely to
   succeed until the solution that provides the OVF package has been upgraded or
   patched to provide a valid OVF package for the agent virtual machine.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager attempts the OVF provisioning again.
   
   Attributes:
       error: An optional list of errors that caused this issue.
           
           These errors are generated by the
           vCenter server.
   """
   error: list[pyVmomi.vmodl.MethodFault] = []


class OvfInvalidProperty(AgentIssue):
   """
   An agent virtual machine needs to be provisioned or reconfigured, but an OVF
   property is either missing or has an invalid value.
   
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
   An agent failed to be transitioned to a LCCM Solution.
   
   This is an active remediable issue. To remediate, resolve the issue via vLCM
   System VMs API
   
   Since: vEAM API 9.0
   """
   pass


class UnknownAgentVm(HostIssue):
   """
   Deprecated: Presence of unknown VMs is no more acceptableAn agent virtual machine has been found in the vCenter inventory that does
   not belong to any agency in this vSphere ESX Agent Manager server instance.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   powers off (if powered on) and deletes the agent virtual machine.
   
   Attributes:
       vm: The unknown agent virtual machine.
   """
   vm: pyVmomi.vim.VirtualMachine

class VibCannotPutHostInMaintenanceMode(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module requires the host to be in maintenance mode, but the vSphere ESX Agent Manager
   is unable toput the host in maintenance mode.
   
   This can happen if there are virtual machines running on the host that cannot
   be moved and must be stopped before the host can enter maintenance mode.
   
   This is an active remediable issue. To remediate, the vSphere ESX Agent Manager will try again
   to put the host into maintenance mode. However, the vSphere ESX Agent Manager will not power
   off or move any virtual machines to put the host into maintenance mode. This must be
   done by the client.
   """
   pass

class VibCannotPutHostOutOfMaintenanceMode(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.ESXi host is in Maintenance Mode.
   
   This prevents powering on and
   re-configuring Agent Virtual Machines. Also if the host's entering in
   Maintenance Mode was initiated by vSphere Esx Agent Manager, the same is
   responsible to initiate exit Maintenance Mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   puts the host out of Maintenance Mode.
   """
   pass

class VibDependenciesNotMetByHost(VibNotInstalled):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module is expected to be installed on a host, but the dependencies,
   describred within the module, were not satisfied by the host.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   attempts the VIB installation again.
   """
   pass

class VibInvalidFormat(VibNotInstalled):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module is expected to be installed on a host, but it failed to install
   since the VIB package is in an invalid format.
   
   The installation is unlikely to
   succeed until the solution providing the bundle has been upgraded or patched to
   provide a valid VIB package.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager attempts the VIB installation again.
   """
   pass

class VibRequirementsNotMetByHost(VibNotInstalled):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module is expected to be installed on a host, but the system
   requirements, describred within the module, were not satisfied by the host.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   attempts the VIB installation again.
   """
   pass

class VibRequiresHostInMaintenanceMode(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module has been uploaded to the host, but will not be fully installed
   until the host has been put in maintenance mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager puts the host into maintenance
   mode.
   """
   pass

class VibRequiresHostReboot(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module has been uploaded to the host, but will not be activated
   until the host is rebooted.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager puts the host into maintenance
   mode and reboots it.
   """
   pass

class VibRequiresManualInstallation(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module failed to install, but failed to do so because automatic installation
   by vSphere ESX Agent Manager is not allowed on the host.
   
   This is a passive remediable issue. To remediate, go to VMware Update Manager
   and install the required bulletins on the host or add the bulletins to the
   host's image profile.
   
   Attributes:
       bulletin: A non-empty array of bulletins required to be installed on the host.
   """
   bulletin: list[str] = []

class VibRequiresManualUninstallation(VibIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A VIB module failed to uninstall, but failed to do so because automatic uninstallation
   by vSphere ESX Agent Manager is not allowed on the host.
   
   This is a passive remediable issue. To remediate, go to VMware Update Manager
   and uninstall the required bulletins on the host or remove the bulletins from the
   host's image profile.
   
   Attributes:
       bulletin: A non-empty array of bulletins required to be uninstalled on the host.
   """
   bulletin: list[str] = []


class VmCorrupted(VmIssue):
   """
   An agent virtual machine is corrupted.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager deletes and
   reprovisions the agent virtual machine. To remediate manually, fix the missing file issue and power on the
   agent virtual machine.
   
   Attributes:
       missingFile: An optional path for a missing file.
   """
   missingFile: _typing.Optional[str] = None

class VmHookFailed(VmIssue):
   """
   The VM hook remediation failed.
   
   In order to remediate the issue:
   Resolve the issue via vLCM System VMs API and process the hook within the
   timeout configured for the System VM Solution this issue's VM belongs to.
   
   Since: vEAM API 9.0
   """
   pass

class VmHookTimedout(VmIssue):
   """
   The VM hook remediation timed out.
   
   In order to remediate the issue:
   Resolve the issue via vLCM System VMs API and process the hook within the
   timeout configured for the System VM Solution this issue's VM belongs to.
   
   Since: vEAM API 9.0
   """
   pass

class VmInaccessible(VmIssue):
   """
   The connection state of the agent Virtual Machine is
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

class VmMarkedAsTemplate(VmIssue):
   """
   Deprecated: template agent VMs are not used anymore by VM deployment and
   monitoringAn agent virtual machine is a virtual machine template.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   converts the agent virtual machine template to a virtual machine.
   """
   pass

class VmOrphaned(VmIssue):
   """
   An agent virtual machine exists on a host, but the host is no longer part of scope for the
   agency.
   
   This typically happens if a host is disconnected when the agency
   configuration is changed.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager deletes the agent virtual machine.
   """
   pass

class VmPoweredOn(VmIssue):
   """
   An agent virtual machine is expected to be powered off, but the agent virtual machine is powered on.
   
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

class VmRequiresHostOutOfMaintenanceMode(VmNotDeployed):
   """
   An agent virtual machine is expected to be deployed on a host, but the agent
   virtual machine cannot be deployed because the host is in Maintenance Mode.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   takes the host out of Maintenance Mode and deploys the agent virtual machine.
   
   Resolving this issue in vSphere Lifecycle Manager environment will be no-op.
   In those cases user must take the host out of Maintenance Mode manually or
   wait vSphere Lifecycle Manager cluster remediation to complete (if any).
   
   Since: vEAM API 7.2
   """
   pass

class VmSuspended(VmIssue):
   """
   An agent virtual machine is expected to be powered on, but the agent virtual machine is suspended.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager powers on the agent virtual machine.
   """
   pass


class VmWrongFolder(VmIssue):
   """
   Deprecated: EAM does not try to override any action powerful user has takenAn agent virtual machine is expected to be located in a designated agent
   virtual machine folder, but is found in a different folder.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   moves the agent virtual machine back into the designated agent folder.
   
   Attributes:
       currentFolder: The folder in which the virtual machine currently resides.
       requiredFolder: The ESX agent folder in which the virtual machine should reside.
   """
   currentFolder: pyVmomi.vim.Folder
   requiredFolder: pyVmomi.vim.Folder


class VmWrongResourcePool(VmIssue):
   """
   Deprecated: EAM does not try to override any action powerful user has takenAn agent virtual machine is expected to be located in a designated agent
   virtual machine resource pool, but is found in a different resource pool.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   moves the agent virtual machine back into the designated agent resource pool.
   
   Attributes:
       currentResourcePool: The resource pool in which the VM currently resides.
       requiredResourcePool: The ESX agent resource pool in which the VM should reside.
   """
   currentResourcePool: pyVmomi.vim.ResourcePool
   requiredResourcePool: pyVmomi.vim.ResourcePool
