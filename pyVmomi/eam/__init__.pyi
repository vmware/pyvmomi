# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import issue as issue
from . import vib as vib

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.eam.issue
import pyVmomi.eam.vib
import pyVmomi.vim.vApp



class EamObject(pyVmomi.VmomiSupport.ManagedObject):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Base class for the `Agent`, `Agency` and
   `EsxAgentManager` classes.
   """
   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.The `RuntimeInfo` represents the runtime information of the vSphere ESX Agent
      Manager managed
      objects `pyVmomi.eam.Agency` and `pyVmomi.eam.Agent`.
      
      The runtime information provides
      two kinds of information, namely, the
      desired goal state of the entity and the status with regards to conforming
      to that goal state.
      
      Attributes:
          status: The health of the managed entity.
              
              This denotes how well the entity conforms to the
              goal state.
          issue: Current issues that have been detected for this entity.
              
              Each issue can be remediated
              by invoking `pyVmomi.eam.EamObject.resolve` or `pyVmomi.eam.EamObject.resolveAll`.
          goalState: The desired state of the entity.
          entity: The `pyVmomi.eam.Agent` or `pyVmomi.eam.Agency` with which this `RuntimeInfo` object is associated.
      """
      class Status(pyVmomi.VmomiSupport.Enum):
         """
         Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.`Status` defines a health value that denotes how well the entity
         conforms to the goal state.
         
         Attributes:
             green: The entity is in perfect compliance with the goal state.
             yellow: The entity is actively working to reach the desired goal state.
             red: The entity has reached an issue which prevents it from reaching the desired goal
                 state.
                 
                 To remediate any offending issues, look at `pyVmomi.eam.EamObject.RuntimeInfo.issue`
                 and use either `pyVmomi.eam.EamObject.resolve` or
                 `pyVmomi.eam.EamObject.resolveAll`.
         """
         green: _typing.ClassVar['EamObject.RuntimeInfo.Status'] = 'green'
         yellow: _typing.ClassVar['EamObject.RuntimeInfo.Status'] = 'yellow'
         red: _typing.ClassVar['EamObject.RuntimeInfo.Status'] = 'red'

      class GoalState(pyVmomi.VmomiSupport.Enum):
         """
         Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.The `GoalState` enumeration defines the goal of the entity.
         
         Attributes:
             enabled: The entity should be fully deployed and active.
                 
                 If the entity is an
                 `pyVmomi.eam.Agency`, it should install VIBs and deploy and power on all agent
                 virtual machines. If the entity is an `pyVmomi.eam.Agent`, its VIB should be installed and its
                 agent virtual machine should be deployed and powered on.
             disabled: The entity should be fully deployed but inactive.
                 
                 f the entity is an
                 `pyVmomi.eam.Agency`, the behavior is similar to the `enabled` goal state, but
                 agents are not powered on (if they have been powered on they are powered
                 off).
             uninstalled: The entity should be completely removed from the vCenter Server.
                 
                 If the entity is an
                 `pyVmomi.eam.Agency`, no more VIBs or agent virtual machines are deployed. All installed VIBs
                 installed by the `pyVmomi.eam.Agency` are uninstalled and any deployed agent virtual machines
                 are powered off (if they have been powered on) and deleted.
                 If the entity is an `pyVmomi.eam.Agent`, its VIB is uninstalled and the virtual machine is
                 powered off and deleted.
         """
         enabled: _typing.ClassVar['EamObject.RuntimeInfo.GoalState'] = 'enabled'
         disabled: _typing.ClassVar['EamObject.RuntimeInfo.GoalState'] = 'disabled'
         uninstalled: _typing.ClassVar['EamObject.RuntimeInfo.GoalState'] = 'uninstalled'

      status: str
      issue: list[pyVmomi.eam.issue.Issue] = []
      goalState: str
      entity: EamObject

   def Resolve(self, issueKey: list[int]) -> list[int]:
      """
      Resolves the issues specified in the input.
      
      If an issue is remediable, ESX
      Agent Manager
      tries to resolve the misconfiguration that caused the issue. If it is not
      remediable, the offending issue is removed and ESX Agent Manager assumes that the issue has been
      resolved.
      
      Requires modify privileges.
      
      See Also: `pyVmomi.eam.issue.Issue`
      
      Args:
          issueKey: A non-empty array of issue keys.
      
      Returns:
          A possibly empty array of issue keys for the issues that were not found on the
          entity. This can happen if `resolve` is called with issue keys that were
          resolved just prior to calling `resolve` or if an issue is currently not resolvable.
      """
      ...
   def ResolveAll(self) -> None:
      """
      Resolve all outstanding issues.
      
      The method calls `pyVmomi.eam.EamObject.resolve`
      with all issues the `EsxAgentManager`, `Agency`, or
      `Agent` have encountered. It is the equivalent of calling the following methods:
      - `agent.resolve(getIssueKeys(agent.getRuntime().getIssue()));`
        for `Agent` objects
      - `agency.resolve(getIssueKeys(agency.getRuntime().getIssue()));`
        for `Agency` objects
      - `esxAgentManager.resolve(getIssueKeys(esxAgentManager.getIssue()));`
        for the `EsxAgentManager` object.
        
      Requires modify privileges.
      
      See Also: `pyVmomi.eam.issue.Issue`
      """
      ...
   def QueryIssue(self, issueKey: list[int]) -> list[pyVmomi.eam.issue.Issue]:
      """
      Current issues that have been detected for this entity.
      
      Each issue can be remediated
      by invoking `pyVmomi.eam.EamObject.resolve` or `pyVmomi.eam.EamObject.resolveAll`.
      
      Requires view privileges.
      
      Args:
          issueKey: An optional array of issue keys. If not set, all issues for this
              entity are returned.
      
      Returns:
          A possibly empty array of issues that match the input `issueKey` array. Note
          that the returned array can be smaller than `issueKey` if one or more
          issue keys refers to issues that this entity does not have.
      """
      ...


class Agency(EamObject):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An `Agency` handles the deployment of a single type of agent
   virtual machine and any associated VIB bundle, on a set of compute resources.
   
   For a solution to deploy multiple types of agents, it must create multiple
   agencies by using `createAgency` on `pyVmomi.eam.EsxAgentManager` (see
   `pyVmomi.eam.EsxAgentManager.createAgency`).
   
   Creating an agency is a long-running process. vSphere ESX Agent Manager must
   install VIBs, configure hosts, install agent virtual machines and do many
   more things. Each of these steps can take a considerable amount of time.
   vSphere ESX Agent Manager can also encounter problems when creating the
   agency. In this case, the solution must remediate the problem. See
   `pyVmomi.eam.issue.Issue` for a description of the kinds of issue that vSphere ESX Agent
   Manager will raise. Similarly, removing an agency from vSphere ESX Agent
   Manager is also a long-running process that involves many steps. Removing an
   agency can also raise issues.
   
   Use the `goalState` and `status` properties to show the
   progress of creating or removing an Agency. The `goalState` and
   `status` properties are found in the runtime information of an
   `Agency` (see `pyVmomi.eam.EamObject.RuntimeInfo.status` in
   `pyVmomi.eam.Agency.runtime`):
   - `goalState`. The goal state describes the overall goal of an
     `Agency`. The goal state can be `enabled` or
     `uninstalled`:
     - `enabled`. The `Agency` continuously deploys VIBs
       and agent virtual machines, powers on agent virtual machines, and monitors
       agents for issues.
     - `uninstalled`. The `Agency` uninstalls any
       installed VIBs and powers off and deletes any deployed agent virtual
       machines.
   - `status`. The status of the `Agency` regarding the
     given goal state. Status can be either red, yellow or green:
     - `red`. An issue is preventing the `Agency` from
       reaching its desired goal state. See `pyVmomi.eam.EamObject.RuntimeInfo.issue` in
       `pyVmomi.eam.Agency.runtime` for the types of issues that can block this
       `Agency`.
     - `yellow`. The `Agency` is actively working to reach
       the desired goal state. For the `enabled` goal state, this means
       that this `Agency` is currently installing VIBs, deploying agent
       virtual machines, and powering them on.
     - `green`. The `Agency` has reached the desired goal
       state. The `Agency` is no longer actively scheduling new tasks but
       is monitoring the vCenter Server for changes that might conflict with this
       `Agency`'s goal state.
       
   The following image shows in general terms how the status changes in the
   life-cycle of an `Agency`.
   
   \"Agency degraded\" means that something has happened in the vCenter Server
   that causes this `Agency` to actively schedule new tasks to reach
   the goal state. For example, adding a host to a cluster covered by the scope
   of the `Agency`, which causes ESX Agent Manager to install a VIB
   and deploy an agent virtual machine on the new host.
   A solution should monitor the list of issues associated with this
   `Agency`.
   
   The solution can poll `pyVmomi.eam.Agency.runtime`.
   """
   class VMResourcePool(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM System VMs APIs.Represents the mapping of a VM resource pool to a compute resource.
      
      Attributes:
          resourcePoolId: Resource pool identifier.
              
              The resource pool must be present in the
              corresponding compute resource.
          computeResourceId: Compute resource identifier.
      """
      resourcePoolId: pyVmomi.vim.ResourcePool
      computeResourceId: pyVmomi.vim.ComputeResource

   class VMFolder(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM System VMs APIs.Represents the mapping of a VM folder to a datacenter.
      
      Attributes:
          folderId: Folder identifier.
              
              The folder must be present in the corresponding
              datacenter.
          datacenterId: Datacenter identifier.
      """
      folderId: pyVmomi.vim.Folder
      datacenterId: pyVmomi.vim.Datacenter

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.This is the configuration of an `Agency`.
      
      It determines on
      which compute resources to deploy the agents, which VIB to install, which
      OVF package to install, and how to configure these items by setting the
      OVF environment properties.
      
      Attributes:
          agentConfig: A list of `pyVmomi.eam.Agent.ConfigInfo`s for hosts covered by this
              `Agency`.
              
              When provisioning a new agent to a host, vSphere
              ESX Agent Manager tries to find, from left to right in the array, a
              match for an `pyVmomi.eam.Agent.ConfigInfo` and stops searching at the first
              one that it finds.
              If `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set, the array needs to contain only a
              single agent config. In that case the agent config is not bound to a
              specific host, but to the whole cluster.
          scope: The scope of the `Agency`.
          manuallyMarkAgentVmAvailableAfterProvisioning: If set to `true`, the client of this agency must manually
              mark the agent as ready after the agent virtual machine has been
              provisioned.
              
              This is useful if the client of this solution performs
              some extra reconfiguration of the agent virtual machine before it is
              powered on.
          manuallyMarkAgentVmAvailableAfterPowerOn: If set to `true`, the client of this agency must manually
              mark the agent as ready after the agent virtual machine has been
              powered on.
              
              In this case, DRS will not regard the agent virtual machine
              as ready until the client has marked the agent as ready.
          optimizedDeploymentEnabled: If set to `true`, ESX Agent Manager will use vSphere Linked
              Clones to speed up the deployment of agent virtual machines.
              
              Using
              linked clones implies that the agent virtual machines cannot use
              Storage vMotion to move to another vSphere datastore.
              If set to `false`, ESX Agent Manager will use Full VM
              Cloning.
              If unset default is `true`.
          agentName: An optional name to use when naming agent virtual machines.
              
              For
              example, if set to \"example-agent\", each agent virtual machine will be
              named \"example-agent (1)\", \"example-agent (2)\", and so on. The maximum
              length of `agentName` is 70 characters.
          agencyName: Name of the agency.
              
              Must be set when creating the agency.
          useUuidVmName: Property `agentName` is required if this property is set to
              `true`.
              
              If set to `true`, ESX Agent Manager will name virtual
              machines with UUID suffix. For example, \"example-agent-UUID\".
              In this case, the maximum length of `agentName` is 43
              characters.
              
              If not set or is set to `false`, virtual
              machines will not contain UUID in their name.
          manuallyProvisioned: Set to true if agent VMs are manually provisioned.
              
              If unset, defaults
              to false.
          manuallyMonitored: Set to true if agent VMs are manually monitored.
              
              If unset, defaults to
              false. This can only be set to true if
              `pyVmomi.eam.Agency.ConfigInfo.manuallyProvisioned` is set to true.
          bypassVumEnabled: Set to true will install VIBs directly on the hosts even if VMware
              Update Manager is installed.
              
              If unset, defaults to false.
          agentVmNetwork: Specifies the networks which to be configured on the agent VMs.
              
              This property is only applicable for pinned to host VMs - i.e.
              (`pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy`) is not set.
              
              If not set or `pyVmomi.eam.Agency.ConfigInfo.preferHostConfiguration` is set to true, the
              default host agent VM network (configured through
              vim.host.EsxAgentHostManager) is used, otherwise the first network from
              the array that is present on the host is used.
              
              At most one of `pyVmomi.eam.Agency.ConfigInfo.agentVmNetwork` and `pyVmomi.eam.Agency.ConfigInfoEx.vmNetworkMapping`
              needs to be set.
          agentVmDatastore: The datastores used to configure the storage on the agent VMs.
              
              This property is required if `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set and
              `pyVmomi.eam.Agency.ConfigInfoEx.datastoreSelectionPolicy` is not set. In that case the first
              element from the list is used.
              
              If not set or `pyVmomi.eam.Agency.ConfigInfo.preferHostConfiguration` is set to true and
              `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is not set, the default host agent VM
              datastore (configured through vim.host.EsxAgentHostManager) is used,
              otherwise the first datastore from the array that is present on the
              host is used.
              
              If `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set at most one of
              `pyVmomi.eam.Agency.ConfigInfo.agentVmDatastore` and `pyVmomi.eam.Agency.ConfigInfoEx.datastoreSelectionPolicy` needs
              to be set. If `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is not set
              `pyVmomi.eam.Agency.ConfigInfoEx.datastoreSelectionPolicy` takes precedence over
              `pyVmomi.eam.Agency.ConfigInfo.agentVmDatastore` .
          preferHostConfiguration: If set to true the default agent VM datastore and network will take
              precedence over `pyVmomi.eam.Agency.ConfigInfo.agentVmNetwork` and
              `pyVmomi.eam.Agency.ConfigInfo.agentVmDatastore` when configuring the agent
              VMs.
              
              This property is not used if `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set.
          ipPool: If set, a property with id \"ip\" and value an IP from the pool is added
              to the vApp configuration of the deployed VMs.
          resourcePools: Defines the resource pools where VMs to be deployed.
              
              If specified, the VMs for every compute resource in the scope will be
              deployed to its corresponding resource pool.
              If not specified, the agent VMs for each compute resource will be
              deployed under top level nested resource pool created for the agent
              VMs. If unable to create a nested resource pool, the root resource pool
              of the compute resource will be used.
          folders: Defines the folders where VMs to be deployed.
              
              If specified, the VMs for every compute resource in the scope will be
              deployed to its corresponding folder. The link is made between the
              compute resource parent and the datacenter the folder belongs to
              `pyVmomi.eam.Agency.VMFolder.datacenterId`.
              If not specified, the agent VMs for each compute resource will be
              deployed in top level folder created in each datacenter for the agent
              VMs.
      """
      agentConfig: list[Agent.ConfigInfo] = []
      scope: _typing.Optional[Agency.Scope] = None
      manuallyMarkAgentVmAvailableAfterProvisioning: _typing.Optional[bool] = None
      manuallyMarkAgentVmAvailableAfterPowerOn: _typing.Optional[bool] = None
      optimizedDeploymentEnabled: _typing.Optional[bool] = None
      agentName: _typing.Optional[str] = None
      agencyName: _typing.Optional[str] = None
      useUuidVmName: _typing.Optional[bool] = None
      manuallyProvisioned: _typing.Optional[bool] = None
      manuallyMonitored: _typing.Optional[bool] = None
      bypassVumEnabled: _typing.Optional[bool] = None
      agentVmNetwork: list[pyVmomi.vim.Network] = []
      agentVmDatastore: list[pyVmomi.vim.Datastore] = []
      preferHostConfiguration: _typing.Optional[bool] = None
      ipPool: _typing.Optional[pyVmomi.vim.vApp.IpPool] = None
      resourcePools: list[Agency.VMResourcePool] = []
      folders: list[Agency.VMFolder] = []

   class Scope(pyVmomi.vmodl.DynamicData):
      """Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Scope specifies which where to deploy agents."""
      pass

   class ComputeResourceScope(Agency.Scope):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Scope specifies on which compute resources to deploy a solution's agents.
      
      Attributes:
          computeResource: Compute resources on which to deploy the agents.
              
              If `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set, the array needs to
              contain exactly one cluster compute resource.
      """
      computeResource: list[pyVmomi.vim.ComputeResource] = []

   @property
   def solutionId(self) -> str:
      """
      The ID of the solution that owns this `Agency`.
      
      If the agency
      is owned by a VC extension, this is the extension's key. Otherwise, this
      is same as `pyVmomi.eam.Agency.owner`. The users in the latter case are
      either regular or solution users.
      
      Requires view privileges.
      """
      ...
   @property
   def owner(self) -> _typing.Optional[str]:
      """
      The principal name of the user that owns this `Agency`.
      
      If the
      agency is owned by a VC extension, this method returns null.
      
      Requires view privileges.
      """
      ...
   @property
   def config(self) -> Agency.ConfigInfo:
      """
      The configuration of this `Agency`.
      
      Specifies how this
      `Agency` deploys its agents and VIBs.
      
      Requires view privileges.
      """
      ...
   @property
   def runtime(self) -> EamObject.RuntimeInfo:
      """
      Gets the runtime information for this agency.
      
      Requires view privileges.
      """
      ...
   @property
   def agent(self) -> list[Agent]:
      """
      An array of agents deployed by this agent manager.
      
      Requires view privileges.
      """
      ...

   def QuerySolutionId(self) -> str:
      """
      Deprecated: Use `pyVmomi.eam.Agency.solutionId` insteadThe ID of the solution that owns this `Agency`.
      
      If the agency
      is owned by a VC extension, this is the extension's key. Otherwise, this
      is same as `pyVmomi.eam.Agency.owner`. The users in the latter case are
      either regular or solution users.
      
      Requires view privileges.
      
      Returns:
          The solution ID.
      """
      ...
   def QueryConfig(self) -> Agency.ConfigInfo:
      """
      Deprecated: Use `pyVmomi.eam.Agency.config` insteadThe configuration of this `Agency`.
      
      Specifies how this
      `Agency` deploys its agents and VIBs.
      
      Requires view privileges.
      
      Returns:
          The configuration of this `Agency`.
      """
      ...
   def Update(self, config: Agency.ConfigInfo) -> None:
      """
      Updates the agency configuration used by this `Agency` to
      deploy agents and VIBs.
      
      vSphere ESX Agent Manager generates a diff between
      the old configuration and the new one and updates the `Agency`
      accordingly.
      
      Requires modify privileges.
      
      Args:
          config: The new configuration for this `Agency`
      
      Raises:
          pyVmomi.eam.fault.InvalidAgentConfiguration: Thrown if one or more agent configurations are invalid.
          pyVmomi.eam.fault.InvalidAgencyScope: Thrown if one or more compute resources in the scope cannot be
              found in vCenter or there is no configured resource pool or
              folder where the VMs to be deployed.
          pyVmomi.eam.fault.InvalidUrl: Thrown if either the agent virtual machine URL or VIB URL
              cannot be parsed or if the resource referred to cannot be
              downloaded.
      """
      ...
   def QueryRuntime(self) -> EamObject.RuntimeInfo:
      """
      Deprecated: Use `pyVmomi.eam.Agency.runtime` insteadGets the runtime information for this agency.
      
      Requires view privileges.
      
      Returns:
          The runtime information.
      """
      ...
   def QueryAgent(self) -> list[Agent]:
      """
      Deprecated: Use `pyVmomi.eam.Agency.agent` insteadAn array of agents deployed by this agent manager.
      
      Requires view privileges.
      """
      ...
   def RegisterAgentVm(self, agentVm: pyVmomi.vim.VirtualMachine) -> Agent:
      """
      Deprecated: use automatically provisioned VMs and register hooks to have
      control post provisioning and power onAdds an agent VM to this agency.
      
      Used if
      `pyVmomi.eam.Agency.ConfigInfo.manuallyProvisioned` is set to true. The method
      does nothing if the agent VM is already registered with this agency.
      
      Requires modify privileges.
      
      Args:
          agentVm: The managed object reference to the agent VM.
      
      Raises:
          pyVmomi.vmodl.fault.ManagedObjectNotFound: Thrown if agentVm does not exist in vCenter.
      """
      ...
   def UnregisterAgentVm(self, agentVm: pyVmomi.vim.VirtualMachine) -> None:
      """
      Deprecated: use automatically provisioned VMs and register hooks to have
      control post provisioning and power onRemoves an agent VM to this agency.
      
      Used if
      `pyVmomi.eam.Agency.ConfigInfo.manuallyProvisioned` is set to true. The method
      does nothing if the agent VM is not registered with this agency.
      
      Requires modify privileges.
      
      Args:
          agentVm: The managed object reference to the agent VM.
      """
      ...
   def Enable(self) -> None:
      """
      Deprecated: since agencies are always created as enabled. In addition,
      enabling already uninstalled agency is not supported.Sets the goal state of this `Agency` to `enabled`.
      
      This causes the agency to continuously deploy and monitor agents.
      
      Requires modify privileges.
      """
      ...
   def Disable(self) -> None:
      """
      Deprecated: its definition is not consistent across agent VMs and VIBs.
      It is impossible to be defined since there is no corresponding
      state of ESXi vibs.Sets the goal state of this `Agency` to `disabled`.
      
      This powers off any powered on agent virtual machines, but continues
      provisioning agents to hosts that are added to the compute resources in
      the agency's scope, and removes agents from hosts that are taken out of
      the scope.
      
      Requires modify privileges.
      """
      ...
   def Uninstall(self) -> None:
      """
      Sets the goal state of this `Agency` to
      `uninstalled`.
      
      This initiates the uninstallation of this
      `Agency`, which causes all agents to be removed.
      
      The best practice when destroying an agency is to call
      `uninstall`, wait for the runtime status to turn green, and
      then invoke `pyVmomi.eam.Agency.destroyAgency`. When waiting for this
      `Agency` to be uninstalled the solution can then attend to and
      resolve any raised issues.
      
      Requires modify privileges.
      """
      ...
   def DestroyAgency(self) -> None:
      """
      Destroys this Agency.
      
      Any agents that the `Agency` has are
      removed. Until the agents have been removed, it is possible to view the
      runtime state of this `Agency` but it is not possible to modify
      its configuration or change its goal state. After all agents have been
      removed, any subsequent call on this `Agency` will throw a
      `ManagedObjectNotFound` exception.
      
      Requires modify privileges.
      """
      ...
   def AddIssue(self, issue: pyVmomi.eam.issue.Issue) -> pyVmomi.eam.issue.Issue:
      """
      Deprecated: Adds an issue to this agency.
      
      `pyVmomi.eam.issue.Issue.key` and `pyVmomi.eam.issue.Issue.time` is
      overwritten so that `pyVmomi.eam.issue.Issue.key` becomes unique on this server and
      `pyVmomi.eam.issue.Issue.time` is the current time.
      
      Requires modify privileges.
      
      Args:
          issue: A new issue.
      
      Returns:
          The same issue where the key and time is set.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Thrown if issue typeId is unknown.
      """
      ...


class Agent(EamObject):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An `Agent` is the vSphere ESX Agent Manager managed object
   responsible for deploying an `Agency` on a single host.
   
   The
   `Agent` maintains the state of the current deployment in its
   runtime information (see `pyVmomi.eam.Agent.runtime`).
   
   An `Agent` has the same `goalState` and
   `status` properties as an `Agency`, that are used in
   the same way:
   - `goalState`. The goal state describes the overall goal of this
     `Agent`. It can be `enabled` or
     `uninstalled`:
     - `enabled`. The `Agent` deploys its VIB, its agent
       virtual machine, and powers on the agent virtual machine. The
       `Agent` monitors in vCenter the status of the installation of the
       VIB (in case it is uninstalled outside of vSphere ESX Agent Manager) and of
       the agent virtual machine (in case an operation is performed on it outside of
       vSphere ESX Agent Manager).
     - `uninstalled`. The `Agent` uninstalls any installed
       VIB and power off and delete the deployed agent virtual machine.
   - `status`. The status of the `Agent` regarding the
     given goal state. Status can be either red, yellow or green:
     - `red`. An issue is preventing the `Agent` from
       reaching its desired goal state. See `pyVmomi.eam.EamObject.RuntimeInfo.issue` in
       `pyVmomi.eam.Agent.runtime` for the types of issues that can block this
       `Agent`.
     - `yellow`. The `Agent` is actively working to reach
       the desired goal state. For the `enabled` goal state, this means
       that this `Agent` is installing its VIB, deploying the agent
       virtual machine, and powering it on.
     - `green`. The `Agent` has reached the desired goal
       state. The `Agent` is no longer actively scheduling new tasks but
       is monitoring vCenter for changes that might conflict with this
       `Agent`'s goal state.
   """
   class RuntimeInfo(EamObject.RuntimeInfo):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Extends `RuntimeInfo` with information regarding the deployment
      of an agent on a specific host.
      
      Attributes:
          vmPowerState: The power state of an agent virtual machine.
          receivingHeartBeat: True if the vSphere ESX Agent Manager is receiving heartbeats from the
              agent virtual machine.
          host: The agent host.
          vm: The agent virtual machine.
          vmIp: The IP address of the agent virtual machine
          vmName: The name of the agent virtual machine.
          esxAgentResourcePool: The ESX agent resource pool in which the agent virtual machine resides.
          esxAgentFolder: The ESX agent folder in which the agent virtual machine resides.
          installedBulletin: An optional array of IDs of installed bulletins for this agent.
          installedVibs: Information about the installed vibs on the host.
          agency: The agency this agent belongs to.
          vmHook: Active VM hook.
              
              If present agent is actively waiting for `pyVmomi.eam.Agent.markAsAvailable`.
              See `pyVmomi.eam.Agent.VmHook`.
      """
      vmPowerState: pyVmomi.vim.VirtualMachine.PowerState
      receivingHeartBeat: bool
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
      vmIp: _typing.Optional[str] = None
      vmName: str
      esxAgentResourcePool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      esxAgentFolder: _typing.Optional[pyVmomi.vim.Folder] = None
      installedBulletin: list[str] = []
      installedVibs: list[pyVmomi.eam.vib.VibInfo] = []
      agency: _typing.Optional[Agency] = None
      vmHook: _typing.Optional[Agent.VmHook] = None

   class VmHook(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Represents an active hook of the VM lifecycle which EAM is waiting on to
      be processed by the client.
      
      The supported hooks are defined by
      `pyVmomi.eam.Agency.ConfigInfo.manuallyMarkAgentVmAvailableAfterProvisioning`
      and
      `pyVmomi.eam.Agency.ConfigInfo.manuallyMarkAgentVmAvailableAfterProvisioning`.
      See `pyVmomi.eam.Agent.markAsAvailable`
      
      Attributes:
          vm: The VM for which lifecycle is this hook.
              
              This VM may differ from `pyVmomi.eam.Agent.RuntimeInfo.vm` while an upgrade
              of the agent VM is in progress.
          vmState: The current VM lifecycle state.
      """
      class VmState(pyVmomi.VmomiSupport.Enum):
         """
         Represents the state of the VM lifecycle.
         
         Attributes:
             provisioned: The VM is provisioned and not powered-on.
             poweredOn: The VM is powered on.
             prePowerOn: The VM is about to be powered on as part of a VM upgrade workflow.
         """
         provisioned: _typing.ClassVar['Agent.VmHook.VmState'] = 'provisioned'
         poweredOn: _typing.ClassVar['Agent.VmHook.VmState'] = 'poweredOn'
         prePowerOn: _typing.ClassVar['Agent.VmHook.VmState'] = 'prePowerOn'

      vm: pyVmomi.vim.VirtualMachine
      vmState: str

   class StoragePolicy(pyVmomi.vmodl.DynamicData):
      """Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Specifies the storage policies configured on Agent VMs."""
      pass

   class VsanStoragePolicy(Agent.StoragePolicy):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Specifies vSAN specific storage policy configured on Agent VMs.
      
      Attributes:
          profileId: ID of a storage policy profile created by the user.
              
              The type of the
              profile must be `pyVmomi.vim.vm.DefinedProfileSpec`. The ID must be valid
              `pyVmomi.vim.vm.DefinedProfileSpec.profileId`.
      """
      profileId: str

   class SslTrust(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Specifies an SSL trust policy.
      
      Since: vEAM API 8.2
      """
      pass

   class PinnedPemCertificate(Agent.SslTrust):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Specifies an SSL policy that trusts one specific pinned PEM encoded
      SSL certificate.
      
      Attributes:
          sslCertificate: PEM encoded pinned SSL certificate of the server that needs to be
              trusted.
      
      Since: vEAM API 8.2
      """
      sslCertificate: str

   class AnyCertificate(Agent.SslTrust):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Specifies an SSL policy that trusts any SSL certificate.
      
      Since: vEAM API 8.2
      """
      pass

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.A description of what should be put on a host.
      
      By setting the
      `productLineId` and `hostVersion`, you can specify
      the types of hosts for which to use the `ConfigInfo`.
      
      Attributes:
          productLineId: The product line ID of the host.
              
              Examples of values are \"esx\" or
              \"embeddedEsx\". If omitted, the host's product line ID is not considered
              when matching an `AgentPackage` against a host.
          hostVersion: A dot-separated string of the host version.
              
              Examples of values are
              \"4.1.0\" \"3.5\", \"4.*\" where * is a wildcard meaning any version minor
              version of the major version 4. If omitted, the host version will not
              be considered when matching an `AgentPackage` against a
              host.
              This property is not used if
              `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set. It is client's
              responsibility to trigger an agency upgrade with a new
              `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl`.
          ovfPackageUrl: The URL of the solution's agent OVF package.
              
              If not set, no agent
              virtual machines are installed on the hosts covered by the scope.
              If `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy` is set, the VM needs to
              be agnostic to the different host versions inside the cluster.
          authenticationScheme: The authentication scheme needed to access the OVF URL.
              
              The supported schemes are listed in `pyVmomi.eam.Agent.ConfigInfo.AuthenticationScheme`
              Default value is `NONE` if not specified.
              
              If the scheme is not `null` and is not set to `NONE`
              then `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl` must point to the VC
              
              Since: vEAM API 9.0
          ovfSslTrust: Specifies an SSL trust policy to be use for verification of the
              server that hosts the `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl`.
              
              If not set, the server
              certificate is validated against the trusted root certificates of the
              OS (Photon) and VECS (TRUSTED_ROOTS).
              
              Since: vEAM API 8.2
          ovfEnvironment: The part of the OVF environment that can be set by the solution.
              
              This
              is where Properties that the agent virtual machine's OVF descriptor
              specifies are set here. All properties that are specified as
              user-configurable must be set.
          vibUrl: An optional URL to an offline bundle.
              
              If not set, no VIB is installed
              on the hosts in the scope. Offline bundles are only supported on 4.0
              hosts and later.
              
              VIB downgrade is not permitted - in case a VIB with the same name, but
              lower version is installed on a host in the scope the VIB installation
              on that host will not succeed.
              
              If two or more agents have the same VIB with different versions on the
              same host, the install/uninstall behaviour is undefined (the VIB may
              remain installed, etc.).
              
              The property is not used if `pyVmomi.eam.Agency.ConfigInfoEx.vmPlacementPolicy`
              is set.
          vibSslTrust: Specifies an SSL trust policy to be use for verification of the
              server that hosts the `pyVmomi.eam.Agent.ConfigInfo.vibUrl`.
              
              If not set, the server
              certificate is validated against the trusted root certificates of the
              OS (Photon) and VECS (TRUSTED_ROOTS).
              
              Since: vEAM API 8.2
          vibMatchingRules: Optional Vib matching rules.
              
              If set, the Vib, specified by vibUrl, will
              be installed either
              - if there is installed Vib on the host which name and version match
                the regular expressions in the corresponding rule
              - or there isn't any installed Vib on the host with name which
                matches the Vib name regular expression in the corresponding rule. Vib
                matching rules are usually used for controlling VIB upgrades, in which
                case the name regular expression matches any previous versions of the
                agency Vib and version regular expression determines whether the
                existing Vib should be upgraded.
                
              For every Vib in the Vib package, only one Vib matching rule can be
              defined. If specified more than one, it is not determined which one
              will be used. The Vib name regular expression in the Vib matching rule
              will be matched against the name of the Vib which will be installed.
              Only rules for Vibs which are defined in the Vib package metadata will
              be taken in account.
          vibName: An optional name of a VIB.
              
              If set, no VIB is installed on the host. The
              host is checked if a VIB with vibName is already installed on it. Also
              the vibUrl must not be set together with the vibUrl.
          dvFilterEnabled: If set to `true`, the hosts in the scope must be configured
              for DvFilter before VIBs and agent virtual machines are deployed on
              them.
              
              If not set or set to `false`, no DvFilter
              configuration is done on the hosts.
          rebootHostAfterVibUninstall: An optional boolean flag to specify whether the agent's host is
              rebooted after the VIB is uninstalled.
              
              If not set, the default value is
              `false`. If set to `true`, the agent gets a
              `pyVmomi.eam.issue.VibRequiresHostReboot` issue after a successful
              uninstallation.
          vmciService: If set the virtual machine will be configured with the services and
              allow VMCI access from the virtual machine to the installed VIB.
          ovfDiskProvisioning: AgentVM disk provisioning type.
              
              Defaults to `none` if not specified.
          vmStoragePolicies: Defines the storage policies configured on Agent VMs.
              
              Storage policies
              are configured on all VM related objects including disks.
              NOTE: The property needs to be configured on each update, otherwise
              vSphere ESX Agent Manager will unset this configuration for all future
              agent VMs.
          vmResourceConfiguration: Specifies the resource configuration to be used when deploying an Agent
              VM.
              
              It must correspond to the Configuration element of the
              DeploymentOptionSection in the OVF specification.
              
              Since: vEAM API 8.3
      """
      class OvfDiskProvisioning(pyVmomi.VmomiSupport.Enum):
         """
         Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Defines the type of disk provisioning for the target Agent VMs.
         
         Attributes:
             none: Denotes no specific type for disk provisioning.
                 
                 Disks will be
                 provisioned as defaulted by vSphere.
             thin: Disks will be provisioned with only used space allocated.
             thick: Disks will be provisioned with full size allocated.
         """
         none: _typing.ClassVar['Agent.ConfigInfo.OvfDiskProvisioning'] = 'none'
         thin: _typing.ClassVar['Agent.ConfigInfo.OvfDiskProvisioning'] = 'thin'
         thick: _typing.ClassVar['Agent.ConfigInfo.OvfDiskProvisioning'] = 'thick'

      class AuthenticationScheme(pyVmomi.VmomiSupport.Enum):
         """
         Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Supported authentication schemes used to access an OVF URL.
         
         Attributes:
             NONE: Accessing the OVF URL doesn't require authentication.
             VMWARE_SESSION_ID: Accessing the OVF URL requires Vmware client sessionID.
         
         Since: vEAM API 9.0
         """
         NONE: _typing.ClassVar['Agent.ConfigInfo.AuthenticationScheme'] = 'NONE'
         VMWARE_SESSION_ID: _typing.ClassVar['Agent.ConfigInfo.AuthenticationScheme'] = 'VMWARE_SESSION_ID'

      productLineId: _typing.Optional[str] = None
      hostVersion: _typing.Optional[str] = None
      ovfPackageUrl: _typing.Optional[str] = None
      authenticationScheme: _typing.Optional[str] = None
      ovfSslTrust: _typing.Optional[Agent.SslTrust] = None
      ovfEnvironment: _typing.Optional[Agent.OvfEnvironmentInfo] = None
      vibUrl: _typing.Optional[str] = None
      vibSslTrust: _typing.Optional[Agent.SslTrust] = None
      vibMatchingRules: list[Agent.VibMatchingRule] = []
      vibName: _typing.Optional[str] = None
      dvFilterEnabled: _typing.Optional[bool] = None
      rebootHostAfterVibUninstall: _typing.Optional[bool] = None
      vmciService: list[str] = []
      ovfDiskProvisioning: _typing.Optional[str] = None
      vmStoragePolicies: list[Agent.StoragePolicy] = []
      vmResourceConfiguration: _typing.Optional[str] = None

   class OvfEnvironmentInfo(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.The `OvfEnvironment` is used to assign OVF environment
      properties in the `pyVmomi.eam.Agent.ConfigInfo`.
      
      It specifies the values that
      map to properties in the agent virtual machine's OVF descriptor.
      
      Attributes:
          ovfProperty: The OVF properties that are assigned to the agent virtual machine's OVF
              environment when it is powered on.
      """
      class OvfProperty(pyVmomi.vmodl.DynamicData):
         """
         Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.One OVF property.
         
         Attributes:
             key: The name of the property in the OVF descriptor.
             value: The value of the property.
         """
         key: str
         value: str

      ovfProperty: list[Agent.OvfEnvironmentInfo.OvfProperty] = []

   class VibMatchingRule(pyVmomi.vmodl.DynamicData):
      """
      Deprecated: VIB matching rules are no longer supported by EAM. Same
      overlaps with VIB dependency requirements which reside in each
      VIB's metadata.Specifies regular expressions for Vib name and version.
      
      Attributes:
          vibNameRegex: Vib name regular expression.
          vibVersionRegex: Vib version regular expression.
      """
      vibNameRegex: str
      vibVersionRegex: str

   @property
   def runtime(self) -> Agent.RuntimeInfo:
      """
      Runtime information for this agent.
      
      This includes important information
      about the current deployment of the agent's VIB, virtual machine, and
      host.
      
      Requires view privileges.
      """
      ...
   @property
   def config(self) -> Agent.ConfigInfo:
      """The configuration of this `Agent`."""
      ...

   def QueryRuntime(self) -> Agent.RuntimeInfo:
      """
      Deprecated: Use `pyVmomi.eam.Agent.runtime` insteadRuntime information for the agent.
      
      This includes important information
      about the current deployment of the agent's VIB, virtual machine, and
      host.
      
      Requires view privileges.
      
      Returns:
          The `Agent`'s runtime information.
      """
      ...
   def MarkAsAvailable(self) -> None:
      """
      Mark this agent's VM as available.
      
      Used when the agency this agent belongs to
      has
      `pyVmomi.eam.Agency.ConfigInfo.manuallyMarkAgentVmAvailableAfterProvisioning` or
      `pyVmomi.eam.Agency.ConfigInfo.manuallyMarkAgentVmAvailableAfterPowerOn` set to
      `true` and `pyVmomi.eam.Agent.RuntimeInfo.vmHook` is present.
      See `pyVmomi.eam.Agent.RuntimeInfo.vmHook`
      """
      ...
   def QueryConfig(self) -> Agent.ConfigInfo:
      """Deprecated: Use `pyVmomi.eam.Agent.config` insteadThe configuration of this `Agent`."""
      ...


class EsxAgentManager(EamObject):
   """
   The `EsxAgentManager` is the main entry point for a solution to
   create agencies in the vSphere ESX Agent Manager server.
   
   In vCenter 6.0, a solution is either a vCenter extension or a regular
   user.
   
   The vSphere ESX Agent Manager VMODL API distinguishes between two types of
   users: VC extensions and regular vCenter users. These users have different
   privileges in the vSphere ESX Agent Manager VMODL API:
   - VC extensions have the privileges to call anything in the vSphere ESX
     Agent Manager VMODL API.
   - Regular vCenter users have restrictions on what methods they can call.
     The methods that a vCenter user that is not an extension can call are
     annotated with two types of privileges, `Eam.View` and
     `Eam.Modify`:
     - `Eam.View`. If a method has the `Eam.View`
       privilege, a user can call that method if they have the `EAM.View`
       privilege in vCenter.
     - `Eam.Modify`. Similarly to `Eam.View`, if a method
       has the `Eam.Modify` privilege, a user can call that method if
       they have the `EAM.Modify` privilege in vCenter. If a user has the
       `EAM.Modify` privilege, they automatically have
       `EAM.View`.
       
   In vCenter 6.5 every solution, which is making VMODL API calls to
   EsxAgentManager, should be aware of the possibility, that the data from
   vCenter database might not be fully loaded. In all such cases the clients
   will receive an ESX Agent Manager runtime fault:
   EamServiceNotInitialized.
   NOTE: No issues are associated with `EsxAgentManager` any longer.
   """
   class MaintenanceModePolicy(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.`MaintenanceModePolicy` defines how ESX Agent Manager is going
      to put into maintenance mode hosts which are part of a cluster not managed
      by vSphere Lifecycle Manager.
      
      Attributes:
          singleHost: Only a single host at a time will be put into maintenance mode.
          multipleHosts: Hosts will be put into maintenance mode simultaneously.
              
              If vSphere DRS
              is enabled, its recommendations will be used. Otherwise, it will be
              attempted to put in maintenance mode simultaneously as many host as
              possible.
      
      Since: vEAM API 7.4
      """
      singleHost: _typing.ClassVar['EsxAgentManager.MaintenanceModePolicy'] = 'singleHost'
      multipleHosts: _typing.ClassVar['EsxAgentManager.MaintenanceModePolicy'] = 'multipleHosts'

   @property
   def agency(self) -> list[Agency]:
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An array of all `pyVmomi.eam.Agency` objects.
      
      If called by a vCenter user with
      the vCenter `EAM.View` or `EAM.Modify` privilege,
      this returns all agencies registered in vSphere ESX Agent Manager. If
      called by a solution, this property only returns the agencies created by
      the solution (and only those which have not been destroyed).
      
      Requires view privileges.
      """
      ...
   @property
   def issue(self) -> list[pyVmomi.eam.issue.Issue]:
      """
      Deprecated: This method is deprecated since the EAM object does not
      handles issue anymore. At the moment the implementation
      returns an empty array of issues.Current issues that have been detected for this entity.
      
      Each issue can be
      remediated by invoking `pyVmomi.eam.EamObject.resolve` or
      `pyVmomi.eam.EamObject.resolveAll`.
      
      Requires view privileges.
      """
      ...

   def QueryAgency(self) -> list[Agency]:
      """
      Deprecated: Use `pyVmomi.eam.EsxAgentManager.agency` insteadAn array of all `pyVmomi.eam.Agency` objects.
      
      If called by a vCenter user with
      the vCenter `EAM.View` or `EAM.Modify` privilege,
      this returns all agencies registered in vSphere ESX Agent Manager. If
      called by a solution, this property only returns the agencies created by
      the solution (and only those which have not been destroyed).
      
      Requires view privileges.
      
      Returns:
          The possibly empty set of agencies registered in the vSphere ESX
          Agent Manager server.
      """
      ...
   def CreateAgency(self, agencyConfigInfo: Agency.ConfigInfo, initialGoalState: str) -> Agency:
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Creates an Agency.
      
      The initial goal state is given to the method by the
      second parameter. Throws `InvalidArgument` if the
      `agencyName` is not set in the `agencyConfigInfo`.
      
      Requires modify privileges.
      
      Args:
          agencyConfigInfo: The configuration that describes how to deploy the agents in the
              created agency.
          initialGoalState: Deprecated. No sense to create agency in other state than
              `enabled`. `disabled` is deprecated
              whereas `uninstalled` is useless.
              The initial goal state of the agency. See
              `pyVmomi.eam.EamObject.RuntimeInfo.GoalState`.
      
      Returns:
          The created agency.
      
      Raises:
          pyVmomi.eam.fault.InvalidAgentConfiguration: Thrown if the agent configuration is empty or if one or more
              agent configurations are invalid.
          pyVmomi.eam.fault.InvalidAgencyScope: Thrown if one or more compute resources in the scope cannot be
              found in vCenter or there is no configured resource pool or
              folder where the VMs to be deployed.
          pyVmomi.eam.fault.InvalidUrl: Thrown if either the agent virtual machine URL or VIB URL
              cannot be parsed or if the resource referred to cannot be
              downloaded.
      """
      ...
   def ScanForUnknownAgentVm(self) -> None:
      """
      Deprecated: Presence of unknown VMs is no more acceptableScans the vCenter inventory for any unknown agent virtual machine.
      
      An
      issue is generated for each unknown agent virtual machine found during
      this scan.
      
      Requires view privileges.
      """
      ...
   def SetMaintenanceModePolicy(self, policy: str) -> None:
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Configures maintenance mode policy for clusters not managed by vSphere
      Lifecycle Manasger.
      
      See Also: `pyVmomi.eam.EsxAgentManager.MaintenanceModePolicy`
      
      Args:
          policy: The policy to use.
      
      Since: vEAM API 7.4
      """
      ...
   def GetMaintenanceModePolicy(self) -> str:
      """
      Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Obtains maintenance policy for for clusters not managed by vSphere
      Lifecycle Manasger.
      
      See Also: `pyVmomi.eam.EsxAgentManager.MaintenanceModePolicy`
      
      Returns:
          Currently configured policy.
      
      Since: vEAM API 7.4
      """
      ...


class Task(pyVmomi.VmomiSupport.ManagedObject):
   """Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.Returned when invoking long-running operations in vSphere ESX Agent Manager."""
   pass
