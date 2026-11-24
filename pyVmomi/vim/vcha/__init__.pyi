# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.vm.customization



class FailoverClusterConfigurator(pyVmomi.VmomiSupport.ManagedObject):
   """
   FailoverClusterConfigurator provides operations to create and configure
   a vCenter High Availability Cluster (VCHA Cluster).
   
   A VCHA Cluster consists of three VMs. One is the Active vCenter VM that
   serves client requests. Second is the Passive VM that is identical to the
   Active vCenter VM in terms of resources and capabilities. Passive VM
   constantly receives updates from Active VM and takes over the role of
   Active vCenter VM in the event of failover. Third is the Witness VM that
   acts as a quorum VM in a VCHA Cluster. Sole purpose of Witness VM is to
   avoid classic split-brain problem in a VCHA Cluster.
   A VCHA Cluster can be deployed in two possible ways -
   1\\. Automatic deployment - Configuration (described below) inputs for each
   node in a VCHA Cluster is provided by the user. A Deployment workflow
   is used that automatically deploys Passive and Witness VM and configures
   each node to form a VCHA Cluster.
   2\\. Manual deployment - User provisions and creates Passive and Witness
   VMs and uses Configuration workflow to configure Active, Passive and
   Witness VM to form a VCHA Cluster. Passive and Witness VMs must be
   created using the VM-Clone operation with Active VM as the source.
   """
   class ClusterNetworkConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      The Cluster network config spec allows specification of
      the second network adapter is used for communication between
      the nodes of a VCHA cluster.
      
      Attributes:
          networkPortGroup: The portgroup that is associated with the VCHA Cluster IP
              address for VCHA cluster traffic for the second adapter to be
              added to the Active vCenter.
          ipSettings: VCHA Cluster network configuration of the node.
              
              All cluster communication (state replication, heartbeat,
              cluster messages) happens over this network.
              Only a single Gateway IPv4 Address is supported.
              IPAddress and NetMask must be specified or an InvalidArgument
              exception will be reported.
      """
      networkPortGroup: pyVmomi.vim.Network
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class SourceNodeSpec(pyVmomi.vmodl.DynamicData):
      """
      The SourceNodeSpec class defines specification of
      the source node that is used to initiate the configuration or
      deployment for VCHA.
      
      Attributes:
          managementVc: Credentials for the management vCenter Server that is managing
              this node.
          activeVc: VirtualMachine reference for this vCenter Server.
      """
      managementVc: pyVmomi.vim.ServiceLocator
      activeVc: pyVmomi.vim.VirtualMachine

   class NodeNetworkSpec(pyVmomi.vmodl.DynamicData):
      """
      The NodeNetworkSpec class defines network specification of a node
      in the VCHA Cluster.
      
      Attributes:
          ipSettings: VCHA Cluster network configuration of the node.
              
              All cluster communication (state replication, heartbeat,
              cluster messages) happens over this network.
      """
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class PassiveNodeNetworkSpec(FailoverClusterConfigurator.NodeNetworkSpec):
      """
      The PassiveNodeNetworkSpec class defines VCHA Failover and Cluster
      network configuration of the Passive node VM in the VCHA Cluster.
      
      Attributes:
          failoverIpSettings: Failover IP address that this node must assume after the failover
              to serve client requests.
              
              If not specified, it will assume the public
              IP address of the Active vCenter Server.
      """
      failoverIpSettings: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None

   class VchaClusterNetworkSpec(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterNetworkSpec class contains network
      configuration information for a VCHA Cluster.
      
      Attributes:
          witnessNetworkSpec: Network spec for the Witness node.
          passiveNetworkSpec: Network spec for the Passive node.
      """
      witnessNetworkSpec: FailoverClusterConfigurator.NodeNetworkSpec
      passiveNetworkSpec: FailoverClusterConfigurator.PassiveNodeNetworkSpec

   class NodeDeploymentSpec(pyVmomi.vmodl.DynamicData):
      """
      The NodeDeploymentSpec class defines location
      specification of the nodes the VCHA Cluster along with Management
      vCenter Server information that manages node VM.
      
      Attributes:
          esxHost: ESX host on which the VM is to be deployed.
              
              For behavior when an esxHost is not specified,
          datastore: Datastore used for deploying the VM.
              
              For behavior when a datastore is not specified,
          publicNetworkPortGroup: Name of the portgroup that is associated with the public IP address
              where clients connect to vCenter Server.
              
              If a portgroup is not
              specified same portgroup present on source is used to deploy the VM
              with an assumption that portgroup is present on destination.
          clusterNetworkPortGroup: Name of the portgroup that is associated with the VCHA Cluster IP
              address where clients connect to vCenter Server.
              
              If a portgroup is not
              specified same portgroup present on source is used to deploy the VM
              with an assumption that portgroup is present on destination.
          folder: Folder in which the VM is to be created.
          resourcePool: ResourcePool that will be used to deploy this node.
              
              If the ResourcePool is not specified, the root resource pool for the
              host will be used.
          managementVc: Management vCenter Server managing this VM.
              
              If the managementVc is not specified, managementVc specified as
              part of SourceNodeSpec is used.
          nodeName: nodeName here refers to a name that will be assigned to the VM to which
              this node will be deployed to.
          ipSettings: VCHA Cluster network configuration of the node.
              
              All cluster communication (state replication, heartbeat,
              cluster messages) happens over this network.
      """
      esxHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      publicNetworkPortGroup: _typing.Optional[pyVmomi.vim.Network] = None
      clusterNetworkPortGroup: _typing.Optional[pyVmomi.vim.Network] = None
      folder: pyVmomi.vim.Folder
      resourcePool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      managementVc: _typing.Optional[pyVmomi.vim.ServiceLocator] = None
      nodeName: str
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class PassiveNodeDeploymentSpec(FailoverClusterConfigurator.NodeDeploymentSpec):
      """
      The PassiveNodeDeploymentSpec class defines VCHA Cluster configuration
      of the Passive node VM in the VCHA Cluster.
      
      Attributes:
          failoverIpSettings: Failover IP address that this node must assume after the failover
              to serve client requests.
              
              If not specified, it will assume the public
              IP address of the Active vCenter Server.
      """
      failoverIpSettings: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None

   class VchaClusterConfigSpec(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterConfigSpec class contains IP addresses of
      Passive and Witness nodes to configure and form the VCHA Cluster.
      
      Passive and Witness nodes are assumed to be pre-configured
      to allow access to them over the specified IP addresses.
      Active Node IP address is not required as it is retrieved from
      the already configured interface on VCHA Cluster network.
      
      Attributes:
          passiveIp: IP Address of Passive node in the VCHA Cluster network.
          witnessIp: IP Address of Witness node in the VCHA Cluster network.
      """
      passiveIp: str
      witnessIp: str

   class VchaClusterDeploymentSpec(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterDeploymentSpec class contains
      deployment information for creating and configuring a VCHA Cluster.
      
      Attributes:
          passiveDeploymentSpec: Deployment spec for the Passive node
          witnessDeploymentSpec: Deployment spec for the Witness node
          activeVcSpec: Active vCenter Server specification required to deploy
              VCHA Cluster.
          activeVcNetworkConfig: The Cluster network config spec allows creation and configuration of
              the second Network adapter of the Active or Source VCenter.
              
              The second network adapter is used for communication between
              the nodes of a VCHA cluster.
      """
      passiveDeploymentSpec: FailoverClusterConfigurator.PassiveNodeDeploymentSpec
      witnessDeploymentSpec: FailoverClusterConfigurator.NodeDeploymentSpec
      activeVcSpec: FailoverClusterConfigurator.SourceNodeSpec
      activeVcNetworkConfig: _typing.Optional[FailoverClusterConfigurator.ClusterNetworkConfigSpec] = None

   class FailoverNodeInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          clusterIpSettings: VCHA Cluster network configuration of the node.
              
              All cluster communication (state replication, heartbeat,
              cluster messages) happens over this network.
          failoverIp: Failover IP address that this node will assume after the failover
              to serve client requests.
              
              Each failover node can have a different
              failover IP address.
          biosUuid: BIOS UUID for the node.
              
              It is set only if the VCHA Cluster was
              formed using automatic provisioning by the deploy API.
      """
      clusterIpSettings: pyVmomi.vim.vm.customization.IPSettings
      failoverIp: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None
      biosUuid: _typing.Optional[str] = None

   class WitnessNodeInfo(pyVmomi.vmodl.DynamicData):
      """
      The WitnessNodeInfo class defines configuration
      information for the Witness node in the cluster
      
      Attributes:
          ipSettings: VCHA Cluster network configuration of the Witness node.
          biosUuid: BIOS UUID for the node.
              
              It is set only if the VCHA Cluster was
              formed using automatic provisioning by the deploy API.
      """
      ipSettings: pyVmomi.vim.vm.customization.IPSettings
      biosUuid: _typing.Optional[str] = None

   class VchaState(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          configured: VCHA cluster is configured.
          notConfigured: VCHA cluster is not configured.
          invalid: VCHA cluster is in an invalid/dirty state.
          prepared: VC appliance has been prepared for VCHA cluster configuration.
      """
      configured: _typing.ClassVar['FailoverClusterConfigurator.VchaState'] = 'configured'
      notConfigured: _typing.ClassVar['FailoverClusterConfigurator.VchaState'] = 'notConfigured'
      invalid: _typing.ClassVar['FailoverClusterConfigurator.VchaState'] = 'invalid'
      prepared: _typing.ClassVar['FailoverClusterConfigurator.VchaState'] = 'prepared'

   class VchaClusterConfigInfo(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterConfigInfo class contains
      configuration information of the three nodes of a VCHA
      Cluster.
      
      Attributes:
          failoverNodeInfo1: Node configuration information for the VCHA Cluster
          failoverNodeInfo2: Node configuration information for the VCHA Cluster
          witnessNodeInfo: Node configuration information for the VCHA Cluster
          state: Current state of VCHA Cluster.
              
              `pyVmomi.vim.vcha.FailoverClusterConfigurator.VchaState` lists all
              possible states.
              If the state is invalid or notConfigured, the other fields in this
              object will be unset.
      """
      failoverNodeInfo1: _typing.Optional[FailoverClusterConfigurator.FailoverNodeInfo] = None
      failoverNodeInfo2: _typing.Optional[FailoverClusterConfigurator.FailoverNodeInfo] = None
      witnessNodeInfo: _typing.Optional[FailoverClusterConfigurator.WitnessNodeInfo] = None
      state: str

   @property
   def disabledConfigureMethod(self) -> list[pyVmomi.VmomiSupport.ManagedMethod]:
      """
      A list of method names that must not be called and will throw
      a fault due to some other method running that the disabled method
      can cause side-effects for.
      
      This list may include the following methods:
      - `pyVmomi.vim.vcha.FailoverClusterConfigurator.deploy`
      - `pyVmomi.vim.vcha.FailoverClusterConfigurator.configure`
      - `pyVmomi.vim.vcha.FailoverClusterConfigurator.createPassiveNode`
      - `pyVmomi.vim.vcha.FailoverClusterConfigurator.createWitnessNode`
      - `pyVmomi.vim.vcha.FailoverClusterConfigurator.destroy`
        
      As with other disabled methods there will be no property updates
      on this property when called with non-zero property collector versions.
      """
      ...

   def Prepare(self, networkSpec: FailoverClusterConfigurator.VchaClusterNetworkSpec) -> pyVmomi.vim.Task:
      """
      Prepares the vCenter appliance for a VCHA cluster deployment.
      
      This preparation operation saves the network configuration of the cluster
      and configures the Active node to be cloned for a VCHA configuration.
      Prepares the VCHA Active node for ssh keys, vpostgres replication
      and related configuration file setup needed for a VCHA cluster.
      If the Active node Cluster network adapter does not exist
      the prepare operation will fail.
      No changes will be made if the cluster is already configured.
      
      Args:
          networkSpec: contains the information needed to prepare
              a VCHA Cluster and configure networking.
      """
      ...
   def Deploy(self, deploymentSpec: FailoverClusterConfigurator.VchaClusterDeploymentSpec) -> pyVmomi.vim.Task:
      """
      Deploys and Configures VCHA on the local vCenter as a single API.
      
      This deployment operation automatically provisions and creates a
      Passive and a Witness node followed by configuring each node such that
      a 3 node VCHA Cluster is formed. After configuration, the VCHA Cluster
      is enabled on a best effort basis, but if this operation does not
      succeed, `pyVmomi.vim.vcha.FailoverClusterManager.setClusterMode` must be
      called to enable it. State replication or failover is not allowed
      until the VCHA Cluster is enabled. The current vCenter Server continues
      to serve client requests during and after the deployment.
      If the activeVcNetworkConfig spec if filled in, the cluster network
      will be created and configured.
      No changes will be made if the cluster network is already configured.
      
      Args:
          deploymentSpec: contains the information needed to deploy and
              configure a VCHA Cluster
      """
      ...
   def Configure(self, configSpec: FailoverClusterConfigurator.VchaClusterConfigSpec) -> pyVmomi.vim.Task:
      """
      Configure VCHA on the local vCenter Server.
      
      This operation configures the VC appliance with VCHA specific inputs
      and uses already deployed Passive and Witness nodes to set up the
      VCHA cluster. After configuration, the VCHA Cluster is enabled
      on a best effort basis, but if this operation does not succeed,
      `pyVmomi.vim.vcha.FailoverClusterManager.setClusterMode` must be called
      to enable it. State replication or failover is not allowed
      until the VCHA Cluster is enabled. The current vCenter Server
      continues to serve client requests during and after the configuration.
      
      Args:
          configSpec: contains the configuration for the cluster
      """
      ...
   def CreatePassiveNode(self, passiveDeploymentSpec: FailoverClusterConfigurator.PassiveNodeDeploymentSpec, sourceVcSpec: FailoverClusterConfigurator.SourceNodeSpec) -> pyVmomi.vim.Task:
      """
      Creates a Passive node in a degraded VCHA Cluster with node location
      information and pre-existing VCHA Cluster configuration from the
      Active node.
      
      Args:
          passiveDeploymentSpec: contains deployment specification for the
              passive node
          sourceVcSpec: contains specification for the source vCenter
              server that is used to create Passive node
      """
      ...
   def CreateWitnessNode(self, witnessDeploymentSpec: FailoverClusterConfigurator.NodeDeploymentSpec, sourceVcSpec: FailoverClusterConfigurator.SourceNodeSpec) -> pyVmomi.vim.Task:
      """
      Creates a Witness node in a degraded VCHA Cluster with node location
      information and pre-existing VCHA Cluster configuration from the
      Active node.
      
      Args:
          witnessDeploymentSpec: contains deployment specification for the
              witness node
          sourceVcSpec: contains specification for the source vCenter
              server that is used to create Witness node
      """
      ...
   def GetConfig(self) -> FailoverClusterConfigurator.VchaClusterConfigInfo:
      """
      Returns the configuration information for each node that is part of
      the VCHA Cluster.
      
      Returns:
          Returns a data structure specifying configuration for Active,
          Passive and Witness node in the Cluster.
      """
      ...
   def Destroy(self) -> pyVmomi.vim.Task:
      """
      Destroys the VCHA cluster setup and removes all VCHA specific
      configuration from the VCVA appliance.
      
      The active node in the cluster
      continues to run as a standalone VCVA appliance after the destroy
      operation has been performed.
      This operation is allowed under the following circumstances:
      \\- VCHA cluster is disabled
      \\- The node is in an isolated state
      \\- VCHA Deploy/Configure has failed
      """
      ...


class FailoverClusterManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   FailoverClusterManager provides operations to manage a vCenter
   High Availability Cluster (VCHA Cluster).
   
   A VCHA Cluster consists of three VMs. One is the Active vCenter VM that
   serves client requests. Second is the Passive VM that is identical to the
   Active vCenter VM in terms of resources and capabilities. Passive VM
   constantly receives updates from Active VM and takes over the role of
   Active vCenter VM in the event of failover. Third is the Witness VM that
   acts as a quorum VM in a VCHA Cluster. Sole purpose of Witness VM is to
   avoid classic split-brain problem in a VCHA Cluster.
   A VCHA Cluster has following states -
   1\\. Healthy - All three nodes in a VCHA Cluster are healthy and connected.
   State replication between Active and Passive node is working and both
   nodes are in-sync.
   2\\. Degraded - A VCHA Cluster is said to be in degraded state when it has
   lost one of the three nodes. Node loss can be due to various reasons and
   as a result the lost node is not visible to other two nodes. If an Active
   node is lost, Passive node will take the role of Active node. If Passive or
   Witness node is lost, Active node will continue to serve requests. A VCHA
   Cluster can also be in degraded state if state replication fails between
   Active and Passive nodes.
   3\\. Isolated - All three nodes are isolated from each other. If this happens
   while VCHA Cluster is in enabled mode, Active node stops serving client
   requests. If nodes are isolated in a disabled VCHA Cluster mode, Active
   node continues to serve client requests.
   A VCHA Cluster has following modes -
   1\\. Enabled - State replication between Active and Passive nodes is
   enabled and automatic failover happens if Active node fails while the
   VCHA Cluster is in a healthy state.
   2\\. Disabled - All three nodes are part of VCHA Cluster but state
   replication and automatic failover is disabled.
   3\\. Maintenance - All three nodes are part of VCHA Cluster but automatic
   failover is disabled while state replication continues. Active node continues
   to serve client requests even if Passive and Witness nodes are lost.
   """
   class VchaNodeRole(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          active: Node is having a role of Active.
              
              In this role, node runs a vCenter
              Server that serves client requests.
          passive: Node is having a role of Passive.
              
              In this role node, runs as a standby
              for the Active vCenter Server and receives state updates. This node
              takes over the role of Active vCenter Server upon failover.
          witness: Node is having a role of Witness.
              
              In this role, node acts as a quorum
              node for avoiding the classic split-brain problem.
      """
      active: _typing.ClassVar['FailoverClusterManager.VchaNodeRole'] = 'active'
      passive: _typing.ClassVar['FailoverClusterManager.VchaNodeRole'] = 'passive'
      witness: _typing.ClassVar['FailoverClusterManager.VchaNodeRole'] = 'witness'

   class VchaClusterMode(pyVmomi.VmomiSupport.Enum):
      """
      VchaClusterMode enum defines the possible modes for a VCHA Cluster.
      
      Attributes:
          enabled: VCHA Cluster is enabled.
              
              State replication between the Active and
              Passive node is enabled and automatic failover is allowed.
          disabled: VCHA Cluster is disabled.
              
              State replication between the Active and
              Passive node is disabled and automatic failover is not allowed.
          maintenance: VCHA Cluster is in maintenance mode.
              
              State replication between the
              Active and Passive node is enabled but automatic failover
              is not allowed.
      """
      enabled: _typing.ClassVar['FailoverClusterManager.VchaClusterMode'] = 'enabled'
      disabled: _typing.ClassVar['FailoverClusterManager.VchaClusterMode'] = 'disabled'
      maintenance: _typing.ClassVar['FailoverClusterManager.VchaClusterMode'] = 'maintenance'

   class VchaClusterState(pyVmomi.VmomiSupport.Enum):
      """
      VchaClusterState enum defines the possible states for a VCHA Cluster.
      
      Attributes:
          healthy: All three nodes in a VCHA Cluster are healthy and connected.
              
              State
              replication between Active and Passive node is working and both
              nodes are in sync.
          degraded: A VCHA Cluster is said to be in a degraded state for
              either or all of the following reasons:
              \\- There is a node loss.
              
              \\- State replication between the Active and Passive node fails.
          isolated: All three nodes are isolated from each other.
      """
      healthy: _typing.ClassVar['FailoverClusterManager.VchaClusterState'] = 'healthy'
      degraded: _typing.ClassVar['FailoverClusterManager.VchaClusterState'] = 'degraded'
      isolated: _typing.ClassVar['FailoverClusterManager.VchaClusterState'] = 'isolated'

   class VchaNodeState(pyVmomi.VmomiSupport.Enum):
      """
      VchaNodeState enum defines possible state a node can be in a
      VCHA Cluster.
      
      Attributes:
          up: Node is up and has joined the VCHA Cluster.
          down: Node is down and has left the VCHA Cluster.
      """
      up: _typing.ClassVar['FailoverClusterManager.VchaNodeState'] = 'up'
      down: _typing.ClassVar['FailoverClusterManager.VchaNodeState'] = 'down'

   class VchaNodeRuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      The VchaNodeRuntimeInfo class describes a node's
      runtime information in a VCHA Cluster.
      
      Attributes:
          nodeState: Last known state of the node.
              
              `pyVmomi.vim.vcha.FailoverClusterManager.VchaNodeState`
              lists all possible states.
          nodeRole: Last known role of the node.
              
              `pyVmomi.vim.vcha.FailoverClusterManager.VchaNodeRole`
              lists all possible roles.
          nodeIp: IP address for the node in the replication network.
      """
      nodeState: str
      nodeRole: str
      nodeIp: str

   class VchaClusterRuntimeInfo(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterRuntimeInfo class describes the
      runtime information of a VCHA Cluster.
      
      This includes the last known
      state of the cluster and last known states of each node.
      
      Attributes:
          clusterState: Last known state of the VCHA Cluster.
              
              `pyVmomi.vim.vcha.FailoverClusterManager.VchaClusterState` lists all possible states.
          nodeInfo: Runtime information for each node in the VCHA Cluster.
          clusterMode: Operational mode of the VCHA Cluster.
              
              `pyVmomi.vim.vcha.FailoverClusterManager.VchaClusterMode`
              lists all possible modes.
      """
      clusterState: str
      nodeInfo: list[FailoverClusterManager.VchaNodeRuntimeInfo] = []
      clusterMode: str

   class VchaClusterHealth(pyVmomi.vmodl.DynamicData):
      """
      The VchaClusterHealth class describes the overall
      VCHA Cluster health.
      
      Health information include the last known runtime
      information about the VCHA Cluster along with health messages and any
      additional information applicable to the current VCHA Cluster health.
      If the cluster state is healthy, there will not be any health messages
      or additional information provided.
      
      Attributes:
          runtimeInfo: Runtime information of the VCHA Cluster
          healthMessages: A collection of Messages describing the reason for a non-healthy
              Cluster.
          additionalInformation: A collection of additional information regarding the health messages.
      """
      runtimeInfo: FailoverClusterManager.VchaClusterRuntimeInfo
      healthMessages: list[pyVmomi.vmodl.LocalizableMessage] = []
      additionalInformation: list[pyVmomi.vmodl.LocalizableMessage] = []

   @property
   def disabledClusterMethod(self) -> list[pyVmomi.VmomiSupport.ManagedMethod]:
      """
      A list of method names that must not be called and will throw
      a fault due to some other method running that the disabled method
      can cause side-effects for.
      
      This list may include the following methods:
      - `pyVmomi.vim.vcha.FailoverClusterManager.setClusterMode`
      - `pyVmomi.vim.vcha.FailoverClusterManager.getClusterMode`
      - `pyVmomi.vim.vcha.FailoverClusterManager.initiateFailover`
      - `pyVmomi.vim.vcha.FailoverClusterManager.getClusterHealth`
        
      GetClusterHealth will also be disabled if Deploy is in progress.
      As with other disabled methods there will be no property updates
      on this property when called with non-zero property collector versions.
      """
      ...

   def SetClusterMode(self, mode: str) -> pyVmomi.vim.Task:
      """
      setClusterMode method allows caller to manipulate the mode of a
      VCHA Cluster
      Following mode transitions are allowed -
      enabled -> disabled - Allowed only in healthy and degraded states.
      
      enabled -> maintenance - Allowed only in healthy state.
      disabled -> enabled - Allowed only in healthy state.
      maintenance -> enabled - Allowed only in healthy state with all nodes
      are running the same version.
      maintenance -> disabled - Allowed only in healthy state with all nodes
      are running the same version.
      All other transitions are not allowed.
      VCHA Cluster configuration remains intact in any of the cluster modes.
      """
      ...
   def GetClusterMode(self) -> str:
      """Returns current mode of a VCHA Cluster."""
      ...
   def GetClusterHealth(self) -> FailoverClusterManager.VchaClusterHealth:
      """Returns last known health of the VCHA Cluster."""
      ...
   def InitiateFailover(self, planned: bool) -> pyVmomi.vim.Task:
      """
      Allows a caller to initiate a failover from Active vCenter Server node
      to the Passive node.
      
      By default it is a forced failover. The planned
      flag can be used to initiate it as a planned failover.
      For forced failover, Active node immediately initiates a failover. This
      may result into a data loss after failover.
      For planned failover, Active node flushes all the state to the
      Passive node, waits for the flush to complete before causing a failover.
      After the failover, Passive node starts without any data loss.
      A failover is allowed only in the following cases -
      1\\. Cluster's mode is enabled and all cluster members are present.
      2\\. Cluster's mode is maintenance and all cluster members are present.
      API throws an exception in all other cases.
      
      Args:
          planned: \\- if false, a failover is initiated immediate and may
              result in data loss.
              if true, a failover is initiated after the Active node
              flushes its state to Passive and there is no data loss.
      """
      ...
