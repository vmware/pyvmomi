# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.cns
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.event
import pyVmomi.vim.profile
import pyVmomi.vim.vm
import pyVmomi.vmodl.fault
import pyVmomi.vim.vm.device
import pyVmomi.vim.vm.guest



class VimFault(pyVmomi.vmodl.MethodFault):
   """
   The common base type for all virtual infrastructure management
   exceptions.
   """
   pass


class ActiveDirectoryFault(VimFault):
   """
   Base fault for Active Directory related problems.
   
   Attributes:
       errorCode: The error code reported by the Active Directory API.
   """
   errorCode: _typing.Optional[int] = None


class EVCConfigFault(VimFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster has failed.
   
   Attributes:
       faults: The faults that caused this EVC test to fail,
           such as `pyVmomi.vim.fault.FeatureRequirementsNotMet` faults.
   """
   faults: list[pyVmomi.vmodl.MethodFault] = []


class ActiveVMsBlockingEVC(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster, or to
   select a less-featureful EVC mode for a cluster where EVC is already
   enabled, has failed for the following reason:
   - The cluster contains hosts that expose additional compatibility-
     relevant CPU features beyond those present in the baseline of the
     requested EVC mode.
   - Those hosts have powered-on or suspended virtual machines.
     
   Therefore the EVC configuration has been rejected since it may suppress
   CPU features that are currently in-use.
   
   Attributes:
       evcMode: The requested EVC mode.
       host: Hosts with active virtual machines that are blocking the operation,
           because the hosts expose compatibility-relevant CPU features not present
           in the baseline of the requested EVC mode.
           
           Note that in rare cases, a host may be on this list even if its
           `pyVmomi.vim.host.Summary.maxEVCModeKey` corresponds to the
           requested EVC mode. This means that even though that EVC mode is the
           best match for the host's hardware, the host still has some features
           beyond those present in the baseline for that EVC mode.
       hostName: The names of the hosts in the host array.
   """
   evcMode: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []

class HostConfigFault(VimFault):
   """Base class for all Host configuration related faults"""
   pass

class AdminDisabled(HostConfigFault):
   """
   Fault thrown if an attempt to disable the Administrator permission
   on a host of which the Administrator permission has already been disabled.
   """
   pass

class AdminNotDisabled(HostConfigFault):
   """
   Fault thrown if an attempt to enable the Administrator permission
   on a host of which the Administrator permission is not disabled.
   """
   pass

class MigrationFault(VimFault):
   """
   Base object type for issues that can occur when reassigning the execution
   host of a virtual machine using migrate or relocate.
   
   These issues are typically
   used as argument in the MigrationEvent. When a MigrationFault is used as a value
   in a MigrationEvent, the type of MigrationEvent determines if the issue is a
   warning or an error (for example, MigrationHostWarningEvent or
   MigrationHostErrorEvent). When thrown as an exception, the fault is an error.
   
   Issues are categorized as errors or warnings according to the following
   criteria:
   
   If the virtual machine is powered on:
   1. Error for fatal problems with the VMotion interfaces or licensing.
   2. Error if VMotion would fail.
   3. Error if VMotion would in any way interrupt the continuous and consistent
      operation of the virtual machine.
   4. Warning for potential performance or connectivity problems between the
      source and destination VMotion interfaces.
   5. Warning if the virtual machine's currently disconnected devices may not
      be connectable after VMotion.
      
   If the virtual machine is powered off or suspended:
   1. Error if the destination host cannot access all the files that comprise
      the virtual machine (including virtual disks).
   2. Error if aspects of the virtual machine are not supported by the
      destination host's hardware or software.
   3. Warning if problems would occur when powering on or resuming the
      virtual machine, if the usage/configuration of the destination
      host were to remain in its current state.
   """
   pass


class AffinityConfigured(MigrationFault):
   """
   Virtual machine has a configured memory and/or CPU affinity that will
   prevent VMotion.
   
   This is an error for powered-on virtual machines.
   
   Attributes:
       configuredAffinity: Configured affinity types for the virtual machine.
           
           See `pyVmomi.vim.fault.AffinityConfigured.Affinity` for valid values.
   """
   class Affinity(pyVmomi.VmomiSupport.Enum):
      """Types of affinities."""
      memory: _typing.ClassVar['AffinityConfigured.Affinity'] = 'memory'
      cpu: _typing.ClassVar['AffinityConfigured.Affinity'] = 'cpu'

   configuredAffinity: list[str] = []

class HostConnectFault(VimFault):
   """
   A base class for faults that are related to connecting or
   adding a host to the inventory.
   """
   pass


class AgentInstallFailed(HostConnectFault):
   """
   An AgentInstallFailed fault is thrown when VirtualCenter
   fails to install the VirtualCenter agent on a host.
   
   For example, a fault is
   thrown if the agent software cannot be uploaded to the host or an error occurred
   during the agent installation.
   
   Attributes:
       reason: The reason why the agent install failed, if known.
           
           Values should come from `pyVmomi.vim.fault.AgentInstallFailed.Reason`.
       statusCode: The status code returned by the agent installer, if it was run.
       installerOutput: The output (stdout/stderr) from executing the agent installer.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          NotEnoughSpaceOnDevice: There is not enough storage space on the host to install the agent.
          PrepareToUpgradeFailed: Failed to initialize the upgrade directory on the host.
          AgentNotRunning: The agent was installed but is not running.
          AgentNotReachable: The agent was installed but did not respond to requests.
          InstallTimedout: The agent install took too long.
          SignatureVerificationFailed: The signature verification for the installer failed.
          AgentUploadFailed: Failed to upload the agent installer.
          AgentUploadTimedout: The agent upload took too long.
          UnknownInstallerError: The agent installer failed for an unknown reason.
      """
      NotEnoughSpaceOnDevice: _typing.ClassVar['AgentInstallFailed.Reason'] = 'NotEnoughSpaceOnDevice'
      PrepareToUpgradeFailed: _typing.ClassVar['AgentInstallFailed.Reason'] = 'PrepareToUpgradeFailed'
      AgentNotRunning: _typing.ClassVar['AgentInstallFailed.Reason'] = 'AgentNotRunning'
      AgentNotReachable: _typing.ClassVar['AgentInstallFailed.Reason'] = 'AgentNotReachable'
      InstallTimedout: _typing.ClassVar['AgentInstallFailed.Reason'] = 'InstallTimedout'
      SignatureVerificationFailed: _typing.ClassVar['AgentInstallFailed.Reason'] = 'SignatureVerificationFailed'
      AgentUploadFailed: _typing.ClassVar['AgentInstallFailed.Reason'] = 'AgentUploadFailed'
      AgentUploadTimedout: _typing.ClassVar['AgentInstallFailed.Reason'] = 'AgentUploadTimedout'
      UnknownInstallerError: _typing.ClassVar['AgentInstallFailed.Reason'] = 'UnknownInstallerError'

   reason: _typing.Optional[str] = None
   statusCode: _typing.Optional[int] = None
   installerOutput: _typing.Optional[str] = None

class AlreadyBeingManaged(HostConnectFault):
   """
   AlreadyBeingManaged fault is thrown by the host
   connect method if the host is already being managed
   by a VirtualCenter server.
   
   Attributes:
       ipAddress: IP address of server that is currently managing the host.
   """
   ipAddress: str

class AlreadyConnected(HostConnectFault):
   """
   AlreadyConnect fault is thrown by the host connect method
   if the host is already connected to a VirtualCenter server.
   
   This might occur if the host has been added more than once
   in the same VirtualCenter in different folders or compute
   resources.
   
   Attributes:
       name: Name of the host
   """
   name: str


class AlreadyExists(VimFault):
   """
   An AlreadyExists fault is thrown when an attempt is made to add an element
   to a collection, if the element's key, name, or identifier already exists in that
   collection.
   """
   name: _typing.Optional[str] = None

class AlreadyUpgraded(VimFault):
   """
   An AlreadyUpgraded fault is thrown when an attempt is made to upgrade the
   virtual hardware of a Virtual machine whose virtual hardware is already
   up-to-date.
   """
   pass


class AnswerFileUpdateFailed(VimFault):
   """
   Could not update the answer file as it has invalid inputs.
   
   Attributes:
       failure: Failures encountered during answer file update
   """
   class UpdateFailure(pyVmomi.vmodl.DynamicData):
      """
      DataObject which represents the errors that occurred when an
      answer file update was performed.
      
      Attributes:
          userInputPath: The user input that has the error
          errMsg: Message which explains the error
      """
      userInputPath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   failure: list[AnswerFileUpdateFailed.UpdateFailure] = []

class SnapshotFault(VimFault):
   """Base type for Snapshot-related errors."""
   pass

class ApplicationQuiesceFault(SnapshotFault):
   """
   This fault is thrown when creating a quiesced snapshot failed
   because the (user-supplied) custom pre-freeze script in the
   virtual machine exited with a non-zero return code.
   
   This indicates that the script failed to perform its quiescing
   task, which causes us to fail the quiesced snapshot operation.
   """
   pass

class AuthMinimumAdminPermission(VimFault):
   """
   This fault is thrown when the requested change
   would result in a loss of full administrative privileges
   for at least one user or group.
   """
   pass

class DvsFault(VimFault):
   """
   Base class for faults that can be thrown while invoking a distributed virtual switch
   operation.
   """
   pass


class BackupBlobReadFailure(DvsFault):
   """
   Thrown if backupConfig blob is corrupted
   
   Attributes:
       entityName: The entity name on which backupConfig read failed
       entityType: The entity type on which backupConfig read failed
       fault: The fault that occurred.
   """
   entityName: str
   entityType: str
   fault: pyVmomi.vmodl.MethodFault


class BackupBlobWriteFailure(DvsFault):
   """
   Thrown if backupConfig blob write fails
   
   Attributes:
       entityName: The entity name on which backupConfig write failed
       entityType: The entity type on which backupConfig write failed
       fault: The fault that occurred.
   """
   entityName: str
   entityType: str
   fault: pyVmomi.vmodl.MethodFault

class BlockedByFirewall(HostConfigFault):
   """
   Fault indicating that firewall configuration prevents
   an operation from completing successfully.
   """
   pass

class InvalidCAMServer(ActiveDirectoryFault):
   """
   Fault indicating that the CAM server
   for camServer cannot be reached,
   or is not a valid IP address.
   
   Attributes:
       camServer: The address of the CAM server.
   """
   camServer: str

class CAMServerRefusedConnection(InvalidCAMServer):
   """
   Fault indicating that the CAM server
   cannot be connected.
   """
   pass

class FileFault(VimFault):
   """
   The common base type for all file-related exceptions.
   
   Attributes:
       file: The file in question.
   """
   file: str

class CannotAccessFile(FileFault):
   """
   This fault is thrown when an operation fails because of insufficient
   permissions to access a file.
   """
   pass

class CannotAccessLocalSource(VimFault):
   """
   An CannotAccessLocalSourceFault exception is thrown when a
   an attempt is made to upload license content
   and the local source cannot be accessed.
   """
   pass

class VmConfigFault(VimFault):
   """
   Base for configuration / environment issues that can be thrown when powering on or
   changing the configuration of a virtual machine.
   
   Subclasses of this fault is also
   used as recent why a migration can fail.
   """
   pass

class CannotAccessVmComponent(VmConfigFault):
   """
   One of the virtual machine's components is not accessible on the execution host.
   
   This is a base class. Subclasses will encode the type of component that is not
   accessible.
   """
   pass

class CannotAccessVmDevice(CannotAccessVmComponent):
   """
   One of the virtual machine's devices uses a backing that is not accessible
   on the host.
   
   Following is a discussion of this fault's use in migration validation.
   This is an error if the device is currently connected and a warning
   otherwise. Devices that can be disconnected can only be connected if the virtual
   machine is powered on.
   
   The usage of this fault is slightly different if the backing of a device is
   inherently host-local, and therefore not shared or globally named among
   hosts. (Examples of such backings: physical CD-ROM drive, physical serial
   port.) If a device with such a backing is currently connected, that will
   be a migration error. If the device is disconnected, there will be a
   warning if no backing with the same name exists on the destination host.
   If the device is disconnected and a backing with the same name exists on
   the destination host, this is neither a warning nor an error case, even
   though the destination host's backing is not the same instance as the
   source host's. It is assumed that use of the host-local backing is what is
   desired for the device.
   
   Attributes:
       device: The label of the device.
       backing: The backing of the device.
       connected: The connected/disconnected state of the device.
   """
   device: str
   backing: str
   connected: bool


class CannotAccessNetwork(CannotAccessVmDevice):
   """
   A network associated with the virtual machine is not accessible.
   
   If returned as
   part of migration checks, this is an error if either of the following is true,
   a warning otherwise:
   - The virtual ethernet card device backing is a distributed virtual switch,
     of which the destination host is not a member
   - The virtual ethernet card device backing is a standard network and the
     the device is connected
   
   Attributes:
       network: A reference to the network that cannot be accessed
   """
   network: _typing.Optional[pyVmomi.vim.Network] = None


class CannotAccessVmConfig(CannotAccessVmComponent):
   """
   One or more of the virtual machine's configuration files are not accessible.
   
   Attributes:
       reason: Contains the reason why the VM file could not be found.
           
           This is typically
           a FileFault.
   """
   reason: pyVmomi.vmodl.MethodFault


class CannotAccessVmDisk(CannotAccessVmDevice):
   """
   One of the virtual machine's virtual disks is not accessible.
   
   Attributes:
       fault: The reason why the disk could not be accessed
   """
   fault: pyVmomi.vmodl.MethodFault

class CannotAddHostWithFTVmAsStandalone(HostConnectFault):
   """Can not add a host with fault tolerance vms to be standalone"""
   pass

class CannotAddHostWithFTVmToDifferentCluster(HostConnectFault):
   """
   Can not add a host with fault tolerance vms to a different cluster other
   than the one used other vms in the same fault tolerance group.
   """
   pass

class CannotAddHostWithFTVmToNonHACluster(HostConnectFault):
   """Can not add a host with fault tolerance vms to a non HA enabled cluster"""
   pass

class VmFaultToleranceIssue(VimFault):
   """
   Base object type for issues that can occur during operations
   related to fault tolerance protection for virtual machines.
   """
   pass


class CannotChangeDrsBehaviorForFtSecondary(VmFaultToleranceIssue):
   """
   This fault is used to report that the DRS behavior cannot be modified
   for a FT secondary virtual machine
   
   Attributes:
       vm: The virtual machine whose behavior cannot be modified
       vmName: Name of the virtual machine
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class CannotChangeHaSettingsForFtSecondary(VmFaultToleranceIssue):
   """
   This fault is used to report that the HA settings cannot be modified
   for a FT secondary virtual machine
   
   Attributes:
       vm: The FT secondary virtual machine whose behavior cannot be modified
       vmName: Name of the FT secondary virtual machine
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class VsanFault(VimFault):
   """
   Base exception class for VSAN-specific faults raised for host
   or cluster operations.
   
   See Also: `pyVmomi.vim.host.VsanSystem`, `pyVmomi.vim.ComputeResource.reconfigureEx`
   """
   pass

class CannotChangeVsanClusterUuid(VsanFault):
   """
   Fault thrown for cases that a VSAN cluster UUID may not be changed.
   
   For example, the VSAN cluster UUID for a host may not be changed so long
   as that host is enabled for VSAN.
   The VSAN cluster UUID for a given `pyVmomi.vim.ClusterComputeResource` may
   not be changed so long as that vim.ClusterComputeResource is enabled for
   VSAN.
   
   See Also: `pyVmomi.vim.host.VsanSystem.update`, `pyVmomi.vim.ComputeResource.reconfigureEx`
   """
   pass

class CannotChangeVsanNodeUuid(VsanFault):
   """
   Fault thrown for cases that a VSAN node UUID may not be changed.
   
   For example, the VSAN node UUID for a host may not be changed so long as
   that host is enabled for VSAN.
   
   See Also: `pyVmomi.vim.host.VsanSystem.update`, `pyVmomi.vim.ComputeResource.reconfigureEx`
   """
   pass


class CannotComputeFTCompatibleHosts(VmFaultToleranceIssue):
   """
   This fault is used if FT compatible hosts cannot be computed for a VM
   
   Attributes:
       vm: The virtual machine for FT compatible hosts is being computed
       vmName: Name of the virtual machine
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class CannotCreateFile(FileFault):
   """
   A CannotCreateFile exception is thrown if a file create
   operation fails.
   """
   pass

class CustomizationFault(VimFault):
   """Base for exceptions that can be thrown from the customizer."""
   pass

class CannotDecryptPasswords(CustomizationFault):
   """
   The VirtualCenter server is unable to decrypt passwords stored in
   the customization specification.
   """
   pass

class CannotDeleteFile(FileFault):
   """
   A CannotDeleteFile exception is thrown if a file-deletion
   operation fails.
   """
   pass


class CannotDisableDrsOnClustersWithVApps(pyVmomi.vmodl.RuntimeFault):
   """
   This fault is thrown when an attempt is made to disable DRS on a cluster,
   which contains a vApp.
   """
   pass

class CannotDisableSnapshot(VmConfigFault):
   """
   Fault thrown when an attempt is made to disable snapshots on a virtual
   machine which has a snapshot.
   
   To disable the snapshot feature, the
   virtual machine must not currently have a snapshot.
   """
   pass

class CannotDisconnectHostWithFaultToleranceVm(VimFault):
   """
   This fault is thrown when an attempt is made to disconnect a host, which
   has one or more fault tolerance vms and is not in maintenance mode.
   
   Attributes:
       hostName: The name of the host to be disconnected
   """
   hostName: str


class CannotEnableVmcpForCluster(VimFault):
   """
   This fault is thrown when an attempt is made to enable VM Component Protection
   on a cluster which contains a host that does not support this feature.
   
   Attributes:
       host: Report the host with APD timeout disabled.
           
           If the host is set it points to the host which is the reason
           for this fault i.e this host has ADPTimeout disabled.
       hostName: If set this reports the hostName.
           
           This is used for printing the host name in the
           localized message as the host may have been removed
           from the vCenter's inventory by the time localization would
           be taking place.
       reason: This reports the reason for host not meeting the requirements
           for enabling vSphere VMCP.
           
           It can be the following reason.
           - APDTimeout disabled.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          APDTimeoutDisabled: APD timeout has been disabled on one of the host
      """
      APDTimeoutDisabled: _typing.ClassVar['CannotEnableVmcpForCluster.Reason'] = 'APDTimeoutDisabled'

   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None

class CannotModifyConfigCpuRequirements(MigrationFault):
   """
   A virtual machine's total CPU feature requirements are determined by
   overlaying the requirements specified in its configuration (if any) on top
   of the requirements specified in the descriptor for its guest OS.
   
   It is
   therefore possible for a host change to implicitly change a virtual
   machine's CPU feature requirements. The guest OS descriptor may have
   different requirements on the new host. Or, if the virtual machine
   currently specifies requirements in its configuration, those requirements
   will be lost if the new host does not support this.
   
   This fault indicates that the virtual machine's CPU feature requirements
   would change because of a migration, and also that the destination host
   does not support storing CPU feature requirements in the virtual machine's
   configuration. (If the destination host does support such an action,
   WillModifyConfigCpuRequirements is used instead of this fault.)
   
   For a powered-off virtual machine, this is a warning. The migration may
   proceed, but the virtual machine will be operating under different
   CPU feature requirements if it is powered on after the migration.
   
   For a powered-on or suspended virtual machine, this is an error.
   """
   pass


class CannotMoveFaultToleranceVm(VimFault):
   """
   This fault is thrown when an attempt is made to move a fault tolerance
   vm to a different resource pool or cluster.
   
   Attributes:
       moveType: The type of the move
       vmName: The virtual machine name to be moved.
   """
   class MoveType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          resourcePool: Move out of the resource pool
          cluster: Move out of the cluster
      """
      resourcePool: _typing.ClassVar['CannotMoveFaultToleranceVm.MoveType'] = 'resourcePool'
      cluster: _typing.ClassVar['CannotMoveFaultToleranceVm.MoveType'] = 'cluster'

   moveType: str
   vmName: str

class CannotMoveHostWithFaultToleranceVm(VimFault):
   """
   This fault is thrown when an attempt is made to move a host which has
   one or more fault tolerance vms out of the current cluster.
   """
   pass

class CannotMoveVmWithDeltaDisk(MigrationFault):
   """
   This fault is thrown when an attempt is made to relocate a virtual machine
   with virtual disk(s) having delta disk backing.
   
   Attributes:
       device: The label of the delta disk device
   """
   device: str

class CannotMoveVmWithNativeDeltaDisk(MigrationFault):
   """
   This fault is thrown when an attempt is made to migrate a virtual machine
   with native delta disks to different datastores.
   """
   pass

class CannotMoveVsanEnabledHost(VsanFault):
   """
   Fault thrown for the case that an attempt is made to move a host which
   is enabled for VSAN into an unsuitable `pyVmomi.vim.ClusterComputeResource`.
   
   The destination vim.ClusterComputeResource may be disabled for VSAN, or
   may be using VSAN with a different cluster UUID.
   
   See Also: `pyVmomi.vim.ClusterComputeResource.addHost`, `pyVmomi.vim.ClusterComputeResource.moveHostInto`, `pyVmomi.vim.ClusterComputeResource.moveInto`, `pyVmomi.vim.fault.VsanClusterUuidMismatch`, `pyVmomi.vim.fault.DestinationVsanDisabled`
   """
   pass

class CannotPlaceWithoutPrerequisiteMoves(VimFault):
   """
   This fault is thrown when Storage DRS cannot recommend to place disks of
   a virtual machine without moving existing virtual disks in a
   datastore cluster.
   """
   pass

class InvalidState(VimFault):
   """
   An InvalidState fault is thrown if the
   operation failed due to the current state of the system.
   """
   pass


class CannotPowerOffVmInCluster(InvalidState):
   """
   This fault is reported when a user attempts to power off or
   suspend a VM when the HA master agent to which vCenter Server is
   connected does not manage the VM.
   
   Attributes:
       operation: The operation being performed.
           
           Values come from
           `pyVmomi.vim.fault.CannotPowerOffVmInCluster.Operation`.
       vm: The Virtual Machine
       vmName: Name of the Virtual Machine
   """
   class Operation(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          suspend: suspend
          powerOff: power off
          guestShutdown: guest shutdown
          guestSuspend: guest suspend
      """
      suspend: _typing.ClassVar['CannotPowerOffVmInCluster.Operation'] = 'suspend'
      powerOff: _typing.ClassVar['CannotPowerOffVmInCluster.Operation'] = 'powerOff'
      guestShutdown: _typing.ClassVar['CannotPowerOffVmInCluster.Operation'] = 'guestShutdown'
      guestSuspend: _typing.ClassVar['CannotPowerOffVmInCluster.Operation'] = 'guestSuspend'

   operation: str
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class CannotReconfigureVsanWhenHaEnabled(VsanFault):
   """
   Fault thrown for the case that an attempt is made to reconfigure VSAN
   when HA is currently enabled for a given `pyVmomi.vim.ClusterComputeResource`.
   
   See Also: `pyVmomi.vim.ComputeResource.reconfigureEx`
   """
   pass


class CannotUseNetwork(VmConfigFault):
   """
   A network associated with the virtual machine is accessible, but it
   cannot be used for some reason.
   
   Attributes:
       device: The label of the network device.
       backing: The backing of the network device.
       connected: The connected/disconnected state of the device.
       reason: Reason describing why the network cannot be used.
       network: A reference to the network that cannot be used
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          NetworkReservationNotSupported: Network does not support reservation
          MismatchedNetworkPolicies: Source and destination networks do not have same security policies
          MismatchedDvsVersionOrVendor: Source and destination DVS do not have same version or vendor
          VMotionToUnsupportedNetworkType: VMotion to unsupported destination network type
          NetworkUnderMaintenance: The network is under maintenance
          MismatchedEnsMode: Source and destination networks do not have same ENS(Enhanced Network Stack) mode
          MismatchedRealTimeDvs: Source and destination networks do not have the same real-time flag
              
              Since: vSphere API Release 8.0.3.1
          NsxNetworkAvailabilityDegraded: Destination NSX network availability level degraded
      """
      NetworkReservationNotSupported: _typing.ClassVar['CannotUseNetwork.Reason'] = 'NetworkReservationNotSupported'
      MismatchedNetworkPolicies: _typing.ClassVar['CannotUseNetwork.Reason'] = 'MismatchedNetworkPolicies'
      MismatchedDvsVersionOrVendor: _typing.ClassVar['CannotUseNetwork.Reason'] = 'MismatchedDvsVersionOrVendor'
      VMotionToUnsupportedNetworkType: _typing.ClassVar['CannotUseNetwork.Reason'] = 'VMotionToUnsupportedNetworkType'
      NetworkUnderMaintenance: _typing.ClassVar['CannotUseNetwork.Reason'] = 'NetworkUnderMaintenance'
      MismatchedEnsMode: _typing.ClassVar['CannotUseNetwork.Reason'] = 'MismatchedEnsMode'
      MismatchedRealTimeDvs: _typing.ClassVar['CannotUseNetwork.Reason'] = 'MismatchedRealTimeDvs'
      NsxNetworkAvailabilityDegraded: _typing.ClassVar['CannotUseNetwork.Reason'] = 'NsxNetworkAvailabilityDegraded'

   device: str
   backing: str
   connected: bool
   reason: str
   network: _typing.Optional[pyVmomi.vim.Network] = None

class ClockSkew(HostConfigFault):
   """Fault indicating that the clock skew in the system exceeds the limit."""
   pass

class CloneFromSnapshotNotSupported(MigrationFault):
   """
   An attempt is being made to clone a virtual machine from a snapshot
   point, and this is not supported.
   
   See Also: `pyVmomi.vim.vm.CloneSpec.snapshot`, `pyVmomi.vim.vm.Capability.snapshotConfigSupported`, `pyVmomi.vim.host.Capability.cloneFromSnapshotSupported`
   """
   pass

class CnsFault(VimFault):
   """
   Base class for all CNS faults.
   
   Attributes:
       reason: A message to indicate detailed information about the error.
   """
   reason: str


class CnsAlreadyRegisteredFault(CnsFault):
   """
   CnsAlreadyRegisteredFault is thrown when an existing backing object
   which is already registered as CNS volume is registered again.
   
   Attributes:
       volumeId: CNS volume ID of the backing object.
   """
   volumeId: pyVmomi.vim.cns.VolumeId

class CnsPlacementFault(CnsFault):
   """
   This is a base class for all the type of placement faults
   that occur during volume provisioning.
   """
   pass


class CnsInCompatibleFault(CnsPlacementFault):
   """
   This fault indicates that the datastore is not compatible with the
   given storage policy.
   
   Attributes:
       errors: Array of faults that prevents the datastore from being compatible
           with the storage policy.
   """
   errors: list[pyVmomi.vmodl.MethodFault] = []

class CnsMissingControllerFault(CnsFault):
   """This fault indicates CNS can not attach volume to VM because of missing controller."""
   pass


class CnsMissingPrivilegeFault(CnsPlacementFault):
   """
   This fault indicates that the API client is missing one or more
   necessary privilege.
   
   Attributes:
       privileges: Array of missing privileges.
   """
   privileges: list[str] = []


class CnsNotRegisteredFault(CnsFault):
   """
   CnsNotRegisteredFault will be thrown when the backing object exists in VC
   but not registered as a CNS volume.
   
   Attributes:
       volumeId: CNS volume ID of the backing object.
   """
   volumeId: pyVmomi.vim.cns.VolumeId

class CnsRankedLowerFault(CnsPlacementFault):
   """
   This fault indicates that the datastore is ranked lower and
   some other datastore is selected for the volume placement.
   """
   pass


class CnsSnapshotNotFoundFault(CnsFault):
   """
   This fault indicates CNS cannot find a given snapshot
   
   Attributes:
       volumeId: Volume ID of missing snapshot.
       SnapshotId: Missing snapshot ID.
   """
   volumeId: _typing.Optional[pyVmomi.vim.cns.VolumeId] = None
   SnapshotId: pyVmomi.vim.cns.SnapshotId


class CnsVolumeAlreadyExistsFault(CnsFault):
   """
   This fault is thrown when create request comes in for a volume that
   has already been created.
   
   Attributes:
       volumeId: CNS volume ID.
       datastore: Datastore on which the CNS volume already exists.
   """
   volumeId: pyVmomi.vim.cns.VolumeId
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None


class CnsVolumeNotFoundFault(CnsFault):
   """
   This fault indicates CNS cannot find a given volume
   
   Attributes:
       volumeId: Missing volume ID.
   """
   volumeId: pyVmomi.vim.cns.VolumeId

class CollectorAddressUnset(DvsFault):
   """
   The distributed virtual switch received a reconfiguration request to
   activate ipfix monitoring of the switch traffic.
   
   However, the address
   and/or the port of the ipfix collector has not been specified.
   """
   pass

class ConcurrentAccess(VimFault):
   """
   A ConcurrentAccess fault is thrown when an operation
   fails because another operation has modified the
   datastructure.
   
   For non-transactional operations, such as a recursive
   delete of a subtree of the inventory, the operation might
   fail with ConcurrentAccess if another thread has added
   a new entity to the hierarchy.
   """
   pass


class ConflictingConfiguration(DvsFault):
   """
   Thrown if the configurations of the objects are in conflict.
   
   Attributes:
       configInConflict: The configurations that are in conflict.
   """
   class Config(pyVmomi.vmodl.DynamicData):
      """
      This class defines the configuration that is in conflict.
      
      Attributes:
          entity: The entity on which the configuration is in conflict.
          propertyPath: The property paths that are in conflict.
      """
      entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
      propertyPath: str

   configInConflict: list[ConflictingConfiguration.Config] = []


class ConflictingDatastoreFound(pyVmomi.vmodl.RuntimeFault):
   """
   ConflictingDatastoreFound is thrown when the conflicting datastores
   with the same url but backed by different disks are found in the host
   and the target datacenter.
   
   Attributes:
       name: The name of the datastore.
       url: The unique locator for the datastore.
   """
   name: str
   url: str

class OvfFault(VimFault):
   """
   A common base type fault for all Ovf related faults.
   
   The structure of OvfFault is as listed.
   - OvfFault
     - OvfInvalidPackage
       - OvfXmlFormat
       - OvfWrongNamespace
       - OvfElement
         - OvfElementInvalidValue
         - OvfUnexpectedElement
         - OvfDuplicateElement
         - OvfMissingElement
         - OvfMissingElementNormalBoundary
         - OvfDuplicatedElementBoundary
       - OvfAttribute
         - OvfMissingAttribute
         - OvfInvalidValue
           - OvfInvalidValueFormatMalformed
           - OvfInvalidValueConfiguration
           - OvfInvalidValueReference
           - OvfInvalidValueEmpty
       - OvfProperty
         - OvfPropertyType
         - OvfPropertyValue
         - OvfPropertyNetwork
         - OvfPropertyQualifier
         - OvfPropertyQualifierWarning
     - OvfConstraint
       - OvfDiskOrderConstraint
       - OvfHostResourceConstraint
     - OvfUnsupportedPackage
       - OvfNoHostNic
       - OvfInvalidVmName
       - OvfUnsupportedAttribute
         - OvfUnsupportedAttributeValue
       - OvfUnsupportedElement
         - OvfUnsupportedElementValue
         - OvfUnsupportedSection
         - OvfNoSpaceOnController
       - OvfUnsupportedType
       - OvfUnsupportedSubType
       - OvfHardwareCheck
       - OvfNoSupportedHardwareFamily
     - OvfExport
       - OvfExportFailed
       - OvfHardwareExport
         - OvfUnsupportedDeviceExport
         - OvfUnknownDeviceBacking
         - OvfConnectedDevice
           - OvfConnectedDeviceISO
         - OvfUnableToExportDisk
       - OvfPropertyExport
       - OvfPropertyNetworkExport
       - OvfDuplicatedPropertyIdExport
     - OvfImport (these are typically returned as warnings)
       - OvfImportFailed
       - OvfHardwareCheck
       - OvfMissingHardware
       - OvfCpuCompatibility
       - OvfCpuCompatibilityCheckNotSupported
       - OvfUnsupportedDiskProvisioning
       - OvfDuplicatedPropertyIdImport
       - OvfNetworkMappingNotSupported
     - OvfSystemFault
       - OvfDiskMappingNotFound
       - OvfHostValueNotParsed
       - OvfInternalError
       - OvfUnsupportedDeviceBackingOption
       - OvfUnsupportedDeviceBackingInfo
       - OvfToXmlUnsupportedElement
       - OvfUnknownDevice
       - OvfUnknownEntity
     - OvfConsumerCallbackFault
       - OvfConsumerFault
       - OvfConsumerCommunicationError
       - OvfConsumerInvalidSection
       - OvfConsumerUndeclaredSection
       - OvfConsumerUndefinedPrefix
         
   All messages go into the vimlocale
   """
   pass

class OvfExport(OvfFault):
   """A common base class to host all the Ovf Lib Export Exceptions."""
   pass


class ConnectedIso(OvfExport):
   """
   Attributes:
       cdrom: The CD-ROM drive that caused the event.
       filename: The filename of the ISO
   """
   cdrom: pyVmomi.vim.vm.device.VirtualCdrom
   filename: str

class VirtualHardwareCompatibilityIssue(VmConfigFault):
   """
   There is a problem with the compatibility between the intended execution host
   and the virtual machine.
   
   This may be an error or warning depending on
   the specific fault subclass.
   """
   pass


class CpuIncompatible(VirtualHardwareCompatibilityIssue):
   """
   Deprecated: As of vSphere API 6.5 use
   `pyVmomi.vim.fault.FeatureRequirementsNotMet`The host is not compatible with the CPU feature requirements of the
   virtual machine, for a particular CPUID register.
   
   A subclass of this fault
   may be used to express the incompatibilities in a more easily
   understandable format.
   
   Attributes:
       level: The CpuIdInfo level where a problem was detected.
           
           Other levels may
           also have problems.
       registerName: The CpuIdInfo register where a problem was detected.
           
           Other registers
           may also have problems. Possible register names are eax, ebx, ecx, or edx.
       registerBits: The contents of the register on the target host, in CpuIdInfo register
           format.
           
           The '-' character indicates an unknown value.
       desiredBits: The desired values for the register's bits.
           
           The 'x' character indicates
           don't-care.
       host: The host that is not compatible with the requirements.
   """
   level: int
   registerName: str
   registerBits: _typing.Optional[str] = None
   desiredBits: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class CpuCompatibilityUnknown(CpuIncompatible):
   """
   Deprecated: As of VI API 2.5, use `pyVmomi.vim.fault.CpuIncompatible` and its other subclasses,
   not this one.Compatibility between the virtual machine's host and its CPU
   feature requirements cannot be determined, because not enough information
   is available about the CPU features of the host.
   """
   pass

class CpuHotPlugNotSupported(VmConfigFault):
   """
   Thrown when virtual CPUs cannot be hot-added or hot-removed from
   the virtual machine.
   """
   pass

class CpuIncompatible1ECX(CpuIncompatible):
   """
   Deprecated: As of vSphere API 6.5 use
   `pyVmomi.vim.fault.FeatureRequirementsNotMet`Convenience subclass for calling out some named features among the
   incompatibilities found in CPUID level 1 register ecx.
   
   Attributes:
       sse3: Flag to indicate bit 0 is incompatible.
       pclmulqdq: Flag to indicate bit 1 is incompatible.
       ssse3: Flag to indicate bit 9 is incompatible.
       sse41: Flag to indicate bit 19 is incompatible.
       sse42: Flag to indicate bit 20 is incompatible.
       aes: Flag to indicate bit 25 is incompatible.
       other: Flag to indicate that bits other than 0/1/9/19/20/25 are incompatible.
           
           I.e. the detected incompatibilities cannot be completely described by
           the sse3, pclmulqdq, ssse3, sse41, sse42, and/or aes flags.
       otherOnly: Flag to indicate that the sse3, pclmulqdq, ssse3, sse41, sse42, and aes
           flags are all false, and the \"other\" flag is true.
           
           Purely a convenience
           property for the client processing this fault.
   """
   sse3: bool
   pclmulqdq: bool
   ssse3: bool
   sse41: bool
   sse42: bool
   aes: bool
   other: bool
   otherOnly: bool

class CpuIncompatible81EDX(CpuIncompatible):
   """
   Deprecated: As of vSphere API 6.5 use
   `pyVmomi.vim.fault.FeatureRequirementsNotMet`Convenience subclass for calling out some named features among the
   incompatibilities found in CPUID level 0x80000001 register edx.
   
   Attributes:
       nx: Flag to indicate bit 20 is incompatible.
       ffxsr: Flag to indicate bit 25 is incompatible.
       rdtscp: Flag to indicate bit 27 is incompatible.
       lm: Flag to indicate bit 29 is incompatible.
       other: Flag to indicate that bits other than 20/25/27/29 are incompatible.
           
           I.e. the detected incompatibilities cannot be completely described by
           the nx, ffxsr, rdtscp, and/or lm flags.
       otherOnly: Flag to indicate that the nx, ffxsr, rdtscp, and lm flags are all false,
           and the \"other\" flag is true.
           
           Purely a convenience property for the
           client processing this fault.
   """
   nx: bool
   ffxsr: bool
   rdtscp: bool
   lm: bool
   other: bool
   otherOnly: bool

class CustomizationPending(CustomizationFault):
   """
   A customization operation is already pending on this virtual
   machine and is awaiting power-up to complete.
   """
   pass


class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The virtual machine uses a device type that is not supported on the
   host.
   
   If this fault is returned as a subfault of
   `pyVmomi.vim.fault.DisallowedMigrationDeviceAttached`, this indicates that although
   this device may be supported on the destination host, the hosts do
   not support the requested migration of the virtual machine while
   using this device.
   
   Attributes:
       device: The label of the device.
       reason: The specific reason why the device is not supported.
           
           Values should come from `pyVmomi.vim.fault.DeviceNotSupported.Reason`.
           This might not be set if we're not sure of the reason, or
           if this doesn't make sense in the context. For example,
           in the `pyVmomi.vim.fault.DisallowedMigrationDeviceAttached` context
           we already know the problem.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Reasons why a virtual device would not be supported on a host.
      
      Attributes:
          host: The host does not support this virtual device at all.
          guest: The device is supported by the host in general, but not for
              the specific guest OS the virtual machine is using.
          ft: The device is supported by the host and guest OS, but not for
              the vSphere Fault Tolerance.
              
              Since: vSphere API Release 8.0.3.0
      """
      host: _typing.ClassVar['DeviceNotSupported.Reason'] = 'host'
      guest: _typing.ClassVar['DeviceNotSupported.Reason'] = 'guest'
      ft: _typing.ClassVar['DeviceNotSupported.Reason'] = 'ft'

   device: str
   reason: _typing.Optional[str] = None

class DeviceBackingNotSupported(DeviceNotSupported):
   """
   The device is backed by a backing type which is not supported
   for this particular device.
   
   If this fault is returned as a subfault of
   DisallowedMigrationDeviceAttached, this indicates that although
   this backing for the device may be supported on the destination
   host, the hosts do not support the requested migration of the
   virtual machine while using this device with this backing.
   
   Attributes:
       backing: The type of the backing.
   """
   backing: str

class DVPortNotSupported(DeviceBackingNotSupported):
   """
   The virtual machine is configured to use a DVPort, which is not
   supported on the host.
   
   This could be because the host
   does not support VDS at all, or because the host has not
   joined a VDS.
   """
   pass


class DasConfigFault(VimFault):
   """
   This fault indicates that some error has occurred during the
   configuration of the host for HA.
   
   This may be subclassed by a more specific fault.
   
   Attributes:
       reason: The reason why the HA configuration failed, if known.
           
           Values should come from `pyVmomi.vim.fault.DasConfigFault.DasConfigFaultReason`.
       output: The output (stdout/stderr) from executing the configuration.
       event: The list of events containing details why the configuration failed, if known.
   """
   class DasConfigFaultReason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          HostNetworkMisconfiguration: There is a problem with the host network configuration.
          HostMisconfiguration: There is a problem with the host configuration.
          InsufficientPrivileges: The privileges were insufficient for the operation.
          NoPrimaryAgentAvailable: There was no running primary agent available to contact.
              
              Check that your other hosts don't have HA errors
          Other: The HA configuration failed for other reasons.
          NoDatastoresConfigured: No datastores defined for this host
          CreateConfigVvolFailed: Failure to create config vvol
          VSanNotSupportedOnHost: Host in vSAN cluster does not support vSAN.
          DasNetworkMisconfiguration: There is a problem with the cluster network configuration.
          SetDesiredImageSpecFailed: Setting desired imageSpec in Personality Manager failed
          ApplyHAVibsOnClusterFailed: The ApplyHA call to Personality Manager failed
      """
      HostNetworkMisconfiguration: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'HostNetworkMisconfiguration'
      HostMisconfiguration: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'HostMisconfiguration'
      InsufficientPrivileges: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'InsufficientPrivileges'
      NoPrimaryAgentAvailable: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'NoPrimaryAgentAvailable'
      Other: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'Other'
      NoDatastoresConfigured: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'NoDatastoresConfigured'
      CreateConfigVvolFailed: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'CreateConfigVvolFailed'
      VSanNotSupportedOnHost: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'VSanNotSupportedOnHost'
      DasNetworkMisconfiguration: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'DasNetworkMisconfiguration'
      SetDesiredImageSpecFailed: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'SetDesiredImageSpecFailed'
      ApplyHAVibsOnClusterFailed: _typing.ClassVar['DasConfigFault.DasConfigFaultReason'] = 'ApplyHAVibsOnClusterFailed'

   reason: _typing.Optional[str] = None
   output: _typing.Optional[str] = None
   event: list[pyVmomi.vim.event.Event] = []


class DatabaseError(pyVmomi.vmodl.RuntimeFault):
   """
   A DatabaseError exception is thrown if an
   operation failed when accessing the external
   database.
   
   This typically is because
   the database is (temporarily) unavailable or
   because of network problems.
   """
   pass


class DatacenterMismatch(MigrationFault):
   """
   The input arguments had entities that did not belong to the same
   datacenter.
   
   Attributes:
       invalidArgument: The list of invalid arguments.
       expectedDatacenter: The expected datacenter for the arguments.
   """
   class Argument(pyVmomi.vmodl.DynamicData):
      """
      An input entity argument that belongs to a mismatched datacenter.
      
      Attributes:
          entity: The invalid input entity.
          inputDatacenter: The datacenter for this entity.
      """
      entity: pyVmomi.vim.ManagedEntity
      inputDatacenter: _typing.Optional[pyVmomi.vim.Datacenter] = None

   invalidArgument: list[DatacenterMismatch.Argument] = []
   expectedDatacenter: pyVmomi.vim.Datacenter


class InvalidDatastore(VimFault):
   """
   An InvalidDatastore exception is thrown if an operation fails because of a
   problem with the specified datastore.
   
   Typically, a subclass of this
   exception is thrown, indicating a problem such as an inaccessible datastore
   or an invalid datastore path.
   
   Attributes:
       datastore: The datastore that is invalid.
       name: The name of the datastore that is invalid.
   """
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   name: _typing.Optional[str] = None


class DatastoreNotWritableOnHost(InvalidDatastore):
   """
   This exception is thrown if a datastore is not
   writable on the target host.
   
   Attributes:
       host: The target host on which the datastore is not writable.
   """
   host: pyVmomi.vim.HostSystem


class DeltaDiskFormatNotSupported(VmConfigFault):
   """
   Thrown on an attempt to use an unsupported delta disk format.
   
   Attributes:
       datastore: The datastores which do not support the specified format.
       deltaDiskFormat: The format not supported.
           
           See `pyVmomi.vim.vm.device.VirtualDisk.DeltaDiskFormat`.
   """
   datastore: list[pyVmomi.vim.Datastore] = []
   deltaDiskFormat: str

class DestinationSwitchFull(CannotAccessNetwork):
   """
   For one of the networks that the virtual machine is using, the corresponding
   switch on the host is full.
   
   If returned as part of migration checks, this is an error
   if either of the following is true, a warning otherwise:
   - The virtual ethernet card device backing is a distributed virtual switch
   - The virtual ethernet card device backing is a standard network and the
     the device is connected
   """
   pass

class DestinationVsanDisabled(CannotMoveVsanEnabledHost):
   """
   Fault thrown for the case that an attempt is made to move a host which
   is enabled for VSAN into a `pyVmomi.vim.ClusterComputeResource` which is
   disabled for VSAN.
   
   See Also: `pyVmomi.vim.fault.CannotMoveVsanEnabledHost`
   
   Attributes:
       destinationCluster: Name of the disabled destination `pyVmomi.vim.ClusterComputeResource`.
   """
   destinationCluster: str

class DeviceControllerNotSupported(DeviceNotSupported):
   """
   The device in question is supported, but the device-controller
   combination is not supported.
   
   If this fault is returned as a subfault of
   DisallowedMigrationDeviceAttached, this indicates that although
   this device-controller combination may be supported on the
   destination host, the hosts do not support the requested migration
   of the virtual machine while using this device and controller.
   
   Attributes:
       controller: The type of the controller.
   """
   controller: str


class InvalidVmConfig(VmConfigFault):
   """
   Thrown when virtual machine creation or configuration fails.
   
   This is
   a base type for all virtual machine configuration errors.
   
   Attributes:
       property: Path of the property in configSpec that has an invalid value.
   """
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None

class InvalidDeviceSpec(InvalidVmConfig):
   """
   An InvalidDeviceSpec exception is thrown if
   a virtual machine creation or configuration fails because a device
   specification contains an invalid value.
   
   Attributes:
       deviceIndex: Index of the device in the configuration specification that has the invalid value.
   """
   deviceIndex: int

class DeviceHotPlugNotSupported(InvalidDeviceSpec):
   """
   A DeviceHotPlugNotSupported exception is thrown if the specified device
   cannot be hot-added or hot-removed from the virtual machine
   at this time.
   """
   pass

class DeviceNotFound(InvalidDeviceSpec):
   """
   A DeviceNotFound exception is thrown if
   a device to be edited or removed
   cannot be found.
   
   Most likely, the client incorrectly passed
   the device key.
   """
   pass

class DeviceUnsupportedForVmPlatform(InvalidDeviceSpec):
   """
   A DeviceUnsupportedForVmPlatform exception is thrown if the specified device
   is not supported on the platform on which the virtual machine is being
   created/configured.
   
   For example, this exception might be thrown if a client
   incorrectly attempts to add a device supported only on ESX Server to a
   virtual machine on a hosted product.
   """
   pass

class DeviceUnsupportedForVmVersion(InvalidDeviceSpec):
   """
   A DeviceUnsupportedForVmVersion exception is thrown if a specific device
   is not supported for a given version of the virtual machine.
   
   Attributes:
       currentVersion: The current version of the virtual machine.
       expectedVersion: The minimum expected virtual machine version needed to
           support this device.
   """
   currentVersion: str
   expectedVersion: str

class DigestNotSupported(DeviceNotSupported):
   """
   The digest file of the specified virtual disk is not supported.
   
   Typically, this fault is returned as part of a parent fault like
   `pyVmomi.vim.fault.VmConfigIncompatibleForFaultTolerance`, indicating that the
   virtual disk's digest file needs to be changed before fault tolerance can be
   enabled on the associated virtual machine.
   """
   pass

class DirectoryNotEmpty(FileFault):
   """
   This fault is thrown when an operation fails because the specified
   directory is not empty.
   """
   pass

class DisableAdminNotSupported(HostConfigFault):
   """
   Fault thrown when an attempt is made to move a disk with associated snapshots to a destination host.
   
   If such a move were to occur, snapshots associated with the disk would be irrevocably
   lost. This is always an error.
   """
   pass


class DisallowedChangeByService(pyVmomi.vmodl.RuntimeFault):
   """
   Fault thrown if the disallowed operation is invoked by the client.
   
   The
   change is disallowed because it conflicts with target state maintained
   by a service. The corresponding method is usually not disabled because
   only a subset of changes carried out by the method is disallowed. For
   example, an online extend executed via virtual machine reconfigure
   method is not allowed if replication is enabled on a virtual machine.
   
   Attributes:
       serviceName: The service that has disallowed the change.
       disallowedChange: The change this is not allowed, the set of possible values is
           described in `pyVmomi.vim.fault.DisallowedChangeByService.DisallowedChange`.
   """
   class DisallowedChange(pyVmomi.VmomiSupport.Enum):
      """
      The disallowed change type.
      
      Attributes:
          hotExtendDisk: Online extend disk operation.
      """
      hotExtendDisk: _typing.ClassVar['DisallowedChangeByService.DisallowedChange'] = 'hotExtendDisk'

   serviceName: str
   disallowedChange: _typing.Optional[str] = None

class DisallowedDiskModeChange(InvalidDeviceSpec):
   """
   Thrown when the `pyVmomi.vim.VirtualMachine.reconfigure` operation
   includes a change to the `pyVmomi.vim.vm.device.VirtualDiskOption.DiskMode`
   property.
   
   This property cannot be changed as long as a virtual machine
   has an existing snapshot.
   """
   pass


class DisallowedMigrationDeviceAttached(MigrationFault):
   """
   The virtual machine is using a type of device that prevents migration.
   
   Attributes:
       fault: A fault specifies the particular device issue.
           
           This is typically
           a subclass of VirtualHardwareCompatibilityIssue, such as
           RawDiskNotSupported, RemoteDeviceNotSupported, or SharedBusControllerNotSupported
   """
   fault: pyVmomi.vmodl.MethodFault


class DisallowedOperationOnFailoverHost(pyVmomi.vmodl.RuntimeFault):
   """
   Fault thrown when an attempt is made to perform a disallowed operation on a
   host that has been configured as a failover host in an cluster that has High
   Availability enabled.
   
   See `pyVmomi.vim.cluster.FailoverHostAdmissionControlPolicy`.
   Examples of such operations are destroying a host, moving a host out of a cluster,
   or powering on a virtual machine on a specific host.
   
   Attributes:
       host: The failover host.
       hostname: Name of the failover host.
   """
   host: pyVmomi.vim.HostSystem
   hostname: str

class DisconnectedHostsBlockingEVC(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster, or to
   select a less-featureful EVC mode for a cluster where EVC is already enabled,
   has failed because the cluster contains one or more disconnected hosts.
   """
   pass


class VsanDiskFault(VsanFault):
   """
   Base exception class for VSAN disk-related faults.
   
   Attributes:
       device: The canonical name for the disk at hand, if applicable.
   """
   device: _typing.Optional[str] = None

class DiskHasPartitions(VsanDiskFault):
   """
   Fault used for disks which have existing, non-VSAN partitions.
   
   See Also: `pyVmomi.vim.host.StorageSystem.updateDiskPartitions`, `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`
   """
   pass

class DiskIsLastRemainingNonSSD(VsanDiskFault):
   """
   Fault thrown for the case that an attempt is made to delete the last
   `pyVmomi.vim.vsan.host.DiskMapping.nonSsd` from a `pyVmomi.vim.vsan.host.DiskMapping`.
   
   See Also: `pyVmomi.vim.host.VsanSystem.removeDisk`, `pyVmomi.vim.host.VsanSystem.removeDiskMapping`
   """
   pass

class DiskIsNonLocal(VsanDiskFault):
   """
   Fault used for disks which are ineligible for VSAN because they are
   considered non-local.
   
   See Also: `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`
   """
   pass

class DiskIsUSB(VsanDiskFault):
   """
   Fault used for disks which are ineligible for VSAN because they are USB
   disks.
   
   See Also: `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`
   """
   pass

class DiskMoveTypeNotSupported(MigrationFault):
   """
   Specifying non-standard disk movement types is not supported.
   
   See Also: `pyVmomi.vim.vm.RelocateSpec.diskMoveType`, `pyVmomi.vim.vm.RelocateSpec.DiskLocator.diskMoveType`
   """
   pass

class DiskNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The host does not support the backings for the disks specified by the virtual
   machine.
   
   For example, this fault is thrown if a virtual machine is created from
   a template that specifies backings that the host does not have. Similarly, this fault
   is thrown if a virtual machine is registered on a host that does not support the
   specified backings.
   
   Attributes:
       disk: The ID of disk that is not supported.
   """
   disk: int

class DiskTooSmall(VsanDiskFault):
   """Fault used for disks which are too small for usage by VSAN."""
   pass

class DomainNotFound(ActiveDirectoryFault):
   """
   Fault indicating that the domain controller
   for domainName cannot be reached.
   
   Attributes:
       domainName: The domain that cannot be accessed.
   """
   domainName: str

class DrsDisabledOnVm(VimFault):
   """
   This fault is thrown when DRS cannot move a virtual machine because
   DRS is disabled on it (i.e., it is pinned on its registered host).
   """
   pass


class DrsVmotionIncompatibleFault(VirtualHardwareCompatibilityIssue):
   """
   This fault is thrown when DRS tries to migrate a virtual machine to a host,
   but finds that the host is incompatible with the given virtual machine.
   
   Attributes:
       host: The host that is incompatible with a given virtual machine.
   """
   host: pyVmomi.vim.HostSystem

class DuplicateDisks(VsanDiskFault):
   """
   Fault used to denote a duplicate set of disks were incorrectly specified
   for a given operation.
   
   See Also: `pyVmomi.vim.host.VsanSystem.addDisks`, `pyVmomi.vim.host.VsanSystem.initializeDisks`
   """
   pass


class DuplicateName(VimFault):
   """
   A DuplicateName exception is thrown because a name already exists
   in the same name space.
   
   Attributes:
       name: The name that is already bound in the name space.
       object: Managed object that already holds the name.
   """
   name: str
   object: pyVmomi.VmomiSupport.ManagedObject

class DuplicateVsanNetworkInterface(VsanFault):
   """
   Fault thrown for cases that duplicate network interface names are
   incorrectly specified for a VSAN operation.
   
   See Also: `pyVmomi.vim.host.VsanSystem.update`, `pyVmomi.vim.ComputeResource.reconfigureEx`
   
   Attributes:
       device: The network interface name found to be duplicated.
   """
   device: str


class DvsApplyOperationFault(DvsFault):
   """
   Thrown if a vSphere Distributed Switch apply operation failed to set or remove
   some of the specified objects.
   
   Attributes:
       objectFault: Faults occurred on the host during a DistributedVirtualSwitch operation.
   """
   class FaultOnObject(pyVmomi.vmodl.DynamicData):
      """
      The fault occurred during an apply operation.
      
      Attributes:
          objectId: The object identifier.
              
              It should be UUID for vSphere Distributed Switches,
              keys for vNetwork distributed portgroups and ports.
          type: The Type of the objects.
          fault: The fault that occurred.
      """
      objectId: str
      type: type
      fault: pyVmomi.vmodl.MethodFault

   objectFault: list[DvsApplyOperationFault.FaultOnObject] = []


class DvsNotAuthorized(DvsFault):
   """
   Thrown if
   `pyVmomi.vim.DistributedVirtualSwitch.Capability.dvsOperationSupported`
   is false and `pyVmomi.vim.DistributedVirtualSwitch.ConfigInfo.extensionKey` is not same
   as the extension key of the login-session.
   
   Attributes:
       sessionExtensionKey: The extension key associated with the user-session.
       dvsExtensionKey: The value of `pyVmomi.vim.DistributedVirtualSwitch.ConfigInfo.extensionKey`.
   """
   sessionExtensionKey: _typing.Optional[str] = None
   dvsExtensionKey: _typing.Optional[str] = None


class DvsOperationBulkFault(DvsFault):
   """
   Thrown if a DistributedVirtualSwitch operation failed on some of the host members.
   
   Attributes:
       hostFault: Faults occurred on the host during a DistributedVirtualSwitch operation.
   """
   class FaultOnHost(pyVmomi.vmodl.DynamicData):
      """
      The fault occurred on the host during an operation.
      
      Attributes:
          host: The host.
          fault: The fault that occurred.
      """
      host: pyVmomi.vim.HostSystem
      fault: pyVmomi.vmodl.MethodFault

   hostFault: list[DvsOperationBulkFault.FaultOnHost] = []


class DvsScopeViolated(DvsFault):
   """
   Deprecated: as of vSphere API 5.5Thrown if a entity trying to connect to a port or portgroup but it is not in the
   port or portgroup's scope.
   
   Attributes:
       scope: The configured scope.
       entity: The entity that violates the scope.
   """
   scope: list[pyVmomi.vim.ManagedEntity] = []
   entity: pyVmomi.vim.ManagedEntity


class NotSupportedHost(HostConnectFault):
   """
   A NotSupportedHostFault occurs when the host is of a type
   that is not supported.
   
   Attributes:
       productName: The name of the unsupported product if available;
           for example, \"VMware ESX Server\".
       productVersion: The version of the unsupported product; for example, \"1.5.2\"
   """
   productName: _typing.Optional[str] = None
   productVersion: _typing.Optional[str] = None

class NotSupportedHostInCluster(NotSupportedHost):
   """
   A NotSupportedHostInCluster fault occurs when the host does not support
   the necessary features to participate in the cluster.
   """
   pass


class EVCAdmissionFailed(NotSupportedHostInCluster):
   """
   The host does not satisfy the admission requirements for the Enhanced
   VMotion Compatibility mode of the cluster.
   
   Attributes:
       faults: The faults that caused this EVC test to fail
           (e.g.
           
           FeatureRequirementsNotMet faults).
   """
   faults: list[pyVmomi.vmodl.MethodFault] = []

class EVCAdmissionFailedCPUFeaturesForMode(EVCAdmissionFailed):
   """
   The host's CPU hardware is a family/model that should support the
   Enhanced VMotion Compatibility mode of the cluster, but some necessary
   CPU features are not present.
   
   Attributes:
       currentEVCModeKey: The Enhanced VMotion Compatibility mode that is currently in effect for
           the cluster.
   """
   currentEVCModeKey: str

class EVCAdmissionFailedCPUModel(EVCAdmissionFailed):
   """
   The host's CPU hardware is a family/model that does not support any
   Enhanced VMotion Compatibility mode.
   """
   pass

class EVCAdmissionFailedCPUModelForMode(EVCAdmissionFailed):
   """
   The host's CPU hardware is a family/model that does not support the Enhanced
   VMotion Compatibility mode of the cluster.
   
   Attributes:
       currentEVCModeKey: The Enhanced VMotion Compatibility mode that is currently in effect for
           the cluster.
   """
   currentEVCModeKey: str

class EVCAdmissionFailedCPUVendor(EVCAdmissionFailed):
   """
   The host's CPU vendor does not match the required CPU vendor for the
   Enhanced VMotion Compatibility mode of the cluster.
   
   Attributes:
       clusterCPUVendor: The CPU vendor required for entering the cluster.
       hostCPUVendor: The CPU vendor of the host.
   """
   clusterCPUVendor: str
   hostCPUVendor: str

class EVCAdmissionFailedCPUVendorUnknown(EVCAdmissionFailed):
   """
   The host's CPU vendor is unknown, which prevents admission into an Enhanced
   VMotion Compatibility cluster.
   """
   pass

class EVCAdmissionFailedHostDisconnected(EVCAdmissionFailed):
   """
   The host is not connected, which prevents admission into an Enhanced
   VMotion Compatibility cluster.
   """
   pass

class EVCAdmissionFailedHostSoftware(EVCAdmissionFailed):
   """The host's software does not support any Enhanced VMotion Compatibility mode."""
   pass

class EVCAdmissionFailedHostSoftwareForMode(EVCAdmissionFailed):
   """
   The host's software does not support the Enhanced VMotion Compatibility
   mode of the cluster.
   """
   pass

class EVCAdmissionFailedVmActive(EVCAdmissionFailed):
   """
   An attempt to move or add a host into an Enhanced VMotion Compatibility
   cluster has failed for the following reason:
   - The host exposes additional compatibility-relevant CPU features beyond
     those present in the baseline mandated by the cluster's EVC mode.
   - The host has powered-on or suspended virtual machines.
     
   Therefore the host may not be admitted into the cluster, since its virtual
   machines may be using CPU features suppressed in the cluster.
   
   Note that in rare cases, this may occur even if the host's
   `pyVmomi.vim.host.Summary.maxEVCModeKey` corresponds to the EVC
   mode of the cluster. This means that even though that EVC mode is the best
   match for the host's hardware, the host still has some features beyond
   those present in the baseline for that EVC mode.
   """
   pass

class EVCModeIllegalByVendor(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster, or change
   the EVC configuration on an EVC-enabled cluster, has failed because the
   selected EVC mode is not legal for the CPU hardware vendor of the hosts
   currently in the cluster.
   
   Attributes:
       clusterCPUVendor: The CPU vendor in use in the cluster.
       modeCPUVendor: The CPU vendor for the requested EVC mode.
   """
   clusterCPUVendor: str
   modeCPUVendor: str


class EVCModeUnsupportedByHosts(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster has failed
   because there are hosts in the cluster with a CPU feature baseline below the
   desired EVC mode.
   
   Attributes:
       evcMode: The requested EVC mode.
       host: The set of hosts which are blocking EVC because their CPU hardware does
           not support the requested EVC mode.
       hostName: The names of the hosts in the host array.
   """
   evcMode: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostHardware(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility (EVC) on a cluster has
   failed because one or more hosts in the cluster do not match the desired
   featureset and lack hardware support for EVC.
   
   Attributes:
       host: The set of hosts which are blocking EVC because their CPU hardware does
           not support CPUID override.
       hostName: The names of the hosts in the host array.
   """
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostSoftware(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility (EVC) on a cluster has
   failed because one or more hosts in the cluster lack software support for
   EVC.
   
   Attributes:
       host: The set of hosts which are blocking EVC because their virtualization
           software does not support CPUID override.
       hostName: The names of the hosts in the host array.
   """
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []

class EightHostLimitViolated(VmConfigFault):
   """
   Only virtual machines on eight different hosts can have a single
   virtual disk backing opened for read at once.
   
   This fault occurs when moving or powering on this virtual
   machine would cause a violation of the above constraint.
   This only occurs when multiple virtual machines are sharing a
   single disk backing.
   
   Note that there is no limit on the number of virtual machines
   who share a disk backings, so long as they are running on
   eight or fewer hosts.
   """
   pass


class EncryptionKeyRequired(InvalidState):
   """
   An EncryptionKeyRequired fault occurs when an operation fails due
   to one or more required encryption keys.
   
   Attributes:
       requiredKey: A list of required key identifiers.
   """
   requiredKey: list[pyVmomi.vim.encryption.CryptoKeyId] = []


class ExpiredFeatureLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   An ExpiredFeatureLicense fault is thrown if an attempt to acquire an Addon license
   'feature failed for count 'count'.
   """
   feature: str
   count: int
   expirationDate: _datetime.datetime

class ExpiredAddonLicense(ExpiredFeatureLicense):
   """
   An ExpiredAddonLicense fault is thrown if an attempt to acquire an Addon license
   'feature failed for count 'count'.
   """
   pass

class ExpiredEditionLicense(ExpiredFeatureLicense):
   """
   An ExpiredEditionLicense fault is thrown if an attempt to acquire an Edition license
   'feature failed for count 'count'.
   """
   pass


class ExtendedFault(VimFault):
   """
   This fault is the container for faults logged by extensions.
   
   Attributes:
       faultTypeId: The id of the type of extended fault.
       data: Key/value pairs associated with fault.
   """
   faultTypeId: str
   data: list[pyVmomi.vim.KeyValue] = []


class FailToEnableSPBM(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   Fault type that could be thrown when enabling SPBM(Storage Policy
   Based Management) feature of a compute resource.
   
   Attributes:
       cs: The compute resource
       csName: The computer resource name
       hostLicenseStates: Array of `pyVmomi.vim.ComputeResource.HostSPBMLicenseInfo` that
           contains SPBM license information for all hosts in the compute resource
   """
   cs: pyVmomi.vim.ComputeResource
   csName: str
   hostLicenseStates: list[pyVmomi.vim.ComputeResource.HostSPBMLicenseInfo] = []


class FailToLockFaultToleranceVMs(pyVmomi.vmodl.RuntimeFault):
   """
   Thrown when trying to state lock a Fault Tolerance VM, and the
   other VM in the same Fault Tolerance pair is already locked.
   
   Attributes:
       vmName: The name of the vm to be locked.
       vm: The vm to be locked, this can be a Fault Tolerance primary or secondary VM
       alreadyLockedVm: The vm that is already locked, this can be a Fault Tolerance primary or secondary VM
   """
   vmName: str
   vm: pyVmomi.vim.VirtualMachine
   alreadyLockedVm: pyVmomi.vim.VirtualMachine


class FaultToleranceAntiAffinityViolated(MigrationFault):
   """
   More than one VM in the same fault tolerance group are placed on the same host
   
   Attributes:
       hostName: The name of the host.
       host: The host.
   """
   hostName: str
   host: pyVmomi.vim.HostSystem


class FaultToleranceCannotEditMem(VmConfigFault):
   """
   The memory size, reservation, limit or shares of a virtual machine cannot
   be edited if Fault Tolerance is turned on
   
   Attributes:
       vmName: The name of the VM.
       vm: The VM.
   """
   vmName: str
   vm: pyVmomi.vim.VirtualMachine

class FaultToleranceCpuIncompatible(CpuIncompatible):
   """
   Convenience subclass for calling out some named features among the
   incompatibilities found in CPUID level 1 register ecx for FT vms.
   
   Attributes:
       model: Flag to indicate CPU model is incompatible.
       family: Flag to indicate CPU family is incompatible.
       stepping: Flag to indicate CPU stepping is incompatible.
   """
   model: bool
   family: bool
   stepping: bool

class FaultToleranceNeedsThickDisk(MigrationFault):
   """
   Fault Tolerance VM requires thick disks
   
   Attributes:
       vmName: The name of the VM.
   """
   vmName: str


class FaultToleranceNotLicensed(VmFaultToleranceIssue):
   """
   This fault is thrown when fault tolerance has not been licensed on the
   source or destination host.
   
   It must be licensed on both hosts.
   
   Attributes:
       hostName: The host name
   """
   hostName: _typing.Optional[str] = None

class FaultToleranceNotSameBuild(MigrationFault):
   """
   The destination host does not have the same build or Fault Tolerance
   feature version number as the source host.
   
   Attributes:
       build: The string.
   """
   build: str


class FaultTolerancePrimaryPowerOnNotAttempted(VmFaultToleranceIssue):
   """
   This fault is used to report that VirtualCenter did not attempt to power on
   a Fault Tolerance secondary virtual machine because it was unable to
   power on the corresponding Fault Tolerance primary virtual machine.
   
   Attributes:
       secondaryVm: The secondary virtual machine that was not attempted
       primaryVm: The corresponding primary virtual machine
   """
   secondaryVm: pyVmomi.vim.VirtualMachine
   primaryVm: pyVmomi.vim.VirtualMachine


class FaultToleranceVmNotDasProtected(VimFault):
   """
   A FaultToleranceVmNotDasProtected fault occurs when an Fault Tolerance VM
   is not protected by HA and the operation for terminating the primary VM
   or secondary VM is invoked.
   
   Attributes:
       vm: The Fault Toelrance primary VM
       vmName: Name of the VM
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class FcoeFault(VimFault):
   """Deprecated: As of vSphere API 8.0. Software FCoE not supported.Base class for faults that can be thrown while invoking FCoE management operations."""
   pass

class FcoeFaultPnicHasNoPortSet(FcoeFault):
   """
   Deprecated: As of vSphere API 8.0. Software FCoE not supported.This fault indicates the given Software Fcoe NIC has no uplink ports
   that is required for initiating a discovery.
   """
   nicDevice: str


class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
   """
   The host does not meet feature requirements of the virtual machine.
   
   Attributes:
       featureRequirement: The feature requirements that were not met.
       vm: The virtual machine whose feature requirements were not met.
       host: The host whose capabilities did not meet the virtual machine's feature requirements.
   """
   featureRequirement: list[pyVmomi.vim.vm.FeatureRequirement] = []
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class FileAlreadyExists(FileFault):
   """
   This fault is thrown when an operation attempts to create a file using the name of
   an existing file.
   """
   pass

class FileBackedPortNotSupported(DeviceNotSupported):
   """
   The virtual machine has a port (either a SerialPort or a ParallelPort) which is
   backed by a file.
   
   This is an error when migrating a virtual machine with the device
   connected, and can be returned as a subfault of DisallowedMigrationDeviceAttached.
   """
   pass

class FileLocked(FileFault):
   """Thrown if an attempt is made to lock a file that is already in use."""
   pass

class FileNameTooLong(FileFault):
   """
   This fault is thrown when an operation fails because the name of the
   specified file is too long.
   """
   pass

class FileNotFound(FileFault):
   """
   This fault is thrown when an operation fails because the specified file
   does not exist.
   """
   pass

class FileNotWritable(FileFault):
   """Thrown if an attempt is made to write to a read-only file."""
   pass


class FileTooLarge(FileFault):
   """
   This fault is thrown when an operation fails because the file is larger
   than the maximum file size supported by the datastore.
   
   Attributes:
       datastore: The name of the datastore that does not support the file's size.
       fileSize: The size (in bytes) of the file.
       maxFileSize: The max file size (in bytes) supported on the datastore.
   """
   datastore: str
   fileSize: pyVmomi.VmomiSupport.long
   maxFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class FilesystemQuiesceFault(SnapshotFault):
   """
   This fault is thrown when creating a quiesced snapshot failed
   because the create snapshot operation exceeded the time limit
   for holding off I/O in the frozen VM.
   
   This indicates that when we attempted to thaw the VM after
   creating the snapshot, we got an error back indicating that
   the VM was not frozen anymore. In this case, we roll back
   the entire snapshot create operation and throw this exception.
   """
   pass


class ResourceInUse(VimFault):
   """
   A ResourceInUse fault indicating that some error has occurred because a
   resource was in use.
   
   Information about the resource that is in use may
   be supplied.
   
   Attributes:
       type: Type of resource that is in use.
       name: Name of the instance of the resource that is in use.
   """
   type: _typing.Optional[type] = None
   name: _typing.Optional[str] = None


class FilterInUse(ResourceInUse):
   """
   A FilterInUse fault indicates that some error has occurred because an
   IO filter was in use.
   
   Attributes:
       disk: Virtual disks that use the filter.
   """
   disk: list[pyVmomi.vim.vm.device.VirtualDiskId] = []


class FtIssuesOnHost(VmFaultToleranceIssue):
   """
   The FtIssuesOnHost fault reports issues that prevent a particular
   host from being used as the register or power on host for a Fault
   Tolerance secondary virtual machine
   
   Attributes:
       host: The host which has Fault Tolerance issues.
       hostName: Name for the host which has Fault Tolerance issues.
       errors: Information on the details of the Fault Tolerance issues
   """
   class HostSelectionType(pyVmomi.VmomiSupport.Enum):
      """
      HostSelectionType defines how the host was selected
      
      Attributes:
          user: The host was specified by the user
          vc: The host was selected by Virtual Center
          drs: The host was selected by DRS
      """
      user: _typing.ClassVar['FtIssuesOnHost.HostSelectionType'] = 'user'
      vc: _typing.ClassVar['FtIssuesOnHost.HostSelectionType'] = 'vc'
      drs: _typing.ClassVar['FtIssuesOnHost.HostSelectionType'] = 'drs'

   host: pyVmomi.vim.HostSystem
   hostName: str
   errors: list[pyVmomi.vmodl.MethodFault] = []

class FtVmHostRuleViolation(VmConfigFault):
   """
   The virtual machine if powered on or VMotioned, would violate an
   FT VM-Host rule.
   
   Attributes:
       vmName: The vm that can not be powered on or VMotioned without violating FT Metro
           Cluster placement rule.
       hostName: The host that the virtual machine can not be powered on without violating
           FT Metro Cluster placement rule.
       hostGroup: Indicate the Host Group for FT Metro Cluster enabled Virtual Machine.
   
   Since: vSphere API Release 8.0.3.0
   """
   vmName: str
   hostName: str
   hostGroup: str


class MigrationFeatureNotSupported(MigrationFault):
   """
   A migration operation that requires feature support on source and
   destination hosts is lacking support on the host.
   
   Attributes:
       atSourceHost: Whether this error is for the source host.
       failedHostName: The name of the host.
       failedHost: The host.
   """
   atSourceHost: bool
   failedHostName: str
   failedHost: pyVmomi.vim.HostSystem

class FullStorageVMotionNotSupported(MigrationFeatureNotSupported):
   """
   An operation on a powered-on virtual machine requests a simultaneous change
   of storage location and execution host, but the host does not have that
   capability.
   """
   pass


class GatewayConnectFault(HostConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayConnectFault is a base fault type for the faults thrown by a gateway
   server used to connect to a host.
   
   Attributes:
       gatewayType: The type of the gateway used for the connection to the host.
       gatewayId: Identifier of the gateway that is used for the connection to the host.
       gatewayInfo: Human-readable information about the host gateway server.
       details: Details of the cause for this fault.
           
           This is the way in which Host
           Gateway servers propagate opaque error messages through vCenter Server.
   """
   gatewayType: str
   gatewayId: str
   gatewayInfo: str
   details: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class GatewayToHostConnectFault(GatewayConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayToHostConnectFault is thrown by the gateway used to communicate
   with a host, if an error occurs in the communication between the gateway and
   the host.
   
   More details may be provided by a subfault.
   
   Attributes:
       hostname: Hostname of the host that the gateway is communicating with.
       port: Port specified for the connection between the gateway and the host.
   """
   hostname: str
   port: _typing.Optional[int] = None

class GatewayHostNotReachable(GatewayToHostConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayHostNotReachable is thrown by the gateway used to connect to a host,
   if an error occurs while establishing a connection to that host.
   
   The fault may provide a more detailed message of what caused the problem.
   """
   pass

class GatewayNotFound(GatewayConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayNotFound is thrown by vCenter Server, if no host gateway with the
   specified type/id and available resources is known to the vCenter Server.
   """
   pass

class GatewayNotReachable(GatewayConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayNotReachable is thrown by vCenter Server when it fails to establish
   a connection to the host gateway server.
   
   This fault may occur due to
   network connectivity problems or inability to establish secure connection
   between the gateway server and vCenter Server.
   """
   pass

class GatewayOperationRefused(GatewayConnectFault):
   """
   Deprecated: Not used sine vSphere 6.5GatewayOperationRefused is thrown by vCenter Server when a gateway server denies to
   accept more connection due to resource limitation.
   
   The fault may occur due
   to specific configuration of the Gateway server to work with limited
   resources or due to physical limitation to handle more host connections.
   """
   pass

class GatewayToHostAuthFault(GatewayToHostConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayToHostAuthFault is thrown by the gateway used to communicate with a
   host, if the gateway cannot authenticate to the host with the provided
   authentication data.
   
   The fault provides information, which of the properties given in the
   authentication data are invalid or if more properties are required.
   
   See Also: `pyVmomi.vim.host.GatewaySpec.hostAuthParams`
   
   Attributes:
       invalidProperties: List of properties that have been provided in the authentication data
           but have wrong values.
       missingProperties: List of properties that do not have their values specified in the
           provided authentication data but are required.
   """
   invalidProperties: list[str] = []
   missingProperties: list[str] = []


class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
   """
   Deprecated: Not used since vSphere 6.5GatewayToHostTrustVerifyFault is thrown by the gateway used to communicate
   with a host, if it cannot establish a trusted connection to the host with
   the provided host verification token parameter.
   
   The fault provides a list of opaque <key,value> properties, which the end
   user has to verify in order to trust the host and a verification token,
   which can be used to state that those exact properties are valid.
   
   See Also: `pyVmomi.vim.host.GatewaySpec.trustVerificationToken`
   
   Attributes:
       verificationToken: A unique verification token, that can be used to state the the listed
           properties are valid.
       propertiesToVerify: A key/value list of properties that need user verification in order
           for the gateway to trust the host to succeed.
           
           For instance the user may
           need to verify an SSL thumbprint or a whole certificate.
   """
   verificationToken: str
   propertiesToVerify: list[pyVmomi.vim.KeyValue] = []


class GenericDrsFault(VimFault):
   """
   DRS returns more than one faults for each virtual machine, or DRS returns
   `pyVmomi.vim.fault.VimFault` because of some internal errors.
   
   Attributes:
       hostFaults: This is an optional field to return the detailed information back to
           the client.
           
           This optional array may consist of the exact fault for
           some hosts in the cluster.
   """
   hostFaults: list[pyVmomi.vmodl.MethodFault] = []

class GenericVmConfigFault(VmConfigFault):
   """
   Thrown when a running virtual machine reports an error.
   
   Attributes:
       reason: Message from the virtual machine
   """
   reason: str

class GuestOperationsFault(VimFault):
   """The common base type for all guest operations faults."""
   pass


class GuestAuthenticationChallenge(GuestOperationsFault):
   """
   Fault is thrown when a call to `pyVmomi.vim.vm.guest.AuthManager.acquireCredentials` requires a challenge
   response in order to authenticate in the guest.
   
   The authToken string
   in serverChallenge contains a base64 encoded challenge token.
   
   Attributes:
       serverChallenge: Contains the server challenge information
       sessionID: Contains a session ID number that associates the server response
           with the initial request.
   """
   serverChallenge: pyVmomi.vim.vm.guest.GuestAuthentication
   sessionID: pyVmomi.VmomiSupport.long

class GuestComponentsOutOfDate(GuestOperationsFault):
   """
   A GuestComponentsOutOfDate exception is thrown when an
   operation fails because the guest operations agent is out of date and lacks
   the functionality to execute the operation.
   """
   pass

class GuestMultipleMappings(GuestOperationsFault):
   """
   A GuestMultipleMappings exception is thrown when an
   operation fails because the guest alias store mapping file
   contains multiple conflicting instances of the same certificate
   and username.
   """
   pass

class GuestOperationsUnavailable(GuestOperationsFault):
   """
   A GuestOperationsUnavailable exception is thrown when an
   operation fails to contact the guest operations agent
   running inside the virtual machine.
   """
   pass

class GuestPermissionDenied(GuestOperationsFault):
   """
   A GuestPermissionDenied exception is thrown when an
   operation fails because the authentication used
   is insufficient to perform the operation.
   """
   pass


class GuestProcessNotFound(GuestOperationsFault):
   """
   A GuestProcessNotFound exception is thrown when an
   operation fails because the guest process specified does not exist.
   
   Attributes:
       pid: The process ID that was not found.
   """
   pid: pyVmomi.VmomiSupport.long


class GuestRegistryFault(GuestOperationsFault):
   """
   A GuestRegistryFault exception is thrown when an operation fails
   because of some errors in accessing/modifying the guest registry.
   
   Attributes:
       windowsSystemErrorCode: The windows system error number from GetLastError().
   """
   windowsSystemErrorCode: pyVmomi.VmomiSupport.long

class GuestRegistryKeyFault(GuestRegistryFault):
   """
   A GuestRegistryKeyFault exception is thrown when an operation fails
   because of some errors in accessing/modifying a guest registry key.
   
   Attributes:
       keyName: The full path to the windows registry key.
   """
   keyName: str

class GuestRegistryKeyAlreadyExists(GuestRegistryKeyFault):
   """
   A GuestRegistryKeyAlreadyExists exception is thrown when an operation fails
   because the guest registry key specified already exists.
   """
   pass

class GuestRegistryKeyHasSubkeys(GuestRegistryKeyFault):
   """
   A GuestRegistryKeyHasSubkeys exception is thrown when an operation fails
   because the guest registry key has subkeys.
   
   If a delete on the key is
   desired, please use the recursive delete option.
   """
   pass

class GuestRegistryKeyInvalid(GuestRegistryKeyFault):
   """
   A GuestRegistryKeyInvalid exception is thrown when an operation fails
   because the guest registry key specified was not valid (most probably
   due to an invalid HKEY Root in the key path), or does not exist.
   """
   pass

class GuestRegistryKeyParentVolatile(GuestRegistryKeyFault):
   """
   A GuestRegistryKeyParentVolatile exception is thrown when trying to create
   a non-volatile registry subkey under a volatile registry parent key.
   """
   pass

class GuestRegistryValueFault(GuestRegistryFault):
   """
   A GuestRegistryValueFault exception is thrown when an operation fails
   because of some errors in accessing/modifying a guest registry value.
   
   Attributes:
       keyName: The full path to the windows registry key containing the value.
       valueName: The name of the value.
   """
   keyName: str
   valueName: str

class GuestRegistryValueNotFound(GuestRegistryValueFault):
   """
   A GuestRegistryValueNotFound exception is thrown when an operation fails
   because the guest registry Value specified was not found.
   """
   pass

class HAErrorsAtDest(MigrationFault):
   """
   The destination compute resource is HA-enabled, and HA is not running
   properly.
   
   This will cause the following problems:
   1\\) The VM will not have HA protection.
   2\\) If this is an intracluster VMotion, HA will not be properly
   informed that the migration completed. This can have serious
   consequences to the functioning of HA.
   """
   pass

class HeterogenousHostsBlockingEVC(EVCConfigFault):
   """
   An attempt to enable Enhanced VMotion Compatibility on a cluster has failed
   because the cluster contains CPUs from more than one vendor.
   """
   pass


class HostAccessRestrictedToManagementServer(pyVmomi.vmodl.fault.NotSupported):
   """
   Fault thrown when an attempt is made to adjust resource settings
   directly on a host that is being managed by VC.
   
   VC is currently the
   source of truth for all resource pools on the host.
   Examples of methods affected by this are:
   - create respool
   - update respool
   - change VM resource settings.
   
   Attributes:
       managementServer: Name/IP of the server currently managing this host.
   """
   managementServer: str


class HostConfigFailed(HostConfigFault):
   """
   Fault to indicate configuration of the host failed.
   
   Configuration could have failed because of multiple
   reasons and individual failures will be reported in
   \\#failure.
   """
   failure: list[pyVmomi.vmodl.MethodFault] = []


class HostHasComponentFailure(VimFault):
   """
   The host has a component failure and thus can cause issues for VMs running or
   to be running on it.
   
   Attributes:
       hostName: The host that has the component failure.
       componentType: The type of the component that has failed.
           
           Values come from `pyVmomi.vim.fault.HostHasComponentFailure.HostComponentType`.
       componentName: The name of the component that has failed.
   """
   class HostComponentType(pyVmomi.VmomiSupport.Enum):
      Datastore: _typing.ClassVar['HostHasComponentFailure.HostComponentType'] = 'Datastore'

   hostName: str
   componentType: str
   componentName: str

class HostInDomain(HostConfigFault):
   """
   Fault indicating that an operation cannot be performed while
   the host is part of a Windows domain.
   """
   pass


class HostIncompatibleForFaultTolerance(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to configure a fault tolerant
   virtual machine on a host that is incompatible.
   
   Attributes:
       reason: The specific reason why the host does not support fault tolerance.
           
           Values should come from `pyVmomi.vim.fault.HostIncompatibleForFaultTolerance.Reason`.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Reasons why fault tolerance is not supported on the host.
      
      Attributes:
          product: The product does not support fault tolerance.
          processor: The product supports fault tolerance but the host CPU does not.
      """
      product: _typing.ClassVar['HostIncompatibleForFaultTolerance.Reason'] = 'product'
      processor: _typing.ClassVar['HostIncompatibleForFaultTolerance.Reason'] = 'processor'

   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None


class HostIncompatibleForRecordReplay(VimFault):
   """
   Deprecated: as of vSphere API 6.0This fault is thrown when an attempt is made record or replay
   a virtual machine on a host that is incompatible.
   
   Attributes:
       reason: The specific reason why the host does not support record/replay.
           
           Values should come from `pyVmomi.vim.fault.HostIncompatibleForRecordReplay.Reason`.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Reasons why record/replay is not supported on a host.
      
      Attributes:
          product: The product does not support record/replay.
          processor: The product supports record/replay but the host CPU does not.
      """
      product: _typing.ClassVar['HostIncompatibleForRecordReplay.Reason'] = 'product'
      processor: _typing.ClassVar['HostIncompatibleForRecordReplay.Reason'] = 'processor'

   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None


class HostInventoryFull(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """A HostInventoryFull is thrown if the inventory has reach the max capacity of hosts."""
   capacity: int

class HostPowerOpFailed(VimFault):
   """This fault is thrown when a host power operation fails."""
   pass


class HostSpecificationOperationFailed(VimFault):
   """
   Fault thrown when an operation, on host specification or host sub
   specification for a host, failed.
   
   Attributes:
       host: The host on which host specification operation failed.
   """
   host: pyVmomi.vim.HostSystem

class SnapshotCopyNotSupported(MigrationFault):
   """
   An attempt is being made to move or copy a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported
   because of some aspect of the virtual machine configuration, virtual
   machine power state, or the requested disk placement.
   
   This is an error
   for move operations (where the source is deleted after the copy) and a
   warning for clones (where the source is preserved).
   """
   pass

class HotSnapshotMoveNotSupported(SnapshotCopyNotSupported):
   """
   An attempt is being made to move a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported by the
   host because the virtual machine is currently powered on.
   """
   pass

class HttpFault(VimFault):
   """
   Generic base class for outbound HTTP communication errors.
   
   Attributes:
       statusCode: HTTP status code received from external web-server.
       statusMessage: HTTP status message received from external web-server.
   """
   statusCode: int
   statusMessage: str

class IDEDiskNotSupported(DiskNotSupported):
   """
   Deprecated: As of VI API 2.5, use `pyVmomi.vim.fault.DeviceControllerNotSupported`.The virtual machine uses a virtual disk with an IDE controller, but this
   is not supported on the host.
   """
   pass


class IORMNotSupportedHostOnDatastore(VimFault):
   """
   A IORMNotSupportedHostOnDatastore fault occurs when the datastore is connected
   to one or more hosts that do not support storage I/O resource management.
   
   Attributes:
       datastore: The datastore.
       datastoreName: The name of the datastore.
       host: The list of hosts that do not support storage I/O
           resource management.
   """
   datastore: pyVmomi.vim.Datastore
   datastoreName: str
   host: list[pyVmomi.vim.HostSystem] = []

class ImportHostAddFailure(DvsFault):
   """
   Thrown if failure occurs while adding host to DVS during import operation
   
   Attributes:
       hostIp: Hosts on which import operation failed
   """
   hostIp: list[str] = []


class ImportOperationBulkFault(DvsFault):
   """
   Thrown if a Import operation fails
   
   Attributes:
       importFaults: Faults occurred during the import operation
   """
   class FaultOnImport(pyVmomi.vmodl.DynamicData):
      """
      The fault occurred on the entity during an import operation.
      
      Attributes:
          entityType: The entity type on which import failed.
              
              See `pyVmomi.vim.dvs.EntityBackup.EntityType`
              for valid values
          key: The key on which import failed
          fault: The fault that occurred.
      """
      entityType: _typing.Optional[str] = None
      key: _typing.Optional[str] = None
      fault: pyVmomi.vmodl.MethodFault

   importFaults: list[ImportOperationBulkFault.FaultOnImport] = []


class InUseFeatureManipulationDisallowed(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """A InUseFeatureManipulationDisallowed fault is thrown if an Vim.LicenseAssignmentManager.SetFeatureInUse or Vim.LicenseAssignmentManager.ResetFeatureInUse call can not complete because a feature is not available or the manipulation is not allowed."""
   pass


class InaccessibleDatastore(InvalidDatastore):
   """
   An InaccessibleDatastore exception is thrown if the datastore corresponding to the
   given datastore path isn't currently accessible.
   """
   detail: _typing.Optional[str] = None

class InaccessibleFTMetadataDatastore(InaccessibleDatastore):
   """
   An InaccessibleFTMetadataDatastore exception is thrown if the datastore
   corresponding to the specified FT Metadata Datastore path isn't currently
   accessible.
   """
   pass

class InaccessibleVFlashSource(VimFault):
   """
   An InaccessibleVFlashSource exception is thrown when
   an attempt is made to access the vFlash resource on
   the host, such as creating vFlash cache file for the
   virtual disk.
   
   Attributes:
       hostName: Name of the host which has the vFlash resource
   """
   hostName: str

class IncompatibleDefaultDevice(MigrationFault):
   """
   A default device (see `pyVmomi.vim.vm.ConfigOption.defaultDevice` for a
   definition) which the virtual machine is using is incompatible with
   the corresponding default device which will be created on the target host.
   
   This is an issue with powered-on or suspended migration under some
   circumstances. The problem is that in cases where the virtual machine
   must be recreated, it will have the default device created with default
   settings that are appropriate for the target host. If those are not
   compatible with the settings for that device that the virtual machine is currently
   using, then resuming the virtual machine on the target host might fail.
   
   This might happen if the device in question were reconfigured or the default
   is different between the source and the destination host. An example of
   a default device and associated setting which might cause this is
   `pyVmomi.vim.vm.device.VirtualVideoCard.videoRamSizeInKB`.
   This is an error.
   
   Attributes:
       device: The label of the device.
   """
   device: str


class IncompatibleHostForFtSecondary(VmFaultToleranceIssue):
   """
   The IncompatibleHostForFtSecondary fault is thrown when an invalid
   host has been specified when calling `pyVmomi.vim.VirtualMachine.createSecondary`
   or `pyVmomi.vim.VirtualMachine.enableSecondary`.
   
   Attributes:
       host: The host that is not compatible with the secondary virtual machine.
       error: Information on why the host that was specified could not be used for
           the FaultTolerance Secondary VirtualMachine.
   """
   host: pyVmomi.vim.HostSystem
   error: list[pyVmomi.vmodl.MethodFault] = []

class ReplicationFault(VimFault):
   """Base type for Replication-related errors."""
   pass


class IncompatibleHostForVmReplication(ReplicationFault):
   """
   A IncompatibleHostForVmReplication is thrown when a VM is powered
   on or migrated to a host which does not support the replication
   configuration of the VM.
   
   Attributes:
       vmName: The VM which has replication configured
       hostName: The host which is incompatible for VM replication
       reason: The reason why the host is incompatible
   """
   class IncompatibleReason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          rpo: Host does not support the RPO configured for VM replication.
          netCompression: Host does not support network compression configured for VM
              replication.
      """
      rpo: _typing.ClassVar['IncompatibleHostForVmReplication.IncompatibleReason'] = 'rpo'
      netCompression: _typing.ClassVar['IncompatibleHostForVmReplication.IncompatibleReason'] = 'netCompression'

   vmName: str
   hostName: str
   reason: str


class IncompatibleSetting(pyVmomi.vmodl.fault.InvalidArgument):
   """
   Thrown when two parameters in the customization settings conflict with each other.
   
   For example, a client may not specify both a Workgroup and a DomainName.
   
   Attributes:
       conflictingProperty: The name of the setting that is conflicting.
   """
   conflictingProperty: pyVmomi.VmomiSupport.PropertyPath

class IncorrectFileType(FileFault):
   """
   Thrown when an operation fails because the files do not match a
   specified file type.
   """
   pass


class IncorrectHostInformation(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A IncorrectHostInformation is thrown if the host does not provide the information
   needed to acquire the correct set of licenses.
   """
   pass

class IndependentDiskVMotionNotSupported(MigrationFeatureNotSupported):
   """
   An operation on a powered-on virtual machine requests that the virtual
   machine's disks be moved without choosing a new home datastore for the
   virtual machine, but the host does not have that capability.
   """
   pass

class InsufficientResourcesFault(VimFault):
   """
   Base fault that occurs when an operation conflicts with a resource configuration
   policy.
   
   For example, this fault occurs if a power-on operation reserves more memory
   than is allocated to a resource pool.
   """
   pass

class InsufficientAgentVmsDeployed(InsufficientResourcesFault):
   """
   This fault is returned when the required number of deployed agent virtual
   machines is not currently deployed on a host and hence the host cannot be
   used to run client virtual machines.
   
   Attributes:
       requiredNumAgentVms: The number of agent virtual machines required to be deployed on the host.
       currentNumAgentVms: The number of agent virtual machines currently deployed on the host.
   """
   hostName: str
   requiredNumAgentVms: int
   currentNumAgentVms: int


class InsufficientCpuResourcesFault(InsufficientResourcesFault):
   """
   CPU resources admission control failed
   
   Attributes:
       unreserved: The CPU available in the resource pool requested in MHz.
       requested: The CPU resource amount requested in the failed operation in MHz.
   """
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long

class InsufficientDisks(VsanDiskFault):
   """
   Fault used to denote an insufficient group of disks for a given operation.
   
   See Also: `pyVmomi.vim.host.VsanSystem.addDisks`, `pyVmomi.vim.host.VsanSystem.initializeDisks`
   """
   pass

class InsufficientFailoverResourcesFault(InsufficientResourcesFault):
   """
   This is thrown if an operation would violate the configured failover level of a HA
   cluster.
   
   In a HA cluster, virtual machines provide high availability by moving among physical
   machines in the event of a failure. HA Admission Control ensures that the total
   resource requirements for the set of virtual machines in a HA cluster does not exceed
   the resources that would be available in the worst-case scenario failure. If HA
   Admission Control is not used, physical machines may have insufficient resources to
   provide the expected level of service.
   
   This fault indicates that the virtual machine operation you attempted would have
   created a situation where the remaining physical machines would not meet the needs of
   the virtual machines in the event of a failure.
   """
   pass

class InsufficientGraphicsResourcesFault(InsufficientResourcesFault):
   """Graphics resources admission control failed"""
   pass


class InsufficientHostCapacityFault(InsufficientResourcesFault):
   """
   The host does not have enough capacity for running the virtual machine.
   
   Attributes:
       host: The host which does not have the enough capacity.
   """
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None


class InsufficientHostCpuCapacityFault(InsufficientHostCapacityFault):
   """
   The host does not have enough CPU capacity for running the virtual machine.
   
   Attributes:
       unreserved: The CPU available on the host in MHz.
       requested: The CPU resource amount requested in the failed operation in MHz.
   """
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientHostMemoryCapacityFault(InsufficientHostCapacityFault):
   """
   The host does not have enough memory capacity for running the virtual machine.
   
   Attributes:
       unreserved: The memory available on the host in bytes.
       requested: The memory resource amount requested in the failed operation in bytes.
   """
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientMemoryResourcesFault(InsufficientResourcesFault):
   """
   Memory resource admission control failed
   
   Attributes:
       unreserved: The memory available in the resource pool requested in bytes.
       requested: The memory resource amount requested in the failed operation in bytes.
   """
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long

class InsufficientNetworkCapacity(InsufficientResourcesFault):
   """The host does not have enough network capacity for running the virtual machine."""
   pass


class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
   """
   Insufficient network resource pool bandwidth
   
   Attributes:
       dvsName: Distributed Virtual Switch containing the resource pool
           having insufficient network bandwidth.
       dvsUuid: UUID of the distributed Virtual Switch containing the resource pool
           having insufficient network bandwidth.
       resourcePoolKey: Key of the resource pool on which network bandwidth is requested.
       available: Network bandwidth available (in MBs) in the requested resource pool.
       requested: Network bandwidth amount requested (in MBs).
       device: List of network devices that are requesting or already have requested
           bandwidth on the network resource pool.
   """
   dvsName: str
   dvsUuid: str
   resourcePoolKey: str
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long
   device: list[str] = []

class InsufficientPerCpuCapacity(InsufficientHostCapacityFault):
   """The host does not have enough per CPU capacity."""
   pass

class InsufficientStandbyResource(InsufficientResourcesFault):
   """
   This fault is thrown when Distributed Power Management cannot perform
   a given operation because there are insufficient CPU/memory resources
   on standby hosts (if any) to meet the requirements of the operation.
   """
   pass


class InsufficientStandbyCpuResource(InsufficientStandbyResource):
   """
   This fault is thrown when Distributed Power Management cannot perform
   a given operation because there is insufficient CPU resource
   on standby hosts (if any) to meet the requirements of the operation.
   
   Attributes:
       available: The total amount of CPU resource available (in MHz) on all the usable hosts
           in the cluster (including powered on and standby hosts).
       requested: The additional amount of CPU resource (other than that on the hosts included
           in \"available\") needed (in MHz).
   """
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientStandbyMemoryResource(InsufficientStandbyResource):
   """
   This fault is thrown by Distributed Power Management algorithm.
   
   It indicates
   that there are insufficient memory resources on standby hosts (if any)
   to meet the requirements of a given operation.
   
   Attributes:
       available: The total amount of memory resource available (in bytes) on all the usable hosts
           in the cluster (including powered on and standby hosts).
       requested: The additional amount of memory resource (other than that on the hosts included
           in \"available\") needed (in bytes).
   """
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientStorageIops(VimFault):
   """
   The datastore does not have enough IOPs capacity for running the virtual machine.
   
   Attributes:
       unreservedIops: The IOPs available on the datastore
       requestedIops: The IOPs resource amount requested in the failed operation
       datastoreName: Name of the datastore with insufficient capacity
   """
   unreservedIops: pyVmomi.VmomiSupport.long
   requestedIops: pyVmomi.VmomiSupport.long
   datastoreName: str

class InsufficientStorageSpace(InsufficientResourcesFault):
   """
   The fault occurs when Storage DRS cannot perform a given operation (e.g., fix the
   out of space condition, or place a virtual disk) because there is insufficient
   storage space in the given storage pod to meet the requirements of the operation.
   """
   pass


class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
   """
   Insufficient vFlash resource to consume
   
   Attributes:
       freeSpaceInMB: The vFlash resource available capacity in MB.
       freeSpace: The vFlash resource available capacity in bytes.
       requestedSpaceInMB: The vFlash resource amount requested in MB.
       requestedSpace: The vFlash resource amount requested in bytes.
   """
   freeSpaceInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   freeSpace: pyVmomi.VmomiSupport.long
   requestedSpaceInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   requestedSpace: pyVmomi.VmomiSupport.long

class InvalidAffinitySettingFault(VimFault):
   """
   An InvalidAffinitySettingsFault is thrown if an invalid affinity setting is
   specified for a virtual machine.
   """
   pass

class InvalidBmcRole(VimFault):
   """
   An InvalidBmcRole fault is thrown when a BMC user doesn't have the necessary
   privileges.
   
   BMC (Board Management Controller) is a piece of hardware required for
   IPMI.
   """
   pass

class PlatformConfigFault(HostConfigFault):
   """
   A PlatformConfigFault is a catch-all fault indicating that some error has
   occurred regarding the configuration of the host.
   
   Data about the fault is
   available and will be presented as a platform specific string.
   
   This information carried by this fault cannot be localized. Most likely
   this information will already have been localized to the locale of the
   server that generated this fault. Where possible, a more specific fault
   will be thrown.
   
   Attributes:
       text: Platform specific text string describing this error.
   """
   text: str

class InvalidBundle(PlatformConfigFault):
   """
   An Invalid Bundle fault is thrown if an operation fails because of a
   problem with the supplied bundle.
   """
   pass

class InvalidCAMCertificate(InvalidCAMServer):
   """
   Fault indicating that the CAM server's certificate
   cannot be verified.
   """
   pass

class InvalidLogin(VimFault):
   """
   Thrown when a server logon fails due to a bad user name or
   password.
   """
   pass

class InvalidClientCertificate(InvalidLogin):
   """
   This exception is thrown when a client has provided a
   certificate that fails certificate validation at the server.
   """
   pass

class InvalidController(InvalidDeviceSpec):
   """
   An InvalidController exception is thrown if
   a device refers to a controller that cannot be found.
   
   For example, an exception might be thrown if the client
   incorrectly passes a controller key,
   or if the client did not specify a controller where one is
   required (such as for disks or CD-ROMs).
   """
   controllerKey: int


class InvalidDasConfigArgument(pyVmomi.vmodl.fault.InvalidArgument):
   """
   This fault is thrown when an attempt is made to configure an HA cluster with
   invalid argument.
   
   Attributes:
       entry: The entry for the invalid argument
       clusterName: Name of the cluster to be configured
   """
   class EntryForInvalidArgument(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          admissionControl: Policies for admission control
          userHeartbeatDs: User-specified heartbeat datastores
          vmConfig: VM override
      """
      admissionControl: _typing.ClassVar['InvalidDasConfigArgument.EntryForInvalidArgument'] = 'admissionControl'
      userHeartbeatDs: _typing.ClassVar['InvalidDasConfigArgument.EntryForInvalidArgument'] = 'userHeartbeatDs'
      vmConfig: _typing.ClassVar['InvalidDasConfigArgument.EntryForInvalidArgument'] = 'vmConfig'

   entry: _typing.Optional[str] = None
   clusterName: _typing.Optional[str] = None


class InvalidDasRestartPriorityForFtVm(pyVmomi.vmodl.fault.InvalidArgument):
   """
   This fault is thrown when an attempt is made to set the DAS restart
   priority of a FT VM to disabled.
   
   Attributes:
       vm: The virtual machine
       vmName: The name of the virtual machine
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class InvalidDatastorePath(InvalidDatastore):
   """
   An InvalidDatastorePath exception is thrown if a datastore path violates
   the expected format.
   
   The expected format is \"[dsName] path\", e.g.
   \"[storage1] folder/Vm1.vmdk\". This exception is also thrown if a datastore
   corresponding to the given datastore path is not found.
   
   Attributes:
       datastorePath: The invalid datastore path name, if one was provided.
   """
   datastorePath: str


class InvalidDatastoreState(InvalidState):
   """
   The datastore is in an invalid state (e.g., maintenance mode)
   for a given operation.
   
   Attributes:
       datastoreName: The name of the datastore.
   """
   datastoreName: _typing.Optional[str] = None

class InvalidDeviceBacking(InvalidDeviceSpec):
   """
   An InvalidDeviceBacking exception is thrown if
   a device with an incompatible
   device backing is added or edited.
   """
   pass


class InvalidDeviceOperation(InvalidDeviceSpec):
   """
   An InvalidDeviceOperation exception is thrown if
   virtual machine creation or configuration fails because an invalid
   operation is attempted on the given device.
   
   Attributes:
       badOp: The invalid operation attempted.
       badFileOp: The invalid file operation attempted.
   """
   badOp: _typing.Optional[pyVmomi.vim.vm.device.VirtualDeviceSpec.Operation] = None
   badFileOp: _typing.Optional[pyVmomi.vim.vm.device.VirtualDeviceSpec.FileOperation] = None

class InvalidFormat(VmConfigFault):
   """
   Throws when an invalid format is detected.
   
   For example, when
   a virtual machine is registered and the system is unable to parse
   the files as a virtual machine.
   """
   pass

class InvalidDiskFormat(InvalidFormat):
   """The disk format is either corrupted or not supported."""
   pass


class InvalidDrsBehaviorForFtVm(pyVmomi.vmodl.fault.InvalidArgument):
   """
   This fault is thrown when an attempt is made to set the DRS behavior
   of an FT VM to an unsupported value.
   
   Currently, the only supported
   behavior is DRS Disabled.
   
   Attributes:
       vm: The virtual machine
       vmName: The name of the virtual machine
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class InvalidEditionLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   An ExpiredEditionLicense fault is thrown if an attempt to acquire an Edition license
   'feature failed for count 'count'.
   """
   feature: str

class InvalidEvent(VimFault):
   """
   A InvalidEvent fault is thrown when the event
   is malformed.
   """
   pass


class InvalidFolder(VimFault):
   """
   An InvalidFolderFault exception is thrown when a
   node is moved to an invalid place in the hierarchy.
   
   This can be because it is a child of the current node,
   or a wrong kind of container.
   
   Attributes:
       target: Reference to invalid target.
   """
   target: pyVmomi.vim.ManagedEntity

class InvalidGuestLogin(GuestOperationsFault):
   """
   An InvalidGuestLogin exception is thrown when an operation fails because
   authentication information used to authenticate with the guest was not
   accepted.
   """
   pass


class InvalidHostState(InvalidState):
   """
   The host has an invalid state.
   
   Attributes:
       host: The host that has an invalid state.
   """
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class InvalidHostConnectionState(InvalidHostState):
   """The host has an invalid connection state."""
   pass

class InvalidHostName(HostConfigFault):
   """The attempted operation requires that the host has a suitable FQDN."""
   pass


class InvalidIndexArgument(pyVmomi.vmodl.fault.InvalidArgument):
   """
   An InvalidIndexArgument exception is thrown if the
   index was not found
   
   Attributes:
       key: Value of index that was not found
   """
   key: str


class InvalidIpfixConfig(DvsFault):
   """
   Illegal value specified for a property of the switch's IpfixConfig.
   
   Attributes:
       property: Path of the property in IpfixConfig that has an invalid value.
   """
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None

class InvalidIpmiLoginInfo(VimFault):
   """
   A InvalidIpmiLoginInfo fault is thrown when the IPMI user name and/or password is
   invalid.
   """
   pass

class InvalidIpmiMacAddress(VimFault):
   """
   A InvalidIpmiMacAddress fault is thrown when the IPMI mac address provided by the
   user doesn't match with the observed mac address on the host.
   """
   userProvidedMacAddress: str
   observedMacAddress: str

class InvalidLicense(VimFault):
   """
   Thrown when
   an attempt is made to upload license content
   that is invalid.
   
   Attributes:
       licenseContent: The content of the license being reported as invalid.
   """
   licenseContent: str

class InvalidLocale(VimFault):
   """Thrown when a locale name is unknown or invalid."""
   pass


class InvalidName(VimFault):
   """
   A InvalidName fault is thrown when the name
   contains an invalid character or format.
   
   Attributes:
       name: The invalid name.
       entity: Entity, if any, that has an invalid name.
   """
   name: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None

class NasConfigFault(HostConfigFault):
   """
   Base class for all network-attached storage configuration faults.
   
   Attributes:
       name: Name of the Nas datastore being configured.
   """
   name: str

class InvalidNasCredentials(NasConfigFault):
   """
   This fault is thrown when an operation to configure a CIFS volume
   fails because the credentials specified in the
   `pyVmomi.vim.host.NasVolume.Specification` are incorrect.
   
   Attributes:
       userName: The username associated with the CIFS connection.
   """
   userName: str

class VAppPropertyFault(VmConfigFault):
   """
   The base fault for all vApp property configuration issues
   
   Attributes:
       id: The fully-qualified id of the property, including instance and class
           identifiers.
       category: The user-readable category
       label: The user-readable label
       type: The type specified for the property
       value: The value of the property
   """
   id: str
   category: str
   label: str
   type: str
   value: str

class InvalidNetworkInType(VAppPropertyFault):
   """The network specified in the property does not exists."""
   pass

class InvalidNetworkResource(NasConfigFault):
   """
   This fault is thrown when an operation to configure a NAS volume fails
   because the network resource specified is invalid.
   
   Attributes:
       remoteHost: The host that runs the CIFS or NFS server.
       remotePath: The remote share.
   """
   remoteHost: str
   remotePath: str

class InvalidOperationOnSecondaryVm(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to invoke an operation on
   a secondary virtual machine that is only supported on the primary virtual
   machine of the fault tolerant group.
   
   Attributes:
       instanceUuid: Instance UUID of the secondary virtual machine.
   """
   instanceUuid: str


class InvalidPowerState(InvalidState):
   """
   This exception is thrown if the
   power operation attempted could not be performed given
   the current power state of the virtual machine.
   
   Attributes:
       requestedState: Power state of the virtual machine required to
           allow the operation to succeed.
       existingState: Power state of the virtual machine that
           prevented the operation from succeeding.
   """
   requestedState: _typing.Optional[pyVmomi.vim.VirtualMachine.PowerState] = None
   existingState: pyVmomi.vim.VirtualMachine.PowerState

class InvalidPrivilege(VimFault):
   """
   A InvalidPrivilege fault is thrown when the privilege
   does not exist.
   
   Attributes:
       privilege: The invalid privilege.
   """
   privilege: str


class InvalidProfileReferenceHost(pyVmomi.vmodl.RuntimeFault):
   """
   A InvalidProfileReferenceHost fault is thrown when a valid host is not
   associated with a profile in the Virtual Center inventory.
   
   This could
   be because there is no host associated with the profile or because the
   associated host is incompatible with the profile.
   
   Attributes:
       reason: The reason for the invalid reference host if known.
       host: The incompatible host if associated with the profile.
       profile: The profile with the invalid or missing reference host.
       profileName: The profile name: the replacement of the member above.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          incompatibleVersion: The associated host and profile version are incompatible.
          missingReferenceHost: There is no reference host associated with the profile.
      """
      incompatibleVersion: _typing.ClassVar['InvalidProfileReferenceHost.Reason'] = 'incompatibleVersion'
      missingReferenceHost: _typing.ClassVar['InvalidProfileReferenceHost.Reason'] = 'missingReferenceHost'

   reason: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   profile: _typing.Optional[pyVmomi.vim.profile.Profile] = None
   profileName: _typing.Optional[str] = None

class InvalidPropertyType(VAppPropertyFault):
   """The type specification in the property in invalid."""
   pass

class InvalidPropertyValue(VAppPropertyFault):
   """The value of the property is not valid given the type of the property."""
   pass

class InvalidResourcePoolStructureFault(InsufficientResourcesFault):
   """
   This fault is thrown when an operation will cause the structure of a resource
   pool hierarchy to exceed its limit.
   
   The limits are typically imposed by the total
   number of nodes, maximum fan-out, and total depth of the hierarchy.
   """
   pass


class InvalidScheduledTask(pyVmomi.vmodl.RuntimeFault):
   """
   This exception is thrown when an unauthorized
   user runs a scheduled task.
   
   Since: vSphere API Release 8.0.2.0
   """
   pass

class InvalidSnapshotFormat(InvalidFormat):
   """
   Thrown when an invalid snapshot configuration is detected.
   
   For
   example, when a virtual machine's snapshot tree includes
   snapshots that are no longer present.
   """
   pass


class InvalidVmState(InvalidState):
   """
   The VM has an invalid state.
   
   Attributes:
       vm: The VM that has an invalid state.
   """
   vm: pyVmomi.vim.VirtualMachine


class InventoryHasStandardAloneHosts(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """A InventoryHasStandardAloneHosts fault is thrown if an assignment operation tries to downgrade a license that does have allow hosts licensed with StandardAlone license in the inventory."""
   hosts: list[str] = []

class IpHostnameGeneratorError(CustomizationFault):
   """An error occurred while running the IP/hostname generator application"""
   pass

class IscsiFault(VimFault):
   """Base class for faults that can be thrown while invoking iSCSI management operations."""
   pass

class IscsiFaultInvalidVnic(IscsiFault):
   """
   This fault indicates an attempt is made to bind a Virtual NIC to an iSCSI adapter
   where the Virtual NIC has no association with the adapter.
   
   For ex: The uplink for
   the given Virtual NIC is not valid for the iSCSI HBA.
   """
   vnicDevice: str

class IscsiFaultPnicInUse(IscsiFault):
   """This fault indicates the given Physical NIC is being used by iSCSI HBA."""
   pnicDevice: str

class IscsiFaultVnicAlreadyBound(IscsiFault):
   """This fault indicates that the given Virtual NIC is already bound to the iSCSI HBA."""
   vnicDevice: str

class IscsiFaultVnicHasActivePaths(IscsiFault):
   """This fault indicates the given Virtual NIC has active storage paths associated with it."""
   vnicDevice: str

class IscsiFaultVnicHasMultipleUplinks(IscsiFault):
   """
   This fault indicates that the Virtual NIC has multiple uplinks and not suitable for iSCSI
   multi-pathing and can not be bound to iSCSI HBA.
   """
   vnicDevice: str

class IscsiFaultVnicHasNoUplinks(IscsiFault):
   """
   This fault indicates the given Virtual NIC has no uplinks and not suitable for iSCSI
   multi-pathing configuration.
   """
   vnicDevice: str

class IscsiFaultVnicHasWrongUplink(IscsiFault):
   """
   This fault indicates the given Virtual NIC has the wrong Physical uplink
   for iSCSI multi-pathing configuration.
   
   The Physical uplink is not associated
   with the iSCSI Host Bus Adapter.
   
   Attributes:
       vnicDevice: Contains the VMkernel virtual NIC device name.
   """
   vnicDevice: str

class IscsiFaultVnicInUse(IscsiFault):
   """This fault indicates the given Virtual NIC is being used by iSCSI and the requested operation can't be completed."""
   vnicDevice: str

class IscsiFaultVnicIsLastPath(IscsiFault):
   """
   This fault indicates that the given Virtual NIC is associated with the only path to the storage.
   
   Any attempt to unbind this
   from iSCSI HBA would result in storage being inaccessible.
   """
   vnicDevice: str

class IscsiFaultVnicNotBound(IscsiFault):
   """
   This fault indicates an attempt was made to remove a Virtual NIC from an iSCSI HBA while
   Virtual NIC is not associated with the adapter.
   """
   vnicDevice: str

class IscsiFaultVnicNotFound(IscsiFault):
   """This fault indicates an attempt was made to add a non-existent Virtual NIC adapter."""
   vnicDevice: str

class KeyNotFound(VimFault):
   """
   An KeyNotFound fault is returned when the key does not exist among
   key value pairs.
   
   Attributes:
       key: The non existing key.
   """
   key: str

class LargeRDMConversionNotSupported(MigrationFault):
   """
   The virtual machine is using a 2TB+ RDM device and operation is
   unable to convert the disk to a different type.
   
   Attributes:
       device: The name of the disk device using the RDM.
   """
   device: str


class LargeRDMNotSupportedOnDatastore(VmConfigFault):
   """
   The virtual machine is configured with a 2TB+ Raw Disk Mapping.
   
   This is not
   supported on the datastore.
   
   Attributes:
       device: The label of the 2TB+ RDM device that would have its backing placed on
           the datastore.
           
           This is not guaranteed to be the only such device.
       datastore: The datastore.
       datastoreName: The name of the datastore.
   """
   device: str
   datastore: pyVmomi.vim.Datastore
   datastoreName: str

class LegacyNetworkInterfaceInUse(CannotAccessNetwork):
   """
   A virtual machine's network connectivity cannot be determined
   because it uses a legacy network interface.
   
   If returned as part of migration checks,
   this is an error if the virtual machine is currently connected to the legacy
   interface, and a warning otherwise.
   """
   pass


class LicenseAssignmentFailed(pyVmomi.vmodl.RuntimeFault):
   """
   A LicenseAssignmentFailed fault is thrown when VirtualCenter
   fails to assign a license to an entity.
   
   Attributes:
       reason: The reason why the assignment failed, if known.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          keyEntityMismatch: The license and the entity to which it is to be assigned are not compatible.
          downgradeDisallowed: The license downgrade is disallowed because some features are in use.
          inventoryNotManageableByVirtualCenter: The inventory has hosts which are not manageable by vCenter unless in evaluation.
          hostsUnmanageableByVirtualCenterWithoutLicenseServer: The inventory has hosts that need the license server to be configured unless vCenter is in evaluation
      """
      keyEntityMismatch: _typing.ClassVar['LicenseAssignmentFailed.Reason'] = 'keyEntityMismatch'
      downgradeDisallowed: _typing.ClassVar['LicenseAssignmentFailed.Reason'] = 'downgradeDisallowed'
      inventoryNotManageableByVirtualCenter: _typing.ClassVar['LicenseAssignmentFailed.Reason'] = 'inventoryNotManageableByVirtualCenter'
      hostsUnmanageableByVirtualCenterWithoutLicenseServer: _typing.ClassVar['LicenseAssignmentFailed.Reason'] = 'hostsUnmanageableByVirtualCenterWithoutLicenseServer'

   reason: _typing.Optional[str] = None


class LicenseDowngradeDisallowed(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A LicenseDowngradeDisallowed fault is thrown if an assignment operation tries to downgrade a license that does have certain licensed features which are in use.
   
   Attributes:
       features: List of conflicting features that prevent
           downgrade
   """
   edition: str
   entityId: str
   features: list[pyVmomi.vmodl.KeyAnyValue] = []

class LicenseEntityNotFound(VimFault):
   """
   An LicenseEntityNotFound fault is thrown when an attempt is
   do any operation on an entity/licensed asset that does not exist.
   
   Example, remove an entity that does not exist.
   """
   entityId: str


class LicenseExpired(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A LicenseExpired fault is thrown if it an operation is unsuccessful because the license used for the operation has expired.
   
   Attributes:
       licenseKey: License key that has expired
   """
   licenseKey: str


class LicenseKeyEntityMismatch(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A LicenseKeyEntityMismatch fault is thrown if an assignment operation tries to assign a license that does not apply to an entity.
   
   For example assigning a host license to VirtualCenter.
   """
   pass


class LicenseRestricted(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   This fault is thrown if the required licenses were unable to be checked
   out due to a restriction in the option file of the license server.
   """
   pass

class LicenseServerUnavailable(VimFault):
   """
   This fault is thrown when the License Server
   is unavailable during an attempt to change license state.
   
   Attributes:
       licenseServer: The name of the unavailable license server.
   """
   licenseServer: str


class LicenseSourceUnavailable(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A LicenseSourceUnavailable is thrown if it is unable to check out a license because
   the license source is unavailable.
   
   Attributes:
       licenseSource: License source
   """
   licenseSource: pyVmomi.vim.LicenseManager.LicenseSource


class LimitExceeded(VimFault):
   """
   This exception is thrown if one of the arguments passed to the function exceeds
   a limit.
   
   Attributes:
       property: The name of the property that exceeds the limit.
       limit: The limit value.
   """
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None
   limit: _typing.Optional[int] = None

class LinuxVolumeNotClean(CustomizationFault):
   """
   Customization operation is performed on a linux source vm that
   was not shut down properly.
   
   If the filesystem has significant
   fsck errors on it, customization process cannot make changes
   to it.
   """
   pass

class LogBundlingFailed(VimFault):
   """
   A LogBundlingFailed exception is thrown when generation of a diagnostic
   data bundle fails.
   """
   pass

class MaintenanceModeFileMove(MigrationFault):
   """
   Migration of the virtual machine to the target host will need a move of
   virtual machine files, like configuration file or virtual disks, which is
   not permitted if the source host is in maintenance mode.
   """
   pass


class UnsupportedDatastore(VmConfigFault):
   """
   The virtual machine is not supported on the target datastore.
   
   This fault is
   thrown by provisioning operations when an attempt is made to create a virtual
   machine on an unsupported datastore (for example, creating a non-legacy
   virtual machine on a legacy datastore).
   
   Attributes:
       datastore: The invalid datastore for this virtual machine.
   """
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class MemoryFileFormatNotSupportedByDatastore(UnsupportedDatastore):
   """
   Virtual memory file format is not supported on the datastore.
   
   Attributes:
       datastoreName: The name of the Datastore.
       type: Datastore file system volume type.
           
           See `pyVmomi.vim.Datastore.Summary.type`
   """
   datastoreName: str
   type: str

class MemoryHotPlugNotSupported(VmConfigFault):
   """Thrown when memory cannot be hot-added or hot-removed from the virtual machine."""
   pass

class MemorySizeNotRecommended(VirtualHardwareCompatibilityIssue):
   """
   The memory amount of the virtual machine is not within the recommended
   memory bounds for the virtual machine's guest OS.
   
   Attributes:
       memorySizeMB: The configured memory size of the virtual machine.
       minMemorySizeMB: The minimum recommended memory size.
       maxMemorySizeMB: The maximum recommended memory size.
   """
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int

class MemorySizeNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The memory amount of the virtual machine is not within the acceptable
   guest memory bounds supported by the virtual machine's host.
   
   Attributes:
       memorySizeMB: The configured memory size of the virtual machine.
       minMemorySizeMB: The minimum acceptable memory size.
       maxMemorySizeMB: The maximum acceptable memory size.
   """
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int


class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
   """
   The memory amount of the virtual machine is not within the acceptable
   guest memory bounds supported by the virtual machine's datastore.
   
   Attributes:
       datastore: The datastore which does not support the requested memory size.
       memorySizeMB: The configured memory size of the virtual machine.
       maxMemorySizeMB: The maximum acceptable memory size supported by the datastore.
   """
   datastore: pyVmomi.vim.Datastore
   memorySizeMB: int
   maxMemorySizeMB: int

class MemorySnapshotOnIndependentDisk(SnapshotFault):
   """
   Thrown if a request to take a memory snapshot is issued
   on a virtual machine with an independent disk.
   """
   pass


class MethodAlreadyDisabledFault(pyVmomi.vmodl.RuntimeFault):
   """
   A MethodAlreadyDisabledFault fault is thrown when an attempt
   is made to disable a method that is already disabled.
   """
   sourceId: str


class MethodDisabled(pyVmomi.vmodl.RuntimeFault):
   """
   A MethodDisabled fault is thrown if a disabled method
   is invoked by the client.
   
   The method denote an invalid state
   operation or may have been explicitly disabled.
   """
   source: _typing.Optional[str] = None

class MigrationDisabled(MigrationFault):
   """
   An MigrationDisabled fault is thrown if the
   migration failed due to disabled migration
   """
   pass

class MigrationNotReady(MigrationFault):
   """
   The VM to be migrated is not ready for the migration operation.
   
   This might
   because the VM is still in the progress of powering on or resuming from a
   suspended state.
   """
   reason: str

class MismatchedBundle(VimFault):
   """
   A MismatchedBundle fault is thrown when the bundle supplied for
   `pyVmomi.vim.host.FirmwareSystem.restoreConfiguration` does not match the
   specifications of the host
   
   Attributes:
       bundleUuid: The uuid of the host that the bundle was generated for
       hostUuid: The uuid of the host
       bundleBuildNumber: The build number of the host that the bundle was generated for
       hostBuildNumber: The build number of the host
   """
   bundleUuid: str
   hostUuid: str
   bundleBuildNumber: int
   hostBuildNumber: int

class MismatchedNetworkPolicies(MigrationFault):
   """
   Deprecated: As of vSphere API 5.5, use `pyVmomi.vim.fault.CannotUseNetwork` with
   a correct reason for the fault.The virtual machine network uses different offload or security
   policies on the destination host than on the source host.
   
   This is an error
   if the virtual machine is currently connected to the network, and a warning
   otherwise.
   
   Attributes:
       device: The label of the interface device.
       backing: The name of the network.
       connected: The connected/disconnected state of the device.
   """
   device: str
   backing: str
   connected: bool

class MismatchedVMotionNetworkNames(MigrationFault):
   """
   The source and destination hosts do not use the same network name for
   their VMotion interfaces.
   
   This is a warning for migrating powered-on virtual
   machines.
   
   Attributes:
       sourceNetwork: The name of the network used by the source host VMotion interface.
       destNetwork: The name of the network used by the destination host VMotion interface.
   """
   sourceNetwork: str
   destNetwork: str

class MissingBmcSupport(VimFault):
   """
   A MissingBmcSupport fault is thrown when a host's BMC doesn't support IPMI.
   
   BMC (Board Management Controller) is a piece of hardware required for IPMI.
   """
   pass

class MissingController(InvalidDeviceSpec):
   """
   A controller key has not been specified for a new device
   that requires a controller, such as a disk or CD-ROM device.
   """
   pass

class MissingIpPool(VAppPropertyFault):
   """No IP pool is associated with a network."""
   pass

class MissingLinuxCustResources(CustomizationFault):
   """
   Usable open source components required for Linux customization were not found
   on the server.
   """
   pass

class MissingNetworkIpConfig(VAppPropertyFault):
   """No IP configuration exists for network."""
   pass

class VAppConfigFault(VimFault):
   """
   Base for configuration / environment issues that can be thrown when powering on or
   changing the configuration of a vApp.
   """
   pass

class MissingPowerOffConfiguration(VAppConfigFault):
   """
   Attempting to power-off a vApp for which no virtual machines has been
   configured to power off.
   """
   pass

class MissingPowerOnConfiguration(VAppConfigFault):
   """
   Attempting to power-on a vApp service for which no virtual machines has been
   configured to power on.
   """
   pass

class MissingWindowsCustResources(CustomizationFault):
   """A usable sysprep file was not found on the server."""
   pass

class MksConnectionLimitReached(InvalidState):
   """
   Thrown when a mouse-keyboard-screen connection ticket to a virtual machine
   cannot be granted because the configured connection limit has been reached.
   
   Attributes:
       connectionLimit: MKS connection limit for the virtual machine.
   """
   connectionLimit: int


class MountError(CustomizationFault):
   """
   Customization failed because the customization process was unable to mount a remote
   virtual disk file.
   
   Attributes:
       vm: The virtual machine to be customized.
       diskIndex: Index into the virtual machine's device list,
           representing the key value that identifies the virtual device
           that is the presumed boot disk.
   """
   vm: pyVmomi.vim.VirtualMachine
   diskIndex: int

class MultiWriterNotSupported(DeviceNotSupported):
   """
   The multi-writer sharing of the specified virtual disk is not supported.
   
   Typically, this fault is returned as part of a parent fault like
   `pyVmomi.vim.fault.VmConfigIncompatibleForFaultTolerance`, indicating that the
   virtual disk's multi-writer sharing needs to be changed before fault
   tolerance can be enabled on the associated virtual machine.
   """
   pass


class MultipleCertificatesVerifyFault(HostConnectFault):
   """
   MultipleCertificatesVerifyFault is thrown by the host connect method
   `pyVmomi.vim.HostSystem.reconnect` as well as the methods to add a host to
   VirtualCenter (`pyVmomi.vim.Folder.addStandaloneHost` and
   `pyVmomi.vim.ClusterComputeResource.addHost`) if VirtualCenter detects that the
   host has different SSL certificates for different management ports.
   
   This
   can occur, for example, if an ESX 2.x host has different SSL certificates
   for the authd service (port 902) and the Management UI port (port 443).
   VirtualCenter is not able to manage such hosts. To fix this issue, the user
   should modify the host to ensure there is only one certificate for
   all services. Alternatively, different certificates are allowed as long as each
   certificate is verifiable (trusted) by the VirtualCenter server.
   
   Attributes:
       thumbprintData: The thumbprints (and associated ports) used by the services on the host.
   """
   class ThumbprintData(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          port: The port used by the service.
          thumbprint: The SSL thumbprint of the host's certificate used by the service.
      """
      port: int
      thumbprint: str

   thumbprintData: list[MultipleCertificatesVerifyFault.ThumbprintData] = []

class MultipleSnapshotsNotSupported(SnapshotFault):
   """
   Fault thrown when an attempt is made to create a second snapshot on a VM that only
   supports a single snapshot at a time.
   """
   pass


class NamespaceFull(VimFault):
   """
   A NamespaceFull fault is thrown when an operation
   on namespace requires more space to complete.
   
   Attributes:
       name: The namespace in question.
       currentMaxSize: Current maximum size.
       requiredSize: Size necessary to complete operation.
           
           If not present,
           system was not able to determine how much space would
           be necessary to complete operation.
   """
   name: str
   currentMaxSize: pyVmomi.VmomiSupport.long
   requiredSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class NamespaceLimitReached(VimFault):
   """
   A NamespaceLimitReached fault is thrown when the maximum allowed
   namespaces for a virtual machine will be exceeded.
   
   Attributes:
       limit: Allowed maximum number of namespaces per virtual machine.
   """
   limit: _typing.Optional[int] = None

class NamespaceWriteProtected(VimFault):
   """
   A NamespaceWriteProtected fault is thrown when an operation
   on namespace fails because namespace is write-protected.
   
   Attributes:
       name: The namespace in question.
   """
   name: str

class NasConnectionLimitReached(NasConfigFault):
   """
   This fault is thrown when an operation to configure a CIFS volume fails
   because the request exceeds the maximum allowed connections on this host
   for the specified remote path.
   
   Attributes:
       remoteHost: The host that runs the NFS server.
       remotePath: The remote share.
   """
   remoteHost: str
   remotePath: str

class NasSessionCredentialConflict(NasConfigFault):
   """
   This fault is thrown when an operation to configure a CIFS volume fails
   when attempting to log on more than once with the same user name.
   
   Attributes:
       remoteHost: The host that runs the NFS server.
       remotePath: The remote share.
   """
   remoteHost: str
   remotePath: str
   userName: str

class NasVolumeNotMounted(NasConfigFault):
   """
   This fault is thrown when an operation to configure a NAS datastore
   fails because the specified NFS volume is not mounted.
   
   Attributes:
       remoteHost: The host that runs the NFS server.
       remotePath: The remote share.
   """
   remoteHost: str
   remotePath: str

class NetworkCopyFault(FileFault):
   """A network copy of the file failed."""
   pass

class NetworkDisruptedAndConfigRolledBack(VimFault):
   """
   Thrown if network configuration change disconnected the host from vCenter server
   and has been rolled back.
   
   Attributes:
       host: The name of host on which the network configuration was rolled back.
   """
   host: str

class NetworkInaccessible(NasConfigFault):
   """
   This fault is thrown when an operation to configure a NAS volume fails
   because network access is unavailable.
   """
   pass


class NetworksMayNotBeTheSame(MigrationFault):
   """
   Used as a warning if a virtual machine provisioning operation is done
   across datacenters.
   
   This warns that the network used by the virtual
   machine before and after the operation may not be the same even though
   the two networks have the same name. This is because network names
   are only unique within a datacenter.
   
   Attributes:
       name: The name of the network.
   """
   name: _typing.Optional[str] = None

class NicSettingMismatch(CustomizationFault):
   """
   The number of network adapter settings in the customization specification
   does not match the number of network adapters present in the virtual machine.
   
   Attributes:
       numberOfNicsInSpec: The number of network adapter settings specified in the customization
           specification.
       numberOfNicsInVM: The number of network adapters present in the virtual machine.
   """
   numberOfNicsInSpec: int
   numberOfNicsInVM: int


class NoActiveHostInCluster(InvalidState):
   """
   A NoActiveHostInCluster fault is thrown when there is no host in a valid
   state in the given compute resource to perform a specified operation.
   
   This
   can happen, for example, if all the hosts are disconnected or in maintenance
   mode.
   
   Attributes:
       computeResource: The compute resource that does not have any active hosts.
   """
   computeResource: pyVmomi.vim.ComputeResource


class NoAvailableIp(VAppPropertyFault):
   """
   There are no more IP addresses available on the given network.
   
   Attributes:
       network: A reference to the network
   """
   network: pyVmomi.vim.Network

class NoClientCertificate(VimFault):
   """
   This exception is thrown when a client has connected without supplying a
   certificate but the associated call expects that the client has done so.
   """
   pass

class NoCompatibleDatastore(VimFault):
   """
   A NoCompatibleDatastore fault is thrown when Storage DRS cannot find a compatible
   datastore in a given storage pod to place a disk or a virtual machine.
   
   a virtual machine.
   """
   pass

class NoCompatibleHardAffinityHost(VmConfigFault):
   """
   The cluster contains no hosts satisfying the hard VM/host affinity rules
   constraint for the VM.
   
   Attributes:
       vmName: The vm for which there are no compatible hard-affine hosts in the cluster.
   """
   vmName: str


class NoCompatibleHost(VimFault):
   """
   A NoCompatibleHost fault is thrown when DRS cannot find a compatible
   host in a given compute resource to run a virtual machine on.
   
   Attributes:
       host: The list of hosts that are not compatible, each element has a
           corresponding fault in the error array.
       error: An error in this array indicates why the corresponding host in the
           host array is incompatible.
   """
   host: list[pyVmomi.vim.HostSystem] = []
   error: list[pyVmomi.vmodl.MethodFault] = []

class NoCompatibleHostWithAccessToDevice(NoCompatibleHost):
   """
   This fault is used to report that a FT VM cannot be placed because there is
   no compatible host that can access all devices required to be connected when
   the VM powers on.
   """
   pass

class NoCompatibleSoftAffinityHost(VmConfigFault):
   """
   The cluster contains no hosts satisfying the soft VM/host affinity rules
   constraint for the VM.
   
   Attributes:
       vmName: The vm for which there are no compatible soft-affine hosts in the cluster.
   """
   vmName: str

class NoConnectedDatastore(VimFault):
   """
   The fault occurs when Storage DRS cannot move a virtual machine because
   the host it is registered on is not connected to any other datastore
   in the storage pod.
   """
   pass

class NoDiskFound(VimFault):
   """
   This exception is thrown when a virtual machine
   which has no virtual disks is being upgraded or relaid out
   using the VirtualMachine.upgradeVirtualHardware or upgradeVmLayout
   commands.
   """
   pass

class NoDiskSpace(FileFault):
   """
   This fault is thrown when an operation fails because of insufficient
   disk space.
   
   Attributes:
       datastore: The name of the datastore with insufficient disk space.
   """
   datastore: str

class NoDisksToCustomize(CustomizationFault):
   """None of the disks attached to the VM are suitable for customization."""
   pass

class NoGateway(HostConfigFault):
   """
   This error occurs when an operation fails because of vmkernel gateway
   is unset.
   """
   pass

class NoGuestHeartbeat(MigrationFault):
   """
   A powered-on virtual machine has a guest OS with Tools installed, but it does not
   have a valid heartbeat.
   """
   pass


class NoHost(HostConnectFault):
   """
   A NoHostFault fault occurs when a host
   cannot be reached.
   """
   name: _typing.Optional[str] = None


class NoHostSuitableForFtSecondary(VmFaultToleranceIssue):
   """
   The NoHostSuitableForFtSecondary fault is thrown when the system is unable to
   find a suitable host for the Fault Tolerance secondary virtual machine.
   
   This fault can be thrown when Virtual Center is trying to place or power on
   a Fault Tolerance Secondary, in both DRS or non-DRS cases.
   
   Attributes:
       vm: The primary virtual machine corresponding to the secondary virtual
           machine.
       vmName: The name of the primary virtual machine corresponding to the secondary
           virtual machine.
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class NoLicenseServerConfigured(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   The NoLicenseServerConfigured fault is thrown when there is no
   valid license server configured for the system and the system
   is not in evaluation mode.
   
   Any operation occurs that requires
   evaluation license or a valid license will throw the
   NoLicenseServerConfigured. This can happen with the new licensing
   scheme that is a hybrid of flex-based licensing and serial number
   based licensing. There can be cases where VirtualCenter is licensed
   by a serial number and there is no need for a flex license server.
   These cases are valid as long as no operation that requires flex-
   based license server is invoked, for example, adding a pre-4.0
   host that requires flex licenses. If however, such an operation is
   invoked, the NoLicenseServerConfigured fault is thrown.
   """
   pass

class NoPeerHostFound(HostPowerOpFailed):
   """This fault is thrown when no peer host is found to wake up this host."""
   pass


class NoPermission(pyVmomi.vmodl.fault.SecurityError):
   """
   Thrown when an operation is denied because of privileges
   not held on managed object(s).
   
   Attributes:
       object: The managed object on which a permission is required.
       privilegeId: The privilege identifier required
       missingPrivileges: List of entities and missing privileges for each entity
           
           Since: vSphere API Release 7.0.3.2
   """
   class EntityPrivileges(pyVmomi.vmodl.DynamicData):
      """
      Entity and privileges for the entity
      
      Since: vSphere API Release 7.0.3.2
      """
      entity: pyVmomi.VmomiSupport.ManagedObject
      privilegeIds: list[str] = []

   object: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   privilegeId: _typing.Optional[str] = None
   missingPrivileges: list[NoPermission.EntityPrivileges] = []

class NoPermissionOnAD(ActiveDirectoryFault):
   """
   Fault indicating that the user account used to connect to the
   Active Directory doesn not have enough permissions for the action
   that was attempted.
   """
   pass

class NoPermissionOnHost(HostConnectFault):
   """
   This indicates that the user account used to connect to the host does
   not have enough permissions to enable VirtualCenter to manage the host.
   """
   pass


class NoPermissionOnNasVolume(NasConfigFault):
   """
   This fault is thrown when an operation to configure a NAS volume fails
   because of insufficient user permissions.
   
   For CIFS volumes, this implies that the user specified in the
   `pyVmomi.vim.host.NasVolume.Specification` does not have access to the
   network resource.
   """
   userName: _typing.Optional[str] = None

class NoSubjectName(VimFault):
   """
   This exception is thrown when an extension has attempted to use certificate-based
   authentication but the extension has been registered without a subject name.
   """
   pass

class NoVcManagedIpConfigured(VAppPropertyFault):
   """
   The IP address of the VC server has not be configured, and a vApp
   property is requesting to use it.
   """
   pass

class NoVirtualNic(HostConfigFault):
   """
   This error occurs when an operation fails because of
   no virtual NIC available.
   """
   pass

class NoVmInVApp(VAppConfigFault):
   """
   Attempting to power-on or power-off a vApp that contains no
   virtual machines.
   """
   pass

class NonADUserRequired(ActiveDirectoryFault):
   """
   Fault indicating that an operation must be executed by a
   non Active Directory user.
   """
   pass

class NonHomeRDMVMotionNotSupported(MigrationFeatureNotSupported):
   """
   An operation on a powered-on virtual machine requests that an existing
   Raw Disk Mapping end up in a location other than the new home datastore
   for the virtual machine, but the host does not have that capability.
   
   Attributes:
       device: The label of an RDM device for which an unsupported move was requested.
           
           This is not guaranteed to be the only such device.
   """
   device: str

class NonPersistentDisksNotSupported(DeviceNotSupported):
   """
   The virtual machine has nonpersistent virtual disk.
   
   This is an error for
   any powered-on migration which involves moving virtual disks.
   """
   pass

class NonVmwareOuiMacNotSupportedHost(NotSupportedHost):
   """
   The host does not support VM that has VPX assigned prefix or ranged based
   MAC address (i.e.
   
   MAC is not prefixed with 00:50:56:[80-BF])
   
   Attributes:
       hostName: The name of the host.
   """
   hostName: str

class NotADirectory(FileFault):
   """
   This fault is thrown when an operation fails because the specified object
   is not a directory.
   """
   pass

class NotAFile(FileFault):
   """
   This fault is thrown when an operation fails because the specified object
   is not a file.
   """
   pass

class NotAuthenticated(NoPermission):
   """
   Thrown when an operation is denied because the session
   has not yet successfully logged in.
   """
   pass

class NotEnoughCpus(VirtualHardwareCompatibilityIssue):
   """
   The host hardware does not have enough CPU cores to support the number of
   virtual CPUs in the virtual machine.
   
   If the host is using hyperthreading, NotEnoughLogicalCpus is
   employed instead of NotEnoughCpus.
   
   Attributes:
       numCpuDest: The number of CPUs present on the host.
       numCpuVm: The number of virtual CPUs present in the virtual machine.
   """
   numCpuDest: int
   numCpuVm: int


class NotEnoughLogicalCpus(NotEnoughCpus):
   """
   The host hardware does not have enough logical CPUs (hyperthreads) to
   support the number of virtual CPUs in the virtual machine.
   
   Attributes:
       host: The host that does not have enough logical CPUs.
   """
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class NotFound(VimFault):
   """
   A NotFound error occurs when a referenced component of a managed
   object cannot be found.
   
   The referenced component can be a data
   object type (such as a role or permission) or a primitive
   (such as a string).
   
   For example, if the missing referenced component is a data object, such as
   VirtualSwitch, the NotFound error is
   thrown. The NotFound error is also thrown if the data object is found, but the referenced name
   (for example, \"vswitch0\") is not.
   """
   pass


class NotSupportedDeviceForFT(VmFaultToleranceIssue):
   """
   Deprecated: as of vSphere API 7.0. Not used since vSphere API 6.5.VMs with pvscsi or vmxnet3 virtual devices support Fault Tolerance only
   on 4.1 or later hosts.
   
   Attributes:
       host: The host
       hostName: The host name
       vm: The virtual machine
       vmName: The virtual machine name
       deviceType: The device type
       deviceLabel: The device label
   """
   class DeviceType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          virtualVmxnet3: vmxnet3 virtual Ethernet adapter
          paraVirtualSCSIController: paravirtualized SCSI controller
      """
      virtualVmxnet3: _typing.ClassVar['NotSupportedDeviceForFT.DeviceType'] = 'virtualVmxnet3'
      paraVirtualSCSIController: _typing.ClassVar['NotSupportedDeviceForFT.DeviceType'] = 'paraVirtualSCSIController'

   host: pyVmomi.vim.HostSystem
   hostName: _typing.Optional[str] = None
   vm: pyVmomi.vim.VirtualMachine
   vmName: _typing.Optional[str] = None
   deviceType: str
   deviceLabel: _typing.Optional[str] = None

class NotSupportedHostForChecksum(VimFault):
   """Base class for host checksum related faults"""
   pass

class NotSupportedHostForVFlash(NotSupportedHost):
   """
   The host does not support vFlash feature.
   
   Attributes:
       hostName: The name of the host.
   """
   hostName: str

class NotSupportedHostForVmcp(NotSupportedHost):
   """
   The host does not support VM Component Protection.
   
   Attributes:
       hostName: The name of the host.
   """
   hostName: str

class NotSupportedHostForVmemFile(NotSupportedHost):
   """
   The host does not support VM Component Protection.
   
   Attributes:
       hostName: The name of the host.
   """
   hostName: str

class NotSupportedHostForVsan(NotSupportedHost):
   """
   The host does not support VSAN.
   
   Attributes:
       hostName: The name of the host.
   """
   hostName: str


class NotSupportedHostInDvs(NotSupportedHost):
   """
   A NotSupportedHostInDvs fault occurs when the host does not support
   the necessary features to participate in the DVS.
   
   Attributes:
       switchProductSpec: The product spec of the DVS.
           
           This determines which host versions may
           participate in the DVS; that information may be queried by using
           `pyVmomi.vim.dvs.DistributedVirtualSwitchManager.queryCompatibleHostSpec`.
   """
   switchProductSpec: pyVmomi.vim.dvs.ProductSpec

class NotSupportedHostInHACluster(NotSupportedHost):
   """
   A NotSupportedHostInHACluster fault occurs when the host does not support
   the necessary features to participate in the HA cluster.
   
   Attributes:
       hostName: The name of the host.
       build: The product build number of the host.
   """
   hostName: str
   build: str

class NotUserConfigurableProperty(VAppPropertyFault):
   """
   The property value cannot be changed since it is not
   user configurable.
   """
   pass

class NumVirtualCoresPerSocketNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The host's software does not support enough cores per socket to
   accommodate the virtual machine.
   
   This is always an error.
   
   Attributes:
       maxSupportedCoresPerSocketDest: The maximum number of cores per socket supported on the host.
       numCoresPerSocketVm: The number of cores per socket in the virtual machine.
   """
   maxSupportedCoresPerSocketDest: int
   numCoresPerSocketVm: int

class NumVirtualCpusExceedsLimit(InsufficientResourcesFault):
   """
   This fault is thrown when the total number of virtual CPUs present or requested
   in virtual machines' configuration has exceeded the limit on the host.
   
   Attributes:
       maxSupportedVcpus: The maximum number of virtual CPUs supported on the host.
   """
   maxSupportedVcpus: int


class NumVirtualCpusIncompatible(VmConfigFault):
   """
   The number of virtual CPUs present or requested in the virtual machine's
   configuration is not supported for a specific feature.
   
   Attributes:
       reason: The reason for the incompatibility.
           
           See `pyVmomi.vim.fault.NumVirtualCpusIncompatible.Reason` for valid values.
       numCpu: The number of virtual CPUs in the virtual machine.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Reasons why the number of virtual CPUs is incompatible.
      
      Attributes:
          recordReplay: The virtual machine needs to support record/replay functionality.
          faultTolerance: The virtual machine is enabled for fault tolerance.
      """
      recordReplay: _typing.ClassVar['NumVirtualCpusIncompatible.Reason'] = 'recordReplay'
      faultTolerance: _typing.ClassVar['NumVirtualCpusIncompatible.Reason'] = 'faultTolerance'

   reason: str
   numCpu: int

class NumVirtualCpusNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The host's software does not support enough virtual CPUs to
   accommodate the virtual machine.
   
   This is always an error.
   
   Attributes:
       maxSupportedVcpusDest: The maximum number of virtual CPUs supported on the host.
       numCpuVm: The number of virtual CPUs in the virtual machine.
   """
   maxSupportedVcpusDest: int
   numCpuVm: int

class OperationDisabledByGuest(GuestOperationsFault):
   """
   An OperationDisabledByGuest exception is thrown when an
   operation fails because the guest operations agent has been configured to
   disable the operation.
   """
   pass


class OperationDisallowedOnHost(pyVmomi.vmodl.RuntimeFault):
   """
   An OperationDisallowedOnHost is thrown if an operation is diasllowed
   on host when a direct connection is used.
   
   Examples for such operations include VM powering on / memory hot-plug
   which could potentially violate hard-enforcement licenses if allowed
   on host.
   The functionality these operations provide is still available, but only
   through calls to an external entity.
   """
   pass

class OperationNotSupportedByGuest(GuestOperationsFault):
   """
   An OperationNotSupportedByGuest exception is thrown when an
   operation fails because the guest OS does not support
   the operation (e.g., Registry manipulation in Linux guests.).
   """
   pass


class OutOfBounds(VimFault):
   """
   Thrown if a parameter exceeds the acceptable range of values.
   
   Attributes:
       argumentName: This should be the name of the field that holds the allowed maximum
           (for example, Host.capability.maxSupportedVMs).
   """
   argumentName: pyVmomi.VmomiSupport.PropertyPath

class OvfInvalidPackage(OvfFault):
   """
   Base fault class for all Invalid OVF package faults.
   
   Attributes:
       lineNumber: XML OVF descriptor line numbers
   """
   lineNumber: int

class OvfAttribute(OvfInvalidPackage):
   """
   An OVF descriptor Attribute base class.
   
   Attributes:
       elementName: Element name where the attribute is defined
       attributeName: Attribute name
   """
   elementName: str
   attributeName: str


class OvfHardwareExport(OvfExport):
   """
   A common base class to host all the OvfLib Export Exceptions for hardware.
   
   Attributes:
       device: The virtual device we are exporting to OVF
       vmPath: The path to the VM containing the device.
           
           This path shows the location of the VM in the vApp hierarchy, on the form:
           
           /ParentVApp/ChildVApp/VMName
   """
   device: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice] = None
   vmPath: str

class OvfConnectedDevice(OvfHardwareExport):
   pass

class OvfConnectedDeviceFloppy(OvfConnectedDevice):
   """
   Attributes:
       filename: The filename of the floppy image
   """
   filename: str

class OvfConnectedDeviceIso(OvfConnectedDevice):
   """
   Attributes:
       filename: The filename of the ISO
   """
   filename: str

class OvfConstraint(OvfInvalidPackage):
   """
   A base fault for Ovf descriptor constraints
   
   Attributes:
       name: The name of the element
   """
   name: str

class OvfConsumerCallbackFault(OvfFault):
   """
   Superclass for all faults that can be thrown during the callback to an OVF
   consumer.
   
   The `pyVmomi.vmodl.MethodFault.faultCause` gives details about what went
   wrong.
   
   Attributes:
       extensionKey: The OVF consumer's extension key.
       extensionName: The OVF consumer's extension name.
   """
   extensionKey: str
   extensionName: str

class OvfConsumerCommunicationError(OvfConsumerCallbackFault):
   """
   A fault type indicating that network communication with an OVF consumer failed.
   
   Attributes:
       description: The network library error message.
   """
   description: str


class OvfConsumerFault(OvfConsumerCallbackFault):
   """
   Localized fault that may be thrown by an OVF consumer.
   
   Attributes:
       errorKey: An error code that uniquely describes the fault within this extension.
       message: The error message, localized by the OVF consumer
       params: Additional parameters for this fault
   """
   errorKey: str
   message: str
   params: list[pyVmomi.vim.KeyValue] = []

class OvfConsumerInvalidSection(OvfConsumerCallbackFault):
   """
   A fault type indicating that the XML of a section appended by an OVF consumer was
   invalid.
   
   Attributes:
       lineNumber: The line number in the section on which the error was found.
       description: The XML parser error message.
   """
   lineNumber: int
   description: str

class OvfConsumerPowerOnFault(InvalidState):
   """
   A fault type indicating that the power on operation failed.
   
   Attributes:
       extensionKey: The OVF consumer's extension key.
       extensionName: The OVF consumer's extension name.
       description: A localized, human-readable description of the error.
   """
   extensionKey: str
   extensionName: str
   description: str

class OvfConsumerUndeclaredSection(OvfConsumerCallbackFault):
   """
   A fault type indicating that an OVF consumer appended an undeclared section to an OST.
   
   An undeclared section means a section with a qualified type that the OVF consumer was
   not registered as a handler of.
   
   Attributes:
       qualifiedSectionType: The undeclared qualified section type appended by the OVF consumer.
   """
   qualifiedSectionType: str

class OvfConsumerUndefinedPrefix(OvfConsumerCallbackFault):
   """
   A fault type indicating that an OVF consumer added a section with an unbound prefix.
   
   Attributes:
       prefix: The prefix for which no namespace definition was found.
   """
   prefix: str

class OvfConsumerValidationFault(VmConfigFault):
   """
   Thrown by an OVF consumer if an error occurred while validating an instantiation OST.
   
   Attributes:
       extensionKey: The OVF consumer's extension key.
       extensionName: The OVF consumer's extension name.
       message: The error message, localized by the OVF consumer
   """
   extensionKey: str
   extensionName: str
   message: str

class OvfImport(OvfFault):
   """
   A common base class for errors that can happen during Import and
   that is not due to an invalid package (OvfInvalidPackage).
   
   These
   are typically issued as warnings.
   """
   pass

class OvfCpuCompatibility(OvfImport):
   """
   Attributes:
       registerName: Possible register names are eax, ebx, ecx, or edx.
       level: The CpuId level where a problem was detected.
           
           Other levels may
           also have problems
       registerValue: The register value where the problem was detected
       desiredRegisterValue: The desired register value return from the host
   """
   registerName: str
   level: int
   registerValue: str
   desiredRegisterValue: str

class OvfCpuCompatibilityCheckNotSupported(OvfImport):
   pass

class OvfSystemFault(OvfFault):
   """
   A common base class to host all the OVF subsystems's system faults.
   
   This is a class of fault that can be thrown because of
   some api changes, new hardware that are not supported by
   the host.
   """
   pass

class OvfDiskMappingNotFound(OvfSystemFault):
   """
   Attributes:
       diskName: The disk name that is not found
       vmName: The VM Name
   """
   diskName: str
   vmName: str

class OvfDiskOrderConstraint(OvfConstraint):
   """
   Class used to indicate that the Disks in a DiskSection was not defined
   in the same order as in the Reference section
   """
   pass

class OvfElement(OvfInvalidPackage):
   """
   A base fault for element exceptions in the Ovf XML descriptor.
   
   Attributes:
       name: The name of the element
   """
   name: str

class OvfDuplicateElement(OvfElement):
   """OvfDuplicateElement is thrown if Ovf descriptor contains an invalid duplicate element."""
   pass

class OvfDuplicatedElementBoundary(OvfElement):
   """
   If the Ovf descriptor element have duplicated element bound.
   
   Attributes:
       boundary: Name of duplicated boundary
   """
   boundary: str

class OvfDuplicatedPropertyIdExport(OvfExport):
   """
   Two or more user-configurable properties are
   found with the same fully-qualified property
   name.
   
   Attributes:
       fqid: The fully qualified property id.
   """
   fqid: str

class OvfDuplicatedPropertyIdImport(OvfExport):
   """
   Two or more user-configurable properties are
   found with the same fully-qualified property
   name.
   """
   pass

class OvfElementInvalidValue(OvfElement):
   """
   A class used if a element node is found to have an invalid value.
   
   Base class for OvfProperty errors.
   
   Attributes:
       value: The value of the element
   """
   value: str

class OvfExportFailed(OvfExport):
   """This fault is used if we fail to export an OVF package."""
   pass

class OvfHardwareCheck(OvfImport):
   pass

class OvfHostResourceConstraint(OvfConstraint):
   """
   Class used to indicate that the value in HostResource did not map to
   a valid reference element.
   
   Attributes:
       value: Value of the element
   """
   value: str

class OvfHostValueNotParsed(OvfSystemFault):
   """
   Attributes:
       property: The host property field that could not be parsed.
       value: Value of the field that could not be parsed.
   """
   property: str
   value: str

class OvfImportFailed(OvfImport):
   """This fault is used if we fail to deploy an OVF package."""
   pass

class OvfInternalError(OvfSystemFault):
   """Disk mode not supported"""
   pass

class OvfInvalidValue(OvfAttribute):
   """
   If an invalid value is found in the Ovf descriptor we throw an OvfInvalidValue exception.
   
   Attributes:
       value: Attribute value
   """
   value: str

class OvfInvalidValueConfiguration(OvfInvalidValue):
   """
   If an malformed ovf:configuration attribute value is found in the
   Ovf descriptor we throw an OvfInvalidValueConfiguration exception.
   """
   pass

class OvfInvalidValueEmpty(OvfInvalidValue):
   """If an attribute is found with an empty value where it is not allowed."""
   pass

class OvfInvalidValueFormatMalformed(OvfInvalidValue):
   """
   If an malformed value is found in the Ovf descriptor we throw an OvfInvalidValueFormatMalformed
   exception.
   """
   pass

class OvfInvalidValueReference(OvfInvalidValue):
   """
   If a value refer to something that is not found is found in the Ovf descriptor
   we throw an OvfInvalidValueReference exception.
   """
   pass


class OvfUnsupportedPackage(OvfFault):
   """
   A common base class to host all the Ovf Lib Unsupported Package faults
   
   Attributes:
       lineNumber: OVF descriptor linenumber
   """
   lineNumber: _typing.Optional[int] = None

class OvfInvalidVmName(OvfUnsupportedPackage):
   """
   This fault is used if we can not normalize the vm name
   
   Attributes:
       name: The name of the invalid Virtual Machine
   """
   name: str

class OvfMappedOsId(OvfImport):
   """
   Attributes:
       ovfId: The operating system id specified in the OVF descriptor.
       ovfDescription: The OS description specified in the OVF descriptor.
       targetDescription: The display name of the target OS
   """
   ovfId: int
   ovfDescription: str
   targetDescription: str

class OvfMissingAttribute(OvfAttribute):
   """If the Ovf descriptor is missing an attribute this exception is thrown."""
   pass

class OvfMissingElement(OvfElement):
   """If the Ovf descriptor is missing an Element this exception is thrown."""
   pass

class OvfMissingElementNormalBoundary(OvfMissingElement):
   """
   If the Ovf descriptor element normal boundary is not met this exception is thrown.
   
   Attributes:
       boundary: The missing bound
   """
   boundary: str

class OvfMissingHardware(OvfImport):
   """
   The OVF descriptor does not have a description of
   a required hardware element e.g CPU, Memory
   
   Attributes:
       name: Name of the missing hardware.
       resourceType: OVF rasd resource type of the missing hardware.
   """
   name: str
   resourceType: int

class OvfNetworkMappingNotSupported(OvfImport):
   """
   The network mapping provided for OVF Import
   is not supported by any hosts
   """
   pass

class OvfNoHostNic(OvfUnsupportedPackage):
   """This fault is used if there is no network defined on host"""
   pass

class OvfUnsupportedElement(OvfUnsupportedPackage):
   """
   If the Ovf descriptor has an unsupported element where it is not allowed.
   
   Attributes:
       name: The name of the unsupported element
   """
   name: str

class OvfNoSpaceOnController(OvfUnsupportedElement):
   """
   If the hardware element (RASD) point to a parent controller where there is no
   space left.
   
   Attributes:
       parent: The parent reference
   """
   parent: str

class OvfNoSupportedHardwareFamily(OvfUnsupportedPackage):
   """
   Attributes:
       version: Version found that was not supported
   """
   version: str

class OvfProperty(OvfInvalidPackage):
   """
   A base fault for property faults in the property section of the Ovf XML descriptor.
   
   Attributes:
       type: The type of the property
       value: The value of the property
   """
   type: str
   value: str

class OvfPropertyExport(OvfExport):
   """
   VIM property type that can not be converted to OVF
   
   Attributes:
       type: VIM type
       value: VIM value
   """
   type: str
   value: str

class OvfPropertyNetwork(OvfProperty):
   """A class used indicate there was a property network error"""
   pass

class OvfPropertyNetworkExport(OvfExport):
   """
   VIM property type that refers to a network that
   does not exist in the package since no virtual machines
   are hooked up to it.
   
   Attributes:
       network: name of network
   """
   network: str

class OvfPropertyQualifier(OvfProperty):
   """
   A class used to indicate there was a property qualifier error
   
   Attributes:
       qualifier: qualifiers
   """
   qualifier: str

class OvfPropertyQualifierDuplicate(OvfProperty):
   """
   Indicate that a property qualifier was duplicated.
   
   Attributes:
       qualifier: qualifiers
   """
   qualifier: str

class OvfPropertyQualifierIgnored(OvfProperty):
   """
   Indicate that the was qualifier was ignored
   
   Attributes:
       qualifier: qualifiers
   """
   qualifier: str

class OvfPropertyType(OvfProperty):
   """A class used to indicate there was a property type error"""
   pass

class OvfPropertyValue(OvfProperty):
   """A class used indicate there was a property value error"""
   pass


class OvfToXmlUnsupportedElement(OvfSystemFault):
   """
   Unsupported element to export to XML
   
   Attributes:
       name: The name of the xml element we could not write to the xml descriptor
   """
   name: _typing.Optional[str] = None

class OvfUnableToExportDisk(OvfHardwareExport):
   """
   Attributes:
       diskName: disk name
   """
   diskName: str

class OvfUnexpectedElement(OvfElement):
   """Class used to indicate an unexpected element in the Ovf descriptor"""
   pass


class OvfUnknownDevice(OvfSystemFault):
   """
   Attributes:
       device: The unknown device
       vmName: The name of the Virtual Machine containing the unknown device
   """
   device: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice] = None
   vmName: str


class OvfUnknownDeviceBacking(OvfHardwareExport):
   """
   Attributes:
       backing: The VirtualDevice BackingInfo that is not supported by OVF export.
   """
   backing: pyVmomi.vim.vm.device.VirtualDevice.BackingInfo

class OvfUnknownEntity(OvfSystemFault):
   """
   Attributes:
       lineNumber: line number where the unknown entity was found
   """
   lineNumber: int

class OvfUnsupportedAttribute(OvfUnsupportedPackage):
   """
   If the Ovf descriptor have an unsupported attribute.
   
   Attributes:
       elementName: The name of the element with the unsupported attribute
       attributeName: The name of the unsupported attribute
   """
   elementName: str
   attributeName: str

class OvfUnsupportedAttributeValue(OvfUnsupportedAttribute):
   """
   Used when an OVF descriptor attribute has an unsupported value.
   
   Attributes:
       value: Unsupported attribute value
   """
   value: str


class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
   """
   Attributes:
       elementName: The element name
       instanceId: The InstanceId on the hardware description
       deviceName: The device name
       backingName: The name of the VirtualDevice Backing Info not supported on the device.
   """
   elementName: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   deviceName: str
   backingName: _typing.Optional[str] = None


class OvfUnsupportedDeviceBackingOption(OvfSystemFault):
   """
   Attributes:
       elementName: The element name
       instanceId: The InstanceId for the hardware element
       deviceName: The device name
       backingName: The name of the VirtualDevice Backing Option not supported on the device.
   """
   elementName: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   deviceName: str
   backingName: _typing.Optional[str] = None

class OvfUnsupportedDeviceExport(OvfHardwareExport):
   pass

class OvfUnsupportedDiskProvisioning(OvfImport):
   """
   Disk provisioning not supported
   
   Attributes:
       diskProvisioning: The disk provisioning that was not supported.
       supportedDiskProvisioning: Disk modes supported by the host.
   """
   diskProvisioning: str
   supportedDiskProvisioning: str

class OvfUnsupportedElementValue(OvfUnsupportedElement):
   """
   If the Ovf descriptor has an unsupported value of a element in the
   OVF descriptor.
   
   Attributes:
       value: The unsupported element value
   """
   value: str

class OvfUnsupportedSection(OvfUnsupportedElement):
   """
   If the Ovf descriptor has an unsupported required section.
   
   Attributes:
       info: The info of the unsupported section
   """
   info: str

class OvfUnsupportedSubType(OvfUnsupportedPackage):
   """
   Attributes:
       elementName: The name of the element with the unsupported type
       instanceId: The OVF RASD InstanceId for the hardware description
       deviceType: The device type
       deviceSubType: The device subtype that is unsupported
   """
   elementName: str
   instanceId: str
   deviceType: int
   deviceSubType: str

class OvfUnsupportedType(OvfUnsupportedPackage):
   """
   Attributes:
       name: The name of the element with the unsupported type
       instanceId: The OVF RASD InstanceId for the hardware description
       deviceType: The device type that is unsupported
   """
   name: str
   instanceId: str
   deviceType: int

class OvfWrongElement(OvfElement):
   """If the Ovf descriptor has an element that is not accepted, this exception is thrown."""
   pass

class OvfWrongNamespace(OvfInvalidPackage):
   """
   A OvfWrongNamespace exception is throw if the ovf descriptor has a
   Namespace error as defined in the Ovf spec
   
   Attributes:
       namespaceName: The name of the invalid namespace
   """
   namespaceName: str

class OvfXmlFormat(OvfInvalidPackage):
   """
   Class used to specify if the Ovf XML descriptor could not be parsed
   
   Attributes:
       description: Description of the XML parser error
           
           High level error description
   """
   description: str

class PasswordExpired(InvalidLogin):
   """Thrown when a server login fails due to expired user password."""
   pass

class PatchNotApplicable(VimFault):
   """
   This fault is thrown if a patch install fails because the patch is not
   applicable to the host.
   
   Typically, a subclass of this exception is
   thrown, indicating a problem such as the patch is superseded, already
   installed, or has dependencies missing, and so on.
   
   Attributes:
       patchID: The ID of the patch that is not applicable to the host.
   """
   patchID: str

class PatchAlreadyInstalled(PatchNotApplicable):
   """
   This fault is thrown if a patch install fails because the patch
   is already installed on the host.
   """
   pass


class PatchBinariesNotFound(VimFault):
   """
   This fault is thrown if a patch install fails
   because the binaries associated with the patch are not found.
   
   Attributes:
       patchID: The patch whose associated binaries are not found.
       binary: The binaries that are not found.
   """
   patchID: str
   binary: list[str] = []

class PatchInstallFailed(PlatformConfigFault):
   """
   This is a general-purpose fault indicating that some error has
   occurred regarding a patch install.
   
   Data about the fault is
   available and is presented as a platform specific string.
   
   Attributes:
       rolledBack: Whether or not the patch install has been rolled back.
           
           If not,
           a manual rollback is required.
   """
   rolledBack: bool

class PatchIntegrityError(PlatformConfigFault):
   """
   This fault is thrown if a patch operation fails because the signature of
   the patch did not check out.
   """
   pass


class PatchMetadataInvalid(VimFault):
   """
   This fault is thrown if a patch query or
   installation operation fails because of a problem with the metadata
   associated with the patch.
   
   Typically, a subclass of this exception is
   thrown, indicating a problem such as the metadata is not found or the
   metadata is corrupted.
   
   Attributes:
       patchID: The patch ID whose associated metadata is invalid.
       metaData: The metadata file that is not available or corrupted.
   """
   patchID: str
   metaData: list[str] = []

class PatchMetadataCorrupted(PatchMetadataInvalid):
   """
   This fault is thrown if the metadata associated with a patch is
   corrupted or unreadable when a patch query or install is attempted.
   """
   pass

class PatchMetadataNotFound(PatchMetadataInvalid):
   """
   This fault is thrown if the metadata associated with a patch is not
   found when a patch query or install is attempted.
   """
   pass


class PatchMissingDependencies(PatchNotApplicable):
   """
   This fault is thrown if a patch install fails because the patch
   requires other patches or libraries that are not installed on the host.
   
   Attributes:
       prerequisitePatch: The ID of required patches.
       prerequisiteLib: The names of required libraries or RPMs.
   """
   prerequisitePatch: list[str] = []
   prerequisiteLib: list[str] = []


class PatchSuperseded(PatchNotApplicable):
   """
   This fault is thrown if a patch install fails because the patch is
   superseded by patches already installed.
   
   Attributes:
       supersede: The patches that supersede this patch.
   """
   supersede: list[str] = []

class RDMNotSupported(DeviceNotSupported):
   """
   The virtual machine is configured with a Raw Disk Mapping.
   
   This is not
   supported on the host.
   """
   pass

class PhysCompatRDMNotSupported(RDMNotSupported):
   """
   The virtual machine is configured with a Raw Disk Mapping in physical compatibility mode.
   
   This mode is not supported on the host.
   """
   pass


class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
   """
   The PowerOnFtSecondaryFailed fault is thrown when the system is unable to
   power on a Fault Tolerance secondary virtual machine.
   
   It includes a list
   of failures on different hosts.
   
   Attributes:
       vm: The primary virtual machine corresponding to the secondary that is to
           be powered on
       vmName: The name of the primary virtual machine corresponding to the secondary
           that is to be powered on.
       hostSelectionBy: The host selection type
       hostErrors: Information on why the system can not power on a Fault Tolerance
           secondary virtual machine on specific hosts.
           
           Everything in the array
           should be FtIssuesOnHost.
       rootCause: The reason why powering on secondary failed.
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str
   hostSelectionBy: FtIssuesOnHost.HostSelectionType
   hostErrors: list[pyVmomi.vmodl.MethodFault] = []
   rootCause: pyVmomi.vmodl.MethodFault

class Timedout(VimFault):
   """
   Timedout exception is thrown when a server abandons an operation that
   is taking longer than expected.
   """
   pass


class PowerOnFtSecondaryTimedout(Timedout):
   """
   PowerOnFtSecondaryTimedout exception is thrown when Virtual Center
   fails the operation to power on a Fault Tolerance secondary virtual
   machine because it is taking longer than expected.
   
   Attributes:
       vm: The primary virtual machine corresponding to the secondary that is to
           be powered on
       vmName: The name of the primary virtual machine corresponding to the secondary
           that is to be powered on.
       timeout: The time out value in seconds
   """
   vm: pyVmomi.vim.VirtualMachine
   vmName: str
   timeout: int


class ProfileUpdateFailed(VimFault):
   """
   Errors were detected during Profile update.
   
   Attributes:
       failure: Failures encountered during update/validation
       warnings: Warnings encountered during update/validation
   """
   class UpdateFailure(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          profilePath: Location in the profile which has the error
          errMsg: Message which explains the problem encountered
      """
      profilePath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   failure: list[ProfileUpdateFailed.UpdateFailure] = []
   warnings: list[ProfileUpdateFailed.UpdateFailure] = []


class QuarantineModeFault(VmConfigFault):
   class FaultType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          NoCompatibleNonQuarantinedHost: The cluster does not contain any non-quarantined host satisfying the
              VM/host affinity rules for the VM.
          CorrectionDisallowed: The current DRS migration priority setting disallows generating a
              recommendation to prevent VMs on quarantined hosts.
              
              Thus, the
              violation will not be corrected.
          CorrectionImpact: DRS has determined that evacuation of VMs from quarantined hosts
              impacts respecting cluster constraints or performance goals so they
              are not evacuated.
      """
      NoCompatibleNonQuarantinedHost: _typing.ClassVar['QuarantineModeFault.FaultType'] = 'NoCompatibleNonQuarantinedHost'
      CorrectionDisallowed: _typing.ClassVar['QuarantineModeFault.FaultType'] = 'CorrectionDisallowed'
      CorrectionImpact: _typing.ClassVar['QuarantineModeFault.FaultType'] = 'CorrectionImpact'

   vmName: str
   faultType: str

class QuestionPending(InvalidState):
   """
   Thrown when an operation cannot be performed on a virtual machine
   because it has a pending question requiring user input.
   
   Attributes:
       text: Text of the question from the virtual machine.
   """
   text: str


class QuiesceDatastoreIOForHAFailed(ResourceInUse):
   """
   A QuiesceDatastoreIOForHAFailed fault occurs when the HA agent on a host
   cannot quiesce file activity on a datastore to be unmouonted or removed.
   
   Attributes:
       host: The host.
       hostName: Name of the host.
       ds: The datastore.
       dsName: Name of the datastore.
   """
   host: pyVmomi.vim.HostSystem
   hostName: str
   ds: pyVmomi.vim.Datastore
   dsName: str

class RDMConversionNotSupported(MigrationFault):
   """
   The virtual machine is using an RDM device with compatibility
   mode set to 'physicalMode' and operation is unable to convert
   the disk to a different type.
   
   Attributes:
       device: The name of the disk device using the RDM.
   """
   device: str

class RDMNotPreserved(MigrationFault):
   """
   The virtual machine is configured with a Raw Disk Mapping.
   
   The host only supports Raw
   Disk Mappings in a limited fashion. After the migration, the RDM will function correctly,
   but it will be indistinguishable from a virtual disk when viewing the virtual machine's
   properties. This change will persist even if the virtual machine is migrated
   back to a host with full RDM support.
   
   This is a warning only for migrations to ESX 2.1.x hosts.
   
   Attributes:
       device: The name of the disk device using the RDM.
   """
   device: str


class RDMNotSupportedOnDatastore(VmConfigFault):
   """
   The virtual machine is configured with a Raw Disk Mapping.
   
   This is not
   supported on the datastore.
   
   Attributes:
       device: The label of the RDM device that would have its backing placed on
           the datastore.
           
           This is not guaranteed to be the only such device.
       datastore: The datastore.
       datastoreName: The name of the datastore.
   """
   device: str
   datastore: pyVmomi.vim.Datastore
   datastoreName: str

class RDMPointsToInaccessibleDisk(CannotAccessVmDisk):
   """
   One of the virtual machine's virtual disks is a Raw Disk Mapping
   that is itself accessible, but points to a LUN that is inaccessible.
   """
   pass

class RawDiskNotSupported(DeviceNotSupported):
   """
   The virtual machine has a raw disk attached that is not supported.
   
   This is often
   used as a subfault for DisallowedMigrationDeviceAttached or
   DisallowedSnapshotDeviceAttached.
   """
   pass

class ReadHostResourcePoolTreeFailed(HostConnectFault):
   """
   Fault thrown on host connect if we were unable to correctly read the
   existing tree on the root.
   
   This is bad because then we don't know the
   available resources on the host, and all kinds of admission control will
   fail.
   This just allows for more robust error handling - we should be able to
   read the existing hierarchy under normal conditions.
   """
   pass

class ReadOnlyDisksWithLegacyDestination(MigrationFault):
   """
   The virtual machine uses read-only (undoable or nonpersistent) disks that
   can cause a slower power on at the migration destination.
   
   As a result, VMtion
   could slow down considerably or timeout. This is an issue only for migration of
   powered-on virtual machines from an ESX host with version greater
   than 2.0.x to an ESX host with version 2.0.x. It will be an error if the
   number of such disks is great enough to cause timeout (3 or more), or a warning
   otherwise.
   
   Attributes:
       roDiskCount: The number of read-only disks in use.
       timeoutDanger: Whether this number of disks will cause a timeout failure.
   """
   roDiskCount: int
   timeoutDanger: bool


class RebootRequired(VimFault):
   """
   This fault is thrown if a patch install fails because an installed
   nonchainable patch has not taken effect.
   
   Attributes:
       patch: The nonchainable patch installed.
   """
   patch: _typing.Optional[str] = None

class RecordReplayDisabled(VimFault):
   """
   Deprecated: as of vSphere API 6.0Fault thrown if a record or replay operation cannot be performed
   because these capabilities have been disabled on the virtual machine.
   """
   pass

class RemoteDeviceNotSupported(DeviceNotSupported):
   """
   The virtual machine has a currently connected device with a remote backing.
   
   This is an error when migrating a powered-on virtual machine, and can be returned
   as a subfault of DisallowedMigrationDeviceAttached.
   """
   pass

class RemoveFailed(VimFault):
   """
   This fault is thrown when the client attempts to remove an object that has
   active related objects (for example, a role that has active permissions).
   """
   pass

class ReplicationConfigFault(ReplicationFault):
   """Base type for Replication-related configuration errors."""
   pass


class ReplicationDiskConfigFault(ReplicationConfigFault):
   """
   A ReplicationDiskConfigFault is thrown when there is an issue with
   configuring disk replication properties.
   
   Attributes:
       reason: The reason for the failure.
           
           One of the above.
       vmRef: The virtual machine, for identification purposes.
       key: The disk (device) key in the parent VM for identification
           purposes.
   """
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          diskNotFound: Could not look up device by key
          diskTypeNotSupported: Replication not supported for disk type or backend
          invalidDiskKey: Invalid key value
          invalidDiskReplicationId: Invalid disk replication ID string
          duplicateDiskReplicationId: Another disk in the VM has the same replication ID
          invalidPersistentFilePath: Invalid path (string) for the persistent file
          reconfigureDiskReplicationIdNotAllowed: Attempting to re-configure the disk's replication ID
      """
      diskNotFound: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'diskNotFound'
      diskTypeNotSupported: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'diskTypeNotSupported'
      invalidDiskKey: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'invalidDiskKey'
      invalidDiskReplicationId: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'invalidDiskReplicationId'
      duplicateDiskReplicationId: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'duplicateDiskReplicationId'
      invalidPersistentFilePath: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'invalidPersistentFilePath'
      reconfigureDiskReplicationIdNotAllowed: _typing.ClassVar['ReplicationDiskConfigFault.ReasonForFault'] = 'reconfigureDiskReplicationIdNotAllowed'

   reason: _typing.Optional[str] = None
   vmRef: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   key: _typing.Optional[int] = None

class ReplicationIncompatibleWithFT(ReplicationFault):
   """
   Used to indicate that FT cannot be enabled on a replicated virtual machine
   (returned by `pyVmomi.vim.VirtualMachine.queryFaultToleranceCompatibility`).
   """
   pass


class ReplicationInvalidOptions(ReplicationFault):
   """
   A ReplicationInvalidOptions fault is thrown when the options
   string passed contains invalid characters or broken format.
   
   Attributes:
       options: The invalid options string.
       entity: Entity, if any, that has invalid options.
   """
   options: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None

class ReplicationNotSupportedOnHost(ReplicationFault):
   """Thrown if the replication module is not loaded in the host."""
   pass


class ReplicationVmConfigFault(ReplicationConfigFault):
   """
   A ReplicationVmConfigFault is thrown when there is an issue with
   configuring VM-wide replication properties.
   
   Attributes:
       reason: The reason for the failure.
           
           One of the above `pyVmomi.vim.fault.ReplicationVmConfigFault.ReasonForFault`.
       vmRef: The virtual machine, for identification purposes.
   """
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          incompatibleHwVersion: Incompatible VM hardware version
          invalidVmReplicationId: Invalid VM Replication ID string
          invalidGenerationNumber: Invalid generation number in VM's configuration
          outOfBoundsRpoValue: Invalid RPO value (out of bounds)
          invalidDestinationIpAddress: Invalid destination IP address
          invalidDestinationPort: Invalid destination port
          invalidExtraVmOptions: Malformed extra options list
          staleGenerationNumber: Mismatching generation number (stale)
          reconfigureVmReplicationIdNotAllowed: Attempting to re-configure the VM replication ID
          cannotRetrieveVmReplicationConfiguration: Could not retrieve the VM configuration
          replicationAlreadyEnabled: Attempting to re-enable replication for the VM
          invalidPriorConfiguration: The existing replication configuration of the VM is broken
              (applicable to re-configuration only).
          replicationNotEnabled: Attempting to re-configure or disable replication for a VM
              for which replication has not been enabled.
          replicationConfigurationFailed: Failed to commit the new replication properties for the VM.
          encryptedVm: VM is encrypted
          invalidThumbprint: Remote certificate thumbprint is invalid
          incompatibleDevice: VM hardware contains devices incompatible with replication
      """
      incompatibleHwVersion: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'incompatibleHwVersion'
      invalidVmReplicationId: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidVmReplicationId'
      invalidGenerationNumber: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidGenerationNumber'
      outOfBoundsRpoValue: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'outOfBoundsRpoValue'
      invalidDestinationIpAddress: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidDestinationIpAddress'
      invalidDestinationPort: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidDestinationPort'
      invalidExtraVmOptions: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidExtraVmOptions'
      staleGenerationNumber: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'staleGenerationNumber'
      reconfigureVmReplicationIdNotAllowed: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'reconfigureVmReplicationIdNotAllowed'
      cannotRetrieveVmReplicationConfiguration: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'cannotRetrieveVmReplicationConfiguration'
      replicationAlreadyEnabled: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'replicationAlreadyEnabled'
      invalidPriorConfiguration: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidPriorConfiguration'
      replicationNotEnabled: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'replicationNotEnabled'
      replicationConfigurationFailed: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'replicationConfigurationFailed'
      encryptedVm: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'encryptedVm'
      invalidThumbprint: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'invalidThumbprint'
      incompatibleDevice: _typing.ClassVar['ReplicationVmConfigFault.ReasonForFault'] = 'incompatibleDevice'

   reason: _typing.Optional[str] = None
   vmRef: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class ReplicationVmFault(ReplicationFault):
   """
   A ReplicationVmFault is thrown when there is an issue with
   an operation performed on a replicated `pyVmomi.vim.VirtualMachine`
   
   Attributes:
       reason: The reason for the failure.
           
           One of the above.
       state: The current `pyVmomi.vim.HbrManager.ReplicationVmInfo.State` of the
           `pyVmomi.vim.VirtualMachine`
       instanceId: The name of the instance currently being created.
       vm: The virtual machine, for identification purposes.
   """
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          notConfigured: `pyVmomi.vim.VirtualMachine` is not configured for replication
          poweredOff: `pyVmomi.vim.VirtualMachine` is powered off (and is not undergoing
              offline replication)
          suspended: `pyVmomi.vim.VirtualMachine` is suspended (and is not undergoing
              offline replication)
          poweredOn: `pyVmomi.vim.VirtualMachine` is powered on
          offlineReplicating: `pyVmomi.vim.VirtualMachine` is in the process of creating an
              an offline instance.
          invalidState: `pyVmomi.vim.VirtualMachine` is in an invalid state
          invalidInstanceId: The specified instanceId does not match the `pyVmomi.vim.VirtualMachine`
              instanceId
          closeDiskError: `pyVmomi.vim.VirtualMachine` is in the process of creating an
              offline instance and we are trying to disable it.
              
              The first step is to close the offline disk. If closing disks
              is not successful, throw this fault.
          groupExist: `pyVmomi.vim.VirtualMachine` is trying to create a group already
              owned by another VM.
      """
      notConfigured: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'notConfigured'
      poweredOff: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'poweredOff'
      suspended: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'suspended'
      poweredOn: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'poweredOn'
      offlineReplicating: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'offlineReplicating'
      invalidState: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'invalidState'
      invalidInstanceId: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'invalidInstanceId'
      closeDiskError: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'closeDiskError'
      groupExist: _typing.ClassVar['ReplicationVmFault.ReasonForFault'] = 'groupExist'

   reason: str
   state: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   vm: pyVmomi.vim.VirtualMachine


class ReplicationVmInProgressFault(ReplicationVmFault):
   """
   A ReplicationVmInProgressFault is thrown when a replication operation
   failed to perform on a `pyVmomi.vim.VirtualMachine` because the VM is
   in the middle of another replication activity.
   
   Attributes:
       requestedActivity: The requested activity for VM replication
       inProgressActivity: The in-progress activity for VM replication
   """
   class Activity(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          fullSync: Initial synchronization with the remote site
          delta: Delta updates to generate a consistent instance
      """
      fullSync: _typing.ClassVar['ReplicationVmInProgressFault.Activity'] = 'fullSync'
      delta: _typing.ClassVar['ReplicationVmInProgressFault.Activity'] = 'delta'

   requestedActivity: str
   inProgressActivity: str


class ResourceNotAvailable(VimFault):
   """
   A ResourceNotAvailable fault indicating that some error has occurred because a
   resource was not available.
   
   Information about the resource that is in use may
   be supplied.
   
   Attributes:
       containerType: Type of container that contains the resource.
       containerName: Name of container that contains the resource.
           
           .
       type: Type of resource that is not available.
   """
   containerType: _typing.Optional[type] = None
   containerName: _typing.Optional[str] = None
   type: _typing.Optional[type] = None


class RestrictedByAdministrator(pyVmomi.vmodl.RuntimeFault):
   """
   This fault is thrown when an operation cannot complete because of some
   restriction set by the server administrator.
   """
   details: str


class RestrictedVersion(pyVmomi.vmodl.fault.SecurityError):
   """
   Thrown when the caller is not permitted to perform the specified
   operation due to product versioning restrictions.
   """
   pass

class RollbackFailure(DvsFault):
   """
   Thrown if a Rollback operation fails
   
   Attributes:
       entityName: The entity name on which rollback failed
       entityType: The entity type on which rollback failed
   """
   entityName: str
   entityType: str


class RuleViolation(VmConfigFault):
   """
   The virtual machine if powered on, would violate an
   affinity/anti-affinity rule.
   
   In this case, the VM can still be powered
   on manually by a user who knows what they are doing, but VirtualCenter
   will never automatically move or power on a VM such that it triggers
   the violation.
   
   Attributes:
       host: The host that the virtual machine can not be powered on without
           violate a rule.
       rule: The rule that is violated.
           
           It can be an affinity or anti-affinity rule.
   """
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   rule: pyVmomi.vim.cluster.RuleInfo

class SSLDisabledFault(HostConnectFault):
   """A SSLDisabledFault fault occurs when a host does not have ssl enabled."""
   pass


class SSLVerifyFault(HostConnectFault):
   """
   SSLVerifyFault is thrown by the host connect method if the VC
   server could not verify the authenticity of the host's SSL
   certificate.
   
   Currently, we do not distinguish the various possible reasons why
   the certificate could not be verified because we don't provide a
   way for the user to overwrite these reasons other than turning off
   SSL certificate verification completely.
   The only exception is the case when the certificate was rejected
   because it was self-signed. This is the most likely case when the
   user may want to overwrite the behavior by specifying the
   certificate's thumbprint in the ConnectSpec the next time the user
   connects to the host.
   
   Attributes:
       selfSigned: Whether the host's certificate was self signed
       thumbprint: The thumbprint of the host's certificate.
           
           This field is optional since vSphere 8.0u2.
       certificate: The certificate of the host
           Note: `pyVmomi.vim.fault.SSLVerifyFault.thumbprint` and `pyVmomi.vim.fault.SSLVerifyFault.certificate` parameters are
           mutually exclusive, and should never be used simultaneously.
           
           Since: vSphere API Release 9.0.0.0
   """
   selfSigned: bool
   thumbprint: _typing.Optional[str] = None
   certificate: _typing.Optional[str] = None

class SSPIChallenge(VimFault):
   """
   Thrown during SSPI pass-through authentication if further
   negotiation is required.
   
   Attributes:
       base64Token: The opaque server response token, base-64 encoded.
   """
   base64Token: str

class SecondaryVmAlreadyDisabled(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to disable a secondary
   virtual machine that has already been disabled.
   
   Attributes:
       instanceUuid: Instance UUID of the secondary virtual machine.
   """
   instanceUuid: str

class SecondaryVmAlreadyEnabled(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to enable a secondary
   virtual machine that has already been enabled.
   
   Attributes:
       instanceUuid: Instance UUID of the secondary virtual machine.
   """
   instanceUuid: str

class SecondaryVmAlreadyRegistered(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to register a secondary
   virtual machine with a primary virtual machine with whom it is
   already registered.
   
   Attributes:
       instanceUuid: Instance UUID of the secondary virtual machine.
   """
   instanceUuid: str

class SecondaryVmNotRegistered(VmFaultToleranceIssue):
   """
   This fault is thrown when an attempt is made to unregister a secondary
   virtual machine from a primary virtual machine with whom it has not
   been previously registered.
   
   Attributes:
       instanceUuid: Instance UUID of the secondary virtual machine.
   """
   instanceUuid: str

class SharedBusControllerNotSupported(DeviceNotSupported):
   """
   The virtual machine has one or more SCSI controllers that are engaged
   in bus sharing.
   
   This is an error when migrating a powered-on virtual machine,
   and can be returned as a subfault of DisallowedMigrationDeviceAttached.
   """
   pass


class ShrinkDiskFault(VimFault):
   """
   This exception is thrown when VirtualMachine.shrinkDisk
   encounters an error
   
   Attributes:
       diskId: Disk Id of the virtual disk that caused the fault
   """
   diskId: _typing.Optional[int] = None

class SnapshotCloneNotSupported(SnapshotCopyNotSupported):
   """
   An attempt is being made to copy a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported by the
   host under any circumstances.
   
   This is a warning.
   """
   pass

class SnapshotDisabled(SnapshotFault):
   """
   Fault thrown if a snapshot operation cannot be performed because
   snapshots are disabled on the virtual machine.
   """
   pass


class SnapshotIncompatibleDeviceInVm(SnapshotFault):
   """
   Thrown if a snapshot operation cannot be performed on account
   of an incompatible device.
   
   This fault can be thrown for instance
   if a virtual machine uses a raw disk or a shared bus controller.
   
   Attributes:
       fault: A fault specifies the particular device issue.
           
           This is typically
           a subclass of VirtualHardwareCompatibilityIssue, such as
           RawDiskNotSupported, or SharedBusControllerNotSupported.
   """
   fault: pyVmomi.vmodl.MethodFault

class SnapshotLocked(SnapshotFault):
   """
   Fault thrown when an attempt is made to create or delete a snapshot on a
   virtual machine that has its snapshot locked.
   """
   pass

class SnapshotMoveFromNonHomeNotSupported(SnapshotCopyNotSupported):
   """
   An attempt is being made to move a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported by the
   host because the disk is currently located somewhere other than the virtual
   machine's home datastore.
   """
   pass

class SnapshotMoveNotSupported(SnapshotCopyNotSupported):
   """
   An attempt is being made to move a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported by the
   host under any circumstances.
   """
   pass

class SnapshotMoveToNonHomeNotSupported(SnapshotCopyNotSupported):
   """
   An attempt is being made to move a virtual machine's disk that has
   associated snapshots, and preserving the snapshots is not supported by the
   host because the disk is being moved to some location other than the new
   home datastore for the virtual machine.
   """
   pass

class SnapshotNoChange(SnapshotFault):
   """
   This fault is for a snapshot request on a virtual machine whose state
   has not changed since a previous successful snapshot.
   
   For example, this
   occurs when you suspend the virtual machine, create a snapshot, and
   then request another snapshot of the suspended virtual machine.
   """
   pass


class SnapshotRevertIssue(MigrationFault):
   """
   If the virtual machine is migrated to the destination host, there may be
   a problem reverting to one of its snapshots.
   
   This is a warning. If the
   snapshot name is not set and the event array is empty, then it the snapshot
   might possibly revert correctly. If the name is set and the event array is not
   empty then there surely will be a problem reverting to the snapshot.
   
   Attributes:
       snapshotName: The name of the problematic snapshot.
       event: The problem(s) that would occur on reverting to the snapshot.
           
           This
           is determined similarly to invoking validateMigration on a powered-off
           virtual machine with the snapshot's state. However, not all errors
           or warnings for virtual machine migration are guaranteed to be
           detected for snapshots.
       errors: True if any of the events above are error events.
   """
   snapshotName: _typing.Optional[str] = None
   event: list[pyVmomi.vim.event.Event] = []
   errors: bool

class SoftRuleVioCorrectionDisallowed(VmConfigFault):
   """
   The current DRS migration priority setting prevents generating
   a recommendation to correct the soft VM/Host affinity rules constraint
   violation for the VM so the violation will not be corrected.
   
   Attributes:
       vmName: The vm for which the VM/Host soft affinity rules constraint violation
           is not being corrected by DRS.
   """
   vmName: str

class SoftRuleVioCorrectionImpact(VmConfigFault):
   """
   DRS has determined that correcting the soft VM/Host affinity rules
   constraint violation for the VM impacts respecting cluster constraints
   or performance goals so the violation will not be corrected.
   
   Attributes:
       vmName: The vm for which the VM/Host soft affinity rules constraint violation
           is not being corrected by DRS.
   """
   vmName: str


class SolutionUserRequired(pyVmomi.vmodl.fault.SecurityError):
   """
   Thrown when an operation is denied because the entity
   invoking it is not a Solution User.
   """
   pass

class SsdDiskNotAvailable(VimFault):
   """
   A SsdDiskNotAvailable fault indicating that the specified SSD
   disk is not available.
   
   The disk either has been used or not a
   SSD disk.
   
   Attributes:
       devicePath: The device path of the disk.
   """
   devicePath: str

class StorageDrsCannotMoveDiskInMultiWriterMode(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate one or more virtual disks of a VM because the disk has
   multi-writer mode enabled.
   """
   pass

class StorageDrsCannotMoveFTVm(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate Fault Tolerant VMs across datastores.
   """
   pass

class StorageDrsCannotMoveIndependentDisk(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate an independent disk.
   """
   pass

class StorageDrsCannotMoveManuallyPlacedSwapFile(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate VM because it has a manually selected fixed location for its
   swap file.
   """
   pass

class StorageDrsCannotMoveManuallyPlacedVm(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate a Vm that is placed by user to a specific datastore.
   """
   pass

class StorageDrsCannotMoveSharedDisk(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate a shared virtual disk that is attached to more than one Vm.
   """
   pass

class StorageDrsCannotMoveTemplate(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate template VMs across datastores.
   """
   pass

class StorageDrsCannotMoveVmInUserFolder(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate VMs placed in user-specified folders.
   """
   pass

class StorageDrsCannotMoveVmWithMountedCDROM(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate VMs that have a CD-ROM device mounted.
   """
   pass

class StorageDrsCannotMoveVmWithNoFilesInLayout(VimFault):
   """
   This fault is thrown because Storage DRS cannot generate recommendations
   to relocate VMs that have no files in its file layout.
   """
   pass

class StorageDrsDatacentersCannotShareDatastore(VimFault):
   """
   This fault is thrown when one datastore using Storage DRS is added to two
   different datacenters.
   """
   pass

class StorageDrsDisabledOnVm(VimFault):
   """
   This fault is thrown when Storage DRS cannot move disks of a virtual machine
   because Storage DRS is disabled on it.
   """
   pass

class StorageDrsHbrDiskNotMovable(VimFault):
   """
   This fault is thrown when HMS service cannot move certain secondary
   replica disks per Storage DRS move recommendations
   
   Attributes:
       nonMovableDiskIds: Comma-separated list of disk IDs that are not movable and failed
           Storage DRS recommendation action.
   """
   nonMovableDiskIds: str

class StorageDrsHmsMoveInProgress(VimFault):
   """
   This fault is thrown HMS service is in the process of moving
   a subset of disks for which Storage DRS recommendation is generated.
   """
   pass

class StorageDrsHmsUnreachable(VimFault):
   """
   This fault is thrown when Storage DRS cannot connect to HMS service
   or HMS APIs invoked by Storage DRS error out due to connection issues.
   """
   pass

class StorageDrsIolbDisabledInternally(VimFault):
   """
   Deprecated: As of vSphere8.0 U3, and there is no replacement for it.The fault occurs when Storage DRS disables IO Load balancing internally
   even though it is enabled by the user.
   
   This can happen due to one of the
   following reasons:
   1\\. SIOC couldn't get enabled on at least one of the datastores
   2\\. The connectivity between hosts and datastores is not uniform for all datastores.
   3\\. Some statistics are not available to run IO load balancing
   """
   pass

class StorageDrsRelocateDisabled(VimFault):
   """
   This fault is thrown when Storage DRS cannot move disks of a virtual machine
   because the relocate method of the virtual machine is disabled.
   """
   pass

class StorageDrsStaleHmsCollection(VimFault):
   """
   This fault is thrown when Storage DRS action for relocating
   HMS collection of replica disks does not correspond to current
   HMS inventory configuration and hence, is rejected by HMS service.
   """
   pass

class StorageDrsUnableToMoveFiles(VimFault):
   """
   This fault is thrown when Storage DRS cannot generate recommendations
   to move VM files due to pre-existing cross datastore disk backings.
   """
   pass

class StorageVMotionNotSupported(MigrationFeatureNotSupported):
   """
   An operation on a powered-on virtual machine requests a change of storage
   location, but the host does not have that capability.
   """
   pass


class StorageVmotionIncompatible(VirtualHardwareCompatibilityIssue):
   """
   This fault is thrown when Storage DRS tries to migrate disks of a virtual machine to a datastore,
   but finds that the datastore is incompatible with the given virtual machine.
   
   Attributes:
       datastore: The datastore that is incompatible with a given virtual machine.
   """
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class SuspendedRelocateNotSupported(MigrationFault):
   """
   Either the source host product or the destination host product does not support
   relocation of suspended VMs.
   
   It must be supported on both, in order for the
   relocation to succeed. This fault is only applicable to suspended virtual machines.
   """
   pass

class SwapDatastoreNotWritableOnHost(DatastoreNotWritableOnHost):
   """
   The compute resource and/or virtual machine configurations indicate that
   when executing on the host the virtual machine should use a specific
   datastore, but host does not have read/write access to that datastore.
   
   (It may have no access at all, or read-only access.) If executing on the
   host the virtual machine would instead use its own directory for swapfile
   placement. This is a compatibility warning, not an error.
   """
   pass

class SwapDatastoreUnset(VimFault):
   """
   The compute resource and/or virtual machine configurations indicate that
   when executing on the host the virtual machine should use a swap
   datastore, but the host does not have a swap datastore configured.
   
   If
   executing on the host the virtual machine would instead use its own directory
   for swapfile placement. This is a compatibility warning, not an error.
   Note it is actually the common case for a host to not have a configured
   swap datastore, and the problem may rest with the compute resource and/or
   virtual machine configuration; therefore this is not a HostConfigFault.
   """
   pass

class SwapPlacementOverrideNotSupported(InvalidVmConfig):
   """
   The virtual machine is configured to override the default swapfile placement
   policy, which is not supported on the host.
   """
   pass

class SwitchIpUnset(DvsFault):
   """
   The distributed virtual switch received a reconfiguration request to
   activate a feature that requires a switch IP address.
   
   However, the IP
   address for the switch has not been specified.
   """
   pass

class SwitchNotInUpgradeMode(DvsFault):
   """
   Thrown if an operation is not supported while the DistributedVirtualSwitch
   is not in upgrade mode.
   """
   pass


class TaskInProgress(VimFault):
   """
   The TaskInProgress data object type represents a fault when an operation tries
   to access an entity that already has another (long) operation in progress.
   
   Attributes:
       task: The task already in progress when the operation was attempted.
   """
   task: pyVmomi.vim.Task


class ThirdPartyLicenseAssignmentFailed(pyVmomi.vmodl.RuntimeFault):
   """
   A ThirdPartyLicenseAssignmentFailed fault is thrown when
   the license assignment to a 3rd party module fails.
   
   The 3rd-party modules are installed and ran on ESX hosts,
   so this fault provides both host and module IDs.
   
   Attributes:
       host: The ESX host where 3rd party license was applied.
       module: The asset-id of 3rd party module
       reason: The reason why the assignment failed, if known.
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          licenseAssignmentFailed: A general failure has occurred during assigning license to the 3rd party module
          moduleNotInstalled: The 3rd party module we are trying to license is not installed.
      """
      licenseAssignmentFailed: _typing.ClassVar['ThirdPartyLicenseAssignmentFailed.Reason'] = 'licenseAssignmentFailed'
      moduleNotInstalled: _typing.ClassVar['ThirdPartyLicenseAssignmentFailed.Reason'] = 'moduleNotInstalled'

   host: pyVmomi.vim.HostSystem
   module: str
   reason: _typing.Optional[str] = None

class TooManyConcurrentNativeClones(FileFault):
   """
   Thrown if the number of levels in the snapshot tree exceeds
   the supported maximum.
   """
   pass

class TooManyConsecutiveOverrides(VimFault):
   """
   Thrown if there are too many consecutive user overrides of
   server-managed settings.
   
   There are some properties which users are
   allowed to set only in certain configurations. The system controls them
   in other configurations, and overrides all user updates. If there are
   such frequent user overrides in the system controlled state that the
   next update arrives before the previous override is complete, the
   system can enter a tight loop and appear unresponsive to the user. This
   would typically happen if the user overrides are generated by a script.
   If the number of such user overrides exceeds the supported maximum, we
   conceptually \"throw\" this fault. In practice, this is converted into a
   host-level ConfigIssue in VC.
   """
   pass

class TooManyDevices(InvalidVmConfig):
   """
   Thrown when the number of virtual devices exceeds the maximum for
   a given controller.
   """
   pass

class TooManyDisksOnLegacyHost(MigrationFault):
   """
   Deprecated: As of vSphere 4.1, this error condition is no longer possible.The VM has too many disks which can cause the VM to take a long time
   to power-on.
   
   This can result in migration taking a long time to complete
   or to fail due to timeout. This is a problem only for migration of
   powered-on virtual machines from or to ESX 2.x hosts.
   
   Attributes:
       diskCount: The number disks this VM has.
       timeoutDanger: Whether this number of disks will cause a timeout failure.
   """
   diskCount: int
   timeoutDanger: bool

class TooManyGuestLogons(GuestOperationsFault):
   """
   A TooManyGuestLogons exception is thrown when
   there are too many concurrent login sessions active
   in the guest.
   
   `pyVmomi.vim.vm.guest.AuthManager.releaseCredentials` can be called
   on ticketed sessions that are no longer needed. This will decrease
   the number of concurrent sessions active in the guest.
   """
   pass

class TooManyHosts(HostConnectFault):
   """
   Thrown when a computer resource does not accept any more hosts.
   
   Clusters with DRS or
   HA enabled might impose a limit on the size of the cluster.
   """
   pass

class TooManyNativeCloneLevels(FileFault):
   """
   Thrown if the number of levels in the snapshot tree exceeds
   the supported maximum.
   """
   pass

class TooManyNativeClonesOnFile(FileFault):
   """
   Thrown if the number of levels in the snapshot tree exceeds
   the supported maximum.
   """
   pass

class TooManySnapshotLevels(SnapshotFault):
   """
   Thrown if the number of levels in the snapshot tree exceeds
   the supported maximum.
   """
   pass

class VmToolsUpgradeFault(VimFault):
   """A base fault to indicate that something went wrong when upgrading tools."""
   pass

class ToolsAlreadyUpgraded(VmToolsUpgradeFault):
   """
   Thrown when tools upgrade fails because the version of tools
   installed in the guest is already up-to-date.
   """
   pass

class ToolsAutoUpgradeNotSupported(VmToolsUpgradeFault):
   """
   Thrown when tools upgrade fails because the virtual machine's
   guest operating system doesn't support tools auto-upgrades.
   """
   pass

class ToolsImageCopyFailed(VmToolsUpgradeFault):
   """
   Thrown when the tools image couldn't be copied to the guest
   operating system: disk out of space, file access error, etc.
   """
   pass

class ToolsImageNotAvailable(VmToolsUpgradeFault):
   """
   Thrown when tools install or upgrade fails because the required
   tools image is not available.
   """
   pass

class ToolsImageSignatureCheckFailed(VmToolsUpgradeFault):
   """
   Thrown when tools install or upgrade fails because the
   signature check on the tools image failed.
   """
   pass

class ToolsInstallationInProgress(MigrationFault):
   """
   The virtual machine is currently in the progress of guest tools installation
   that prevents the migration operation.
   """
   pass

class ToolsUnavailable(VimFault):
   """
   A ToolsUnavailableFault exception is thrown when an
   operation fails to contact VMware Tools
   running inside the virtual machine.
   """
   pass

class ToolsUpgradeCancelled(VmToolsUpgradeFault):
   """
   Thrown when tools install or upgrade fails because the
   operation was cancelled by the user.
   """
   pass

class UnSupportedDatastoreForVFlash(UnsupportedDatastore):
   """
   VFlash is not supported on the datastore.
   
   Attributes:
       datastoreName: The name of the Datastore.
       type: Datastore file system volume type.
           
           See `pyVmomi.vim.Datastore.Summary.type`
   """
   datastoreName: str
   type: str

class UncommittedUndoableDisk(MigrationFault):
   """
   Fault thrown when an attempt is made to move or clone an undoable disk with an
   uncommitted REDO log.
   
   This is an error. Undoable disks may be moved but they must
   be committed.
   """
   pass

class UnconfiguredPropertyValue(InvalidPropertyValue):
   """
   The property value has not been configured by the user, so the application
   cannot be started.
   
   This is thrown if a property value is the empty string
   and the types does not allow it. For example, for an integer type or
   a string where the minimum length is 1, and so forth.
   """
   pass

class UncustomizableGuest(CustomizationFault):
   """
   The specified guest operating system is not supported by the guest
   customization process.
   
   Attributes:
       uncustomizableGuestOS: The guest OS ID for the uncustomizable guest.
   """
   uncustomizableGuestOS: str

class UnexpectedCustomizationFault(CustomizationFault):
   """
   Error received when customization fails, possibly due to a scripting runtime
   error or invalid script parameters.
   """
   pass

class UnrecognizedHost(VimFault):
   """
   A UnrecognizedHost is thrown if the VirtualCenter server fails to
   validate the identity of the host using host-key.
   
   If a reconnect is attempted on a host and if the host-key of the host
   has changed since the last successful connection attempt,
   (might be changed by another instance of VirtualCenter), VirtualCenter
   server will fail to recognize the host.
   
   Attributes:
       hostName: Host in the VirtualCenter inventory which failed the identity
           validation.
   """
   hostName: str

class UnsharedSwapVMotionNotSupported(MigrationFeatureNotSupported):
   """
   The compute resource and virtual machine configurations for swapfile
   placement would require the virtual machine swapfile to change location for
   this VMotion; however the host does not support this.
   """
   pass

class UnsupportedGuest(InvalidVmConfig):
   """
   The specified guest operating system is not supported on the host
   that is the target of the operation.
   
   Attributes:
       unsupportedGuestOS: The guest OS ID for the unsupported guest.
   """
   unsupportedGuestOS: str


class UnsupportedVimApiVersion(VimFault):
   """
   This exception will be thrown if a client tries to connect with a unsupported version
   of the Vim API.
   """
   version: _typing.Optional[str] = None

class UnsupportedVmxLocation(VmConfigFault):
   """
   ESX 3 Server products requires the .vmx file to be stored
   on NAS or VMFS3 storage.
   
   If attempting to power on a virtual
   machine with the .vmx file stored on the service console, this
   fault will be thrown.
   """
   pass

class UnusedVirtualDiskBlocksNotScrubbed(DeviceBackingNotSupported):
   """
   The unused disk blocks of the specified virtual disk have not been
   scrubbed on the file system.
   
   Typically, this fault is returned as part of a parent fault like
   `pyVmomi.vim.fault.VmConfigIncompatibleForFaultTolerance`, indicating that the
   unused blocks of the virtual disk must be zeroed-out on the file system before
   before fault tolerance can be enabled on the associated virtual machine.
   """
   pass

class UserNotFound(VimFault):
   """
   Thrown when the request refers to a user or group name that could not
   be resolved.
   
   Attributes:
       principal: Principal value that failed lookup.
       unresolved: Flag to indicate whether or not the lookup was unsuccessful.
           
           A false value indicates that the user does not exist in the directory. A true
           value indicates that the directory could not be contacted, possibly due to a
           network error.
   """
   principal: str
   unresolved: bool

class VAppNotRunning(VmConfigFault):
   """
   A virtual machine in a vApp cannot be powered on unless the
   parent vApp is running.
   """
   pass


class VAppOperationInProgress(pyVmomi.vmodl.RuntimeFault):
   """
   This fault is thrown when an operation is attempted on a target where
   a vApp operation is already in progress.
   
   E.g. when trying to move a
   virtual machine from a vApp that is being powered on.
   """
   pass

class VAppTaskInProgress(TaskInProgress):
   """
   A specialized TaskInProgress when an operation is performed
   on a VM and it is failed due to a vApp-level operation
   is in progress.
   
   For example, while the power-on sequence is
   executed on a vApp, individual power-on's of child VMs are
   failed.
   """
   pass

class VFlashCacheHotConfigNotSupported(VmConfigFault):
   """VFlash cache hot-configuration on a VMDK is not supported."""
   pass


class VFlashModuleNotSupported(VmConfigFault):
   """
   vFlash module is not supported due to its configuration is not
   supported by the host.
   
   Attributes:
       vmName: VM name
       moduleName: The vFlash module name.
       reason: Message of reason.
       hostName: Host name
   """
   class Reason(pyVmomi.VmomiSupport.Enum):
      CacheModeNotSupported: _typing.ClassVar['VFlashModuleNotSupported.Reason'] = 'CacheModeNotSupported'
      CacheConsistencyTypeNotSupported: _typing.ClassVar['VFlashModuleNotSupported.Reason'] = 'CacheConsistencyTypeNotSupported'
      CacheBlockSizeNotSupported: _typing.ClassVar['VFlashModuleNotSupported.Reason'] = 'CacheBlockSizeNotSupported'
      CacheReservationNotSupported: _typing.ClassVar['VFlashModuleNotSupported.Reason'] = 'CacheReservationNotSupported'
      DiskSizeNotSupported: _typing.ClassVar['VFlashModuleNotSupported.Reason'] = 'DiskSizeNotSupported'

   vmName: str
   moduleName: str
   reason: str
   hostName: str

class VFlashModuleVersionIncompatible(VimFault):
   """
   The vFlash module version of the vFlash cache associated with the
   virtual disk of a VM is not compatible with the supported versions of
   the specified vFlash module on the host.
   
   Attributes:
       moduleName: The vFlash module name.
       vmRequestModuleVersion: The VM request module version.
       hostMinSupportedVerson: The minimum supported version of the specified module on the host.
       hostModuleVersion: The version of the specified module on the host.
   """
   moduleName: str
   vmRequestModuleVersion: str
   hostMinSupportedVerson: str
   hostModuleVersion: str

class VMINotSupported(DeviceNotSupported):
   """
   The virtual machine is configured to use a VMI ROM, which is not
   supported on the host.
   """
   pass

class VMOnConflictDVPort(CannotAccessNetwork):
   """
   The virtual machine is using a conflict DVPort, which is a temporary port created
   to avoid conflict with another port.
   
   Conflict DVPort cannot be moved.
   """
   pass

class VMOnVirtualIntranet(CannotAccessNetwork):
   """
   The virtual machine is using a \"virtual intranet\", a virtual network
   that exists only within a single host.
   
   If returned as part of a migration check, this
   is an error if the virtual machine is currently connected to the network and a
   warning otherwise.
   """
   pass

class VMotionAcrossNetworkNotSupported(MigrationFeatureNotSupported):
   """
   An operation on a powered-on virtual machine requests a change of
   networks, but the host does not have that capability.
   """
   pass


class VMotionInterfaceIssue(MigrationFault):
   """
   A VMotion interface has a problem.
   
   This may be an error or warning depending
   on the specific fault subclass. This is an error or warning only when
   migrating a powered-on virtual machine.
   
   Attributes:
       atSourceHost: Whether this error is for the source host.
       failedHost: The name of the host with the bad interface.
       failedHostEntity: The host with the bad interface.
   """
   atSourceHost: bool
   failedHost: str
   failedHostEntity: _typing.Optional[pyVmomi.vim.HostSystem] = None

class VMotionLinkCapacityLow(VMotionInterfaceIssue):
   """
   The VMotion interface does not have the recommended capacity to support
   VMotion.
   
   VMotion is supported on links that have a speed of at least 1000
   Mbps and are full duplex. This is a warning for migrating powered-on virtual
   machines.
   
   Attributes:
       network: Name of the network being used for the VMotion interface.
   """
   network: str

class VMotionLinkDown(VMotionInterfaceIssue):
   """
   The VMotion interface does not have any operational physical links
   associated with it.
   
   This is an error for migrating powered-on virtual
   machines.
   
   Attributes:
       network: Name of the network being used for the VMotion interface.
   """
   network: str

class VMotionNotConfigured(VMotionInterfaceIssue):
   """
   A VMotion interface is not configured (or is misconfigured) on
   either the source or destination host.
   
   This is an error only
   when migrating a powered-on virtual machine.
   """
   pass

class VMotionNotLicensed(VMotionInterfaceIssue):
   """
   VMotion is not licensed on a source or destination host.
   
   It must be licensed on both
   hosts.
   """
   pass

class VMotionNotSupported(VMotionInterfaceIssue):
   """
   The source or the destination host does not support VMotion.
   
   This is an
   error only when migrating a powered-on virtual machine.
   """
   pass

class VMotionProtocolIncompatible(MigrationFault):
   """
   VMotion protocol version incompatibility prevents VMotion from the
   virtual machine's current host to the requested destination host.
   
   (VMotion in the other direction may or may not be supported.)
   """
   pass

class VirtualDiskBlocksNotFullyProvisioned(DeviceBackingNotSupported):
   """
   The disk blocks of the specified virtual disk have not been fully
   provisioned on the file system.
   
   Typically, this fault is returned as part of a parent fault like
   `pyVmomi.vim.fault.VmConfigIncompatibleForFaultTolerance`, indicating that the
   disk blocks of the virtual disk must be fully provisioned on the file system
   before fault tolerance can be enabled on the associated virtual machine.
   """
   pass

class VirtualDiskModeNotSupported(DeviceNotSupported):
   """
   The disk mode of the specified virtual disk is not supported.
   
   Typically, this fault is returned as part of a parent fault like
   `pyVmomi.vim.fault.VmConfigIncompatibleForFaultTolerance`, indicating that the
   virtual disk's mode needs to be changed before fault tolerance can be
   enabled on the associated virtual machine.
   
   Attributes:
       mode: Disk mode that is not supported
   """
   mode: str

class VirtualEthernetCardNotSupported(DeviceNotSupported):
   """The virtual machine's virtual ethernet card is not supported."""
   pass


class VirtualHardwareVersionNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The virtual machine's virtual hardware version is not supported on the host.
   
   Attributes:
       host: The host.
   """
   hostName: str
   host: pyVmomi.vim.HostSystem


class VmAlreadyExistsInDatacenter(InvalidFolder):
   """
   Fault thrown when moving a standalone host between datacenters, and
   one or more of the virtual machines registered on the host are already
   registered to hosts in the target datacenter.
   
   Attributes:
       host: The target host.
       hostname: Name of the target host.
       vm: Virtual machines in the target datacenter which have the same
           registration information as those belonging to the target host.
   """
   host: pyVmomi.vim.HostSystem
   hostname: str
   vm: list[pyVmomi.vim.VirtualMachine] = []


class VmConfigIncompatibleForFaultTolerance(VmConfigFault):
   """
   Thrown when a virtual machine's existing or requested configuration is
   incompatible for fault tolerance.
   
   Attributes:
       fault: Fault indicating the specific configuration issue.
           
           This is typically
           a subclass of VirtualHardwareCompatibilityIssue.
   """
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmConfigIncompatibleForRecordReplay(VmConfigFault):
   """
   Deprecated: as of vSphere API 6.0Thrown when a virtual machine's existing or requested configuration is
   incompatible for record and replay.
   
   Attributes:
       fault: Fault indicating the specific configuration issue.
           
           This is typically
           a subclass of VirtualHardwareCompatibilityIssue.
   """
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
   """
   Configuration issues that can occur during operations
   related to fault tolerance protection for virtual machines.
   
   Attributes:
       reason: The reason for the failure.
       entityName: The entity name.
           
           Depending on the issue, it could
           be virtual machine or host.
       entity: The entity
   """
   class ReasonForIssue(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          haNotEnabled: HA is not enabled on the cluster
          moreThanOneSecondary: There is already a secondary virtual machine for the primary
              virtual machine
          recordReplayNotSupported: The virtual machine does not support record/replay.
              
              Vm::Capability.RecordReplaySupported is false.
          replayNotSupported: It is not possible to turn on Fault Tolerance on this powered-on VM.
              
              The support for record/replay should be enabled or Fault Tolerance
              turned on, when this VM is powered off.
          templateVm: The virtual machine is a template
          multipleVCPU: The virtual machine has more than one virtual CPU
          hostInactive: The host is not active
          ftUnsupportedHardware: The host ftSupported flag is not set because of hardware issues
          ftUnsupportedProduct: The host ftSupported flag is not set because of it is a
              VMware Server 2.0
          missingVMotionNic: No VMotion license or VMotion nic is not configured on the host
          missingFTLoggingNic: FT logging nic is not configured on the host
          thinDisk: The virtual machine has thin provisioned disks
          verifySSLCertificateFlagNotSet: The \"check host certificate\" flag is not set
          hasSnapshots: The virtual machine has one or more snapshots
          noConfig: No configuration information is available for the virtual machine
          ftSecondaryVm: The virtual machine is a fault tolerance secondary virtual machine
          hasLocalDisk: The virtual machine has one or more disks on local datastore
          esxAgentVm: The virtual machine is an ESX agent VM
          video3dEnabled: The virtual machine video device has 3D enabled
          insufficientBandwidth: FT logging nic does not have desired bandwidth
          hasNestedHVConfiguration: The host does not support fault tolerant VM with nested HV or VBS
              enabled.
          hasVFlashConfiguration: The virtual machine has a vFlash memory device or/and disks with
              vFlash cache configured.
          unsupportedProduct: VMware product installed on the host does not support
              fault tolerance
          cpuHvUnsupported: Host CPU does not support hardware virtualization
          cpuHwmmuUnsupported: Host CPU does not support hardware MMU virtualization
          cpuHvDisabled: Host CPU is compatible for replay-based FT, but hardware
              virtualization has been disabled in the BIOS.
          hasEFIFirmware: The virtual machine firmware is of type EFI
          tooManyVCPUs: The host does not support fault tolerance virtual machines
              with the specified number of virtual CPUs.
          tooMuchMemory: The host does not support fault tolerance virtual machines
              with the specified amount of memory.
          vMotionNotLicensed: No VMotion license
              
              Since: vSphere API Release 8.0.3.0
          ftNotLicensed: Host does not have proper FT license
              
              Since: vSphere API Release 8.0.3.0
          haAgentIssue: Host does not have HA agent running properly
              
              Since: vSphere API Release 8.0.3.0
          unsupportedSPBM: The VM has unsupported storage policy
              
              Since: vSphere API Release 8.0.3.0
          hasLinkedCloneDisk: The virtual machine has virtual disk in linked-clone mode
              
              Since: vSphere API Release 8.0.3.0
          unsupportedPMemHAFailOver: Virtual Machine with Pmem HA Failover is not supported
              
              Since: vSphere API Release 7.0.2.0
          unsupportedEncryptedDisk: Virtual Machine with encrypted virtual disk is not supported.
              
              Since: vSphere API Release 8.0.3.0
          ftMetroClusterNotEditable: The virtual machine does not allow to enable or disable FT Metro
              Cluster while FT is turned on.
              
              Since: vSphere API Release 8.0.3.0
          noHostGroupConfigured: Cannot turn on vSphere Fault Tolerance on a FT Metro Cluster enabled VM
              with no Host Group configured.
              
              Since: vSphere API Release 8.0.3.0
      """
      haNotEnabled: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'haNotEnabled'
      moreThanOneSecondary: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'moreThanOneSecondary'
      recordReplayNotSupported: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'recordReplayNotSupported'
      replayNotSupported: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'replayNotSupported'
      templateVm: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'templateVm'
      multipleVCPU: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'multipleVCPU'
      hostInactive: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hostInactive'
      ftUnsupportedHardware: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'ftUnsupportedHardware'
      ftUnsupportedProduct: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'ftUnsupportedProduct'
      missingVMotionNic: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'missingVMotionNic'
      missingFTLoggingNic: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'missingFTLoggingNic'
      thinDisk: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'thinDisk'
      verifySSLCertificateFlagNotSet: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'verifySSLCertificateFlagNotSet'
      hasSnapshots: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasSnapshots'
      noConfig: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'noConfig'
      ftSecondaryVm: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'ftSecondaryVm'
      hasLocalDisk: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasLocalDisk'
      esxAgentVm: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'esxAgentVm'
      video3dEnabled: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'video3dEnabled'
      hasUnsupportedDisk: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasUnsupportedDisk'
      insufficientBandwidth: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'insufficientBandwidth'
      hasNestedHVConfiguration: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasNestedHVConfiguration'
      hasVFlashConfiguration: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasVFlashConfiguration'
      unsupportedProduct: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'unsupportedProduct'
      cpuHvUnsupported: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'cpuHvDisabled'
      hasEFIFirmware: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasEFIFirmware'
      tooManyVCPUs: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'tooManyVCPUs'
      tooMuchMemory: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'tooMuchMemory'
      vMotionNotLicensed: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'vMotionNotLicensed'
      ftNotLicensed: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'ftNotLicensed'
      haAgentIssue: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'haAgentIssue'
      unsupportedSPBM: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'unsupportedSPBM'
      hasLinkedCloneDisk: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'hasLinkedCloneDisk'
      unsupportedPMemHAFailOver: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'unsupportedPMemHAFailOver'
      unsupportedEncryptedDisk: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'unsupportedEncryptedDisk'
      ftMetroClusterNotEditable: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'ftMetroClusterNotEditable'
      noHostGroupConfigured: _typing.ClassVar['VmFaultToleranceConfigIssue.ReasonForIssue'] = 'noHostGroupConfigured'

   reason: _typing.Optional[str] = None
   entityName: _typing.Optional[str] = None
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None


class VmFaultToleranceConfigIssueWrapper(VmFaultToleranceIssue):
   """
   Configuration issues that can occur during operations
   related to fault tolerance protection for virtual machines.
   
   Attributes:
       entityName: The entity name.
           
           Depending on the issue, it could
           be virtual machine or host.
       entity: The entity
       error: The nested error when the reason field is other
   """
   entityName: _typing.Optional[str] = None
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
   """
   Indicates the file backing for some device prevents fault tolerance
   protection
   
   Attributes:
       backingType: The device type of the file backing
   """
   class DeviceType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          virtualFloppy: virtual floppy
          virtualCdrom: virtual Cdrom
          virtualSerialPort: virtual serial port
          virtualParallelPort: virtual parallel port
          virtualDisk: virtual disk
      """
      virtualFloppy: _typing.ClassVar['VmFaultToleranceInvalidFileBacking.DeviceType'] = 'virtualFloppy'
      virtualCdrom: _typing.ClassVar['VmFaultToleranceInvalidFileBacking.DeviceType'] = 'virtualCdrom'
      virtualSerialPort: _typing.ClassVar['VmFaultToleranceInvalidFileBacking.DeviceType'] = 'virtualSerialPort'
      virtualParallelPort: _typing.ClassVar['VmFaultToleranceInvalidFileBacking.DeviceType'] = 'virtualParallelPort'
      virtualDisk: _typing.ClassVar['VmFaultToleranceInvalidFileBacking.DeviceType'] = 'virtualDisk'

   backingType: _typing.Optional[str] = None
   backingFilename: _typing.Optional[str] = None


class VmFaultToleranceOpIssuesList(VmFaultToleranceIssue):
   """
   Container for a list of configuration issues that can occur during
   operations related to fault tolerance protection for virtual machines.
   
   Attributes:
       errors: A list of faults representing errors
   """
   errors: list[pyVmomi.vmodl.MethodFault] = []
   warnings: list[pyVmomi.vmodl.MethodFault] = []


class VmFaultToleranceTooManyFtVcpusOnHost(InsufficientResourcesFault):
   """
   This fault is returned when a host has more than the recommended number of
   Fault Tolerance vCPUs running on it.
   
   Attributes:
       hostName: The name of the host
       maxNumFtVcpus: The recommended number of FT protected vCPUs on a host.
   """
   hostName: _typing.Optional[str] = None
   maxNumFtVcpus: int


class VmFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   """
   This fault is returned when a host has more than the recommended number of
   Fault Tolerance VMs running on it.
   
   Attributes:
       maxNumFtVms: The recommended number of Fault Tolerance VMs running on the host.
   """
   hostName: _typing.Optional[str] = None
   maxNumFtVms: int

class VmHostAffinityRuleViolation(VmConfigFault):
   """
   The virtual machine if powered on or VMotioned, would violate a VM-Host affinity rule.
   
   Attributes:
       vmName: The vm that can not be powered on or VMotioned without violating a rule.
       hostName: The host that the virtual machine can not be powered on without violating a rule.
   """
   vmName: str
   hostName: str


class VmLimitLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A VmLimitLicense fault is thrown if powering on the virtual
   machine would exceed the maximum number of running virtual
   machines allowed.
   
   Attributes:
       limit: The maximum number of running virtual machines
           limit.
   """
   limit: int

class VmMetadataManagerFault(VimFault):
   """
   This fault indicates that some error has occurred during the processing of
   of a MetadataManager operation.
   
   This may be subclassed by a more specific
   fault.
   """
   pass

class VmMonitorIncompatibleForFaultTolerance(VimFault):
   """
   Thrown when turning on Fault Tolerance protection on a running virtual machine
   if the virtual machine is running in a monitor mode that is incompatible.
   """
   pass

class VmPowerOnDisabled(InvalidState):
   """
   This exception is thrown if the power-on of a virtual machine is attempted
   when the operation is disabled on the host
   """
   pass


class VmSmpFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   """
   This fault is returned when a host has more than the recommended number of
   SMP Fault Tolerance VMs running on it.
   
   Attributes:
       hostName: The name of the host
       maxNumSmpFtVms: The recommended number of SMP-Fault Tolerance VMs running on the host.
   """
   hostName: _typing.Optional[str] = None
   maxNumSmpFtVms: int

class VmValidateMaxDevice(VimFault):
   """
   Attributes:
       device: The device
       max: max count for the device
       count: number of devices found in vim.vm.ConfigSpec
   """
   device: str
   max: int
   count: int


class VmWwnConflict(InvalidVmConfig):
   """
   Thrown if a user attempts to assign a
   WWN that is currently being used by other virtual machine or host.
   
   Attributes:
       vm: The virtual machine that is using the same WWN.
       host: The host that is using the same WWN.
       name: The name of the virtual machine/host that is using the same WWN.
       wwn: The WWN that is in conflict.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   name: _typing.Optional[str] = None
   wwn: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VmfsMountFault(HostConfigFault):
   """
   This is a base class for all VMFS volume mount related faults.
   
   Attributes:
       uuid: Vmfs volume uuid
   """
   uuid: str

class VmfsAlreadyMounted(VmfsMountFault):
   """
   A VmfsAlreadyMounted fault indicates that VMFS volume with same UUID
   is already mounted on the host.
   """
   pass

class VmfsAmbiguousMount(VmfsMountFault):
   """
   An 'VmfsAmbiguousMount' fault occurs when ESX is unable to resolve the
   extents of a VMFS volume unambiguously.
   
   This is thrown only when a VMFS
   volume has multiple extents and multiple copies of VMFS volumes are available.
   VMFS layer will not be able to determine how to re-construct the VMFS
   volume as multiple choices are available.
   """
   pass

class VmotionInterfaceNotEnabled(HostPowerOpFailed):
   """
   This fault is thrown when the Vmotion Interface on this host is not enabled.
   
   The Vmotion Interface is needed for waking up the host from standby mode.
   """
   pass

class VolumeEditorError(CustomizationFault):
   """
   An error occurred in the Open Source Components applications during
   volume editing.
   
   Possibly caused by an incompatible cygwin version
   installed in the VirtualCenter server.
   """
   pass


class VramLimitLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   """
   A VramLimitLicense fault is thrown if executing an operation
   would result in exceeding maximum allowed vRAM amount.
   
   For example, this could happen when powering on a VM,
   hot-plugging memory into a running VMm, etc.
   
   Attributes:
       limit: The maximum allowed vRAM amount.
   """
   limit: int

class VsanClusterUuidMismatch(CannotMoveVsanEnabledHost):
   """
   Fault thrown for the case that an attempt is made to move a host which
   is enabled for VSAN into a `pyVmomi.vim.ClusterComputeResource` whose
   VSAN cluster UUID does not match.
   
   See Also: `pyVmomi.vim.fault.CannotMoveVsanEnabledHost`
   
   Attributes:
       hostClusterUuid: The VSAN cluster UUID in use by the host at hand.
       destinationClusterUuid: The VSAN cluster UUID in use by the destination
           `pyVmomi.vim.ClusterComputeResource`.
   """
   hostClusterUuid: str
   destinationClusterUuid: str

class VsanIncompatibleDiskMapping(VsanDiskFault):
   """
   Fault used for the add operation which will result in incompatible
   disk mappings.
   
   See Also: `pyVmomi.vim.host.VsanSystem.initializeDisks`
   """
   pass


class VsanNodeNotMaster(VimFault):
   """
   Fault means that the operation attempted is only possible on a vSAN
   performance collection master node, and that this node was not in that state
   at the point of the API call.
   
   Information about the identity of the master
   is provided for convenience.
   
   Attributes:
       vsanMasterUuid: The vSAN Node UUID of the Master.
           
           May be itself, in which case this means that the
           node is CMMDS master, but can't act in the master role for the operation in question.
           See other fields for possible reasons.
       cmmdsMasterButNotStatsMaster: If true, it means this node is CMMDS master, but is currently not Stats master.
           
           This
           could be because it is in the process of becoming stats master, or because it failed
           to become stats master, e.g. due to the object being inaccessible.
   """
   vsanMasterUuid: _typing.Optional[str] = None
   cmmdsMasterButNotStatsMaster: _typing.Optional[bool] = None

class VsanSslVerifyCertFault(SSLVerifyFault):
   """
   Base class for all faults related to the NotificataionSystem.
   
   Attributes:
       cert: The remote host's single x509 certificate encoded in PEM format.
   """
   cert: str

class VspanDestPortConflict(DvsFault):
   """
   Thrown if a dvPort is used as destination in multiple Distributed Port Mirroring sessions.
   
   Attributes:
       vspanSessionKey1: The key of the Distributed Port Mirroring session whose destination ports include a port
           that is also used as destination ports of other Distributed Port Mirroring sessions
       vspanSessionKey2: The key of the Distributed Port Mirroring session whose destination ports include a port
           that is also used as destination ports of other Distributed Port Mirroring sessions
       portKey: The key of the the port that is used as destination in multiple Distributed Port Mirroring sessions
   """
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortConflict(DvsFault):
   """
   Thrown if a DistributedVirtualPort appears in both the transmitted source and destination
   ports of any Distributed Port Mirroring session.
   
   Attributes:
       vspanSessionKey1: The key of the Distributed Port Mirroring session that is in conflict
       vspanSessionKey2: The key of the Distributed Port Mirroring session that is in conflict
       portKey: The key of the port that is both the transmitted source and destination.
   """
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortMoveFault(DvsFault):
   """
   Thrown when moving a port used as tranmistted source or destination ports in vspan
   session to a promiscuous portgroup if this operation may change
   the non-promiscuous port to promiscuous mode.
   
   Attributes:
       srcPortgroupName: The key of the source portgroup.
       destPortgroupName: The key of the dest portgroup.
       portKey: The key of the port.
   """
   srcPortgroupName: str
   destPortgroupName: str
   portKey: str

class VspanPortPromiscChangeFault(DvsFault):
   """
   Thrown when changing a non-promiscuous port used as tranmistted source or dest
   ports in Distributed Port Mirroring session to promiscuous mode.
   
   Attributes:
       portKey: The key of the port.
   """
   portKey: str

class VspanPortgroupPromiscChangeFault(DvsFault):
   """
   Thrown when changing a non-promiscuous portgroup to promiscuous mode if any port
   in this portgroup is used as transmitted source or dest ports in vspan
   session.
   
   Attributes:
       portgroupName: The key of the port.
   """
   portgroupName: str

class VspanPortgroupTypeChangeFault(DvsFault):
   """
   Thrown when changing a portgroup from static/dynamic binding to
   ephemeral(no binding) if any ports in this portgroup participate in
   Distributed Port Mirroring session.
   
   Attributes:
       portgroupName: The name of the portgroup.
   """
   portgroupName: str

class VspanPromiscuousPortNotSupported(DvsFault):
   """
   Thrown if a promiscuous port appears in transmitted source or destination
   ports of any Distributed Port Mirroring session.
   
   Attributes:
       vspanSessionKey: The key of the Distributed Port Mirroring session in which a promiscuous port is used as
           transmitted source or destination ports.
       portKey: The key of the promiscuous port that appears in transmitted
           source or destination ports.
   """
   vspanSessionKey: str
   portKey: str

class VspanSameSessionPortConflict(DvsFault):
   """
   Thrown if a dvPort appears in both the source and destination
   ports of the same Distributed Port Mirroring session.
   
   Attributes:
       vspanSessionKey: The key of the Distributed Port Mirroring session in which a dvPort appears in both the source and destination ports
       portKey: The key of the port that appears in both the source and
           destination ports of the same Distributed Port Mirroring session.
   """
   vspanSessionKey: str
   portKey: str

class WakeOnLanNotSupported(VirtualHardwareCompatibilityIssue):
   """
   The virtual machine and at least one of its virtual NICs are configured to
   use Wake-on-LAN, but the host does not support Wake-on-LAN for the
   virtual machine's selected guest OS.
   """
   pass

class WakeOnLanNotSupportedByVmotionNIC(HostPowerOpFailed):
   """This fault is thrown when Wake-on-LAN isn't supported by the Vmotion NIC on the host."""
   pass


class WillLoseHAProtection(MigrationFault):
   """
   This fault is reported when the execution of a storage vmotion or
   relocate operation would impact vSphere HA's ability to
   restart a VM.
   
   For storage vmotion, this fault
   is reported when HA protection will be lost after the vmotion
   completes. Consequently, HA would not restart the VM if it
   subsequently failed. For relocate, relocate is not supported on
   VMs that failed before the operation is attempted and are in the
   process of being restarted at the time the operation is performed.
   
   Attributes:
       resolution: The steps the user can take to restore protection if the
           the operation is performed.
           
           Values come from
           `pyVmomi.vim.fault.WillLoseHAProtection.Resolution`.
   """
   class Resolution(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          svmotion: storage vmotion resolution
          relocate: relocate resolution
      """
      svmotion: _typing.ClassVar['WillLoseHAProtection.Resolution'] = 'svmotion'
      relocate: _typing.ClassVar['WillLoseHAProtection.Resolution'] = 'relocate'

   resolution: str

class WillModifyConfigCpuRequirements(MigrationFault):
   """
   A virtual machine's total CPU feature requirements are determined by
   overlaying the requirements specified in its configuration (if any) on top
   of the requirements specified in the descriptor for its guest OS.
   
   It is
   therefore possible for a host change to implicitly change a virtual
   machine's CPU feature requirements. The guest OS descriptor may have
   different requirements on the new host. Or, if the virtual machine
   currently specifies requirements in its configuration, those requirements
   will be lost if the new host does not support this.
   
   This fault indicates that the virtual machine's CPU feature requirements
   would change because of a migration, and also that the destination host
   does support storing CPU feature requirements in the virtual machine's
   configuration. (If the destination host does not support such an action,
   `pyVmomi.vim.fault.CannotModifyConfigCpuRequirements` is used instead of this fault.)
   
   This is a warning to notify the user that the migration process will
   adjust the virtual machine's configuration so that it will be operating
   under an unchanged set of CPU feature requirements on its new host. If the
   user wishes to expose the different guest OS requirements of the new host,
   the user will need to edit the virtual machine's configuration after the
   migration.
   """
   pass

class WillResetSnapshotDirectory(MigrationFault):
   """
   This fault is reported when the execution of a storage vmotion or
   relocate operation would reset the snapshotDirectory settings
   to its default value (VM's home/config directory).
   """
   pass

class WipeDiskFault(VimFault):
   """
   This exception is thrown when VirtualMachine.wipeDisk
   encounters an error
   """
   pass
