# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import check as check
from . import customization as customization
from . import device as device
from . import guest as guest
from . import replication as replication

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.ext
import pyVmomi.vim.host
import pyVmomi.vim.net
import pyVmomi.vim.option
import pyVmomi.vim.vApp
import pyVmomi.vim.vm.customization
import pyVmomi.vim.vm.device
import pyVmomi.vim.vm.guest
import pyVmomi.vim.vm.replication



class AffinityInfo(pyVmomi.vmodl.DynamicData):
   """
   Specification of scheduling affinity.
   
   Scheduling affinity is used for explicitly specifying which
   processors or NUMA nodes may be used by a virtual machine.
   
   Attributes:
       affinitySet: List of nodes (processors for CPU, NUMA nodes for memory) that
           may be used by the virtual machine.
           
           If the array is empty when
           modifying the affinity setting, then any existing affinity is removed.
   """
   affinitySet: list[int] = []


class BaseIndependentFilterSpec(pyVmomi.vmodl.DynamicData):
   """
   The BaseIndependentFilterSpec is base class for two different types
   of independent filter specs `pyVmomi.vim.vm.IndependentFilterSpec`
   and `pyVmomi.vim.vm.EmptyIndependentFilterSpec` which are used to specify
   independent filters to be attached/removed on VMs virtual disk.
   
   Since: vSphere API Release 7.0.2.1
   """
   pass


class BootOptions(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vm.BootOptions` data object defines the boot-time
   behavior of a virtual machine.
   
   You can use the delay options to specify a time interval
   during which you can enter the virtual machine BIOS setup.
   These options provide a solution for the situation that occurs
   when the console attaches to the virtual machine after
   the boot sequence has passed the BIOS setup entry point.
   
   Attributes:
       bootDelay: Delay in milliseconds before starting the boot sequence.
           
           The boot delay specifies a time interval between virtual machine
           power on or restart and the beginning of the boot sequence.
       enterBIOSSetup: If set to `true`, the virtual machine
           automatically enters BIOS setup the next time it boots.
           
           The virtual machine resets this flag to `false`
           so that subsequent boots proceed normally.
       efiSecureBootEnabled: If set to `true`, the virtual machine's firmware will
           perform signature checks of any EFI images loaded during startup, and
           will refuse to start any images which do not pass those signature
           checks.
           
           When creating a new VM:
           \\- If vim.vm.FlagInfo.vbsEnabled is set to `true`,
           and this flag is set to `false` error is returned.
           \\- If this flag is unset and vim.vm.FlagInfo.vbsEnabled is set to
           `true`, the value of this flag is set to `true`.
       bootRetryEnabled: If set to `true`, a virtual machine that fails
           to boot will try again after the `pyVmomi.vim.vm.BootOptions.bootRetryDelay`
           time period has expired.
           
           When `false`,
           the virtual machine waits indefinitely for you to initiate
           boot retry.
       bootRetryDelay: Delay in milliseconds before a boot retry.
           
           The boot retry delay
           specifies a time interval between virtual machine boot failure
           and the subsequent attempt to boot again. The virtual machine
           uses this value only if `pyVmomi.vim.vm.BootOptions.bootRetryEnabled` is true.
       bootOrder: Boot order.
           
           Listed devices are used for booting. After list
           is exhausted, default BIOS boot device algorithm is used for
           booting.
           Note that order of the entries in the list is important:
           device listed first is used for boot first, if that one
           fails second entry is used, and so on.
           Platform may have some internal limit on the number of devices
           it supports. If bootable device is not reached before platform's
           limit is hit, boot will fail. At least single entry is supported
           by all products supporting boot order settings.
       networkBootProtocol: Protocol to attempt during PXE network boot or NetBoot.
   """
   class NetworkBootProtocolType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          ipv4: PXE (or Apple NetBoot) over IPv4.
              
              The default.
          ipv6: PXE over IPv6.
              
              Only meaningful for EFI virtual machines.
      """
      ipv4: _typing.ClassVar['BootOptions.NetworkBootProtocolType'] = 'ipv4'
      ipv6: _typing.ClassVar['BootOptions.NetworkBootProtocolType'] = 'ipv6'

   class BootableDevice(pyVmomi.vmodl.DynamicData):
      """Bootable device."""
      pass

   class BootableDiskDevice(BootOptions.BootableDevice):
      """
      Bootable disk.
      
      Attributes:
          deviceKey: `pyVmomi.vim.vm.device.VirtualDevice.key`
              property of the bootable harddisk.
      """
      deviceKey: int

   class BootableEthernetDevice(BootOptions.BootableDevice):
      """
      Bootable ethernet adapter.
      
      PXE boot is attempted from the device.
      
      Attributes:
          deviceKey: `pyVmomi.vim.vm.device.VirtualDevice.key`
              property of the bootable ethernet adapter.
      """
      deviceKey: int

   class BootableFloppyDevice(BootOptions.BootableDevice):
      """Bootable floppy disk."""
      pass

   class BootableCdromDevice(BootOptions.BootableDevice):
      """
      Bootable CDROM.
      
      First CDROM with bootable media found is used.
      """
      pass

   bootDelay: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   enterBIOSSetup: _typing.Optional[bool] = None
   efiSecureBootEnabled: _typing.Optional[bool] = None
   bootRetryEnabled: _typing.Optional[bool] = None
   bootRetryDelay: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bootOrder: list[BootOptions.BootableDevice] = []
   networkBootProtocol: _typing.Optional[str] = None


class Capability(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains information about the
   operation/capabilities of a virtual machine
   
   Attributes:
       snapshotOperationsSupported: Indicates whether or not a virtual machine supports snapshot operations.
       multipleSnapshotsSupported: Indicates whether or not a virtual machine supports multiple snapshots.
           
           This value is not set when the virtual machine is unavailable, for instance,
           when it is being created or deleted.
       snapshotConfigSupported: Indicates whether or not a virtual machine supports snapshot config.
       poweredOffSnapshotsSupported: Indicates whether or not a virtual machine supports snapshot operations in
           poweredOff state.
           
           This flag doesn't affect vim.VirtualMachine.GetSnapshot,
           which is always supported.
       memorySnapshotsSupported: Indicates whether or not a virtual machine supports memory snapshots.
       revertToSnapshotSupported: Indicates whether or not a virtual machine supports reverting to a snapshot.
       quiescedSnapshotsSupported: Indicates whether or not a virtual machine supports quiesced snapshots.
       disableSnapshotsSupported: Indicates whether or not snapshots can be disabled.
       lockSnapshotsSupported: Indicates whether or not the snapshot tree can be locked.
       consolePreferencesSupported: Indicates whether console preferences can be set for this virtual machine.
       cpuFeatureMaskSupported: Indicates whether CPU feature requirements masks can be set for this
           virtual machine.
           
           Masking for hardware version 9 and newer virtual
           machines is controlled by `pyVmomi.vim.vm.Capability.featureRequirementSupported`.
       s1AcpiManagementSupported: Indicates whether or not a virtual machine supports ACPI S1 settings management.
       settingScreenResolutionSupported: Indicates whether of not this virtual machine supports
           setting the screen resolution of the console window.
           
           This capability depends on the guest operating system
           configured for this virtual machine.
       toolsAutoUpdateSupported: Supports tools auto-update.
       vmNpivWwnSupported: Supports virtual machine NPIV WWN.
       npivWwnOnNonRdmVmSupported: Supports assigning NPIV WWN to virtual machines that don't have RDM disks.
       vmNpivWwnDisableSupported: Indicates whether the NPIV disabling operation is supported the virtual machine.
       vmNpivWwnUpdateSupported: Indicates whether the update of NPIV WWNs are supported on the virtual machine.
       swapPlacementSupported: Flag indicating whether the virtual machine has a configurable
           `pyVmomi.vim.vm.ConfigInfo.swapPlacement`.
       toolsSyncTimeSupported: Indicates whether asking tools to sync time with the host is supported.
       virtualMmuUsageSupported: Indicates whether or not the use of nested page table hardware support
           can be explicitly set.
       diskSharesSupported: Indicates whether resource settings for disks can be
           applied to this virtual machine.
       bootOptionsSupported: Indicates whether boot options can be configured
           for this virtual machine.
       bootRetryOptionsSupported: Indicates whether automatic boot retry can be
           configured for this virtual machine.
       settingVideoRamSizeSupported: Flag indicating whether the video ram size of this virtual machine
           can be configured.
       settingDisplayTopologySupported: Indicates whether of not this virtual machine supports
           setting the display topology of the console window.
           
           This capability depends on the guest operating system
           configured for this virtual machine.
       recordReplaySupported: Indicates whether record and replay functionality is supported on this
           virtual machine.
       changeTrackingSupported: Indicates that change tracking is supported for virtual disks of this
           virtual machine.
           
           However, even if change tracking is supported, it might
           not be available for all disks of the virtual machine. For example,
           passthru raw disk mappings or disks backed by any Ver1BackingInfo cannot
           be tracked.
       multipleCoresPerSocketSupported: Indicates whether multiple virtual cores per socket is supported on this VM.
       hostBasedReplicationSupported: Indicates that host based replication is supported on this virtual
           machine.
           
           However, even if host based replication is supported,
           it might not be available for all disk types. For example, passthru
           raw disk mappings can not be replicated.
       guestAutoLockSupported: Indicates whether features like guest OS auto-lock and MKS connection
           controls are supported for this virtual machine.
       memoryReservationLockSupported: Indicates whether
           `pyVmomi.vim.vm.ConfigInfo.memoryReservationLockedToMax`
           may be set to true for this virtual machine.
       featureRequirementSupported: Indicates whether featureRequirement feature is supported.
       poweredOnMonitorTypeChangeSupported: Indicates whether a monitor type change is supported while this virtual
           machine is in the poweredOn state.
       seSparseDiskSupported: Indicates whether this virtual machine supports the Flex-SE
           (space-efficient, sparse) format for virtual disks.
       nestedHVSupported: Indicates whether this virtual machine supports nested hardware-assisted
           virtualization.
       vPMCSupported: Indicates whether this virtual machine supports virtualized CPU performance
           counters.
       secureBootSupported: Indicates whether secureBoot is supported for this virtual machine.
       perVmEvcSupported: Indicates whether this virtual machine supports Per-VM EVC mode.
       virtualMmuUsageIgnored: Indicates that `pyVmomi.vim.vm.FlagInfo.virtualMmuUsage` is
           ignored by this virtual machine, always operating as if \"on\" was selected.
       virtualExecUsageIgnored: Indicates that `pyVmomi.vim.vm.FlagInfo.virtualExecUsage` is
           ignored by this virtual machine, always operating as if \"hvOn\" was selected.
       diskOnlySnapshotOnSuspendedVMSupported: Indicates whether this virtual machine supports creating disk-only snapshots
           in suspended state.
           
           If this capability is not set, the snapshot of a
           virtual machine in suspended state will always include memory.
       suspendToMemorySupported: Indicates whether this virtual machine supports suspending to memory.
           
           Since: vSphere API Release 7.0.2.0
       toolsSyncTimeAllowSupported: Indicates support for allowing or disallowing all tools time
           sync with host.
           
           Since: vSphere API Release 7.0.1.0
       sevSupported: Indicates support for AMD-SEV (Secure Encrypted Virtualization).
           
           SEV is
           supported when set to true, and unsupported otherwise.
           
           Since: vSphere API Release 7.0.1.0
       pmemFailoverSupported: Indicates support for failover to a different host on VM's with pmem.
           
           Failover is supported when set to true, and unsupported otherwise.
           
           Since: vSphere API Release 7.0.2.0
       requireSgxAttestationSupported: Whether the VM supports requiring SGX remote attestation.
           
           Since: vSphere API Release 8.0.0.1
       changeModeDisksSupported: Indicates support for change mode on virtual disks
           
           Since: vSphere API Release 8.0.0.1
       vendorDeviceGroupSupported: Indicates support for Vendor Device Groups
           
           Since: vSphere API Release 8.0.1.0
       sevSnpSupported: Indicates support for AMD-SEV-SNP (Secure Encrypted Virtualization Secure
           Nested Paging).
           
           SEV-SNP is supported when set to true, and unsupported
           otherwise.
           
           Since: vSphere API Release 9.0.0.0
       tdxSupported: Indicates support for INTEL-TDX (Trusted Domain Extensions).
           
           TDX is
           supported when set to true, and unsupported otherwise.
           
           Since: vSphere API Release 9.0.0.0
       ehvSecureBootSupported: Indicates support for UEFI Secure Boot in EHV VMs.
           
           It is supported when
           set to true, and unsupported otherwise.
           
           Since: vSphere API Release 9.1.0.0
   """
   snapshotOperationsSupported: bool
   multipleSnapshotsSupported: bool
   snapshotConfigSupported: bool
   poweredOffSnapshotsSupported: bool
   memorySnapshotsSupported: bool
   revertToSnapshotSupported: bool
   quiescedSnapshotsSupported: bool
   disableSnapshotsSupported: bool
   lockSnapshotsSupported: bool
   consolePreferencesSupported: bool
   cpuFeatureMaskSupported: bool
   s1AcpiManagementSupported: bool
   settingScreenResolutionSupported: bool
   toolsAutoUpdateSupported: bool
   vmNpivWwnSupported: bool
   npivWwnOnNonRdmVmSupported: bool
   vmNpivWwnDisableSupported: bool
   vmNpivWwnUpdateSupported: bool
   swapPlacementSupported: bool
   toolsSyncTimeSupported: bool
   virtualMmuUsageSupported: bool
   diskSharesSupported: bool
   bootOptionsSupported: bool
   bootRetryOptionsSupported: bool
   settingVideoRamSizeSupported: bool
   settingDisplayTopologySupported: bool
   recordReplaySupported: bool
   changeTrackingSupported: bool
   multipleCoresPerSocketSupported: bool
   hostBasedReplicationSupported: bool
   guestAutoLockSupported: bool
   memoryReservationLockSupported: bool
   featureRequirementSupported: bool
   poweredOnMonitorTypeChangeSupported: bool
   seSparseDiskSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   secureBootSupported: _typing.Optional[bool] = None
   perVmEvcSupported: _typing.Optional[bool] = None
   virtualMmuUsageIgnored: _typing.Optional[bool] = None
   virtualExecUsageIgnored: _typing.Optional[bool] = None
   diskOnlySnapshotOnSuspendedVMSupported: _typing.Optional[bool] = None
   suspendToMemorySupported: _typing.Optional[bool] = None
   toolsSyncTimeAllowSupported: _typing.Optional[bool] = None
   sevSupported: _typing.Optional[bool] = None
   pmemFailoverSupported: _typing.Optional[bool] = None
   requireSgxAttestationSupported: _typing.Optional[bool] = None
   changeModeDisksSupported: _typing.Optional[bool] = None
   vendorDeviceGroupSupported: _typing.Optional[bool] = None
   sevSnpSupported: _typing.Optional[bool] = None
   tdxSupported: _typing.Optional[bool] = None
   ehvSecureBootSupported: _typing.Optional[bool] = None


class TargetInfo(pyVmomi.vmodl.DynamicData):
   """
   The TargetInfo specified a value that can be used in the device backings to
   connect the virtual machine to a physical (or logical) host device.
   
   Attributes:
       name: The identification of the endpoint on the host.
           
           The format of this depends
           on the kind of virtual device this endpoints is used for. For example,
           for a VirtualEthernetCard this would be a networkname, and for a VirtualCDROM
           it would be a device name.
       configurationTag: List of configurations that this device is available for.
           
           This is only filled
           out if more than one configuration is requested.
   """
   class ConfigurationTag(pyVmomi.VmomiSupport.Enum):
      """
      Describes how widely the endpoint is available in a cluster.
      
      Note that these fields are not necessarily mutual-exclusive.
      
      Attributes:
          compliant: Indicates that this device is part of the cluster compliant
              specification.
          clusterWide: Indicates that this is available for all hosts in the cluster.
      """
      compliant: _typing.ClassVar['TargetInfo.ConfigurationTag'] = 'compliant'
      clusterWide: _typing.ClassVar['TargetInfo.ConfigurationTag'] = 'clusterWide'

   name: str
   configurationTag: list[str] = []


class CdromInfo(TargetInfo):
   """
   CdromInfo class contains information about a physical CD-ROM drive on the host.
   
   Attributes:
       description: Description of the physical device.
           
           This is set only by the server.
   """
   description: _typing.Optional[str] = None


class CertThumbprint(pyVmomi.vmodl.DynamicData):
   """
   Describes a single certificate thumbprint that can be used to verify
   the identity of the host before connecting to a running virtual machine.
   
   Attributes:
       thumbprint: The thumbprint of the certificate of the host to which we are
           connecting.
       hashAlgorithm: The hash algorithm used to generate the thumbprint.
           
           `pyVmomi.vim.vm.CertThumbprint.HashAlgorithm` lists the set of supported values.
   
   Since: vSphere API Release 7.0.3.1
   """
   class HashAlgorithm(pyVmomi.VmomiSupport.Enum):
      """
      Set of supported hash algorithms for thumbprints.
      
      Attributes:
          sha256: SHA256
      
      Since: vSphere API Release 7.0.3.1
      """
      sha256: _typing.ClassVar['CertThumbprint.HashAlgorithm'] = 'sha256'

   thumbprint: str
   hashAlgorithm: _typing.Optional[str] = None


class CloneSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for a virtual machine cloning operation.
   
   Attributes:
       location: A type of RelocateSpec that specifies the location of resources the
           newly cloned virtual machine will use.
           
           The location specifies:
           - A datastore where the virtual machine will be located on physical
             storage.
             This is always provided because it indicates where the newly
             created clone will be copied.
           - a resource pool and optionally a host. The resource pool
             determines what compute resources will be available to the clone
             and the host indicates which machine will host the clone.
       template: Specifies whether or not the new virtual machine should be marked as a
           template.
       config: An optional specification of changes to the virtual hardware.
           
           For example, this can be used to, (but not limited to) reconfigure the
           networks the virtual switches are hooked up to in the cloned virtual
           machine.
           
           Use `pyVmomi.vim.vm.RelocateSpec.deviceChange` in
           `pyVmomi.vim.vm.CloneSpec.location`
           for specifying any virtual device changes for disks and networks.
           
           Use `pyVmomi.vim.vm.RelocateSpec.tagSpecs` in
           `pyVmomi.vim.vm.CloneSpec.location`
           for specifying tags to be associated with the cloned virtual machine.
       customization: An optional guest operating system customization specification.
           
           This value is ignored if a template is being created.
       powerOn: Specifies whether or not the new VirtualMachine should be powered on
           after creation.
           
           As part of a customization, this flag is normally set
           to true, since the first power-on operation completes the customization
           process. This flag is ignored if a template is being created.
       snapshot: Snapshot reference from which to base the clone.
           
           If this parameter is set, the clone is based off of the snapshot
           point. This means that the newly created virtual machine will
           have the same configuration as the virtual machine at the time
           the snapshot was taken.
           
           If this property is not set then the clone is based off of the
           virtual machine's current configuration.
           
           Setting this is only supported if the host this virtual machine
           is currently residing on
           `pyVmomi.vim.host.Capability.cloneFromSnapshotSupported`. Such support does not need to
           exist on the destination host for the clone.
           
           Setting this is only supported if the virtual machine supports
           reporting snapshot configuration information. See `pyVmomi.vim.vm.Capability.snapshotConfigSupported`. Such support does not need
           to exist on the destination host for the clone.
       memory: Flag indicating whether to retain a copy of the source virtual machine's
           memory state in the clone.
           
           Retaining the memory state during
           clone results in a clone in suspended state with all network adapters
           removed to avoid network conflicts, except those with a
           VirtualEthernetCard.addressType of \"manual\".
           Users of this flag should take special care so that, when adding a network
           adapter back to the clone, the VM is not resumed on the same VM network
           as the source VM, or else MAC address conflicts could occur.
           When cloning between two hosts with different CPUs outside an EVC cluster,
           users of this flag should be aware that vCenter does not verify
           CPU compatibility between the clone's memory state and the target host
           prior to the clone operation, so the clone may fail to resume
           until it is migrated to a host with a compatible CPU.
           
           This flag is ignored if the snapshot parameter is unset. This flag
           only applies for a snapshot taken on a running or suspended
           virtual machine with the 'memory' parameter set to true, because otherwise
           the snapshot has no memory state. This flag defaults to false.
       tpmProvisionPolicy: Provisioning policy for virtual TPM devices during VM clone operations.
           
           The list of supported values is defined in `pyVmomi.vim.vm.CloneSpec.TpmProvisionPolicy`.
           
           If unset - depending on the virtual TPM operating mode:
           - For a non read-only virtual TPM a globally defined policy is
             used, which by default is set to 'copy'.
           - For a read-only virtual TPM 'copy' is used, if `pyVmomi.vim.vm.CloneSpec.template`
             is specified as 'true', otherwise 'replace' is used.
           
           Since: vSphere API Release 8.0.0.1
   """
   class TpmProvisionPolicy(pyVmomi.VmomiSupport.Enum):
      """
      TPM provisioning policies used when cloning a VM with a virtual TPM
      device.
      
      Attributes:
          copy: The virtual TPM is copied.
              
              The virtual machine clone will have access
              to the original virtual machine's TPM secrets.
          replace: The virtual TPM is replaced with a new one.
              
              The virtual machine clone
              will not have access to the original virtual machine's TPM secrets.
              
              If the virtual TPM operates in read-only mode
              (`vim.vm.device.VirtualTPM.readOnly`), the clone virtual machine
              will be configured with a regularly operating (non read-only) virtual
              TPM.
      
      Since: vSphere API Release 8.0.0.1
      """
      copy: _typing.ClassVar['CloneSpec.TpmProvisionPolicy'] = 'copy'
      replace: _typing.ClassVar['CloneSpec.TpmProvisionPolicy'] = 'replace'

   location: RelocateSpec
   template: bool
   config: _typing.Optional[ConfigSpec] = None
   customization: _typing.Optional[pyVmomi.vim.vm.customization.Specification] = None
   powerOn: bool
   snapshot: _typing.Optional[Snapshot] = None
   memory: _typing.Optional[bool] = None
   tpmProvisionPolicy: _typing.Optional[str] = None


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The ConfigInfo data object type encapsulates the configuration settings and
   virtual hardware for a virtual machine.
   
   This type holds all the information
   that is present in the .vmx configuration file for the virtual machine.
   
   Attributes:
       changeVersion: The changeVersion is a unique identifier for a given version
           of the configuration.
           
           Each change to the configuration
           updates this value. This is typically implemented as an ever
           increasing count or a time-stamp. However, a client should
           always treat this as an opaque string.
       modified: Last time a virtual machine's configuration was modified.
       name: Display name of the virtual machine.
           
           Any / (slash), \\ (backslash), character used in this
           name element is escaped. Similarly, any % (percent) character used in
           this name element is escaped, unless it is used to start an escape
           sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or
           %5c, and a percent is escaped as %25.
       guestFullName: This is the full name of the guest operating system for the virtual machine.
           
           For example: Windows 2000 Professional.
       version: The version string for this virtual machine.
       uuid: 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string
           in \"12345678-abcd-1234-cdef-123456789abc\" format.
       createDate: Time the virtual machine's configuration was created.
       instanceUuid: VirtualCenter-specific 128-bit UUID of a virtual machine, represented
           as a hexadecimal string.
           
           This identifier is used by VirtualCenter to
           uniquely identify all virtual machine instances, including those that
           may share the same SMBIOS UUID.
       npivNodeWorldWideName: A 64-bit node WWN (World Wide Name).
           
           These WWNs are paired with the
           `pyVmomi.vim.vm.ConfigInfo.npivPortWorldWideName` to be used by the NPIV VPORTs instantiated for the
           virtual machine on the physical HBAs of the host. A pair of node and port WWNs
           serves as a unique identifier in accessing a LUN, so that it can be monitored or
           controlled by the storage administrator.
           
           If this property contains a single node WWN, the same node WWN is used to pair
           with all port WWNs listed in `pyVmomi.vim.vm.ConfigInfo.npivPortWorldWideName`. If this property or
           `pyVmomi.vim.vm.ConfigInfo.npivPortWorldWideName` is empty or unset, NPIV WWN is disabled for the
           virtual machine.
       npivPortWorldWideName: A 64-bit port WWN (World Wide Name).
           
           For detail description on WWN, see
           `pyVmomi.vim.vm.ConfigInfo.npivNodeWorldWideName`.
       npivWorldWideNameType: The source that provides/generates the assigned WWNs.
       npivDesiredNodeWwns: The NPIV node WWNs to be extended from the original list of WWN numbers.
           
           This
           property should be set to desired number which is an aggregate of existing
           plus new numbers. Desired Node WWNs should always be greater than the existing
           number of node WWNs
       npivDesiredPortWwns: The NPIV port WWNs to be extended from the original list of WWN numbers.
           
           This
           property should be set to desired number which is an aggregate of existing
           plus new numbers. Desired Node WWNs should always be greater than the existing
           number of port WWNs
       npivTemporaryDisabled: This property is used to enable or disable the NPIV capability on a desired
           virtual machine on a temporary basis.
           
           When this property is set NPIV Vport
           will not be instantiated by the VMX process of the Virtual Machine. When this
           property is set port WWNs and node WWNs in the VM configuration are preserved.
       npivOnNonRdmDisks: This property is used to check whether the NPIV can be enabled on the Virtual
           machine with non-rdm disks in the configuration, so this is potentially not
           enabling npiv on vmfs disks.
           
           Also this property is used to check whether RDM
           is required to generate WWNs for a virtual machine.
       locationId: Hash incorporating the virtual machine's config file location
           and the UUID of the host assigned to run the virtual machine.
       template: Flag indicating whether or not a virtual machine is a template.
       guestId: Guest operating system configured on a virtual machine.
           
           This is a guest identifier that can be used to access the
           `pyVmomi.vim.vm.GuestOsDescriptor`
           list for information about default configuration.
           For more information on possible values, see
           `pyVmomi.vim.vm.GuestOsDescriptor.GuestOsIdentifier`.
       alternateGuestName: Used as display name for the operating system if guestId is `other`
           or `other-64`.
       annotation: Description for the virtual machine.
       files: Information about the files associated with a virtual machine.
           
           This information does not include files for specific virtual disks or
           snapshots.
       tools: Configuration of VMware Tools running in the guest operating system.
       flags: Additional flags for a virtual machine.
       consolePreferences: Legacy console viewer preferences when doing power operations.
       defaultPowerOps: Configuration of default power operations.
       rebootPowerOff: Whether the next reboot will result in a power off.
           
           Since: vSphere API Release 8.0.0.1
       hardware: Processor, memory, and virtual devices for a virtual machine.
       vcpuConfig: Vcpu configuration.
           
           The `vcpuConfig` array is indexed
           by vcpu number.
       cpuAllocation: Resource limits for CPU.
       memoryAllocation: Resource limits for memory.
       latencySensitivity: The latency-sensitivity of the virtual machine.
       memoryHotAddEnabled: Whether memory can be added while this virtual machine is running.
       cpuHotAddEnabled: Whether virtual processors can be added while this
           virtual machine is running.
       cpuHotRemoveEnabled: Whether virtual processors can be removed while this
           virtual machine is running.
       hotPlugMemoryLimit: The maximum amount of memory, in MB, than can be added to a
           running virtual machine.
           
           This value is determined by the
           virtual machine and is specified only if
           `pyVmomi.vim.vm.ConfigInfo.memoryHotAddEnabled`
           is set to true.
       hotPlugMemoryIncrementSize: Memory, in MB that can be added to a running virtual machine
           must be in increments of this value and needs be a
           multiple of this value.
           
           This value is determined by the virtual machine and is specified
           only if `pyVmomi.vim.vm.ConfigSpec.memoryHotAddEnabled`
           has been set to true.
       cpuAffinity: Affinity settings for CPU.
       memoryAffinity: Affinity settings for memory.
       networkShaper: Resource limits for network.
       extraConfig: Additional configuration information for the virtual machine.
       cpuFeatureMask: Specifies CPU feature compatibility masks that override the
           defaults from the `pyVmomi.vim.vm.GuestOsDescriptor`
           of the virtual machine's guest OS.
           
           As of vSphere API 6.5 `pyVmomi.vim.host.FeatureMask`
           is the recommended method for masking virtual machines with
           hardware version 9 and above (newer). They can be viewed via
           `pyVmomi.vim.vm.RuntimeInfo.featureMask`.
       datastoreUrl: Enumerates the set of datastores that this virtual machine is
           stored on, as well as the URL identification for each of these.
           
           Changes to datastores do not generate property updates on this
           property. However, when this property is retrieved it returns the
           current datastore information.
       swapPlacement: Virtual machine swapfile placement policy.
           
           This will be unset if the
           virtual machine's
           `pyVmomi.vim.vm.Capability.swapPlacementSupported`
           capability is false. If swapPlacementSupported is true, the default
           policy is \"inherit\".
       bootOptions: Configuration options for the boot behavior of the virtual machine.
       ftInfo: Fault Tolerance settings for this virtual machine.
       repConfig: vSphere Replication settings for this virtual machine.
           
           Note this may become deprecated in the future releases. We discourage
           any unnecessary dependency on this field.
       vAppConfig: vApp meta-data for the virtual machine
       vAssertsEnabled: Indicates whether user-configured virtual asserts will be
           triggered during virtual machine replay.
       changeTrackingEnabled: Indicates whether changed block tracking for this VM's disks
           is active.
       firmware: Information about firmware type for this Virtual Machine.
           
           Possible values are described in
           `pyVmomi.vim.vm.GuestOsDescriptor.FirmwareType`
           When creating a new VM:
           \\- If vim.vm.FlagInfo.vbsEnabled is set to `true` and
           this property is set to `bios`, error is returned.
           \\- If this property is unset and vim.vm.FlagInfo.vbsEnabled is set
           to `true`, this property is set to `efi`.
       maxMksConnections: Indicates the maximum number of active remote display connections
           that the virtual machine will support.
       guestAutoLockEnabled: Indicates whether the guest operating system will logout any active
           sessions whenever there are no remote display connections open to
           the virtual machine.
       managedBy: Specifies that this VM is managed by a VC Extension.
           
           See the
           `pyVmomi.vim.vm.ConfigSpec.managedBy` property in the ConfigSpec
           for more details.
       memoryReservationLockedToMax: If set true, memory resource reservation for this virtual machine will always be
           equal to the virtual machine's memory size; increases in memory size will be
           rejected when a corresponding reservation increase is not possible.
       initialOverhead: Set of values to be used only to perform admission control when
           determining if a host has sufficient resources for the virtual
           machine to power on.
       nestedHVEnabled: Indicates whether this VM is configured to use nested
           hardware-assisted virtualization.
       vPMCEnabled: Indicates whether this VM have vurtual CPU performance counters
           enabled.
       scheduledHardwareUpgradeInfo: Configuration of scheduled hardware upgrades and result from last
           attempt to run scheduled hardware upgrade.
       forkConfigInfo: Fork configuration of this virtual machines.
           
           If unset, this virtual machine
           is not configured for fork.
       vFlashCacheReservation: Specifies the total vFlash resource reservation for the vFlash caches associated
           with this VM's virtual disks, in bytes.
           
           This reservation must be allocated to power on the VM.
           See `pyVmomi.vim.vm.RuntimeInfo.vFlashCacheAllocation` for allocated
           reservation when VM is powered on.
       vmxConfigChecksum: A checksum of vmx config file.
       messageBusTunnelEnabled: Whether to allow tunneling of clients from the guest VM into the
           common message bus on the host network.
       vmStorageObjectId: Virtual Machine Object Identifier.
           
           With Object-based Storage systems, Virtual Machine home directory
           is backed by an object.
           This identifier will be set only if VM directory resided on
           object-based storage systems.
       swapStorageObjectId: Virtual Machine Swap Object Identifier.
           
           With Object-based Storage systems, VM's Swap is backed by an object.
           This identifier will be set only if VM swap resided on
           object-based storage systems.
       keyId: Virtual Machine cryptographic options.
       guestIntegrityInfo: Guest integrity platform configuration
       migrateEncryption: An enum describing whether encrypted vMotion is required for this VM.
           
           See `pyVmomi.vim.vm.ConfigSpec.EncryptedVMotionModes` for allowed values.
           This defaults to opportunistic for a regular VM, and will be set to
           required for an encrypted VM.
       sgxInfo: Configuration of SGX, Software Guard Extensions for the VM.
       contentLibItemInfo: Content Library Item info.
       ftEncryptionMode: An enum describing whether encrypted Fault Tolerance is required for this
           VM.
           
           See `pyVmomi.vim.vm.ConfigSpec.EncryptedFtModes` for allowed values.
           \\- This defaults to opportunistic for a regular VM, and will be set to
           required for an encrypted VM.
           \\- If this property is unset, the mode of encrypted Fault Tolerance
           will be set to opportunistic.
           
           Since: vSphere API Release 7.0.2.0
       guestMonitoringModeInfo: GMM configuration
       sevEnabled: SEV (Secure Encrypted Virtualization) enabled or not.
           
           SEV is enabled
           when set to true, and disabled otherwise.
           
           Since: vSphere API Release 7.0.1.0
       numaInfo: vNUMA info.
           
           Since: vSphere API Release 8.0.0.1
       pmemFailoverEnabled: Property to indicate PMem HA failover configuration.
           
           \\- When set to TRUE, VMs configured to use PMem
           will be failed over to other hosts by HA, but the data
           in NVDIMM is not persistent.
           \\- When set to FALSE, VMs configured to use PMem will not
           be failed over to other hosts by HA.
           Property is currently only applicable to VMs with NVDimms and
           will fail to set True if vPMem disks are present.
           
           Since: vSphere API Release 7.0.2.0
       vmxStatsCollectionEnabled: Indicates whether VMXStats Collection is enabled/disabled.
           
           \\- If TRUE, VMXStats is enabled for the VM and a scoreboard
           file is created to store stats for various VMX components.
           \\- If FALSE, VMXStats is disabled for the VM and there is
           no scoreboard file created.
           
           Since: vSphere API Release 7.0.3.1
       vmOpNotificationToAppEnabled: Indicates whether operation notification to applications is
           enabled/disabled.
           
           \\- When set to TRUE, application running inside the VM will be
           notified of operations for which they have registered.
           \\- If unset or FALSE, new applications are not allowed to register
           for notifications and RPCs will no longer be supported from
           already registered applications.
           
           Since: vSphere API Release 7.0.3.0
       vmOpNotificationTimeout: Operation notification timeout in seconds.
           
           \\- Specifies the maximum time the application can take to
           prepare for the operation after its been notified. This value is used
           only if `pyVmomi.vim.vm.ConfigInfo.vmOpNotificationToAppEnabled` is set to TRUE.
           \\- If `pyVmomi.vim.vm.ConfigInfo.vmOpNotificationTimeout` is unset, then it defaults to
           cluster/host timeout.
           
           Since: vSphere API Release 8.0.0.1
       deviceSwap: Status of the device swap operation.
           
           Since: vSphere API Release 8.0.0.1
       pmem: Virtual persistent memory info.
           
           Since: vSphere API Release 7.0.3.0
       deviceGroups: Assignable hardware device groups.
           
           Since: vSphere API Release 8.0.0.1
       fixedPassthruHotPlugEnabled: Indicates whether support to add and remove fixed passthrough
           devices when the VM is running is enabled.
           
           When the virtual machine is powered on, this indicates if
           support for hot adding and removing fixed passthrough devices
           was enabled prior to power on. Otherwise, it indicates whether
           it will be enabled when the VM is powered on.
           NOTE: When setting this to true, the memory reservation should
           be equal to the guest memory size or the option to reserve all
           guest memory should be selected. If unset, the current value is
           left unchanged.
           
           Since: vSphere API Release 8.0.1.0
       metroFtEnabled: Indicates whether FT Metro Cluster is enabled/disabled.
           
           \\- If TRUE, FT Metro Cluster is enabled for the VM. An implicit
           Anti-HostGroup will be generated from HostGroup defined for FT
           primary, then affine the primary with one HostGroup and affine the
           secondary with another HostGroup.
           \\- If FALSE or unset, FT Metro Cluster is disabled for the VM. Both FT
           primary and secondary will be put in the same HostGroup.
           
           Since: vSphere API Release 8.0.3.0
       vmxRuntimeConfig: Contains properties that are established when the VM
           powers-on and are later examined when the VM is resumed to ensure that
           the VM is compatible with the suspended device state.
           
           It is only populated while the VM is powered-on.
           
           Since: vSphere API Release 9.0.0.0
       metroFtHostGroup: Indicate the Host Group (`pyVmomi.vim.cluster.HostGroup`) for FT
           Metro Cluster enabled Virtual Machine.
           
           Based on the selected Host Group, FT can divide the hosts in the cluster
           into two groups and ensure to place FT primary and FT secondary in
           different groups.
           
           Since: vSphere API Release 8.0.3.0
       tdxEnabled: TDX (Trust Domain Extensions) enabled or not.
           
           TDX is enabled
           when set to true, and disabled otherwise.
           
           Since: vSphere API Release 9.0.0.0
       sevSnpEnabled: SEV-SNP (Secure Encrypted Virtualization Secure Nested paging) enabled or
           not.
           
           SEV-SNP is enabled when set to true, and disabled otherwise.
           
           Since: vSphere API Release 9.0.0.0
       guestArchitecture: The guest CPU architecture.
           
           For the list of possible values, please see the
           `pyVmomi.vim.vm.GuestOsDescriptor.GuestArchitecture`.
           
           Since: vSphere API Release 9.1.0.0
       extensionCompatibilityConstraint: The full set of extension compatibility constraints registered on this
           virtual machine by its managing extension.
           
           See
           `pyVmomi.vim.vm.ExtensionCompatibilityConstraint` and
           `pyVmomi.vim.vm.ConfigSpec.extensionCompatibilityConstraint` for how
           constraints are registered and what they mean.
           
           When unset, no extension compatibility constraints are registered on the
           virtual machine.
           
           Since: vSphere API Release 9.1.2.0
   """
   class NpivWwnType(pyVmomi.VmomiSupport.Enum):
      """
      The NPIV WWN source type.
      
      Attributes:
          vc: This set of WWNs is generated by VC server.
          host: This set of WWNs is generated by Host Agent.
          external: This set of WWNs is provided by the client.
      """
      vc: _typing.ClassVar['ConfigInfo.NpivWwnType'] = 'vc'
      host: _typing.ClassVar['ConfigInfo.NpivWwnType'] = 'host'
      external: _typing.ClassVar['ConfigInfo.NpivWwnType'] = 'external'

   class SwapPlacementType(pyVmomi.VmomiSupport.Enum):
      """
      Available choices for virtual machine swapfile placement policy.
      
      This is
      the set of legal values for the virtual machine configuration's
      `pyVmomi.vim.vm.ConfigInfo.swapPlacement` property. All
      values except for \"inherit\" and \"vmConfigured\" are also valid values for
      a compute resource configuration's
      `pyVmomi.vim.ComputeResource.ConfigInfo.vmSwapPlacement`
      property.
      
      Attributes:
          inherit: Honor the virtual machine swapfile placement policy of the compute
              resource that contains this virtual machine.
          vmDirectory: Store the swapfile in the same directory as the virtual machine.
          hostLocal: Store the swapfile in the datastore specified by the
              `pyVmomi.vim.host.ConfigInfo.localSwapDatastore`
              property of the virtual machine's host, if that property is set and
              indicates a datastore with sufficient free space.
              
              Otherwise store the
              swapfile in the same directory as the virtual machine.
              
              Note: This setting may degrade VMotion performance.
      """
      inherit: _typing.ClassVar['ConfigInfo.SwapPlacementType'] = 'inherit'
      vmDirectory: _typing.ClassVar['ConfigInfo.SwapPlacementType'] = 'vmDirectory'
      hostLocal: _typing.ClassVar['ConfigInfo.SwapPlacementType'] = 'hostLocal'

   class DatastoreUrlPair(pyVmomi.vmodl.DynamicData):
      """
      Contains the name of a datastore, and its local file path on the host
      currently affiliated with this virtual machine.
      """
      name: str
      url: str

   class OverheadInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about virtualization overhead required to power on the
      virtual machine on the registered host.
      
      Attributes:
          initialMemoryReservation: Memory overhead required for virtual machine to be powered on (in bytes).
          initialSwapReservation: Disk space required for virtual machine to be powered on (in bytes).
              
              This space is used by virtualization infrastructure to swap out
              virtual machine process memory. Location of the file is specified by
              sched.swap.vmxSwapDir virtual machinge advanced config option or
              in case it is not specified - current virtual machine home directory
              is being used.
      """
      initialMemoryReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      initialSwapReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   changeVersion: str
   modified: _datetime.datetime
   name: str
   guestFullName: str
   version: str
   uuid: str
   createDate: _typing.Optional[_datetime.datetime] = None
   instanceUuid: _typing.Optional[str] = None
   npivNodeWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivPortWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivWorldWideNameType: _typing.Optional[str] = None
   npivDesiredNodeWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivDesiredPortWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivTemporaryDisabled: _typing.Optional[bool] = None
   npivOnNonRdmDisks: _typing.Optional[bool] = None
   locationId: _typing.Optional[str] = None
   template: bool
   guestId: str
   alternateGuestName: str
   annotation: _typing.Optional[str] = None
   files: FileInfo
   tools: _typing.Optional[ToolsConfigInfo] = None
   flags: FlagInfo
   consolePreferences: _typing.Optional[ConsolePreferences] = None
   defaultPowerOps: DefaultPowerOpInfo
   rebootPowerOff: _typing.Optional[bool] = None
   hardware: VirtualHardware
   vcpuConfig: list[VcpuConfig] = []
   cpuAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   memoryAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None
   memoryHotAddEnabled: _typing.Optional[bool] = None
   cpuHotAddEnabled: _typing.Optional[bool] = None
   cpuHotRemoveEnabled: _typing.Optional[bool] = None
   hotPlugMemoryLimit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hotPlugMemoryIncrementSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   cpuAffinity: _typing.Optional[AffinityInfo] = None
   memoryAffinity: _typing.Optional[AffinityInfo] = None
   networkShaper: _typing.Optional[NetworkShaperInfo] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []
   cpuFeatureMask: list[pyVmomi.vim.host.CpuIdInfo] = []
   datastoreUrl: list[ConfigInfo.DatastoreUrlPair] = []
   swapPlacement: _typing.Optional[str] = None
   bootOptions: _typing.Optional[BootOptions] = None
   ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
   repConfig: _typing.Optional[ReplicationConfigSpec] = None
   vAppConfig: _typing.Optional[pyVmomi.vim.vApp.VmConfigInfo] = None
   vAssertsEnabled: _typing.Optional[bool] = None
   changeTrackingEnabled: _typing.Optional[bool] = None
   firmware: _typing.Optional[str] = None
   maxMksConnections: _typing.Optional[int] = None
   guestAutoLockEnabled: _typing.Optional[bool] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
   memoryReservationLockedToMax: _typing.Optional[bool] = None
   initialOverhead: _typing.Optional[ConfigInfo.OverheadInfo] = None
   nestedHVEnabled: _typing.Optional[bool] = None
   vPMCEnabled: _typing.Optional[bool] = None
   scheduledHardwareUpgradeInfo: _typing.Optional[ScheduledHardwareUpgradeInfo] = None
   forkConfigInfo: _typing.Optional[ForkConfigInfo] = None
   vFlashCacheReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vmxConfigChecksum: _typing.Optional[pyVmomi.VmomiSupport.binary] = None
   messageBusTunnelEnabled: _typing.Optional[bool] = None
   vmStorageObjectId: _typing.Optional[str] = None
   swapStorageObjectId: _typing.Optional[str] = None
   keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
   guestIntegrityInfo: _typing.Optional[GuestIntegrityInfo] = None
   migrateEncryption: _typing.Optional[str] = None
   sgxInfo: _typing.Optional[SgxInfo] = None
   contentLibItemInfo: _typing.Optional[ContentLibraryItemInfo] = None
   ftEncryptionMode: _typing.Optional[str] = None
   guestMonitoringModeInfo: _typing.Optional[GuestMonitoringModeInfo] = None
   sevEnabled: _typing.Optional[bool] = None
   numaInfo: _typing.Optional[VirtualNumaInfo] = None
   pmemFailoverEnabled: _typing.Optional[bool] = None
   vmxStatsCollectionEnabled: _typing.Optional[bool] = None
   vmOpNotificationToAppEnabled: _typing.Optional[bool] = None
   vmOpNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceSwap: _typing.Optional[VirtualDeviceSwap] = None
   pmem: _typing.Optional[VirtualPMem] = None
   deviceGroups: _typing.Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: _typing.Optional[bool] = None
   metroFtEnabled: _typing.Optional[bool] = None
   vmxRuntimeConfig: list[pyVmomi.vim.option.OptionValue] = []
   metroFtHostGroup: _typing.Optional[str] = None
   tdxEnabled: _typing.Optional[bool] = None
   sevSnpEnabled: _typing.Optional[bool] = None
   guestArchitecture: _typing.Optional[str] = None
   extensionCompatibilityConstraint: _typing.Optional[ExtensionCompatibilityConstraintSet] = None


class ConfigOption(pyVmomi.vmodl.DynamicData):
   """
   This configuration data object type contains information about the execution
   environment for a virtual machine.
   
   This includes information about which features are
   supported, such as:
   - Which guest operating systems are supported.
   - How devices are emulated. For example, that a CD-ROM drive can be emulated
     with a file or that a serial port can be emulated with a pipe.
     
   VirtualCenter can provide a broader environment than any single physical host. This
   is a departure from traditional virtualization approaches, which rely on the host
   system to define the environment for virtual machines. This data object describes
   environment capabilities and is used by VirtualCenter to choose hosts on which to run
   virtual machines.
   
   Attributes:
       version: The version corresponding to this configOption.
       description: A description string for this configOption.
       guestOSDescriptor: List of supported guest operating systems.
           
           The choice of guest operating system may limit the set of valid devices.
           For example, you cannot select Vmxnet with all guest operating systems.
       guestOSDefaultIndex: Index into guestOsDescriptor array denoting the default guest
           operating system.
       hardwareOptions: Processor, memory, and virtual device options for a virtual machine.
       capabilities: Capabilities supported by a virtual machine.
       datastore: The datastore options for this virtual machine.
       defaultDevice: The list of virtual devices that are created on a virtual machine by default.
           
           Clients should not create these devices.
       supportedMonitorType: The monitor types supported by a host.
           
           The acceptable monitor types
           are enumerated by `pyVmomi.vim.vm.FlagInfo.MonitorType`.
       supportedOvfEnvironmentTransport: Specifies the supported property transports that are
           available for the OVF environment
       supportedOvfInstallTransport: Specifies the supported transports for the OVF
           installation phase.
       propertyRelations: The relations between the properties of the virtual
           machine config spec.
   """
   version: str
   description: str
   guestOSDescriptor: list[GuestOsDescriptor] = []
   guestOSDefaultIndex: int
   hardwareOptions: VirtualHardwareOption
   capabilities: Capability
   datastore: DatastoreOption
   defaultDevice: list[pyVmomi.vim.vm.device.VirtualDevice] = []
   supportedMonitorType: list[str] = []
   supportedOvfEnvironmentTransport: list[str] = []
   supportedOvfInstallTransport: list[str] = []
   propertyRelations: list[PropertyRelation] = []


class ConfigOptionDescriptor(pyVmomi.vmodl.DynamicData):
   """
   Contains the definition of a unique key that can be used to
   retrieve a configOption object.
   
   Attributes:
       key: A unique key used to identify a configOption object in this
           `pyVmomi.vim.EnvironmentBrowser`.
       description: A description of the configOption object.
       host: List of hosts to which this descriptor applies.
           
           List of hosts is not set when descriptor is returned
           from `pyVmomi.vim.Datacenter.queryConfigOptionDescriptor`.
       createSupported: Indicates whether the associated set of configuration options
           can be used for virtual machine creation on a given host or
           cluster.
       defaultConfigOption: Indicates whether the associated set of virtual machine
           configuration options is the default one for a given host or
           cluster.
           
           Latest version is marked as default unless
           other version is specified via
           `pyVmomi.vim.ComputeResource.ConfigInfo.defaultHardwareVersionKey`
           or `pyVmomi.vim.Datacenter.ConfigInfo.defaultHardwareVersionKey`.
           If this setting is TRUE, virtual machine creates will use the
           associated set of configuration options, unless a config version is
           explicitly specified in the `pyVmomi.vim.vm.ConfigSpec`.
       runSupported: Indicates whether the associated set of configuration options
           can be used to power on a virtual machine on a given host or
           cluster.
       upgradeSupported: Indicates whether the associated set of configuration options
           can be used as a virtual hardware upgrade target.
   """
   key: str
   description: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   createSupported: bool
   defaultConfigOption: bool
   runSupported: bool
   upgradeSupported: bool


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object type encapsulates configuration settings
   when creating or reconfiguring a virtual machine.
   
   To support incremental changes,
   these properties are all optional. If an optional property is unset,
   or any nested optional property is unset, the property will not
   be changed unless 'unset' is a valid value for the property. To determine
   whether 'unset' is a valid value for a particular property, refer to
   the documentation for that property.
   
   Attributes:
       changeVersion: If specified, the changes are only applied if the current changeVersion matches
           the specified changeVersion.
           
           This field can be used to guard against updates that
           have happened between when configInfo is read and when it is applied.
           
           For more information about how configurations are uniquely identified, see
           `pyVmomi.vim.vm.ConfigInfo.changeVersion`.
       name: Display name of the virtual machine.
           
           Any % (percent) character used in this name parameter must be escaped, unless it
           is used to start an escape sequence. Clients may also escape any other characters
           in this name parameter. Snapshots of virtual machines that have spaces in their
           names and are associated with ESX 2.x servers are not supported. Therefore, if you
           want the option to take snapshots of this virtual machine and you are associating
           it with an ESX 2.x server, do not use spaces in the name.
           
           Reconfigure privilege: VirtualMachine.Config.Rename
       version: The version string for this virtual machine.
           
           This is used only while
           creating a new virtual machine, and can be updated by invoking
           `pyVmomi.vim.VirtualMachine.upgradeVirtualHardware` for this virtual
           machine.
       createDate: Creation date of a virtual machine represented in DateTime format.
           
           This property is populated by the vCenter Server with the date
           and time of creation of the virtual machine. Values provided by the
           client will be ignored.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       uuid: 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string
           in \"12345678-abcd-1234-cdef-123456789abc\" format.
           
           Normally, this property is not set by a client, allowing the
           Virtual Infrastructure environment to assign a UUID when
           the virtual machine is created. However, in some rare cases,
           such as a manual copy of a virtual machine, it may be necessary
           to set this property.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       instanceUuid: VirtualCenter-specific 128-bit UUID of a virtual machine, represented
           as a hexadecimal string.
           
           This identifier is used by VirtualCenter
           to uniquely identify all virtual machine instances in the Virtual
           Infrastructure environment, including those that may share the same
           SMBIOS UUID.
           
           Normally, this property is not set by a client, allowing the
           Virtual Infrastructure environment to assign or change it when
           VirtualCenter detects an identifier conflict between virtual
           machines. This identifier can be modified even when a virtual
           machine is powered on. Clients can specify that vCenter Server
           reassign a new identifier by a providing an empty string. Reassigning
           the identifier is not allowed for Fault Tolerance virtual machines.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       npivNodeWorldWideName: The NPIV node WWN to be assigned to a virtual machine.
           
           This property should only
           be used or set when the value of `pyVmomi.vim.vm.ConfigSpec.npivWorldWideNameOp` property is \"set\".
           Otherwise, an `pyVmomi.vim.fault.InvalidVmConfig` fault will be thrown. If the
           specified node WWN is currently being used by another virtual machine, a
           `pyVmomi.vim.fault.VmWwnConflict` fault will be thrown.
           
           For detail description on WWN, see `pyVmomi.vim.vm.ConfigInfo.npivNodeWorldWideName`.
           
           Reconfigure privilege: VirtualMachine.Config.Settings.
       npivPortWorldWideName: The NPIV port WWN to be assigned to a virtual machine.
           
           This property should only
           be used or set when the value of `pyVmomi.vim.vm.ConfigSpec.npivWorldWideNameOp` property is \"set\".
           Otherwise, an `pyVmomi.vim.fault.InvalidVmConfig` fault will be thrown. If the
           specified port WWN is currently being used by another virtual machine, a
           `pyVmomi.vim.fault.VmWwnConflict` fault will be thrown.
           
           For detail description on WWN, see `pyVmomi.vim.vm.ConfigInfo.npivPortWorldWideName`.
           
           Reconfigure privilege: VirtualMachine.Config.Settings.
       npivWorldWideNameType: This property is used internally in the communication between the
           VirtualCenter server and ESX Server to indicate the source for
           `pyVmomi.vim.vm.ConfigSpec.npivNodeWorldWideName` and
           `pyVmomi.vim.vm.ConfigSpec.npivPortWorldWideName` when `pyVmomi.vim.vm.ConfigSpec.npivWorldWideNameOp` is \"set\".
           
           This property should only be set by the VirtualCenter server.
           
           If this property is set in a call to a VirtualCenter server,
           an `pyVmomi.vim.fault.InvalidVmConfig` fault will always be thrown. In a
           call to an ESX Server host, an `pyVmomi.vim.fault.InvalidVmConfig`
           fault will be thrown if the value of `pyVmomi.vim.vm.ConfigSpec.npivWorldWideNameOp` is not set to
           \"set\".
           
           Reconfigure privilege: VirtualMachine.Config.Settings.
       npivDesiredNodeWwns: The NPIV node WWNs to be extended from the original list of WWN numbers.
           
           This
           property should be set to desired number which is an aggregate of existing
           plus new numbers. Desired Node WWNs should always be greater than the existing
           number of node WWNs
       npivDesiredPortWwns: The NPIV port WWNs to be extended from the original list of WWN numbers.
           
           This
           property should be set to desired number which is an aggregate of existing
           plus new numbers. Desired Node WWNs should always be greater than the existing
           number of port WWNs
       npivTemporaryDisabled: This property is used to enable or disable the NPIV capability on a desired
           virtual machine on a temporary basis.
           
           When this property is set NPIV Vport
           will not be instantiated by the VMX process of the Virtual Machine. When this
           property is set port WWNs and node WWNs in the VM configuration are preserved.
           
           Reconfigure privilege: VirtualMachine.Config.Settings.
       npivOnNonRdmDisks: This property is used to check whether the NPIV can be enabled on the Virtual
           machine with non-rdm disks in the configuration, so this is potentially not
           enabling npiv on vmfs disks.
           
           Also this property is used to check whether RDM
           is required to generate WWNs for a virtual machine.
       npivWorldWideNameOp: The flag to indicate what type of NPIV WWN operation is going to be performed
           on the virtual machine.
           
           If unset, it indicates no change to existing NPIV WWN
           assignment (or not assigned) in the virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.Settings.
       locationId: 128-bit hash based on the virtual machine's configuration file location
           and the UUID of the host assigned to run the virtual machine.
           
           Normally, this property is not set by a client, allowing the
           Virtual Infrastructure environment to assign a location ID when
           the virtual machine is created. However, if the virtual machine's
           configuration file has been manually moved, it may be desirable to clear this
           property, setting it to an empty string, so the property is regenerated.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       guestId: Short guest operating system identifier.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       alternateGuestName: Full name for guest, if guestId is specified as `other`
           or `other-64`.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       annotation: User-provided description of the virtual machine.
           
           Because this property
           is optional in the virtual machine configuration, it is necessary
           to pass an explicit empty string in a ConfigSpec object to remove an annotation
           that is already present in the `pyVmomi.vim.vm.ConfigInfo`
           for a virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.Rename
       files: Information about virtual machine files.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       tools: Configuration of VMware Tools running in the guest operating system.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       flags: Additional flags for a virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       consolePreferences: Legacy console viewer preferences that are used with power operations.
           
           For
           example, power on.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       powerOpInfo: Configuration for default power operations.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       rebootPowerOff: Whether the next reboot will result in a power off.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
           
           Since: vSphere API Release 8.0.0.1
       numCPUs: Number of virtual processors in a virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.CpuCount
       vcpuConfig: Vcpu configuration.
           
           The `vcpuConfig` array is indexed
           by vcpu number.
       numCoresPerSocket: Number of cores among which to distribute
           CPUs in this virtual machine.
           
           Set \"numCoresPerSocket\" with a non-zero value
           to manually configure coresPerSocket size.
           Set \"numCoresPerSocket\" with zero to remove any manual size
           if present, and use default coresPerSocket behavior.
           Leave \"numCoresPerSocket\" unset to continue with existing
           configuration (either manual or default).
       memoryMB: Size of a virtual machine's memory, in MB.
           
           Reconfigure privilege: VirtualMachine.Config.Memory
       memoryHotAddEnabled: Indicates whether or not memory can be added to the virtual
           machine while it is running.
           
           This attribute can only be set when the virtual machine is
           powered-off.
           
           Reconfigure privilege: VirtualMachine.Config.Memory
       cpuHotAddEnabled: Indicates whether or not virtual processors can be added to
           the virtual machine while it is running.
           
           This attribute can only be set when the virtual machine is
           powered-off.
           
           Reconfigure privilege: VirtualMachine.Config.CpuCount
       cpuHotRemoveEnabled: Indicates whether or not virtual processors can be removed
           from the virtual machine while it is running.
           
           This attribute can only be set when the virtual machine is
           powered-off.
           
           Reconfigure privilege: VirtualMachine.Config.CpuCount
       virtualICH7MPresent: Does this virtual machine have Virtual Intel I/O Controller Hub 7
       virtualSMCPresent: Does this virtual machine have System Management Controller
       deviceChange: Set of virtual devices being modified by the configuration operation.
           
           Reconfigure privileges:
           - VirtualMachine.Config.Resource if setting the \"shares\" property of
             a new or existing VirtualDisk device
           - VirtualMachine.Config.RawDevice if adding, removing, or modifying a
             raw device (also required when creating a virtual machine)
           - VirtualMachine.Config.HostUSBDevice if adding, removing, or
             modifying a VirtualUSB device backed by a host USB device (also
             required when creating a virtual machine).
           - VirtualMachine.Interact.DeviceConnection if setting the \"connectable\"
             property of a connectable device
           - VirtualMachine.Interact.SetCDMedia if setting the \"backing\" property
             of a VirtualCdrom device
           - VirtualMachine.Interact.SetFloppyMedia if setting the \"backing\" property
             of a VirtualFloppy device
           - VirtualMachine.Config.EditDevice if setting any property of a
             non-CDROM non-Floppy device
           - VirtualMachine.Config.AddExistingDisk if adding a VirtualDisk, and
             the fileOperation is unset (also required when creating a virtual machine)
           - VirtualMachine.Config.AddNewDisk if adding a VirtualDisk and the
             fileOperation is set (also required when creating a virtual machine)
           - VirtualMachine.Config.RemoveDisk if removing a VirtualDisk device
           - VirtualMachine.Config.AddRemoveDevice if adding or removing any
             device other than disk, raw, or USB device.
           - Network.Assign if if setting the \"backing\" property of a
             VirtualEthernetCard device.
       cpuAllocation: Resource limits for CPU.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       memoryAllocation: Resource limits for memory.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       latencySensitivity: The latency-sensitivity setting of the virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       cpuAffinity: Affinity settings for CPU.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       memoryAffinity: Affinity settings for memory.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       networkShaper: Resource limits for network.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       cpuFeatureMask: Specifies the CPU feature compatibility masks.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
           As of vSphere API 6.5 `pyVmomi.vim.host.FeatureMask`
           is the recommended method for masking virtual machines with
           hardware version 9 and above (newer).
       extraConfig: Additional configuration information for the virtual machine.
           
           This describes a set of modifications to the additional options. If the key is
           already present, it will be reset with the new value provided. Otherwise, a new
           option is added. Keys with empty values will be removed.
           
           Configuration keys that would conflict with parameters that are explicitly
           configurable through other fields in the ConfigSpec object are silently ignored.
           
           Reconfigure privilege: VirtualMachine.Config.AdvancedConfig
           (also required when setting this property while creating a virtual machine)
       swapPlacement: Virtual machine swapfile placement policy.
           
           This may only be set if the
           `pyVmomi.vim.vm.Capability.swapPlacementSupported`
           capability is true for this virtual machine. Any change to this policy
           will take effect the next time the virtual machine powers on, resumes
           from a suspended state, or migrates while powered on.
           
           Reconfigure privilege: VirtualMachine.Config.SwapPlacement
           (also required when setting this property while creating a virtual machine)
       bootOptions: Settings that control the boot behavior of the virtual
           machine.
           
           These settings take effect during the next power-on
           of the virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       vAppConfig: Configuration of vApp meta-data for a virtual machine
       ftInfo: Fault Tolerance settings for this virtual machine.
       repConfig: vSphere Replication settings.
           
           Note this may become deprecated in the future releases. We
           discourage any unnecessary dependency on this field.
           
           Reconfigure privilege: VirtualMachine.Hbr.ConfigureReplication
       vAppConfigRemoved: Set to true, if the vApp configuration should be removed
           
           Reconfigure privilege: VApp.ApplicationConfig
       vAssertsEnabled: Indicates whether user-configured virtual asserts will be
           triggered during virtual machine replay.
           
           This setting takes
           effect during the next replay of the virtual machine.
           
           Enabling this functionality can potentially cause some
           performance overhead during virtual machine execution.
       changeTrackingEnabled: Setting to control enabling/disabling changed block tracking for
           the virtual disks of this VM.
           
           This may only be set if the
           `pyVmomi.vim.vm.Capability.changeTrackingSupported`
           capability is true for this virtual machine. Any change to this property
           will take effect the next time the virtual machine powers on, resumes
           from a suspended state, performs a snapshot create/delete/revert operation
           or migrates while powered on.
           
           Reconfigure privilege: VirtualMachine.Config.ChangeTracking
           (also required when setting this property while creating a virtual machine)
       firmware: Set the desired firmware type for this Virtual Machine.
           
           Possible values are described in
           `pyVmomi.vim.vm.GuestOsDescriptor.FirmwareType`
       maxMksConnections: If set, this setting limits the maximum number of active remote
           display connections that the virtual machine will support to
           the specified value.
           
           Reconfigure privilege: VirtualMachine.Config.MksControl
       guestAutoLockEnabled: If set to True, this causes the guest operating system to automatically
           logout any active sessions whenever there are no remote display
           connections open to the virtual machine.
           
           Reconfigure privilege: VirtualMachine.Config.MksControl
       managedBy: Specifies that this VM is managed by a VC Extension.
           
           This information is primarily used in the Client to show a custom icon for
           managed virtual machines, and a description of the function of the virtual
           machine. If no extension can be found with the extension key in the
           `pyVmomi.vim.ext.ManagedByInfo` object, or the type is not found
           in the `pyVmomi.vim.Extension.managedEntityInfo` list of the
           extension, the default virtual machine icon is used, and no description is
           shown.
           To unset this field pass a `pyVmomi.vim.ext.ManagedByInfo` object with an
           empty `pyVmomi.vim.ext.ManagedByInfo.extensionKey`.
           
           Reconfigure privilege: VirtualMachine.Config.ManagedBy
       extensionCompatibilityConstraint: The full set of extension compatibility constraints for this virtual
           machine, declared by its managing extension (see `pyVmomi.vim.vm.ConfigSpec.managedBy`) so
           that vCenter can protect the VM's properties during operations that would
           change them.
           
           See `pyVmomi.vim.vm.ExtensionCompatibilityConstraint` for the
           meaning of an individual constraint.
           
           When present, `pyVmomi.vim.vm.ExtensionCompatibilityConstraintSet.constraint` is the
           full desired constraint set and is persisted by the same operation that
           creates or reconfigures the VM:
           - At create time, constraints are persisted atomically with the VM.
           - At reconfigure time, the set fully replaces the existing set,
             including clearing it entirely if
             `pyVmomi.vim.vm.ExtensionCompatibilityConstraintSet.constraint` is an empty
             array. Omitting this field (leaving it unset) leaves the existing
             set unchanged.
             
           The constraints in the set are evaluated independently; an operation is
           compatible only if it satisfies every constraint in the set (they are
           logically ANDed). Order is not significant.
           
           Reconfigure privilege: VirtualMachine.Config.ExtensionCompatibility (also
           required at create time, where it is evaluated against the target folder
           rather than the VM).
           
           Since: vSphere API Release 9.1.2.0
       skipExtensionCompatibilityChecks: Whether to skip enforcement of the `pyVmomi.vim.vm.ConfigSpec.extensionCompatibilityConstraint` registered on this virtual machine for
           this reconfigure operation.
           
           Intended for a managing extension's service accounts, so they can
           reconfigure the VMs they manage without being blocked by the constraints
           they registered. Honored only when the caller holds the
           VirtualMachine.ExtensionCompatibility.Bypass privilege on the virtual machine;
           otherwise the operation is rejected. Built-in compatibility checks (host
           compatibility, SPBM, and so on) are still enforced.
           
           When unset, the value is treated as false and the registered constraints
           are enforced.
           
           Since: vSphere API Release 9.1.2.0
       memoryReservationLockedToMax: If set true, memory resource reservation for this virtual machine will always be
           equal to the virtual machine's memory size; increases in memory size will be
           rejected when a corresponding reservation increase is not possible.
           
           This feature
           may only be enabled if it is currently possible to reserve all of the virtual machine's memory.
           
           Reconfigure privilege: VirtualMachine.Config.Resource
       nestedHVEnabled: Specifies that this VM will use nested hardware-assisted virtualization.
           
           When creating a new VM:
           \\- If vim.vm.FlagInfo.vbsEnabled is set to `true`,
           and this flag is set to `false` error is returned.
           \\- If this flag is unset and vim.vm.FlagInfo.vbsEnabled is set to
           `true`, the value of this flag is set to `true`.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       vPMCEnabled: Specifies that this VM will have virtual CPU performance counters
           enabled.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       scheduledHardwareUpgradeInfo: Configuration of scheduled hardware upgrades.
           
           Reconfigure privilege: VirtualMachine.Config.UpgradeVirtualHardware
       vmProfile: Virtual Machine Profile requirement.
           
           Profiles are solution specific.
           Profile Based Storage Management is a vSphere server extension.
           API users who want to provision VMs using Storage Profiles, need to
           interact with it.
           This is an optional parameter and if user doesn't specify profile,
           the default behavior will apply.
       messageBusTunnelEnabled: Whether to allow tunneling of clients from the guest VM into the
           common message bus on the host network.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
       crypto: Virtual Machine cryptographic options.
           
           The cryptographic options are inherited to all disks of the VM.
           The cryptographic options for a disk can be different by setting
           its CryptoSpec.
       migrateEncryption: An enum describing whether encrypted vMotion is required for this VM.
           
           Supported values are listed in `pyVmomi.vim.vm.ConfigSpec.EncryptedVMotionModes`.
           This defaults to opportunistic for a regular VM, and will be set to
           required for an encrypted VM.
       sgxInfo: Configuration of SGX, Software Guard Extensions for the VM.
       ftEncryptionMode: An enum describing whether encrypted Fault Tolerance is required
           for this VM.
           
           Supported values are listed in `pyVmomi.vim.vm.ConfigSpec.EncryptedFtModes`.
           \\- This defaults to opportunistic for a regular VM, and will be set to
           required for an encrypted VM.
           \\- If this property is unset, the mode of encrypted Fault Tolerance
           will be set to opportunistic.
           
           Reconfigure privilege: VirtualMachine.Config.Settings
           
           Since: vSphere API Release 7.0.2.0
       guestMonitoringModeInfo: Configuration of GMM, Guest Monitoring Mode for the VM.
       sevEnabled: SEV (Secure Encrypted Virtualization) enabled or not.
           
           SEV is enabled when
           set to true, and disabled otherwise.
           
           Since: vSphere API Release 7.0.1.0
       virtualNuma: Virtual NUMA information for this VM.
           
           Since: vSphere API Release 8.0.0.1
       motherboardLayout: One of motherboardLayout choices.
           
           Default is i440bxHostBridge. See
           `pyVmomi.vim.vm.VirtualHardware.motherboardLayout`
           
           Since: vSphere API Release 8.0.0.1
       pmemFailoverEnabled: Property to enable/disable PMem HA failover.
           
           \\- When set to TRUE, VMs configured to use PMem
           will be failed over to other hosts by HA, but the data
           in NVDIMM is not persistent.
           \\- When set to FALSE, VMs configured to use PMem will not
           be failed over to other hosts by HA.
           Property is currently only applicable to VMs with NVDimms and
           will fail to set True if vPMem disks are present.
           
           Since: vSphere API Release 7.0.2.0
       vmxStatsCollectionEnabled: Property to enable/disable VMXStats Collection.
           
           \\- Setting this property is only allowed when the VM is powered off
           and will fail otherwise.
           \\- When set to TRUE, VMs will be configured to create a
           scoreboard file to store certain stats for various VMX
           components.
           
           Since: vSphere API Release 7.0.3.1
       vmOpNotificationToAppEnabled: Property to enable/disable operation notification to applications.
           
           \\- When set to TRUE, application running inside the VM will be
           notified of operations for which they have registered.
           \\- If unset defaults to FALSE, no notifications are sent to the
           application.
           
           Since: vSphere API Release 7.0.3.0
       vmOpNotificationTimeout: Operation notification timeout in seconds.
           
           \\- Specifies the maximum time duration the applications may take to
           prepare for the operation after its been notified. This value is used
           only if `pyVmomi.vim.vm.ConfigSpec.vmOpNotificationToAppEnabled` is set to TRUE.
           \\- Timeout has to be a non-zero positive value for applications to
           be able to register and get notifications.
           
           Since: vSphere API Release 8.0.0.1
       deviceSwap: Status of the device swap operation.
           
           Since: vSphere API Release 8.0.0.1
       simultaneousThreads: Number of SMT (Simultaneous multithreading) threads.
           
           \\- Set \"simultaneousThreads\" with a non-zero value to configure threads.
           \\- If unset, then use system defaults.
           
           Since: vSphere API Release 8.0.0.1
       pmem: Configuration for virtual persistent memory.
           
           Since: vSphere API Release 7.0.3.0
       deviceGroups: Assignable hardware device groups.
           
           Since: vSphere API Release 8.0.0.1
       fixedPassthruHotPlugEnabled: Indicates whether support to add and remove fixed passthrough
           devices when the VM is running should be enabled.
           
           This property can only be set when the VM is powered off. If set,
           additional setup will be performed when the VM is powered on
           so that hot adding and removing fixed passthrough devices will
           be possible.
           NOTE: When setting this to true, the memory reservation should
           be equal to the guest memory size or the option to reserve all
           guest memory should be selected. If unset, the current value
           is left unchanged.
           
           Since: vSphere API Release 8.0.1.0
       metroFtEnabled: Indicates whether FT Metro Cluster is enabled/disabled.
           
           \\- If TRUE, FT Metro Cluster is enabled for the VM. An implicit
           Anti-HostGroup will be generated from HostGroup defined for FT
           primary, then affine the primary with one HostGroup and affine the
           secondary with another HostGroup.
           \\- If FALSE or unset, FT Metro Cluster is disabled for the VM. Both FT
           primary and secondary will be put in the same HostGroup.
           
           Since: vSphere API Release 8.0.3.0
       metroFtHostGroup: Indicate the Host Group (`pyVmomi.vim.cluster.HostGroup`) for FT
           Metro Cluster enabled Virtual Machine.
           
           Based on the selected Host Group, FT can divide the hosts in the cluster
           into two groups and ensure to place FT primary and FT secondary in
           different groups.
           
           Since: vSphere API Release 8.0.3.0
       tdxEnabled: TDX (Trust Domain Extensions) enabled or not.
           
           TDX is enabled when
           set to true, and disabled otherwise.
           
           Since: vSphere API Release 9.0.0.0
       sevSnpEnabled: SEV-SNP (Secure Encrypted Virtualization Secure Nested paging) enabled or
           not.
           
           SEV-SNP is enabled when set to true, and disabled otherwise.
           
           Since: vSphere API Release 9.0.0.0
       tagSpecs: Specification of the vSphere tags that need to be modified for this
           virtual machine.
           
           Each TagSpec refers to:
           \\- Operation to be performed, i.e., attach a new tag to a VM with this
           ConfigSpec, or detach an existing tag of a VM with this ConfigSpec.
           \\- Information required to uniquely identify the vSphere tag that needs
           to be attached or detached.
           
           When this field is specified in the ConfigSpec during VM creation or
           VM reconfigure, then each tag specified in tagSpecs is automatically
           attached or detached (based on the operation type) when VM with
           that ConfigSpec is created or reconfigured.
           
           Since: vSphere API Release 9.1.0.0
       vmPlacementPolicies: An optional list of `pyVmomi.vim.vm.VmPlacementPolicy` for this VM.
           
           Each policy
           describes a constraint or preference that can influence where, when
           and how this VM should be placed.
           
           If this ConfigSpec is specified during an operation (such as while
           finding a suitable placement for a VM to create that VM), then
           the placement policies specified here will be automatically enforced
           without requiring the client to separately create any vSphere placement
           policy (such as vSphere compute-policies). For more details, see
           `pyVmomi.vim.vm.VmPlacementPolicy` and different types of placement policies
           derived from it.
           
           Note: These placement policies are only applicable when a VM is managed
           by Supervisor. They will be automatically populated by Supervisor based
           on the placement constraints defined in Supervisor. This field will be
           ignored except when set by Supervisor.
           
           Since setting this field only denotes any additional placement policies
           to be enforced on this VM, any existing placement constraints
           or preferences that this VM is already part of will still apply if this
           field is left unset. For example, if this VM is already part of any
           existing vSphere compute-policies or affinity rules, then they will still
           be considered during this VM's placement.
           
           Since: vSphere API Release 9.1.0.0
   """
   class NpivWwnOp(pyVmomi.VmomiSupport.Enum):
      """
      The root WWN operation mode.
      
      Attributes:
          generate: Generate a new set of WWNs and assign it to the virtual machine.
          set: Take a client-specified set of WWNs (specified in \"wwn\" property) and
              assign them to the virtual machine.
              
              If the new WWN quantity are more
              than existing then we will append them to the existing list of WWNs.
          remove: Remove the currently assigned WWNs from the virtual machine.
          extend: Generate a new set of WWNs and append them to the existing list
      """
      generate: _typing.ClassVar['ConfigSpec.NpivWwnOp'] = 'generate'
      set: _typing.ClassVar['ConfigSpec.NpivWwnOp'] = 'set'
      remove: _typing.ClassVar['ConfigSpec.NpivWwnOp'] = 'remove'
      extend: _typing.ClassVar['ConfigSpec.NpivWwnOp'] = 'extend'

   class EncryptedFtModes(pyVmomi.VmomiSupport.Enum):
      """
      The set of valid encrypted Fault Tolerance modes for a VM.
      
      If the VM is encrypted, its encrypted Fault Tolerance mode
      will be required.
      
      Attributes:
          ftEncryptionDisabled: Do not use encrypted Fault Tolerance, even if available.
          ftEncryptionOpportunistic: Use encrypted Fault Tolerance if source and destination hosts
              support it, fall back to unencrypted Fault Tolerance otherwise.
              
              This is the default option.
          ftEncryptionRequired: Allow only encrypted Fault Tolerance.
              
              If either the source or
              destination host does not support encrypted Fault Tolerance,
              do not allow the Fault Tolerance to occur.
      
      Since: vSphere API Release 7.0.2.0
      """
      ftEncryptionDisabled: _typing.ClassVar['ConfigSpec.EncryptedFtModes'] = 'ftEncryptionDisabled'
      ftEncryptionOpportunistic: _typing.ClassVar['ConfigSpec.EncryptedFtModes'] = 'ftEncryptionOpportunistic'
      ftEncryptionRequired: _typing.ClassVar['ConfigSpec.EncryptedFtModes'] = 'ftEncryptionRequired'

   class EncryptedVMotionModes(pyVmomi.VmomiSupport.Enum):
      """
      The set of valid encrypted vMotion modes for a VM.
      
      If the VM is encrypted, its encrypted vMotion mode will be required.
      
      Attributes:
          disabled: Do not use encrypted vMotion, even if available.
          opportunistic: Use encrypted vMotion if source and destination hosts support it,
              fall back to unencrypted vMotion otherwise.
              
              This is the default option.
          required: Allow only encrypted vMotion.
              
              If the source or destination host does
              not support vMotion encryption, do not allow the vMotion to occur.
      """
      disabled: _typing.ClassVar['ConfigSpec.EncryptedVMotionModes'] = 'disabled'
      opportunistic: _typing.ClassVar['ConfigSpec.EncryptedVMotionModes'] = 'opportunistic'
      required: _typing.ClassVar['ConfigSpec.EncryptedVMotionModes'] = 'required'

   class CpuIdInfoSpec(pyVmomi.vim.option.ArrayUpdateSpec):
      """
      Wrapper class to support incremental updates of the cpuFeatureMask.
      
      As of vSphere API 6.5 `pyVmomi.vim.vm.ConfigSpec.extraConfig` is the recommended method
      for setting the mask for a virtual machine with hardware version 9 and
      above (newer). They can be viewed via
      `pyVmomi.vim.vm.RuntimeInfo.featureMask`.
      """
      info: _typing.Optional[pyVmomi.vim.host.CpuIdInfo] = None

   changeVersion: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   createDate: _typing.Optional[_datetime.datetime] = None
   uuid: _typing.Optional[str] = None
   instanceUuid: _typing.Optional[str] = None
   npivNodeWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivPortWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivWorldWideNameType: _typing.Optional[str] = None
   npivDesiredNodeWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivDesiredPortWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivTemporaryDisabled: _typing.Optional[bool] = None
   npivOnNonRdmDisks: _typing.Optional[bool] = None
   npivWorldWideNameOp: _typing.Optional[str] = None
   locationId: _typing.Optional[str] = None
   guestId: _typing.Optional[str] = None
   alternateGuestName: _typing.Optional[str] = None
   annotation: _typing.Optional[str] = None
   files: _typing.Optional[FileInfo] = None
   tools: _typing.Optional[ToolsConfigInfo] = None
   flags: _typing.Optional[FlagInfo] = None
   consolePreferences: _typing.Optional[ConsolePreferences] = None
   powerOpInfo: _typing.Optional[DefaultPowerOpInfo] = None
   rebootPowerOff: _typing.Optional[bool] = None
   numCPUs: _typing.Optional[int] = None
   vcpuConfig: list[VcpuConfig] = []
   numCoresPerSocket: _typing.Optional[int] = None
   memoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   memoryHotAddEnabled: _typing.Optional[bool] = None
   cpuHotAddEnabled: _typing.Optional[bool] = None
   cpuHotRemoveEnabled: _typing.Optional[bool] = None
   virtualICH7MPresent: _typing.Optional[bool] = None
   virtualSMCPresent: _typing.Optional[bool] = None
   deviceChange: list[pyVmomi.vim.vm.device.VirtualDeviceSpec] = []
   cpuAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   memoryAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None
   cpuAffinity: _typing.Optional[AffinityInfo] = None
   memoryAffinity: _typing.Optional[AffinityInfo] = None
   networkShaper: _typing.Optional[NetworkShaperInfo] = None
   cpuFeatureMask: list[ConfigSpec.CpuIdInfoSpec] = []
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []
   swapPlacement: _typing.Optional[str] = None
   bootOptions: _typing.Optional[BootOptions] = None
   vAppConfig: _typing.Optional[pyVmomi.vim.vApp.VmConfigSpec] = None
   ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
   repConfig: _typing.Optional[ReplicationConfigSpec] = None
   vAppConfigRemoved: _typing.Optional[bool] = None
   vAssertsEnabled: _typing.Optional[bool] = None
   changeTrackingEnabled: _typing.Optional[bool] = None
   firmware: _typing.Optional[str] = None
   maxMksConnections: _typing.Optional[int] = None
   guestAutoLockEnabled: _typing.Optional[bool] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
   extensionCompatibilityConstraint: _typing.Optional[ExtensionCompatibilityConstraintSet] = None
   skipExtensionCompatibilityChecks: _typing.Optional[bool] = None
   memoryReservationLockedToMax: _typing.Optional[bool] = None
   nestedHVEnabled: _typing.Optional[bool] = None
   vPMCEnabled: _typing.Optional[bool] = None
   scheduledHardwareUpgradeInfo: _typing.Optional[ScheduledHardwareUpgradeInfo] = None
   vmProfile: list[ProfileSpec] = []
   messageBusTunnelEnabled: _typing.Optional[bool] = None
   crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   migrateEncryption: _typing.Optional[str] = None
   sgxInfo: _typing.Optional[SgxInfo] = None
   ftEncryptionMode: _typing.Optional[str] = None
   guestMonitoringModeInfo: _typing.Optional[GuestMonitoringModeInfo] = None
   sevEnabled: _typing.Optional[bool] = None
   virtualNuma: _typing.Optional[VirtualNuma] = None
   motherboardLayout: _typing.Optional[str] = None
   pmemFailoverEnabled: _typing.Optional[bool] = None
   vmxStatsCollectionEnabled: _typing.Optional[bool] = None
   vmOpNotificationToAppEnabled: _typing.Optional[bool] = None
   vmOpNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceSwap: _typing.Optional[VirtualDeviceSwap] = None
   simultaneousThreads: _typing.Optional[int] = None
   pmem: _typing.Optional[VirtualPMem] = None
   deviceGroups: _typing.Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: _typing.Optional[bool] = None
   metroFtEnabled: _typing.Optional[bool] = None
   metroFtHostGroup: _typing.Optional[str] = None
   tdxEnabled: _typing.Optional[bool] = None
   sevSnpEnabled: _typing.Optional[bool] = None
   tagSpecs: list[pyVmomi.vim.TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []


class ConfigTarget(pyVmomi.vmodl.DynamicData):
   """
   The ConfigTarget class contains information about \"physical\" devices that can
   be used to back virtual devices.
   
   Attributes:
       numCpus: Number of logical CPUs that can be used to run virtual machines.
           
           If invoked against a cluster, this is the total number of logical CPUs
           available in the cluster.
       numCpuCores: Number of physical CPU cores that are available to run virtual machines.
           
           If invoked against a cluster, this is the total number of physical CPUs
           available in the cluster.
       numNumaNodes: Number of NUMA nodes.
           
           If invoked against a cluster, this is the total number of NUMA nodes
           available in the cluster.
       maxCpusPerHost: Maximum number of CPUs available on a single host.
           
           For standalone hosts, this value will be the same as numCpus.
       smcPresent: Presence of System Management Controller, indicates the host is
           Apple hardware, and thus capable of running Mac OS guest as VM.
       datastore: List of datastores available for virtual disks and associated storage.
       network: List of networks available for virtual network adapters.
       opaqueNetwork: List of opaque networks available for virtual network adapters.
       distributedVirtualPortgroup: List of networks available from DistributedVirtualSwitch for virtual
           network adapters.
       distributedVirtualSwitch: List of distributed virtual switch available for virtual network
           adapters.
       subnetInfo: List of subnets available for virtual network adapters.
           
           Since: vSphere API Release 9.0.0.0
       cdRom: List of CD-ROM devices available for use by virtual CD-ROMs.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualCdrom.AtapiBackingInfo`.
       serial: List of serial devices available to support virtualization.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualSerialPort.DeviceBackingInfo`.
       parallel: List of parallel devices available to support virtualization.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualParallelPort.DeviceBackingInfo`.
       sound: List of sound devices available to support virtualization.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualSoundCard.DeviceBackingInfo`.
       usb: List of USB devices on the host that are available to support
           virtualization.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualUSB.USBBackingInfo`.
       floppy: List of floppy devices available for use by virtual floppies.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualFloppy.DeviceBackingInfo`.
       legacyNetworkInfo: Legacy switch names when using the LegacyNetworkBacking types.
       scsiPassthrough: List of generic SCSI devices.
       scsiDisk: List of physical SCSI disks that can be used as targets for raw disk mapping
           backings.
       ideDisk: List of physical IDE disks that can be used as targets for raw disk backings.
       maxMemMBOptimalPerf: Maximum recommended memory size, in MB, for creating a new virtual machine.
       supportedMaxMemMB: Maximum supported memory size, in MB, for creating a new virtual machine.
           
           Maximum allowed size is smaller of this and limit in
           `pyVmomi.vim.vm.GuestOsDescriptor.supportedMaxMemMB`. When invoked on the
           cluster, maximum size that can be created on at least one host
           in the cluster is reported.
       resourcePool: Information about the current available resources on the current resource pool
           for a virtual machine.
           
           This field is only populated from an Environment browser
           obtained from a virtual machine.
       autoVmotion: Information whether a virtual machine with this ConfigTarget can auto vmotion.
           
           This field is only populated from an Environment browser obtained from a
           virtual machine.
       pciPassthrough: List of generic PCI devices.
       sriov: List of SRIOV devices.
       vFlashModule: List of vFlash modules.
       sharedGpuPassthroughTypes: List of shared GPU passthrough types.
       availablePersistentMemoryReservationMB: Maximum available persistent memory reservation on a compute resource
           in MB.
       dynamicPassthrough: List of Dynamic DirectPath PCI devices.
       sgxTargetInfo: Intel SGX information.
       precisionClockInfo: List of host clock resources available to support virtual precision
           clock device.
           
           Used for
           `pyVmomi.vim.vm.device.VirtualPrecisionClock.SystemClockBackingInfo`
       sevSupported: Indicates whether the compute resource is capable of running AMD Secure
           Encrypted Virtualization (SEV) enabled virtual machines.
           
           The compute
           resource supports SEV when this value is set to true.
           
           Since: vSphere API Release 7.0.1.0
       vgpuDeviceInfo: List of vGPU device capabilities.
           
           Since: vSphere API Release 7.0.3.0
       vgpuProfileInfo: List of vGPU profile attributes.
           
           Since: vSphere API Release 7.0.3.0
       vendorDeviceGroupInfo: List of PCI Vendor Device Groups.
           
           Since: vSphere API Release 8.0.0.1
       maxSimultaneousThreads: Max SMT (Simultaneous multithreading) threads.
           
           Since: vSphere API Release 8.0.0.1
       dvxClassInfo: List of Device Virtualization Extensions (DVX) classes.
           
           Since: vSphere API Release 8.0.0.1
       sevSnpSupported: Indicates whether the compute resource is capable of running AMD Secure
           Encrypted Virtualization Secure Nested Paging (SEV-SNP) enabled virtual
           machines.
           
           The compute resource supports SEV-SNP when this value is set
           to true.
           
           Since: vSphere API Release 9.0.0.0
       tdxSupported: Indicates whether the compute resource is capable of running INTEL Trusted
           Domain Extensions (TDX) enabled virtual machines.
           
           The compute resource
           supports TDX when this value is set to true.
           
           Since: vSphere API Release 9.0.0.0
       vMotionBandwidth: The set of unique vMotion bandwidth(s), in Mbps, set up on the compute
           resource.
           
           Since: vSphere API Release 9.1.0.0
   """
   numCpus: int
   numCpuCores: int
   numNumaNodes: int
   maxCpusPerHost: _typing.Optional[int] = None
   smcPresent: bool
   datastore: list[DatastoreInfo] = []
   network: list[NetworkInfo] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   distributedVirtualPortgroup: list[pyVmomi.vim.dvs.DistributedVirtualPortgroupInfo] = []
   distributedVirtualSwitch: list[pyVmomi.vim.dvs.DistributedVirtualSwitchInfo] = []
   subnetInfo: list[SubnetInfo] = []
   cdRom: list[CdromInfo] = []
   serial: list[SerialInfo] = []
   parallel: list[ParallelInfo] = []
   sound: list[SoundInfo] = []
   usb: list[UsbInfo] = []
   floppy: list[FloppyInfo] = []
   legacyNetworkInfo: list[LegacyNetworkSwitchInfo] = []
   scsiPassthrough: list[ScsiPassthroughInfo] = []
   scsiDisk: list[ScsiDiskDeviceInfo] = []
   ideDisk: list[IdeDiskDeviceInfo] = []
   maxMemMBOptimalPerf: int
   supportedMaxMemMB: _typing.Optional[int] = None
   resourcePool: _typing.Optional[pyVmomi.vim.ResourcePool.RuntimeInfo] = None
   autoVmotion: _typing.Optional[bool] = None
   pciPassthrough: list[PciPassthroughInfo] = []
   sriov: list[SriovInfo] = []
   vFlashModule: list[VFlashModuleInfo] = []
   sharedGpuPassthroughTypes: list[PciSharedGpuPassthroughInfo] = []
   availablePersistentMemoryReservationMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dynamicPassthrough: list[DynamicPassthroughInfo] = []
   sgxTargetInfo: _typing.Optional[SgxTargetInfo] = None
   precisionClockInfo: list[PrecisionClockInfo] = []
   sevSupported: _typing.Optional[bool] = None
   vgpuDeviceInfo: list[VgpuDeviceInfo] = []
   vgpuProfileInfo: list[VgpuProfileInfo] = []
   vendorDeviceGroupInfo: list[VendorDeviceGroupInfo] = []
   maxSimultaneousThreads: _typing.Optional[int] = None
   dvxClassInfo: list[DvxClassInfo] = []
   sevSnpSupported: _typing.Optional[bool] = None
   tdxSupported: _typing.Optional[bool] = None
   vMotionBandwidth: list[pyVmomi.VmomiSupport.long] = []


class ConsolePreferences(pyVmomi.vmodl.DynamicData):
   """
   Preferences for the legacy console application that affect the way it behaves during power
   operations on the virtual machine.
   
   Attributes:
       powerOnWhenOpened: Power on the virtual machine when it is opened in the console.
       enterFullScreenOnPowerOn: Enter full screen mode when this virtual machine is powered on.
       closeOnPowerOffOrSuspend: Close the console application when the virtual machine is powered off
           or suspended.
   """
   powerOnWhenOpened: _typing.Optional[bool] = None
   enterFullScreenOnPowerOn: _typing.Optional[bool] = None
   closeOnPowerOffOrSuspend: _typing.Optional[bool] = None


class ContentLibraryItemInfo(pyVmomi.vmodl.DynamicData):
   """
   Describes the content library item information
   associated with the virtual machine.
   
   Attributes:
       contentLibraryItemUuid: The content library item UUID
       contentLibraryItemVersion: The content library item version is determined and
           managed by content library and this field stamps the version
           provided by CL to the VM.
   """
   contentLibraryItemUuid: str
   contentLibraryItemVersion: _typing.Optional[str] = None


class DatastoreInfo(TargetInfo):
   """
   DatastoreInfo describes a datastore that a virtual disk can be
   stored on.
   
   Attributes:
       datastore: Information about the datastore
       capability: Information about the datastore capabilities
       maxFileSize: The maximum size of a file that can reside on this datastore.
       maxVirtualDiskCapacity: The maximum capacity of a virtual disk which can be created on this volume
       maxPhysicalRDMFileSize: Maximum raw device mapping size (physical compatibility)
       maxVirtualRDMFileSize: Maximum raw device mapping size (virtual compatibility)
       mode: Access mode for this datastore.
           
           This is either
           readOnly or readWrite. A virtual disk needs to be
           stored on readWrite datastore. ISOs can be read
           from a readOnly datastore.
       vStorageSupport: Indicate the states of vStorage hardware acceleration
           support for this datastore.
           
           In the case of a cluster compute resource, this property
           is aggregated from the values reported by individual hosts
           as follows:
           - If at least one host reports
             `vStorageSupported`,
             then it is set to
             `vStorageSupported`.
           - Else if at least one host reports
             `vStorageUnknown`,
             it is set to
             `vStorageUnknown`.
           - Else if at least one host reports
             `vStorageUnsupported`,
             it is set to
             `vStorageUnsupported`.
           - Else it is unset.
       supportedVDiskFormats: A list of virtual disk format types which are supported
           on that datastore.
           
           See `pyVmomi.vim.Datastore.SectorFormat` for the list
           of supported types.
           
           Since: vSphere API Release 9.0.0.0
   """
   datastore: pyVmomi.vim.Datastore.Summary
   capability: pyVmomi.vim.Datastore.Capability
   maxFileSize: pyVmomi.VmomiSupport.long
   maxVirtualDiskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxPhysicalRDMFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxVirtualRDMFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   mode: str
   vStorageSupport: _typing.Optional[str] = None
   supportedVDiskFormats: list[str] = []


class DatastoreOption(pyVmomi.vmodl.DynamicData):
   """
   The DatastoreOption data object describes datastore options
   for a virtual machine.
   
   Attributes:
       unsupportedVolumes: The type of file system volumes on which this virtual machine cannot have
           its disk and configuration files.
   """
   class FileSystemVolumeOption(pyVmomi.vmodl.DynamicData):
      """
      This data object type describes a file system volume option for this
      virtual machine.
      
      Attributes:
          fileSystemType: The type name of the file system volume information object for this
              option.
          majorVersion: The major version of the file system volume information for this
              option.
              
              If not specified, all versions of this file system are included
              in this option. Currently, this value is set only for VMFS volumes.
      """
      fileSystemType: type
      majorVersion: _typing.Optional[int] = None

   unsupportedVolumes: list[DatastoreOption.FileSystemVolumeOption] = []


class DefaultPowerOpInfo(pyVmomi.vmodl.DynamicData):
   """
   The DefaultPowerOpInfo data object type holds the configured defaults for the power
   operations on a virtual machine.
   
   The properties indicated whether to do a \"soft\"
   or guest initiated operation, or a \"hard\" operation.
   
   Attributes:
       powerOffType: Describes the default power off type for this virtual machine.
           
           The possible values are specified by the PowerOpType.
           - hard - Perform power off by using the PowerOff method.
           - soft - Perform power off by using the ShutdownGuest method.
           - preset - The preset value is specified in the defaultPowerOffType
             section.
             
           This setting is advisory and clients can choose to ignore it.
       suspendType: Describes the default suspend type for this virtual machine.
           
           The possible values are specified by the PowerOpType.
           - hard - Perform suspend by using the Suspend method.
           - soft - Perform suspend by using the StandbyGuest method.
           - preset - The preset value is specified in the defaultSuspendType
             section.
             
           This setting is advisory and clients can choose to ignore it.
       resetType: Describes the default reset type for this virtual machine.
           
           The possible values are specified by the PowerOpType.
           - hard - Perform reset by using the Reset method.
           - soft - Perform reset by using the RebootGuest method.
           - preset - The preset value is specified in the defaultResetType
             section.
             
           This setting is advisory and clients can choose to ignore it.
       defaultPowerOffType: Default operation for power off: soft or hard
       defaultSuspendType: Default operation for suspend: soft or hard
       defaultResetType: Default operation for reset: soft or hard
       standbyAction: Behavior of virtual machine when it receives the S1 ACPI call.
   """
   class PowerOpType(pyVmomi.VmomiSupport.Enum):
      """The list of possible default power operations available for the virtual machine"""
      soft: _typing.ClassVar['DefaultPowerOpInfo.PowerOpType'] = 'soft'
      hard: _typing.ClassVar['DefaultPowerOpInfo.PowerOpType'] = 'hard'
      preset: _typing.ClassVar['DefaultPowerOpInfo.PowerOpType'] = 'preset'

   class StandbyActionType(pyVmomi.VmomiSupport.Enum):
      """
      The list of possible standby actions that the virtual machine can take
      for S1 ACPI.
      """
      checkpoint: _typing.ClassVar['DefaultPowerOpInfo.StandbyActionType'] = 'checkpoint'
      powerOnSuspend: _typing.ClassVar['DefaultPowerOpInfo.StandbyActionType'] = 'powerOnSuspend'

   powerOffType: _typing.Optional[str] = None
   suspendType: _typing.Optional[str] = None
   resetType: _typing.Optional[str] = None
   defaultPowerOffType: _typing.Optional[str] = None
   defaultSuspendType: _typing.Optional[str] = None
   defaultResetType: _typing.Optional[str] = None
   standbyAction: _typing.Optional[str] = None


class ProfileSpec(pyVmomi.vmodl.DynamicData):
   """
   The ProfileSpec data object is used to specify the Storage Policy to be
   associated with a Virtual Machine Home or a Virtual Disk.
   """
   pass

class DefaultProfileSpec(ProfileSpec):
   """
   Used to indicate that the Default Storage Policy of the target datastore
   be used for a Virtual Machine Home or a Virtual Disk object.
   
   Neither the association nor the policy data is persisted in Virtual Machine
   configuration. This data is managed by an extension of Virtual Center
   (Storage Policy Based Management).
   """
   pass


class DefinedProfileSpec(ProfileSpec):
   """
   Policy specification that carries a pre-defined Storage Policy to be associated
   with a Virtual Machine Home or a Virtual Disk object.
   
   Such a pre-defined
   policy can be either be vSphere Storage Administrator defined or may come
   from a set of pre-defined policies from Storage Vendor.
   
   Neither the association nor the policy data is persisted in Virtual Machine
   configuration. This data is managed by the an extension of Virtual Center
   (Storage Policy Based Management).
   
   Attributes:
       profileId: Storage Policy Profile identification - Should be
           pbm.profileId but for implementation reasons, could not be.
       replicationSpec: Specification containing replication related parameters, sent to the Replication Data Service
           provider.
       profileData: Profile data sent to the Storage Backend by vSphere.
           
           This data is provided by the SPBM component of the vSphere platform.
           This field should not be set by Virtual Center users.
       profileParams: Parameterized Storage Profiles
           Extra configuration that is not expressed as a capability in the Profile
           definition.
   """
   profileId: str
   replicationSpec: _typing.Optional[pyVmomi.vim.vm.replication.ReplicationSpec] = None
   profileData: _typing.Optional[ProfileRawData] = None
   profileParams: list[pyVmomi.vim.KeyValue] = []


class DeviceRuntimeInfo(pyVmomi.vmodl.DynamicData):
   """
   The DeviceRuntimeInfo data object type provides information about
   the execution state of a single virtual device.
   
   Attributes:
       runtimeState: The device runtime state.
       key: The device key.
   """
   class DeviceRuntimeState(pyVmomi.vmodl.DynamicData):
      """
      Runtime state of a device.
      
      Subclassed for information that is specific
      to certain device types.
      """
      pass

   class VirtualEthernetCardRuntimeState(DeviceRuntimeInfo.DeviceRuntimeState):
      """
      Runtime state of a virtual ethernet card device.
      
      Attributes:
          vmDirectPathGen2Active: Flag to indicate whether VMDirectPath Gen 2 is active on this device.
              
              If false, the reason(s) for inactivity will be provided in one or
              more of `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonVm`,
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonOther`,
              and `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonExtended`.
          vmDirectPathGen2InactiveReasonVm: If `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2Active` is false, this array will be
              populated with reasons for the inactivity that are related to virtual
              machine state or configuration (chosen from
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm`).
              
              Other reasons for
              inactivity will be provided in
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonOther`. If there is a reason
              for inactivity that cannot be described by the available constants,
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonExtended` will be populated
              with an additional explanation provided by the platform.
              
              Note that this list of reasons is not guaranteed to be exhaustive.
          vmDirectPathGen2InactiveReasonOther: If `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2Active` is false, this array will be
              populated with reasons for the inactivity that are not related to
              virtual machine state or configuration (chosen from
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonOther`).
              
              Virtual machine
              related reasons for inactivity will be provided in
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonVm`. If there is a reason
              for inactivity that cannot be described by the available constants,
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonExtended` will be populated
              with an additional explanation provided by the platform.
              
              Note that this list of reasons is not guaranteed to be exhaustive.
          vmDirectPathGen2InactiveReasonExtended: If `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2Active` is false, this property may
              contain an explanation provided by the platform, beyond the reasons
              (if any) enumerated in `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonVm`
              and/or `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.vmDirectPathGen2InactiveReasonOther`.
          uptv2Active: Flag to indicate whether UPTv2(Uniform Pass-through version 2) is active
              on this device.
              
              If true, the network adapter works in the pass-through mode.
              If false, the network adapter still has the network connectivity but
              works in emulated mode and pass-through is not enabled.
              The reason for inactivity is provided in `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2InactiveReasonVm`
              and/or `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2InactiveReasonOther`.
              This flag is unset if not applicable. It indicates network adapter is not a
              vmxnet3 adapter or `pyVmomi.vim.vm.device.VirtualVmxnet3.uptv2Enabled` of it
              is not set to true.
              
              Since: vSphere API Release 8.0.0.1
          uptv2InactiveReasonVm: When `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2Active` is false, this field will be
              populated with reasons for the inactivity that are related to virtual
              machine state or configuration (chosen from
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm`).
              
              Other reasons for
              inactivity will be provided in `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2InactiveReasonOther`.
              This field will be unset if `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2Active` is true or unset.
              
              Note that this field of reasons is not guaranteed to be exhaustive.
              
              Since: vSphere API Release 8.0.0.1
          uptv2InactiveReasonOther: When `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2Active` is false, this field will be
              populated with reasons for the inactivity that are not related to
              virtual machine state or configuration (chosen from
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonOther`).
              
              Virtual machine
              related reasons for inactivity will be provided in
              `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2InactiveReasonVm`.
              This field will be unset if `pyVmomi.vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.uptv2Active` is true or unset.
              
              Note that this field of reasons is not guaranteed to be exhaustive.
              
              Since: vSphere API Release 8.0.0.1
          reservationStatus: The status indicating whether network reservation requirement is violated
              or not on the virtual network adapter.
              
              See `pyVmomi.vim.ManagedEntity.Status`
              for possible values.
              
              `red` indicates that reservation specified on the virtual
              network adapter is not being fulfilled. This can happen if the reservation requested is
              greater than the available capacity reserved for virtual machine traffic on the host.
              
              `green` indicates that the reservation specified on the
              virtual network adapter is being fulfilled.
          attachmentStatus: The status indicating the state of virtual network adapter's attachment
              to an opaque network.
              
              See `pyVmomi.vim.ManagedEntity.Status` for possible values.
              
              `red` indicates that the network adapter
              is not yet successfully attached to opaque network. This can happen if
              corresponding attachment port is missing in the kernel.
              
              `green` indicates that the network
              adapter is successfully attached to opaque network.
          featureRequirement: These network adapter requirements must have equivalent capabilities
              on the virtual switch in order to power on or migrate to the host.
      """
      class VmDirectPathGen2InactiveReasonVm(pyVmomi.VmomiSupport.Enum):
         """
         Attributes:
             vmNptIncompatibleGuest: The virtual machine's guest OS does not support
                 VMDirectPath Gen 2.
             vmNptIncompatibleGuestDriver: The virtual machine's guest network driver does not support
                 VMDirectPath Gen 2.
             vmNptIncompatibleAdapterType: The device type does not support VMDirectPath Gen 2.
             vmNptDisabledOrDisconnectedAdapter: The virtual machine's network adapter is disabled or
                 disconnected, and thus is not participating in VMDirectPath Gen 2.
             vmNptIncompatibleAdapterFeatures: The virtual machine's network adapter has features enabled
                 which preclude it participating in VMDirectPath Gen 2 such
                 as INT-x or PXE booting.
             vmNptIncompatibleBackingType: The device backing is not a DistributedVirtualPortBacking.
             vmNptInsufficientMemoryReservation: The virtual machine does not have full memory reservation
                 required to activate VMDirectPath Gen 2.
             vmNptFaultToleranceOrRecordReplayConfigured: The virtual machine is configured for Fault Tolerance or
                 Record & Replay, which prevents VMDirectPath Gen 2.
             vmNptConflictingIOChainConfigured: Some networking feature has placed a conflicting IOChain on
                 the network adapter, which prevents VMDirectPath Gen 2.
                 
                 Examples
                 include DVFilter.
             vmNptMonitorBlocks: The virtual machine monitor is exercising functionality which
                 which prevents VMDirectPath Gen 2.
             vmNptConflictingOperationInProgress: VMDirectPath Gen 2 is temporarily suspended while the virtual
                 machine executes an operation such as suspend.
             vmNptRuntimeError: VMDirectPath Gen 2 is unavailable due to an unforeseen runtime error
                 in the virtualization platform (typically resource constraints.)
             vmNptOutOfIntrVector: VMDirectPath Gen 2 is unavailable due to host run out of intr
                 vector in host.
                 
                 Guest can configure the vNIC to use less rx/tx
                 queues or use MSI instead of MSIX.
             vmNptVMCIActive: VMDirectPath Gen 2 is unavailable due to Incompatibe feature
                 VMCI is active in the current VM.
                 
                 Kill the relevant VMCI
                 application(s) and restart the VM will allow the vNIC(s) to enter
                 passthrough mode.
         """
         vmNptIncompatibleGuest: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuest'
         vmNptIncompatibleGuestDriver: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuestDriver'
         vmNptIncompatibleAdapterType: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterType'
         vmNptDisabledOrDisconnectedAdapter: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptDisabledOrDisconnectedAdapter'
         vmNptIncompatibleAdapterFeatures: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterFeatures'
         vmNptIncompatibleBackingType: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleBackingType'
         vmNptInsufficientMemoryReservation: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptInsufficientMemoryReservation'
         vmNptFaultToleranceOrRecordReplayConfigured: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptFaultToleranceOrRecordReplayConfigured'
         vmNptConflictingIOChainConfigured: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingIOChainConfigured'
         vmNptMonitorBlocks: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptMonitorBlocks'
         vmNptConflictingOperationInProgress: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingOperationInProgress'
         vmNptRuntimeError: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptRuntimeError'
         vmNptOutOfIntrVector: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptOutOfIntrVector'
         vmNptVMCIActive: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm'] = 'vmNptVMCIActive'

      class VmDirectPathGen2InactiveReasonOther(pyVmomi.VmomiSupport.Enum):
         """
         Attributes:
             vmNptIncompatibleHost: The virtual machine's host does not support VMDirectPath Gen 2.
             vmNptIncompatibleNetwork: The configuration or state of the attached network prevents
                 VMDirectPath Gen 2.
                 
                 Refer to
                 `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonNetwork`
                 and/or
                 `pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo.vmDirectPathGen2InactiveReasonExtended`
                 in the RuntimeInfo of the DistributedVirtualPort connected to this
                 device.
         """
         vmNptIncompatibleHost: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleHost'
         vmNptIncompatibleNetwork: _typing.ClassVar['DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleNetwork'

      vmDirectPathGen2Active: _typing.Optional[bool] = None
      vmDirectPathGen2InactiveReasonVm: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: _typing.Optional[str] = None
      uptv2Active: _typing.Optional[bool] = None
      uptv2InactiveReasonVm: list[str] = []
      uptv2InactiveReasonOther: list[str] = []
      reservationStatus: _typing.Optional[str] = None
      attachmentStatus: _typing.Optional[str] = None
      featureRequirement: list[FeatureRequirement] = []

   runtimeState: DeviceRuntimeInfo.DeviceRuntimeState
   key: int


class DiskDeviceInfo(TargetInfo):
   """
   The DiskDeviceInfo class contains basic information about a specific disk hardware
   device.
   
   Attributes:
       capacity: Size of disk
       vm: List of known virtual machines using this physical disk as a backing
   """
   capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vm: list[pyVmomi.vim.VirtualMachine] = []


class DvxClassInfo(pyVmomi.vmodl.DynamicData):
   """
   Description of a Device Virtualization Extensions (DVX) device class.
   
   Attributes:
       deviceClass: DVX device class.
       vendorName: The label for the vendor name of this class.
           
           The value is defined by vendors of the DVX device class
           as part of their localizable messages.
       sriovNic: Indicates whether the devices of this class are SR-IOV NICs.
       configParams: The configuration parameters for this DVX device class.
   
   Since: vSphere API Release 8.0.0.1
   """
   deviceClass: pyVmomi.vim.ElementDescription
   vendorName: str
   sriovNic: bool
   configParams: list[pyVmomi.vim.option.OptionDef] = []


class DynamicPassthroughInfo(TargetInfo):
   """
   Description of a Dynamic DirectPath PCI device.
   
   Attributes:
       vendorName: The vendor name of this PCI device.
       deviceName: The device name of this PCI device.
       customLabel: The custom label attached to this PCI device.
       vendorId: PCI vendor ID for this device.
       deviceId: PCI device ID for this device.
   """
   vendorName: str
   deviceName: str
   customLabel: _typing.Optional[str] = None
   vendorId: int
   deviceId: int

class EmptyIndependentFilterSpec(BaseIndependentFilterSpec):
   """
   The EmptyIndependentFilterSpec data object is used to specify empty independent
   filter spec.
   
   This object is passed during provisioning workflows to remove all
   attached independent filters.
   
   Since: vSphere API Release 7.0.2.1
   """
   pass

class EmptyProfileSpec(ProfileSpec):
   """
   Specifies an empty Storage Policy for a Virtual Machine Home or a
   Virtual Disk object.
   
   The object is left without any profile association, and hence has no
   explicit policy driven requirements.
   This implies that object's policy driven SLAs are always met trivially.
   """
   pass


class ExtensionCompatibilityConstraint(pyVmomi.vmodl.DynamicData):
   """
   A compatibility constraint declared by a managing extension on a virtual
   machine it manages.
   
   Constraints let a managing extension (identified by
   `pyVmomi.vim.ext.ManagedByInfo`) tell vCenter which properties of a
   managed virtual machine must be protected during operations that would change
   them (for example, relocate or reconfigure). vCenter enforces the constraints
   in the compatibility-check pipeline so that operations which would break the
   extension's assumptions are rejected.
   
   Enforcement is a vCenter mechanism. Operations invoked directly against an
   ESXi host bypass vCenter's compatibility-check pipeline, so these constraints
   are not evaluated on that path.
   
   A constraint has two orthogonal dimensions:
   - `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintType` identifies what property is constrained
     (for example, the resource pool or the storage policy).
   - `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintKind` identifies how the constraint is
     evaluated (for example, the property must not change).
     
   The same property can therefore be constrained in different ways without
   changing this type.
   
   Within a single virtual machine, a constraint's identity is the combination
   of its `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintType` and `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintKind`; that pair is what
   vCenter evaluates against. A virtual machine may carry at most one constraint
   per (constraintType, constraintKind): supplying more than one with the same
   pair is rejected as invalid input rather than silently collapsed.
   `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintName` plays no part in this identity.
   
   Attributes:
       constraintName: An optional descriptive label for the constraint, chosen by the managing
           extension (for example, \"pool-invariant\"), used for identification and
           diagnostics such as constraint reads and violation messages.
           
           The name is descriptive only. It is not required to be unique (extensions
           typically reuse the same names across all the virtual machines they
           manage) and it is not used to evaluate or identify the constraint; the
           constraint's identity is its `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintType` and
           `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintKind`.
       constraintType: The property that this constraint protects.
           
           The values defined today are
           enumerated by `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.ConstraintType` (for example,
           `POOL`). An unrecognized value causes the create or
           reconfigure operation that registers the constraint to fail.
       constraintKind: How the constraint is evaluated.
           
           The only kind defined today is
           `INVARIANT`, which asserts that the
           `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintType` must not change from the virtual
           machine's current value. This field is required and must be set
           explicitly so that a constraint's (constraintType, constraintKind)
           identity is always unambiguous. An unrecognized value causes the create
           or reconfigure operation that registers the constraint to fail.
   
   Since: vSphere API Release 9.1.2.0
   """
   class ConstraintType(pyVmomi.VmomiSupport.Enum):
      """
      The set of `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintType` values defined in this release.
      
      Attributes:
          SERVICE: The virtual machine's vCenter service (cross-vCenter move).
          FOLDER: The virtual machine's folder.
          POOL: The virtual machine's resource pool.
          VM_STORAGE_POLICY: The virtual machine-level storage policy.
          DISK_STORAGE_POLICY: Per-disk storage policies.
          DEVICE: Virtual device configuration (for example, device backings).
      
      Since: vSphere API Release 9.1.2.0
      """
      SERVICE: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'SERVICE'
      FOLDER: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'FOLDER'
      POOL: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'POOL'
      VM_STORAGE_POLICY: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'VM_STORAGE_POLICY'
      DISK_STORAGE_POLICY: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'DISK_STORAGE_POLICY'
      DEVICE: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintType'] = 'DEVICE'

   class ConstraintKind(pyVmomi.VmomiSupport.Enum):
      """
      The set of `pyVmomi.vim.vm.ExtensionCompatibilityConstraint.constraintKind` values defined in this release.
      
      Attributes:
          INVARIANT: The constrained property must not change from the virtual machine's
              current value.
      
      Since: vSphere API Release 9.1.2.0
      """
      INVARIANT: _typing.ClassVar['ExtensionCompatibilityConstraint.ConstraintKind'] = 'INVARIANT'

   constraintName: _typing.Optional[str] = None
   constraintType: str
   constraintKind: str


class ExtensionCompatibilityConstraintSet(pyVmomi.vmodl.DynamicData):
   """
   Represents the set of `pyVmomi.vim.vm.ExtensionCompatibilityConstraint` objects
   declared on a virtual machine.
   
   An empty `pyVmomi.vim.vm.ExtensionCompatibilityConstraintSet.constraint` array means no
   constraints are declared. See the field using this type (for example
   `pyVmomi.vim.vm.ConfigSpec.extensionCompatibilityConstraint`) for how this
   type is used during create and reconfigure.
   
   Attributes:
       constraint: The extension compatibility constraints in this set.
           
           See
           `pyVmomi.vim.vm.ExtensionCompatibilityConstraint` for the meaning of an
           individual constraint.
   
   Since: vSphere API Release 9.1.2.0
   """
   constraint: list[ExtensionCompatibilityConstraint] = []


class FaultToleranceConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   FaultToleranceConfigInfo is a data object type containing Fault Tolerance
   settings for this virtual machine.
   
   role, instanceUuids and configPaths contain information about the
   whole fault tolerance group.
   
   Attributes:
       role: The index of the current VM in instanceUuids array starting from 1, so
           1 means that it is the primary VM.
       instanceUuids: The instanceUuid of all the VMs in this fault tolerance group.
           
           The
           first element is the instanceUuid of the primary VM.
       configPaths: The configuration file path for all the VMs in this fault tolerance
           group.
       orphaned: Indicates whether a secondary VM is orphaned (no longer associated with
           the primary VM).
   """
   role: int
   instanceUuids: list[str] = []
   configPaths: list[str] = []
   orphaned: _typing.Optional[bool] = None


class FaultToleranceConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   FaultToleranceConfigSpec contains information about the metadata file
   and vmdk files for a fault tolerant VM pair.
   
   Attributes:
       metaDataPath: Metadata file information
       secondaryVmSpec: Placement information for secondary
       metroFtEnabled: Indicates whether FT Metro Cluster is enabled/disabled.
           
           \\- If TRUE, FT Metro Cluster is enabled for the VM. An implicit
           Anti-HostGroup will be generated from HostGroup defined for FT
           primary, then affine the primary with one HostGroup and affine the
           secondary with another HostGroup.
           \\- If FALSE or unset, FT Metro Cluster is disabled for the VM. Both FT
           primary and secondary will be put in the same HostGroup.
           
           Since: vSphere API Release 8.0.3.0
       metroFtHostGroup: Indicate the Host Group (`pyVmomi.vim.cluster.HostGroup`) for FT
           Metro Cluster enabled Virtual Machine.
           
           Based on the selected Host Group, FT can divide the hosts in the cluster
           into two groups and ensure to place FT primary and FT secondary in
           different groups.
           
           Since: vSphere API Release 8.0.3.0
   """
   metaDataPath: _typing.Optional[FaultToleranceMetaSpec] = None
   secondaryVmSpec: _typing.Optional[FaultToleranceVMConfigSpec] = None
   metroFtEnabled: _typing.Optional[bool] = None
   metroFtHostGroup: _typing.Optional[str] = None


class FaultToleranceMetaSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object encapsulates the Datastore for the shared metadata file
   for a fault tolerant pair of VMs.
   
   Attributes:
       metaDataDatastore: Datastore for the metadata file
   """
   metaDataDatastore: pyVmomi.vim.Datastore


class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
   """
   FaultTolerancePrimaryConfigInfo is a data object type containing Fault Tolerance
   settings for a primary virtual machine in a fault tolerance group
   """
   secondaries: list[pyVmomi.vim.VirtualMachine] = []


class FaultToleranceSecondaryConfigInfo(FaultToleranceConfigInfo):
   """
   FaultToleranceSecondaryConfigInfo is a data object type containing Fault Tolerance
   settings for a secondary virtual machine in a fault tolerance group
   """
   primaryVM: pyVmomi.vim.VirtualMachine


class FaultToleranceSecondaryOpResult(pyVmomi.vmodl.DynamicData):
   """
   FaultToleranceSecondaryOpResult is a data object that reports on
   the outcome of the `pyVmomi.vim.VirtualMachine.createSecondary` or
   `pyVmomi.vim.VirtualMachine.enableSecondary` operation.
   
   Attributes:
       vm: The Secondary VirtualMachine
       powerOnAttempted: Whether an attempt was made to power on the secondary.
           
           If
           an attempt was made, `pyVmomi.vim.vm.FaultToleranceSecondaryOpResult.powerOnResult` will report the
           status of this attempt.
       powerOnResult: The powerOnResult property reports the outcome of powering on the
           Secondary VirtualMachine if a power on was required.
           
           A power on will
           be attempted if the Primary Virtual Machine is powered on when the
           operation is performed. This object is only reported if `pyVmomi.vim.vm.FaultToleranceSecondaryOpResult.powerOnAttempted` is true. If the outcome of the power-on attempt
           is not successful, the returned `pyVmomi.vim.cluster.PowerOnVmResult`
           object will include an instance of `pyVmomi.vim.cluster.NotAttemptedVmInfo`
           whereas if the attempt was successful, then an instance of
           `pyVmomi.vim.cluster.AttemptedVmInfo` is returned. When
           `pyVmomi.vim.cluster.AttemptedVmInfo` is returned, its
           `pyVmomi.vim.cluster.AttemptedVmInfo.task` property is only set if the cluster
           is a HA-only cluster.
   """
   vm: pyVmomi.vim.VirtualMachine
   powerOnAttempted: bool
   powerOnResult: _typing.Optional[pyVmomi.vim.cluster.PowerOnVmResult] = None


class FaultToleranceVMConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   FaultToleranceVMConfigSpec contains information about placement of
   fault tolerant VM.
   
   Attributes:
       vmConfig: Datastore for the configuration file for the virtual machine, e.g., the
           .vmx file.
           
           This also implicitly defines the configuration directory.
       disks: Array of disks associated with the VM
   """
   class FaultToleranceDiskSpec(pyVmomi.vmodl.DynamicData):
      """
      FaultToleranceDiskSpec contains disk managed object and destination
      datastore of disks associated with a VM.
      
      Attributes:
          disk: Disk Managed Object
          datastore: Destination location for disk
      """
      disk: pyVmomi.vim.vm.device.VirtualDevice
      datastore: pyVmomi.vim.Datastore

   vmConfig: _typing.Optional[pyVmomi.vim.Datastore] = None
   disks: list[FaultToleranceVMConfigSpec.FaultToleranceDiskSpec] = []


class FeatureRequirement(pyVmomi.vmodl.DynamicData):
   """
   Feature requirement contains a key, featureName and an opaque value
   
   Attributes:
       key: Accessor name to the feature requirement test
       featureName: Name of the feature.
           
           Identical to the key.
       value: Opaque value for the feature operation.
           
           Operation is contained
           in the value.
   """
   key: str
   featureName: str
   value: str


class FileInfo(pyVmomi.vmodl.DynamicData):
   """
   The FileInfo data object type contains the locations of virtual machine
   files other than the virtual disk files.
   
   The configurable parameters
   are all in the FileInfo object.
   
   The object also contains a FileLayout object that returns a complete
   list of additional files that makes up the virtual machine
   configuration. This is a read-only structure and is returned when
   the configuration is read. This is ignored during configuration and
   can be left out.
   
   Attributes:
       vmPathName: Path name to the configuration file for the virtual machine, e.g., the
           .vmx file.
           
           This also implicitly defines the configuration directory.
       snapshotDirectory: Path name of the directory that holds suspend and snapshot files
           belonging to the virtual machine.
           
           Prior to vSphere 5.0, this
           directory also holds snapshot redo files. Starting with vSphere 5.0,
           the redo files will stay in the same directory as the snapshotted
           disk, thus this directory will no longer hold the snapshot redo
           files.
           
           This path name defaults to the same directory as the configuration
           file.
           
           ESX Server requires this to indicate a VMFS volume or NAS volume
           (for ESX Server 3).
           In case the configuration file is not stored on VMFS or NAS, this
           property must be set explicitly.
       suspendDirectory: Some products allow the suspend directory to be different than the
           snapshot directory.
           
           On products where this is not possible, setting
           of this property is ignored.
       logDirectory: Directory to store the log files for the virtual machine.
           
           If not specified,
           this defaults to the same directory as the configuration file,
       ftMetadataDirectory: Directory to store the fault tolerance meta data files for the
           virtual machine.
   """
   vmPathName: _typing.Optional[str] = None
   snapshotDirectory: _typing.Optional[str] = None
   suspendDirectory: _typing.Optional[str] = None
   logDirectory: _typing.Optional[str] = None
   ftMetadataDirectory: _typing.Optional[str] = None


class FileLayout(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 4.0, use `pyVmomi.vim.vm.FileLayoutEx` instead.Describes the set of files that makes up a virtual machine on disk.
   
   The
   file layout is broken into 4 major sections:
   - Configuration: Files stored in the configuration directory
   - Log: Files stored in the log directory
   - Disk: Files stored relative to a disk configuration file
   - Snapshot: Stored in the snapshot directory
     
   Often the same directory is used for configuration, log, disk and
   snapshots.
   
   Attributes:
       configFile: A list of files that makes up the configuration of the virtual machine
           (excluding the .vmx file, since that file is represented in the
           FileInfo).
           
           These are relative paths from the configuration directory. A
           slash is always used as a separator. This list will typically include the
           NVRAM file, but could also include other meta-data files.
       logFile: A list of files stored in the virtual machine's log directory.
           
           These are
           relative paths from the logDirectory. A slash is always used as a
           separator.
       disk: Files making up each virtual disk.
       snapshot: Files of each snapshot.
       swapFile: The swapfile specific to this virtual machine, if any.
           
           This is a
           complete datastore path, not a relative path.
   """
   class DiskLayout(pyVmomi.vmodl.DynamicData):
      """
      Enumerats the set of files for each virtual disk.
      
      Attributes:
          key: Identification of the disk in `pyVmomi.vim.vm.ConfigInfo`.
          diskFile: List of files that makes up the virtual disk.
              
              At least one entry
              always exists in this array. The first entry is the main
              descriptor of the virtual disk (the one used when adding the
              disk to a virtual machine). These are complete datastore paths, not
              relative paths.
      """
      key: int
      diskFile: list[str] = []

   class SnapshotLayout(pyVmomi.vmodl.DynamicData):
      """
      Enumerates the set of files that make up a snapshot or redo-point
      
      Attributes:
          key: Identification of the snapshot
          snapshotFile: A list of files that make up the snapshot state.
              
              These are relative
              paths from the snapshotDirectory. A slash is always used as a
              separator.
      """
      key: Snapshot
      snapshotFile: list[str] = []

   configFile: list[str] = []
   logFile: list[str] = []
   disk: list[FileLayout.DiskLayout] = []
   snapshot: list[FileLayout.SnapshotLayout] = []
   swapFile: _typing.Optional[str] = None


class FileLayoutEx(pyVmomi.vmodl.DynamicData):
   """
   Detailed description of files that make up a virtual machine on disk.
   
   The
   file layout is broken into 4 major sections:
   - Configuration: Files stored in the configuration directory
   - Log: Files stored in the log directory
   - Disk: Files stored relative to a disk configuration file
   - Snapshot: Stored in the snapshot directory
     
   Often the same directory is used for configuration, log, disk and
   snapshots.
   
   Attributes:
       file: Information about all the files that constitute the virtual machine
           including configuration files, disks, swap file, suspend file, log files,
           core files, memory file etc.
           
           `pyVmomi.vim.vm.FileLayoutEx.FileType` lists the
           different file-types that make a virtual machine.
       disk: Layout of each virtual disk attached to the virtual machine.
           
           For a virtual machine with snapshots, this property gives only those disks
           that are attached to it at the current point of running.
       snapshot: Layout of each snapshot of the virtual machine.
       timestamp: Time when values in this structure were last updated.
   """
   class FileType(pyVmomi.VmomiSupport.Enum):
      """
      File-type constants.
      
      Attributes:
          config: Config (vmx) file.
          extendedConfig: Extended config (vmxf) file.
          diskDescriptor: Disk descriptor (vmdk) file.
          diskExtent: Disk extent (-flat/-delta/-s/-rdm/-rdmp.vmdk) file.
          digestDescriptor: Disk digest descriptor file.
          digestExtent: Disk digest extent file.
          diskReplicationState: Host based replicated disk persistent state (psf) file.
          log: Log (log) file.
          stat: Virtual machine statistics (stat) file.
          namespaceData: Namespace data file.
          dataSetsDiskModeStore: DataSets disk mode store (dsd) file.
              
              Since: vSphere API Release 8.0.0.0
          dataSetsVmModeStore: DataSets vm mode store (dsv) file.
              
              Since: vSphere API Release 8.0.0.0
          nvram: Non-volatile RAM (nvram) file.
          snapshotData: Snapshot data (vmsn) file.
          snapshotMemory: Snapshot memory (vmem) file.
          snapshotList: Snapshot metadata (vmsd) file.
          snapshotManifestList: Snapshot manifest metadata (-aux.xml) file.
              
              This file is still being created but is no longer necessary since
              the manifest metadata is now available in the snapshot metadata
              (vmsd) file in vSphere 5.0. This type will be deprecated when
              vSphere 4.1 is no longer supported.
          suspend: Suspend (vmss) file.
          suspendMemory: Suspend (vmem) file.
          swap: Swap (vswp) file.
          uwswap: File generated by VMware ESX kernel for a running virtual
              machine.
          core: Core (core) file.
          screenshot: Screenshot file.
          ftMetadata: Fault Tolerance metadata file.
          guestCustomization: Guest image customization file.
      """
      config: _typing.ClassVar['FileLayoutEx.FileType'] = 'config'
      extendedConfig: _typing.ClassVar['FileLayoutEx.FileType'] = 'extendedConfig'
      diskDescriptor: _typing.ClassVar['FileLayoutEx.FileType'] = 'diskDescriptor'
      diskExtent: _typing.ClassVar['FileLayoutEx.FileType'] = 'diskExtent'
      digestDescriptor: _typing.ClassVar['FileLayoutEx.FileType'] = 'digestDescriptor'
      digestExtent: _typing.ClassVar['FileLayoutEx.FileType'] = 'digestExtent'
      diskReplicationState: _typing.ClassVar['FileLayoutEx.FileType'] = 'diskReplicationState'
      log: _typing.ClassVar['FileLayoutEx.FileType'] = 'log'
      stat: _typing.ClassVar['FileLayoutEx.FileType'] = 'stat'
      namespaceData: _typing.ClassVar['FileLayoutEx.FileType'] = 'namespaceData'
      dataSetsDiskModeStore: _typing.ClassVar['FileLayoutEx.FileType'] = 'dataSetsDiskModeStore'
      dataSetsVmModeStore: _typing.ClassVar['FileLayoutEx.FileType'] = 'dataSetsVmModeStore'
      nvram: _typing.ClassVar['FileLayoutEx.FileType'] = 'nvram'
      snapshotData: _typing.ClassVar['FileLayoutEx.FileType'] = 'snapshotData'
      snapshotMemory: _typing.ClassVar['FileLayoutEx.FileType'] = 'snapshotMemory'
      snapshotList: _typing.ClassVar['FileLayoutEx.FileType'] = 'snapshotList'
      snapshotManifestList: _typing.ClassVar['FileLayoutEx.FileType'] = 'snapshotManifestList'
      suspend: _typing.ClassVar['FileLayoutEx.FileType'] = 'suspend'
      suspendMemory: _typing.ClassVar['FileLayoutEx.FileType'] = 'suspendMemory'
      swap: _typing.ClassVar['FileLayoutEx.FileType'] = 'swap'
      uwswap: _typing.ClassVar['FileLayoutEx.FileType'] = 'uwswap'
      core: _typing.ClassVar['FileLayoutEx.FileType'] = 'core'
      screenshot: _typing.ClassVar['FileLayoutEx.FileType'] = 'screenshot'
      ftMetadata: _typing.ClassVar['FileLayoutEx.FileType'] = 'ftMetadata'
      guestCustomization: _typing.ClassVar['FileLayoutEx.FileType'] = 'guestCustomization'

   class FileInfo(pyVmomi.vmodl.DynamicData):
      """
      Basic information about a file.
      
      Attributes:
          key: Key to reference this file.
          name: Name of the file, including the complete datastore path.
          type: Type of the file.
              
              `pyVmomi.vim.vm.FileLayoutEx.FileType` lists
              all valid values.
          size: Size of the file in bytes.
          uniqueSize: Size of the file in bytes corresponding to the file blocks
              that were allocated uniquely.
              
              In other words, if the underlying
              storage supports sharing of file blocks across disk files, the
              property corresponds to the size of the file blocks that were
              allocated only in context of this file, i.e. it does not include
              shared blocks that were allocated in other files.
              This property will be unset if the underlying implementation
              is unable to compute this information. One example of this
              is when the file resides on a NAS datastore whose underlying
              storage doesn't support this metric. In some cases the field
              might be set but the value could be over-estimated due to
              the inability of the NAS based storage to provide an
              accurate value.
          backingObjectId: Backing object's durable and unmutable identifier.
              
              Each backing object has a unique identifier which is not settable.
              This property is applied to the file backed by a storage object,
              such as vvol.
          accessible: Flag which indicates the accessibility of the file
              when the file info object was created.
      """
      key: int
      name: str
      type: str
      size: pyVmomi.VmomiSupport.long
      uniqueSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      backingObjectId: _typing.Optional[str] = None
      accessible: _typing.Optional[bool] = None

   class DiskUnit(pyVmomi.vmodl.DynamicData):
      """
      Information about a single unit of a virtual disk, such as
      the base-disk or a delta-disk.
      
      A disk-unit consists of at least one descriptor
      file, and zero or more extent files.
      
      Sometimes, a disk-unit is also referred to as a backing.
      
      Attributes:
          fileKey: Array of keys of the files that make up the disk unit.
              
              Values here
              correspond to property `pyVmomi.vim.vm.FileLayoutEx.FileInfo.key` in
              `pyVmomi.vim.vm.FileLayoutEx.file`.
              
              At least one entry always exists in this array. Property
              `pyVmomi.vim.vm.FileLayoutEx.FileInfo.type` of the referenced file
              can be used to distinguish the disk descriptor (type `diskDescriptor`) from the extents.
      """
      fileKey: list[int] = []

   class DiskLayout(pyVmomi.vmodl.DynamicData):
      """
      Layout of a virtual disk, including the base- and delta- disks.
      
      A virtual disk typically is made up of a chain of disk-units.
      
      Attributes:
          key: Identifier for the virtual disk in `pyVmomi.vim.vm.VirtualHardware.device`.
          virtualDiskFormat: The sector format of the virtual disk.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for definitions of supported types. If not
              set, the default value is `native_512`.
              
              Since: vSphere API Release 9.0.0.0
          chain: The disk-unit chain that makes up this virtual disk.
      """
      key: int
      virtualDiskFormat: _typing.Optional[str] = None
      chain: list[FileLayoutEx.DiskUnit] = []

   class SnapshotLayout(pyVmomi.vmodl.DynamicData):
      """
      Layout of a snapshot.
      
      Attributes:
          key: Reference to the snapshot.
          dataKey: Key to the snapshot data file in `pyVmomi.vim.vm.FileLayoutEx.file`.
          memoryKey: Key to the snapshot memory file in `pyVmomi.vim.vm.FileLayoutEx.file`.
              
              Powered off snapshots do not have a memory component and in some cases
              the memory component is combined with the data component. When a memory
              component does not exist, the value is initialized to -1.
          disk: Layout of each virtual disk of the virtual machine when the
              snapshot was taken.
      """
      key: Snapshot
      dataKey: int
      memoryKey: int
      disk: list[FileLayoutEx.DiskLayout] = []

   file: list[FileLayoutEx.FileInfo] = []
   disk: list[FileLayoutEx.DiskLayout] = []
   snapshot: list[FileLayoutEx.SnapshotLayout] = []
   timestamp: _datetime.datetime


class FlagInfo(pyVmomi.vmodl.DynamicData):
   """
   The FlagInfo data object type encapsulates the flag settings
   for a virtual machine.
   
   These properties are optional since the same structure
   is used to change the values during an edit or create operation.
   
   Attributes:
       disableAcceleration: Flag to turn off video acceleration for a virtual machine console window.
       enableLogging: Flag to enable logging for a virtual machine.
       useToe: Flag to specify whether or not to use TOE (TCP/IP Offloading).
       runWithDebugInfo: Flag to specify whether or not to run in debug mode.
       monitorType: vmx process type.
           
           See `pyVmomi.vim.vm.FlagInfo.MonitorType`
           for possible values for this property.
       htSharing: Specifies how the VCPUs of a virtual machine are allowed to
           share physical cores on a hyperthreaded system.
           
           Two VCPUs are
           \"sharing\" a core if they are both running on logical CPUs of
           the core at the same time.
       snapshotDisabled: Flag to specify whether snapshots are disabled for this virtual
           machine.
       snapshotLocked: Flag to specify whether the snapshot tree is locked for this virtual machine.
       diskUuidEnabled: Indicates whether disk UUIDs are being used by this virtual machine.
           
           If this flag is set to false, disk UUIDs are not exposed to the guest.
           
           Since products before ESX 3.1 do not support disk UUIDs, moving virtual
           machines from a platform that supports UUID to a platform that does
           not support UUIDs could result in unspecified guest behavior. For
           virtual machines where the ability to move to older platforms is
           important, this flag should be set to false. If the value is unset,
           the behavior 'false' will be used.
       virtualMmuUsage: Indicates whether or not the system will try to use nested page
           table hardware support, if available.
           
           By default, VMware software will determine whether or not
           to use nested page table hardware support based on various factors such
           as the guest operating system type and the physical hardware.
           Certain workloads can benefit from explicitly turning
           nested page table hardware support on or off; this can be set using
           nptUsage flag.
           If the value is unset, the value will default to automatic.
           
           `pyVmomi.vim.vm.FlagInfo.VirtualMmuUsage` represents the set of
           possible values.
       virtualExecUsage: Indicates whether or not the system will try to use Hardware
           Virtualization (HV) support for instruction virtualization,
           if available.
           
           By default, VMware software will determine whether or not
           to use hardware virtualization support based on various factors such
           as the guest operating system type and the physical hardware.
           Certain workloads can benefit from explicitly turning
           hardware virtualization support on or off.
           If the value is unset, the value will default to hvAuto.
           
           `pyVmomi.vim.vm.FlagInfo.VirtualExecUsage` represents the set of
           possible values.
           
           New processors can enable two hardware acceleration technologies
           for virtualization, one for instruction virtualization and the
           other for MMU virtualization. Intel names its hardware-assisted
           instruction virtualization as VT, and its hardware-assisted
           MMU virtualization as EPT. AMD calls them as AMD-V and RVI,
           respectively. For details on these technologies, please refer
           to documents from the processor vendors.
           
           `pyVmomi.vim.vm.FlagInfo.virtualExecUsage` controls instruction
           virtualization; while `pyVmomi.vim.vm.FlagInfo.virtualMmuUsage`
           controls MMU virtualization. \"On\" allows hardware acceleration,
           while \"off\" only allows software solution.
           
           There are four meaningful combinations.
           
           (hvAuto, automatic) - The host chooses which feature to use.
           (hvOn, on) - Use both VT/AMD-V and EPT/RVI.
           (hvOn, off) - Use VT/AMD-V but do not use EPT/RVI.
           (hvOff, off) - Do not use any of these hardware acceleration technologies.
       snapshotPowerOffBehavior: Specifies the power-off behavior for a virtual machine that has
           a snapshot.
           
           If the value is unset, the behavior 'powerOff' will
           be used.
       recordReplayEnabled: Flag to specify whether record and replay operations are
           allowed for this virtual machine.
           
           If this flag is set to 'true', instruction virtualization
           will use hardware virtualization (HV) support. I.e.,
           virtualExecUsage will be set to 'hvOn'.
           If this flag is set to 'false' for a virtual machine that
           already has a recording, replay will be disallowed, though
           the recording will be preserved.
           If the value is unset, the behavior 'false' will be used.
       faultToleranceType: Indicates the type of fault tolerance type the virtual machine is
           configured to use.
           
           `pyVmomi.vim.VirtualMachine.FaultToleranceType` represents the set of
           possible values.
       cbrcCacheEnabled: Flag to specify whether common CBRC digest cache is enabled for this
           virtual machine.
           
           The common CBRC cache is shared between the hot added disks in the VM.
           If this flag is set to 'true' the VM will allocate a common digest
           cache on power on.
       vvtdEnabled: Flag to specify if Intel Virtualization Technology for Directed I/O
           is enabled for this virtual machine.
           
           When creating a new VM:
           \\- If vim.vm.FlagInfo.vbsEnabled is set to `true`,
           and this flag is set to `false` error is returned.
           \\- If this flag is unset and vim.vm.FlagInfo.vbsEnabled is set to
           `true`, the value of this flag is set to `true`.
       vbsEnabled: Flag to specify if Virtualization-based security
           is enabled for this virtual machine.
           
           If set to `true` when creating a new VM, the following VM
           properties might be modified automatically:
           \\- If vim.vm.FlagInfo.vvtdEnabled is not set to `false`,
           it is set to `true`. Else error is returned.
           \\- If vim.vm.ConfigSpec.nestedHVEnabled is not set to `false`,
           it is set to `true`. Else error is returned.
           \\- If vim.vm.BootOptions.efiSecureBootEnabled is not set to
           `false`, it is set to `true`. Else error is
           returned.
           \\- If vim.vm.firmware is not set to `bios`, it is set
           to `efi`. Else error is returned.
   """
   class HtSharing(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: as of vSphere API 6.7.Set of possible values for `pyVmomi.vim.vm.FlagInfo.htSharing`.
      
      Attributes:
          any: VCPUs may freely share cores at any time with any other
              VCPUs (default for all virtual machines on a hyperthreaded
              system).
          none: VCPUs should not share cores with each other or with VCPUs
              from other virtual machines.
              
              That is, each VCPU from this
              virtual machine should always get a whole core to itself,
              with the other logical CPU on that core being placed into
              the \"halted\" state.
          internal: Similar to \"none\", in that VCPUs from this virtual machine
              will not be allowed to share cores with VCPUs from other
              virtual machines.
              
              However, other VCPUs from the same virtual
              machine will be allowed to share cores together. This
              configuration option is only permitted for SMP virtual
              machines. If applied to a uniprocessor virtual machine, it
              will be converted to the \"none\" sharing option.
      """
      any: _typing.ClassVar['FlagInfo.HtSharing'] = 'any'
      none: _typing.ClassVar['FlagInfo.HtSharing'] = 'none'
      internal: _typing.ClassVar['FlagInfo.HtSharing'] = 'internal'

   class PowerOffBehavior(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for `pyVmomi.vim.vm.FlagInfo.snapshotPowerOffBehavior`.
      
      Attributes:
          powerOff: Just power off the virtual machine.
          revert: Revert to the snapshot.
          prompt: Prompt the user for instructions at power-off time.
          take: Take a new snapshot.
      """
      powerOff: _typing.ClassVar['FlagInfo.PowerOffBehavior'] = 'powerOff'
      revert: _typing.ClassVar['FlagInfo.PowerOffBehavior'] = 'revert'
      prompt: _typing.ClassVar['FlagInfo.PowerOffBehavior'] = 'prompt'
      take: _typing.ClassVar['FlagInfo.PowerOffBehavior'] = 'take'

   class MonitorType(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for `pyVmomi.vim.vm.FlagInfo.monitorType`.
      
      Attributes:
          release: Run vmx in default mode, matching the build type of vmkernel.
          debug: Run vmx in debug mode.
          stats: Run vmx in stats mode.
      """
      release: _typing.ClassVar['FlagInfo.MonitorType'] = 'release'
      debug: _typing.ClassVar['FlagInfo.MonitorType'] = 'debug'
      stats: _typing.ClassVar['FlagInfo.MonitorType'] = 'stats'

   class VirtualMmuUsage(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for `pyVmomi.vim.vm.FlagInfo.virtualMmuUsage`.
      
      Attributes:
          automatic: Determine automatically whether to use nested page table hardware support.
          on: Use nested paging hardware support if the physical hardware supports it.
          off: Do not use nested page table hardware support.
      """
      automatic: _typing.ClassVar['FlagInfo.VirtualMmuUsage'] = 'automatic'
      on: _typing.ClassVar['FlagInfo.VirtualMmuUsage'] = 'on'
      off: _typing.ClassVar['FlagInfo.VirtualMmuUsage'] = 'off'

   class VirtualExecUsage(pyVmomi.VmomiSupport.Enum):
      """
      Set of possible values for `pyVmomi.vim.vm.FlagInfo.virtualExecUsage`.
      
      Attributes:
          hvAuto: Determine automatically whether to use hardware virtualization (HV) support.
          hvOn: Use hardware virtualization (HV) support if the physical hardware supports it.
          hvOff: Do not use hardware virtualization (HV) support.
      """
      hvAuto: _typing.ClassVar['FlagInfo.VirtualExecUsage'] = 'hvAuto'
      hvOn: _typing.ClassVar['FlagInfo.VirtualExecUsage'] = 'hvOn'
      hvOff: _typing.ClassVar['FlagInfo.VirtualExecUsage'] = 'hvOff'

   disableAcceleration: _typing.Optional[bool] = None
   enableLogging: _typing.Optional[bool] = None
   useToe: _typing.Optional[bool] = None
   runWithDebugInfo: _typing.Optional[bool] = None
   monitorType: _typing.Optional[str] = None
   htSharing: _typing.Optional[str] = None
   snapshotDisabled: _typing.Optional[bool] = None
   snapshotLocked: _typing.Optional[bool] = None
   diskUuidEnabled: _typing.Optional[bool] = None
   virtualMmuUsage: _typing.Optional[str] = None
   virtualExecUsage: _typing.Optional[str] = None
   snapshotPowerOffBehavior: _typing.Optional[str] = None
   recordReplayEnabled: _typing.Optional[bool] = None
   faultToleranceType: _typing.Optional[str] = None
   cbrcCacheEnabled: _typing.Optional[bool] = None
   vvtdEnabled: _typing.Optional[bool] = None
   vbsEnabled: _typing.Optional[bool] = None

class FloppyInfo(TargetInfo):
   """
   FloppyInfo class contains information about a physical floppy
   drive on the host.
   """
   pass


class ForkConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the fork configuration of this
   virtual machine.
   
   Attributes:
       parentEnabled: Flag to indicate whether this virtual machine is a parent enabled
           virtual machine.
           
           If this vm is not a parent enabled vm this
           property will be unset.
           When set into the vim.vm.ConfigSpec this flag will be ignored.
       childForkGroupId: The fork group ID identifies the parent group of which this child
           VirtualMachine is a child.
           
           Applicable for child VirtualMachines only.
       parentForkGroupId: The fork group ID identifies the parent group which this VirtualMachine
           belongs to.
           
           Applicable for parent VirtualMachines only.
       childType: The flag to indicate the fork child type.
           
           For a persistent child
           virtual machine, once it is powered on, it will become a linked
           clone of its parent and this flag will be set to 'none'.
   """
   class ChildType(pyVmomi.VmomiSupport.Enum):
      """
      Fork child type.
      
      A child could be type of none, persistent, or
      nonpersistent.
      
      Attributes:
          none: The virtual machine is not a child.
          persistent: The virtual machine is a persistent child.
          nonpersistent: The virtual machine is a non-persistent child.
      """
      none: _typing.ClassVar['ForkConfigInfo.ChildType'] = 'none'
      persistent: _typing.ClassVar['ForkConfigInfo.ChildType'] = 'persistent'
      nonpersistent: _typing.ClassVar['ForkConfigInfo.ChildType'] = 'nonpersistent'

   parentEnabled: _typing.Optional[bool] = None
   childForkGroupId: _typing.Optional[str] = None
   parentForkGroupId: _typing.Optional[str] = None
   childType: _typing.Optional[str] = None


class GuestCustomizationManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   GuestCustomizationManager is a singleton managed object that provides APIs
   for guest customization of a running VM.
   """
   def Customize(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication, spec: pyVmomi.vim.vm.customization.Specification, configParams: list[pyVmomi.vim.option.OptionValue]) -> pyVmomi.vim.Task:
      """
      Customize a running virtual machine.
      
      The virtual machine must be in the powered-on state and the VMware Tools
      must be running.
      The VM is typically a cloned VM after the InstantClone operation. See
      `pyVmomi.vim.VirtualMachine.instantClone`.
      
      Args:
          vm: The Virtual Machine managed object reference.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
          spec: Is a `pyVmomi.vim.vm.customization.Specification`.
              It specifies the virtual machine's configuration.
          configParams: additional key/value pair list to support
              third party customization.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the VMware
              Tools is not running.
          pyVmomi.vim.fault.InvalidGuestLogin: if the the guest authentication information
              was not accepted.
          pyVmomi.vim.fault.GuestPermissionDenied: if the provided guest authentication
              is not sufficient to perform the guest customization.
          pyVmomi.vim.fault.CustomizationFault: if a customization error occurs.
      """
      ...
   def StartNetwork(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication) -> pyVmomi.vim.Task:
      """
      Start the network service in the guest, e.g.
      
      acquire IPs from DHCP.
      The virtual machine must be in the powered-on state and the VMware Tools
      must be running.
      The VM is typically a cloned VM after the InstantClone operation. See
      `pyVmomi.vim.VirtualMachine.instantClone`.
      
      Args:
          vm: The Virtual Machine managed object reference.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the VMware
              Tools is not running.
          pyVmomi.vim.fault.InvalidGuestLogin: if the the guest authentication information
              was not accepted.
          pyVmomi.vim.fault.GuestPermissionDenied: if the provided guest authentication
              is not sufficient to perform the guest customization.
          pyVmomi.vim.fault.CustomizationFault: if a customization error occurs.
      """
      ...
   def AbortCustomization(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication) -> pyVmomi.vim.Task:
      """
      Abort any running guest customization process in the guest and remove
      the guest customization lock in the guest as well.
      
      As a result of the
      operation, the guest configuration may be left in an undefined state,
      which is however fine because guest customization is idempotent.
      A later successful guest customization can set the guest configuration
      to a valid state.
      The virtual machine must be in the powered-on state and the VMware Tools
      must be running.
      The VM is typically a cloned VM after the InstantClone operation. See
      `pyVmomi.vim.VirtualMachine.instantClone`.
      
      Args:
          vm: The Virtual Machine managed object reference.
          auth: The guest authentication data. See
              `pyVmomi.vim.vm.guest.GuestAuthentication`.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the VMware
              Tools is not running.
          pyVmomi.vim.fault.InvalidGuestLogin: if the the guest authentication information
              was not accepted.
          pyVmomi.vim.fault.GuestPermissionDenied: if the provided guest authentication
              is not sufficient to perform the guest customization.
          pyVmomi.vim.fault.CustomizationFault: if a customization error occurs.
      """
      ...


class GuestInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about the guest operating system.
   
   Most of this information is collected by VMware Tools.
   In general, be sure you have VMware Tools installed
   and that the virtual machine is running when you access this information.
   
   Attributes:
       toolsStatus: Current status of VMware Tools in the guest operating system, if known.
       toolsVersionStatus: Current version status of VMware Tools in the guest operating system,
           if known.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.GuestInfo.ToolsVersionStatus` for vSphere API 5.0.
       toolsVersionStatus2: Current version status of VMware Tools in the guest operating system,
           if known.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.GuestInfo.ToolsVersionStatus`
       toolsRunningStatus: Current running status of VMware Tools in the guest operating system,
           if known.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.GuestInfo.ToolsRunningStatus`
       toolsVersion: Current version of VMware Tools, if known.
       toolsInstallType: Current installation type of VMware Tools in the guest operating system.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.GuestInfo.ToolsInstallType`
       guestId: Guest operating system identifier (short name), if known.
       guestFamily: Guest operating system family, if known.
       guestFullName: Guest operating system full name, if known.
       guestRebootStatus: Reboot status of the guest operating system, if known.
           
           For older versions of VMware Tools or ESXi,
           the information is not available.
           For uninstall operations, the information is not available.
           For virtual machines that are not powered on, the information
           is not available.
           
           Since: vSphere API Release 9.1.0.0
       guestDetailedData: Guest OS Detailed data.
           
           The guest detailed data string is a property list (space separated,
           name='value' pairs where the value is embedded in single quotes) of
           metadata provided by the guest OS when sufficiently recent tools are
           installed. The fields supplied will vary between distributions and
           distribution versions. The order of these fields is not guaranteed.
           
           The guest detailed data string is not available before a virtual machine
           is first powered on. The guest must first be booted and a supported
           version of tools must be run to record the data (approximately 30-60
           seconds after booting). Once the guest detailed data string has been
           recorded, it will be available whether the virtual machine is powered off
           or on.
           
           Available fields:
           
           Name
            - Description
            - Tools version first available
           
           architecture
            - 'Arm' or 'X86'
            - 11.2.0
           
           bitness
            - '32' or '64'
            - 11.2.0
           
           buildNumber
            - OS build number
            - 11.2.0
           
           cpeString
            - NIST Common Platform Enumeration Specification string, a standardized identifier for the OS
            - 12.2.0
           
           distroAddlVersion
            - Longer OS version string that may contain additional info (e.g. version name)
            - 12.2.0
           
           distroName
            - OS distribution name
            - 11.2.0
           
           distroVersion
            - OS version string
            - 11.2.0
           
           familyName
            - OS family name (Windows, Linux, etc.)
            - 11.2.0
           
           kernelVersion
            - Linux kernel version, Windows 10+ patch number, or Windows build number
            - 11.2.0
           
           prettyName
            - Officially specified distro \"pretty name\"
            - 11.2.0
           
           Since: vSphere API Release 8.0.2.0
       hostName: Hostname of the guest operating system, if known.
       ipAddress: Primary IP address assigned to the guest operating system, if known.
       net: Guest information about network adapters, if known.
       ipStack: Guest information about IP networking stack, if known.
       disk: Guest information about disks.
           
           You can obtain Linux guest disk information for the following file system
           types: Ext2, Ext3, Ext4, ReiserFS, XFS, Btrfs, NTFS, VFAT, UFS, PCFS, HFS,
           and MS-DOS.
           
           NOTE: Installing a more recent version of VMware Tools in the guest may help
           obtain disk information for more file system types. Please refer the VMware Tools
           User Guide for up-to-date supported file system types.
       screen: Guest screen resolution info, if known.
       guestState: Operation mode of guest operating system.
           
           One of:
           - \"running\" - Guest is running normally.
           - \"shuttingdown\" - Guest has a pending shutdown command.
           - \"resetting\" - Guest has a pending reset command.
           - \"standby\" - Guest has a pending standby command.
           - \"notrunning\" - Guest is not running.
           - \"unknown\" - Guest information is not available.
       appHeartbeatStatus: Application heartbeat status.
           
           Please see `pyVmomi.vim.VirtualMachine.AppHeartbeatStatusType`
       guestKernelCrashed: Guest operating system's kernel crash state.
           
           If true, the guest operating system's kernel has crashed.
       appState: Application state.
           
           If vSphere HA is enabled and the vm is configured for Application Monitoring
           and this field's value is \"appStateNeedReset\" then HA will attempt immediately reset
           the vm.
           There are some system conditions which may delay the immediate reset. The immediate
           reset will be performed as soon as allowed by vSphere HA and ESX. If during these
           conditions the value is changed to appStateOk the reset will be cancelled.
       guestOperationsReady: Guest Operations availability.
           
           If true, the virtual machine is ready to process guest operations.
       interactiveGuestOperationsReady: Interactive Guest Operations availability.
           
           If true, the virtual machine is ready to process guest operations
           as the user interacting with the guest desktop.
       guestStateChangeSupported: State change support.
           
           If true, the virtual machine is ready to process soft power operations.
       generationInfo: A list of namespaces and their corresponding generation numbers.
           
           Only namespaces with non-zero
           `pyVmomi.vim.vm.NamespaceManager.CreateSpec.maxSizeEventsFromGuest`
           are guaranteed to be present here.
           Use `pyVmomi.vim.vm.NamespaceManager.listNamespaces` to retrieve list of
           namespaces.
       hwVersion: The hardware version string for this virtual machine.
       customizationInfo: Guest OS Customization status info.
           
           Since: vSphere API Release 7.0.2.0
   """
   class ToolsStatus(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: As of vSphere API 4.0 use `pyVmomi.vim.vm.GuestInfo.ToolsVersionStatus`
      and `pyVmomi.vim.vm.GuestInfo.ToolsRunningStatus`.Current status of VMware Tools running in the guest operating system.
      
      Attributes:
          toolsNotInstalled: VMware Tools has never been installed
              or has not run in the virtual machine.
          toolsNotRunning: VMware Tools is not running.
          toolsOld: VMware Tools is running, but the version is not current.
          toolsOk: VMware Tools is running and the version is current.
      """
      toolsNotInstalled: _typing.ClassVar['GuestInfo.ToolsStatus'] = 'toolsNotInstalled'
      toolsNotRunning: _typing.ClassVar['GuestInfo.ToolsStatus'] = 'toolsNotRunning'
      toolsOld: _typing.ClassVar['GuestInfo.ToolsStatus'] = 'toolsOld'
      toolsOk: _typing.ClassVar['GuestInfo.ToolsStatus'] = 'toolsOk'

   class ToolsVersionStatus(pyVmomi.VmomiSupport.Enum):
      """
      Current version status of VMware Tools installed in the guest operating
      system.
      
      Attributes:
          guestToolsNotInstalled: VMware Tools has never been installed.
          guestToolsNeedUpgrade: VMware Tools is installed, but the version is not current.
          guestToolsCurrent: VMware Tools is installed, and the version is current.
          guestToolsUnmanaged: VMware Tools is installed, but it is not managed by VMWare.
          guestToolsTooOld: VMware Tools is installed, but the version is too old.
          guestToolsSupportedOld: VMware Tools is installed, supported, but a newer version is available.
          guestToolsSupportedNew: VMware Tools is installed, supported, and newer
              than the version available on the host.
          guestToolsTooNew: VMware Tools is installed, and the version is known to be
              too new to work correctly with this virtual machine.
          guestToolsBlacklisted: VMware Tools is installed, but the installed version is
              known to have a grave bug and should be immediately upgraded.
      """
      guestToolsNotInstalled: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsNotInstalled'
      guestToolsNeedUpgrade: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsNeedUpgrade'
      guestToolsCurrent: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsCurrent'
      guestToolsUnmanaged: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsUnmanaged'
      guestToolsTooOld: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsTooOld'
      guestToolsSupportedOld: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsSupportedOld'
      guestToolsSupportedNew: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsSupportedNew'
      guestToolsTooNew: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsTooNew'
      guestToolsBlacklisted: _typing.ClassVar['GuestInfo.ToolsVersionStatus'] = 'guestToolsBlacklisted'

   class ToolsRunningStatus(pyVmomi.VmomiSupport.Enum):
      """
      Current running status of VMware Tools running in the guest
      operating system.
      
      Attributes:
          guestToolsNotRunning: VMware Tools is not running.
          guestToolsRunning: VMware Tools is running.
          guestToolsExecutingScripts: VMware Tools is starting.
      """
      guestToolsNotRunning: _typing.ClassVar['GuestInfo.ToolsRunningStatus'] = 'guestToolsNotRunning'
      guestToolsRunning: _typing.ClassVar['GuestInfo.ToolsRunningStatus'] = 'guestToolsRunning'
      guestToolsExecutingScripts: _typing.ClassVar['GuestInfo.ToolsRunningStatus'] = 'guestToolsExecutingScripts'

   class ToolsInstallType(pyVmomi.VmomiSupport.Enum):
      """
      The installation type of tools in the VM.
      
      Attributes:
          guestToolsTypeUnknown: Installation type is not known.
              
              Most likely tools have been
              installed by OSPs or open-vm-tools, but a version that does
              not report its install type or an install type that we do
              not recognize.
          guestToolsTypeMSI: MSI is the installation type used for VMware Tools on Windows.
          guestToolsTypeTar: Tools have been installed by the tar installer.
          guestToolsTypeOSP: OSPs are RPM or Debian packages tailored for the OS in the VM.
              
              See http://packages.vmware.com
          guestToolsTypeOpenVMTools: open-vm-tools are the open-source version of VMware Tools, may have
              been packaged by the OS vendor.
      """
      guestToolsTypeUnknown: _typing.ClassVar['GuestInfo.ToolsInstallType'] = 'guestToolsTypeUnknown'
      guestToolsTypeMSI: _typing.ClassVar['GuestInfo.ToolsInstallType'] = 'guestToolsTypeMSI'
      guestToolsTypeTar: _typing.ClassVar['GuestInfo.ToolsInstallType'] = 'guestToolsTypeTar'
      guestToolsTypeOSP: _typing.ClassVar['GuestInfo.ToolsInstallType'] = 'guestToolsTypeOSP'
      guestToolsTypeOpenVMTools: _typing.ClassVar['GuestInfo.ToolsInstallType'] = 'guestToolsTypeOpenVMTools'

   class GuestRebootStatus(pyVmomi.vmodl.DynamicData):
      """
      The guest reboot status describes the guest operating system
      reboot status resulting from a VMware Tools install, upgrade,
      or uninstall.
      
      Attributes:
          rebootRequested: Indicates whether a VMware Tools install, upgrade, or uninstall
              requires a reboot of the guest operating system.
              
              Set to true when a VMware Tools install, upgrade, or uninstall has
              requested the guest operating system to be rebooted and no reboot has
              been performed since the request. It is set to false as soon as the
              guest operating system completes a reboot following the request.
          requestingComponents: List of VMware Tools and/or system components that have
              requested the guest operating system be rebooted to complete
              a VMware Tools install, upgrade, or uninstall.
              
              See the VMware Tools Administration Guide for the details of the
              components reported by the install operation.
              If unset, no reboot is pending, or the reboot components list
              information is not available. For older versions of VMware Tools
              or ESXi, the information is not available.
              For uninstall operations, the information is not available.
          requestTimestamp: The time when the reboot request was generated.
              
              If unset, no reboot is pending, or the reboot time information
              is not available. For older versions of VMware Tools or ESXi,
              the information is not available.
              For uninstall operations, the information is not available.
      
      Since: vSphere API Release 9.1.0.0
      """
      rebootRequested: bool
      requestingComponents: list[str] = []
      requestTimestamp: _typing.Optional[_datetime.datetime] = None

   class VirtualDiskMapping(pyVmomi.vmodl.DynamicData):
      """
      Describes the virtual disk backing a local guest disk.
      
      Attributes:
          key: The key of the VirtualDevice.
              
              `pyVmomi.vim.vm.device.VirtualDevice.key`
      """
      key: int

   class DiskInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about each local virtual disk configured in the
      guest operating system.
      
      Attributes:
          diskPath: Name of the virtual disk in the guest operating system.
              
              For example: C:\\
          capacity: Total capacity of the disk, in bytes.
              
              This is part of the virtual machine configuration.
          freeSpace: Free space on the disk, in bytes.
              
              This is retrieved by VMware Tools.
          filesystemType: Filesystem type, if known.
              
              For example NTFS or ext3.
          mappings: VirtualDisks backing the guest partition, if known.
      """
      diskPath: _typing.Optional[str] = None
      capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      freeSpace: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      filesystemType: _typing.Optional[str] = None
      mappings: list[GuestInfo.VirtualDiskMapping] = []

   class NicInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about each virtual network adapter
      configured in the guest operating system.
      
      Attributes:
          network: Name of the virtual switch portgroup or dvPort connected to this adapter.
          ipAddress: IP addresses of the adapter.
          macAddress: MAC address of the adapter.
          connected: Flag indicating whether or not the virtual device is connected.
          deviceConfigId: Link to the corresponding virtual device.
          dnsConfig: DNS configuration of the adapter.
              
              This property is set only when Guest OS supports it.
              See `pyVmomi.vim.vm.GuestInfo.StackInfo` dnsConfig for system wide
              settings.
          ipConfig: IP configuration settings of the adapter
              See `pyVmomi.vim.vm.GuestInfo.StackInfo` ipStackConfig for system wide
              settings.
          netBIOSConfig: NetBIOS configuration of the adapter
      """
      network: _typing.Optional[str] = None
      ipAddress: list[str] = []
      macAddress: _typing.Optional[str] = None
      connected: bool
      deviceConfigId: int
      dnsConfig: _typing.Optional[pyVmomi.vim.net.DnsConfigInfo] = None
      ipConfig: _typing.Optional[pyVmomi.vim.net.IpConfigInfo] = None
      netBIOSConfig: _typing.Optional[pyVmomi.vim.net.NetBIOSConfigInfo] = None

   class StackInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about the Internet Protocol stack
      as configured in the guest operating system.
      
      Attributes:
          dnsConfig: Client DNS configuration.
              
              How DNS queries are resolved.
          ipRouteConfig: IP route table configuration.
          ipStackConfig: Report Kernel IP configuration settings.
              
              The key part contains a unique number in the report.
              The value part contains the 'key=value'
              as provided by the underlying provider.
              For example on Linux, BSD, the
              systcl -a output would be reported as:
              key='5', value='net.ipv4.tcp_keepalive_time = 7200'
          dhcpConfig: Client side DHCP for a given interface.
              
              This reports only the system wide dhcp client settings.
              See NicInfo.IpConfig for per interface settings.
              For example on Linux, BSD systems:
              Using the file dhclient.conf output would be reported as:
              key='1', value='timeout 60;'
              key='2', value='reboot 10;'
      """
      dnsConfig: _typing.Optional[pyVmomi.vim.net.DnsConfigInfo] = None
      ipRouteConfig: _typing.Optional[pyVmomi.vim.net.IpRouteConfigInfo] = None
      ipStackConfig: list[pyVmomi.vim.KeyValue] = []
      dhcpConfig: _typing.Optional[pyVmomi.vim.net.DhcpConfigInfo] = None

   class ScreenInfo(pyVmomi.vmodl.DynamicData):
      """
      Screen settings
      
      Attributes:
          width: Width of the screen in pixels.
          height: Height of the screen in pixels.
      """
      width: int
      height: int

   class GuestState(pyVmomi.VmomiSupport.Enum):
      """
      The possible hints that the guest could display about current tasks
      inside the guest.
      """
      running: _typing.ClassVar['GuestInfo.GuestState'] = 'running'
      shuttingDown: _typing.ClassVar['GuestInfo.GuestState'] = 'shuttingDown'
      resetting: _typing.ClassVar['GuestInfo.GuestState'] = 'resetting'
      standby: _typing.ClassVar['GuestInfo.GuestState'] = 'standby'
      notRunning: _typing.ClassVar['GuestInfo.GuestState'] = 'notRunning'
      unknown: _typing.ClassVar['GuestInfo.GuestState'] = 'unknown'

   class AppStateType(pyVmomi.VmomiSupport.Enum):
      """
      Application state type.
      
      Attributes:
          none: The application state wasn't set from the guest by the application agent.
              
              This is the default.
          appStateOk: The guest's application agent declared its state as normal and doesn't
              require any action
          appStateNeedReset: Guest's application agent asks for immediate reset
      """
      none: _typing.ClassVar['GuestInfo.AppStateType'] = 'none'
      appStateOk: _typing.ClassVar['GuestInfo.AppStateType'] = 'appStateOk'
      appStateNeedReset: _typing.ClassVar['GuestInfo.AppStateType'] = 'appStateNeedReset'

   class NamespaceGenerationInfo(pyVmomi.vmodl.DynamicData):
      """
      A data class for the namespace and its corresponding generation number
      The generation number can be used to track updates to the corresponding
      namespace.
      
      An update to the generation number indicates that the return
      value of `pyVmomi.vim.vm.NamespaceManager.fetchEventsFromGuest` may have
      changed.
      
      Attributes:
          key: The namespace name as the unique key.
          generationNo: Namespace generation number.
              
              Generation number is changed whenever
              there is new unread event pending from the guest to the VMODL.
      """
      key: str
      generationNo: int

   class CustomizationStatus(pyVmomi.VmomiSupport.Enum):
      """
      Guest customization status
      
      Attributes:
          TOOLSDEPLOYPKG_IDLE: No guest customizationSpec has been applied for the VM
          TOOLSDEPLOYPKG_PENDING: The guest customizationSpec has been applied for the VM,
              but the customization process has not yet started inside the guest OS
          TOOLSDEPLOYPKG_RUNNING: The customization process is currently running inside the guest OS
          TOOLSDEPLOYPKG_SUCCEEDED: The customization process has completed successfully inside the
              guest OS
          TOOLSDEPLOYPKG_FAILED: The customizatio process has failed inside the guest OS
      
      Since: vSphere API Release 7.0.2.0
      """
      TOOLSDEPLOYPKG_IDLE: _typing.ClassVar['GuestInfo.CustomizationStatus'] = 'TOOLSDEPLOYPKG_IDLE'
      TOOLSDEPLOYPKG_PENDING: _typing.ClassVar['GuestInfo.CustomizationStatus'] = 'TOOLSDEPLOYPKG_PENDING'
      TOOLSDEPLOYPKG_RUNNING: _typing.ClassVar['GuestInfo.CustomizationStatus'] = 'TOOLSDEPLOYPKG_RUNNING'
      TOOLSDEPLOYPKG_SUCCEEDED: _typing.ClassVar['GuestInfo.CustomizationStatus'] = 'TOOLSDEPLOYPKG_SUCCEEDED'
      TOOLSDEPLOYPKG_FAILED: _typing.ClassVar['GuestInfo.CustomizationStatus'] = 'TOOLSDEPLOYPKG_FAILED'

   class CustomizationInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          customizationStatus: The customization status for this VM
          startTime: The time when the customization process has started inside the
              guest OS
          endTime: The time when the customization process has completed inside the
              guest OS
          errorMsg: Description of the error if there is error for the customization
              process inside the guest OS
      
      Since: vSphere API Release 7.0.2.0
      """
      customizationStatus: str
      startTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None
      errorMsg: _typing.Optional[str] = None

   toolsStatus: _typing.Optional[GuestInfo.ToolsStatus] = None
   toolsVersionStatus: _typing.Optional[str] = None
   toolsVersionStatus2: _typing.Optional[str] = None
   toolsRunningStatus: _typing.Optional[str] = None
   toolsVersion: _typing.Optional[str] = None
   toolsInstallType: _typing.Optional[str] = None
   guestId: _typing.Optional[str] = None
   guestFamily: _typing.Optional[str] = None
   guestFullName: _typing.Optional[str] = None
   guestRebootStatus: _typing.Optional[GuestInfo.GuestRebootStatus] = None
   guestDetailedData: _typing.Optional[str] = None
   hostName: _typing.Optional[str] = None
   ipAddress: _typing.Optional[str] = None
   net: list[GuestInfo.NicInfo] = []
   ipStack: list[GuestInfo.StackInfo] = []
   disk: list[GuestInfo.DiskInfo] = []
   screen: _typing.Optional[GuestInfo.ScreenInfo] = None
   guestState: str
   appHeartbeatStatus: _typing.Optional[str] = None
   guestKernelCrashed: _typing.Optional[bool] = None
   appState: _typing.Optional[str] = None
   guestOperationsReady: _typing.Optional[bool] = None
   interactiveGuestOperationsReady: _typing.Optional[bool] = None
   guestStateChangeSupported: _typing.Optional[bool] = None
   generationInfo: list[GuestInfo.NamespaceGenerationInfo] = []
   hwVersion: _typing.Optional[str] = None
   customizationInfo: _typing.Optional[GuestInfo.CustomizationInfo] = None


class GuestIntegrityInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the guest integrity platform configuration of
   this virtual machine.
   
   Attributes:
       enabled: Flag to indicate whether guest integrity platform feature is enabled for
           this virtual machine.
           
           Guest integrity adds capabilities in the virtual
           platform to detect attacks on the guest OS kernel
   """
   enabled: _typing.Optional[bool] = None


class GuestMonitoringModeInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the GMM (Guest Mode Monitoring) configuration
   of this virtual machine.
   """
   gmmFile: _typing.Optional[str] = None
   gmmAppliance: _typing.Optional[str] = None


class GuestOsDescriptor(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains information to describe a
   particular guest operating system.
   
   Attributes:
       id: Identifier (short name) for the guest operating system.
       family: Family to which this guest operating system belongs.
       fullName: Full name of the guest operating system.
           
           For example, if the value of \"id\" is \"win2000Pro\", then
           the value of \"fullName\" is \"Windows 2000 Professional\".
       supportedMaxCPUs: Maximum number of processors supported for this guest.
       numSupportedPhysicalSockets: Maximum number of sockets supported for this guest.
       numSupportedCoresPerSocket: Maximum number of cores per socket for this guest.
       supportedMinMemMB: Minimum memory requirements supported for this guest, in MB.
       supportedMaxMemMB: Maximum memory requirements supported for this guest, in MB.
       recommendedMemMB: Recommended default memory size for this guest, in MB.
       recommendedColorDepth: Recommended default color depth for this guest.
       supportedDiskControllerList: List of supported disk controller types for this guest.
       recommendedSCSIController: Recommended default SCSI controller type for this guest.
       recommendedDiskController: Recommended default disk controller type for this guest.
       supportedNumDisks: Number of disks supported for this guest.
       recommendedDiskSizeMB: Recommended default disk size for this guest, in MB.
       recommendedCdromController: Recommended default CD-ROM type for this guest.
       supportedEthernetCard: List of supported ethernet cards for this guest.
       recommendedEthernetCard: Recommended default ethernet controller type for this guest.
       supportsSlaveDisk: Flag to indicate whether or not this guest can support
           a disk configured as a slave.
       cpuFeatureMask: Specifies the CPU feature compatibility masks.
       smcRequired: Flag that indicates whether the guest requires an SMC (Apple hardware).
           
           This is logically equivalent to GuestOS = Mac OS
       supportsWakeOnLan: Flag to indicate whether or not this guest can support Wake-on-LAN.
       supportsVMI: Flag indicating whether or not this guest supports the virtual
           machine interface.
       supportsMemoryHotAdd: Whether the memory size for this guest can be changed
           while the virtual machine is running.
       supportsCpuHotAdd: Whether virtual CPUs can be added to this guest
           while the virtual machine is running.
       supportsCpuHotRemove: Whether virtual CPUs can be removed from this guest
           while the virtual machine is running.
       supportedFirmware: Supported firmware types for this guest.
           
           Possible values are described in
           `pyVmomi.vim.vm.GuestOsDescriptor.FirmwareType`
       recommendedFirmware: Recommended firmware type for this guest.
           
           Possible values are described in
           `pyVmomi.vim.vm.GuestOsDescriptor.FirmwareType`
       supportedUSBControllerList: List of supported USB controllers for this guest.
       recommendedUSBController: Recommended default USB controller type for this guest.
       supports3D: Whether this guest supports 3D graphics.
       recommended3D: Recommended 3D graphics for this guest.
       smcRecommended: Whether SMC (Apple hardware) is recommended for this guest.
       ich7mRecommended: Whether I/O Controller Hub is recommended for this guest.
       usbRecommended: Whether USB controller is recommended for this guest.
       supportLevel: Support level of this Guest
           Possible values are described in
           `pyVmomi.vim.vm.GuestOsDescriptor.SupportLevel`
       supportedForCreate: Whether or not this guest should be allowed for selection
           during virtual machine creation.
       vRAMSizeInKB: Video RAM size limits supported by this guest, in KB.
       numSupportedFloppyDevices: Maximum number of floppies supported by this guest.
       wakeOnLanEthernetCard: List of NICs supported by this guest that support Wake-On-Lan.
       supportsPvscsiControllerForBoot: Whether or not this guest can use pvscsi as boot adapter.
       diskUuidEnabled: Whether or not this guest should have disk uuid enabled by default.
       supportsHotPlugPCI: Whether or not this guest supports hot plug of PCI devices.
       supportsSecureBoot: Whether or not this guest supports Secure Boot.
           
           If some of the OS
           releases that fall under this guest OS descriptor support Secure Boot, it
           is reasonable to offer the ability to enable Secure Boot. Only
           meaningful when virtual EFI firmware is in use.
       defaultSecureBoot: Whether or not Secure Boot should be enabled by default for this
           guest OS.
           
           If all OS releases that fall under this guest OS descriptor
           support Secure Boot and are known to operate correctly with Secure Boot
           enabled, it is reasonable to enable it by default. Only meaningful when
           virtual EFI firmware is in use.
       persistentMemorySupported: Support of persistent memory (virtual NVDIMM device).
       supportedMinPersistentMemoryMB: Minimum persistent memory supported for this guest, in MB.
       supportedMaxPersistentMemoryMB: Maximum persistent memory supported for this guest, in MB.
           
           Total size of all the virtual NVDIMM devices should be less
           than this value.
       recommendedPersistentMemoryMB: Recommended default persistent memory size for this guest, in MB.
       persistentMemoryHotAddSupported: Support of persistent memory hot-add operation.
       persistentMemoryHotRemoveSupported: Support of persistent memory hot-remove operation.
       persistentMemoryColdGrowthSupported: Support of virtual NVDIMM cold-growth operation.
       persistentMemoryColdGrowthGranularityMB: Virtual NVDIMM cold-growth granularity in MB.
       persistentMemoryHotGrowthSupported: Support of virtual NVDIMM hot-growth operation.
       persistentMemoryHotGrowthGranularityMB: Virtual NVDIMM hot-growth granularity in MB.
       numRecommendedPhysicalSockets: Recommended number of sockets for this guest.
       numRecommendedCoresPerSocket: Recommended number of cores per socket for this guest.
       vvtdSupported: Support of Intel Virtualization Technology for Directed I/O.
       vbsSupported: Support of Virtualization-based security.
       vsgxSupported: Support for Intel Software Guard Extensions
       vsgxRemoteAttestationSupported: Support for Intel Software Guard Extensions remote attestation.
           
           Since: vSphere API Release 8.0.0.1
       supportsTPM20: Support for TPM 2.0.
       recommendedTPM20: Support for default vTPM
           
           Since: vSphere API Release 8.0.0.1
       vwdtSupported: Support for Virtual Watchdog Timer.
   """
   class GuestOsFamily(pyVmomi.VmomiSupport.Enum):
      """
      Guest operating system family constants.
      
      Attributes:
          windowsGuest: Windows operating system
          linuxGuest: Linux operating system
          netwareGuest: Novell Netware
          solarisGuest: Solaris operating system
          darwinGuestFamily: Mac OS operating system
          otherGuestFamily: Other operating systems
      """
      windowsGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'windowsGuest'
      linuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'linuxGuest'
      netwareGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'netwareGuest'
      solarisGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'solarisGuest'
      darwinGuestFamily: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'darwinGuestFamily'
      otherGuestFamily: _typing.ClassVar['GuestOsDescriptor.GuestOsFamily'] = 'otherGuestFamily'

   class GuestArchitecture(pyVmomi.VmomiSupport.Enum):
      """
      Guest CPU architecture constants.
      
      Attributes:
          x86: x86 architecture.
          arm: ARM architecture.
      
      Since: vSphere API Release 9.1.0.0
      """
      x86: _typing.ClassVar['GuestOsDescriptor.GuestArchitecture'] = 'x86'
      arm: _typing.ClassVar['GuestOsDescriptor.GuestArchitecture'] = 'arm'

   class GuestOsIdentifier(pyVmomi.VmomiSupport.Enum):
      """
      Guest operating system identifier.
      
      Attributes:
          dosGuest: MS-DOS.
          win31Guest: Windows 3.1
          win95Guest: Windows 95
          win98Guest: Windows 98
          winMeGuest: Windows Millennium Edition
          winNTGuest: Windows NT 4
          win2000ProGuest: Windows 2000 Professional
          win2000ServGuest: Windows 2000 Server
          win2000AdvServGuest: Windows 2000 Advanced Server
          winXPHomeGuest: Windows XP Home Edition
          winXPProGuest: Windows XP Professional
          winXPPro64Guest: Windows XP Professional Edition (64 bit)
          winNetWebGuest: Windows Server 2003, Web Edition
          winNetStandardGuest: Windows Server 2003, Standard Edition
          winNetEnterpriseGuest: Windows Server 2003, Enterprise Edition
          winNetDatacenterGuest: Windows Server 2003, Datacenter Edition
          winNetBusinessGuest: Windows Small Business Server 2003
          winNetStandard64Guest: Windows Server 2003, Standard Edition (64 bit)
          winNetEnterprise64Guest: Windows Server 2003, Enterprise Edition (64 bit)
          winLonghornGuest: Windows Longhorn
          winLonghorn64Guest: Windows Longhorn (64 bit)
          winNetDatacenter64Guest: Windows Server 2003, Datacenter Edition (64 bit)
          winVistaGuest: Windows Vista
          winVista64Guest: Windows Vista (64 bit)
          windows7Guest: Windows 7
          windows7_64Guest: Windows 7 (64 bit)
          windows7Server64Guest: Windows Server 2008 R2 (64 bit)
          windows8Guest: Windows 8
          windows8_64Guest: Windows 8 (64 bit)
          windows8Server64Guest: Windows 8 Server (64 bit)
          windows9Guest: Windows 10
          windows9_64Guest: Windows 10 (64 bit)
          windows9Server64Guest: Windows 10 Server (64 bit)
          windows11_64Guest: Windows 11
              
              Since: vSphere API Release 8.0.0.1
          windows12_64Guest: Windows 12
              
              Since: vSphere API Release 8.0.0.1
          windowsHyperVGuest: Windows Hyper-V
          windows2019srv_64Guest: Windows Server 2019
          windows2019srvNext_64Guest: Windows Server 2022
              
              Since: vSphere API Release 7.0.1.0
          windows2022srvNext_64Guest: Windows Server 2025
              
              Since: vSphere API Release 8.0.0.1
          freebsdGuest: FreeBSD
          freebsd64Guest: FreeBSD x64
          freebsd11Guest: FreeBSD 11
          freebsd11_64Guest: FreeBSD 11 x64
          freebsd12Guest: FreeBSD 12
          freebsd12_64Guest: FreeBSD 12 x64
          freebsd13Guest: FreeBSD 13
              
              Since: vSphere API Release 7.0.1.0
          freebsd13_64Guest: FreeBSD 13 x64
              
              Since: vSphere API Release 7.0.1.0
          freebsd14Guest: FreeBSD 14
              
              Since: vSphere API Release 8.0.0.1
          freebsd14_64Guest: FreeBSD 14 x64
              
              Since: vSphere API Release 8.0.0.1
          freebsd15Guest: FreeBSD 15
              
              Since: vSphere API Release 9.0.0.0
          freebsd15_64Guest: FreeBSD 15 x64
              
              Since: vSphere API Release 9.0.0.0
          redhatGuest: Red Hat Linux 2.1
          rhel2Guest: Red Hat Enterprise Linux 2
          rhel3Guest: Red Hat Enterprise Linux 3
          rhel3_64Guest: Red Hat Enterprise Linux 3 (64 bit)
          rhel4Guest: Red Hat Enterprise Linux 4
          rhel4_64Guest: Red Hat Enterprise Linux 4 (64 bit)
          rhel5Guest: Red Hat Enterprise Linux 5
          rhel5_64Guest: Red Hat Enterprise Linux 5 (64 bit)
          rhel6Guest: Red Hat Enterprise Linux 6
          rhel6_64Guest: Red Hat Enterprise Linux 6 (64 bit)
          rhel7Guest: Red Hat Enterprise Linux 7
          rhel7_64Guest: Red Hat Enterprise Linux 7 (64 bit)
          rhel8_64Guest: Red Hat Enterprise Linux 8 (64 bit)
          rhel9_64Guest: Red Hat Enterprise Linux 9 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          rhel10_64Guest: Red Hat Enterprise Linux 10 (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          centosGuest: CentOS 4/5
          centos64Guest: CentOS 4/5 (64-bit)
          centos6Guest: CentOS 6
          centos6_64Guest: CentOS 6 (64-bit)
          centos7Guest: CentOS 7
          centos7_64Guest: CentOS 7 (64-bit)
          centos8_64Guest: CentOS 8 (64-bit)
          centos9_64Guest: CentOS 9 (64-bit)
              
              Since: vSphere API Release 7.0.1.0
          oracleLinuxGuest: Oracle Linux 4/5
          oracleLinux64Guest: Oracle Linux 4/5 (64-bit)
          oracleLinux6Guest: Oracle 6
          oracleLinux6_64Guest: Oracle 6 (64-bit)
          oracleLinux7Guest: Oracle 7
          oracleLinux7_64Guest: Oracle 7 (64-bit)
          oracleLinux8_64Guest: Oracle 8 (64-bit)
          oracleLinux9_64Guest: Oracle 9 (64-bit)
              
              Since: vSphere API Release 7.0.1.0
          oracleLinux10_64Guest: Oracle 10 (64-bit)
              
              Since: vSphere API Release 9.0.0.0
          suseGuest: Suse Linux
          suse64Guest: Suse Linux (64 bit)
          slesGuest: Suse Linux Enterprise Server 9
          sles64Guest: Suse Linux Enterprise Server 9 (64 bit)
          sles10Guest: Suse linux Enterprise Server 10
          sles10_64Guest: Suse Linux Enterprise Server 10 (64 bit)
          sles11Guest: Suse linux Enterprise Server 11
          sles11_64Guest: Suse Linux Enterprise Server 11 (64 bit)
          sles12Guest: Suse linux Enterprise Server 12
          sles12_64Guest: Suse Linux Enterprise Server 12 (64 bit)
          sles15_64Guest: Suse Linux Enterprise Server 15 (64 bit)
          sles16_64Guest: Suse Linux Enterprise Server 16 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          nld9Guest: Novell Linux Desktop 9
          oesGuest: Open Enterprise Server
          sjdsGuest: Sun Java Desktop System
          mandrakeGuest: Mandrake Linux
          mandrivaGuest: Mandriva Linux
          mandriva64Guest: Mandriva Linux (64 bit)
          turboLinuxGuest: Turbolinux
          turboLinux64Guest: Turbolinux (64 bit)
          ubuntuGuest: Ubuntu Linux
          ubuntu64Guest: Ubuntu Linux (64 bit)
          debian4Guest: Debian GNU/Linux 4
          debian4_64Guest: Debian GNU/Linux 4 (64 bit)
          debian5Guest: Debian GNU/Linux 5
          debian5_64Guest: Debian GNU/Linux 5 (64 bit)
          debian6Guest: Debian GNU/Linux 6
          debian6_64Guest: Debian GNU/Linux 6 (64 bit)
          debian7Guest: Debian GNU/Linux 7
          debian7_64Guest: Debian GNU/Linux 7 (64 bit)
          debian8Guest: Debian GNU/Linux 8
          debian8_64Guest: Debian GNU/Linux 8 (64 bit)
          debian9Guest: Debian GNU/Linux 9
          debian9_64Guest: Debian GNU/Linux 9 (64 bit)
          debian10Guest: Debian GNU/Linux 10
          debian10_64Guest: Debian GNU/Linux 10 (64 bit)
          debian11Guest: Debian GNU/Linux 11
          debian11_64Guest: Debian GNU/Linux 11 (64 bit)
          debian12Guest: Debian GNU/Linux 12
              
              Since: vSphere API Release 8.0.0.1
          debian12_64Guest: Debian GNU/Linux 12 (64 bit)
              
              Since: vSphere API Release 8.0.0.1
          debian13Guest: Debian GNU/Linux 13
              
              Since: vSphere API Release 9.0.0.0
          debian13_64Guest: Debian GNU/Linux 13 (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          asianux3Guest: Asianux Server 3
          asianux3_64Guest: Asianux Server 3 (64 bit)
          asianux4Guest: Asianux Server 4
          asianux4_64Guest: Asianux Server 4 (64 bit)
          asianux5_64Guest: Asianux Server 5 (64 bit)
          asianux7_64Guest: Asianux Server 7 (64 bit)
          asianux8_64Guest: Asianux Server 8 (64 bit)
          asianux9_64Guest: Asianux Server 9 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          miraclelinux_64Guest: MIRACLE LINUX (64-bit)
              
              Since: vSphere API Release 9.0.0.0
          pardus_64Guest: Pardus (64-bit)
              
              Since: vSphere API Release 9.0.0.0
          opensuseGuest: OpenSUSE Linux
          opensuse64Guest: OpenSUSE Linux (64 bit)
          fedoraGuest: Fedora Linux
          fedora64Guest: Fedora Linux (64 bit)
          coreos64Guest: CoreOS Linux (64 bit)
          vmwarePhoton64Guest: VMware Photon (64 bit)
          other24xLinuxGuest: Linux 2.4x Kernel
          other26xLinuxGuest: Linux 2.6x Kernel
          otherLinuxGuest: Linux 2.2x Kernel
          other3xLinuxGuest: Linux 3.x Kernel
          other4xLinuxGuest: Linux 4.x Kernel
          other5xLinuxGuest: Linux 5.x Kernel
              
              Since: vSphere API Release 7.0.1.0
          other6xLinuxGuest: Linux 6.x Kernel
              
              Since: vSphere API Release 8.0.0.1
          other7xLinuxGuest: Linux 7.x Kernel
              
              Since: vSphere API Release 9.0.0.0
          genericLinuxGuest: Other Linux
          other24xLinux64Guest: Linux 2.4.x Kernel (64 bit)
          other26xLinux64Guest: Linux 2.6.x Kernel (64 bit)
          other3xLinux64Guest: Linux 3.x Kernel (64 bit)
          other4xLinux64Guest: Linux 4.x Kernel (64 bit)
          other5xLinux64Guest: Linux 5.x Kernel (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          other6xLinux64Guest: Linux 6.x Kernel (64 bit)
              
              Since: vSphere API Release 8.0.0.1
          other7xLinux64Guest: Linux 7.x Kernel (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          otherLinux64Guest: Linux (64 bit)
          solaris6Guest: Solaris 6
          solaris7Guest: Solaris 7
          solaris8Guest: Solaris 8
          solaris9Guest: Solaris 9
          solaris10Guest: Solaris 10 (32 bit)
          solaris10_64Guest: Solaris 10 (64 bit)
          solaris11_64Guest: Solaris 11 (64 bit)
          fusionos_64Guest: FusionOS (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          prolinux_64Guest: ProLinux (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          kylinlinux_64Guest: Kylinlinux (64 bit)
              
              Since: vSphere API Release 9.0.0.0
          flatcar_64Guest: Flatcar (64 bit)
          os2Guest: OS/2
          eComStationGuest: eComStation 1.x
          eComStation2Guest: eComStation 2.0
          netware4Guest: Novell NetWare 4
          netware5Guest: Novell NetWare 5.1
          netware6Guest: Novell NetWare 6.x
          openServer5Guest: SCO OpenServer 5
          openServer6Guest: SCO OpenServer 6
          unixWare7Guest: SCO UnixWare 7
          darwinGuest: Mac OS 10.5
          darwin64Guest: Mac OS 10.5 (64 bit)
          darwin10Guest: Mac OS 10.6
          darwin10_64Guest: Mac OS 10.6 (64 bit)
          darwin11Guest: Mac OS 10.7
          darwin11_64Guest: Mac OS 10.7 (64 bit)
          darwin12_64Guest: Mac OS 10.8 (64 bit)
          darwin13_64Guest: Mac OS 10.9 (64 bit)
          darwin14_64Guest: Mac OS 10.10 (64 bit)
          darwin15_64Guest: Mac OS 10.11 (64 bit)
          darwin16_64Guest: Mac OS 10.12 (64 bit)
          darwin17_64Guest: macOS 10.13 (64 bit)
          darwin18_64Guest: macOS 10.14 (64 bit)
          darwin19_64Guest: macOS 10.15 (64 bit)
          darwin20_64Guest: macOS 11 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          darwin21_64Guest: macOS 12 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          darwin22_64Guest: macOS 13 (64 bit)
              
              Since: vSphere API Release 8.0.0.1
          darwin23_64Guest: macOS 14 (64 bit)
              
              Since: vSphere API Release 8.0.0.1
          vmkernelGuest: VMware ESX 4
          vmkernel5Guest: VMware ESX 5
          vmkernel6Guest: VMware ESX 6
          vmkernel65Guest: VMware ESXi 6.5 AND ESXi 6.7.
          vmkernel7Guest: VMware ESX 7
          vmkernel8Guest: VMware ESX 8
              
              Since: vSphere API Release 8.0.0.1
          vmkernel9Guest: VMware ESX 9
              
              Since: vSphere API Release 9.0.0.0
          amazonlinux2_64Guest: Amazon Linux 2 (64 bit)
          amazonlinux3_64Guest: Amazon Linux 3 (64 bit)
              
              Since: vSphere API Release 7.0.1.0
          crxPod1Guest: CRX Pod 1
          crxSys1Guest: CRX Sys 1
              
              Since: vSphere API Release 8.0.3.0
          rockylinux_64Guest: Rocky Linux (64-bit)
              
              Since: vSphere API Release 8.0.0.1
          almalinux_64Guest: AlmaLinux (64-bit)
              
              Since: vSphere API Release 8.0.0.1
          otherGuest: Other Operating System
          otherGuest64: Other Operating System (64 bit)
      """
      dosGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'dosGuest'
      win31Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win31Guest'
      win95Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win95Guest'
      win98Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win98Guest'
      winMeGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winMeGuest'
      winNTGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNTGuest'
      win2000ProGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win2000ProGuest'
      win2000ServGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win2000ServGuest'
      win2000AdvServGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'win2000AdvServGuest'
      winXPHomeGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winXPHomeGuest'
      winXPProGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winXPProGuest'
      winXPPro64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winXPPro64Guest'
      winNetWebGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetWebGuest'
      winNetStandardGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetStandardGuest'
      winNetEnterpriseGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetEnterpriseGuest'
      winNetDatacenterGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetDatacenterGuest'
      winNetBusinessGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetBusinessGuest'
      winNetStandard64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetStandard64Guest'
      winNetEnterprise64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetEnterprise64Guest'
      winLonghornGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winLonghornGuest'
      winLonghorn64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winLonghorn64Guest'
      winNetDatacenter64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winNetDatacenter64Guest'
      winVistaGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winVistaGuest'
      winVista64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'winVista64Guest'
      windows7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows7Guest'
      windows7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows7_64Guest'
      windows7Server64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows7Server64Guest'
      windows8Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows8Guest'
      windows8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows8_64Guest'
      windows8Server64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows8Server64Guest'
      windows9Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows9Guest'
      windows9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows9_64Guest'
      windows9Server64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows9Server64Guest'
      windows11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows11_64Guest'
      windows12_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows12_64Guest'
      windowsHyperVGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windowsHyperVGuest'
      windows2019srv_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows2019srv_64Guest'
      windows2019srvNext_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows2019srvNext_64Guest'
      windows2022srvNext_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'windows2022srvNext_64Guest'
      freebsdGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsdGuest'
      freebsd64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd64Guest'
      freebsd11Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd11Guest'
      freebsd11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd11_64Guest'
      freebsd12Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd12Guest'
      freebsd12_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd12_64Guest'
      freebsd13Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd13Guest'
      freebsd13_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd13_64Guest'
      freebsd14Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd14Guest'
      freebsd14_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd14_64Guest'
      freebsd15Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd15Guest'
      freebsd15_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'freebsd15_64Guest'
      redhatGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'redhatGuest'
      rhel2Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel2Guest'
      rhel3Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel3Guest'
      rhel3_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel3_64Guest'
      rhel4Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel4Guest'
      rhel4_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel4_64Guest'
      rhel5Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel5Guest'
      rhel5_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel5_64Guest'
      rhel6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel6Guest'
      rhel6_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel6_64Guest'
      rhel7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel7Guest'
      rhel7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel7_64Guest'
      rhel8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel8_64Guest'
      rhel9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel9_64Guest'
      rhel10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rhel10_64Guest'
      centosGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centosGuest'
      centos64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos64Guest'
      centos6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos6Guest'
      centos6_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos6_64Guest'
      centos7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos7Guest'
      centos7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos7_64Guest'
      centos8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos8_64Guest'
      centos9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'centos9_64Guest'
      oracleLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinuxGuest'
      oracleLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux64Guest'
      oracleLinux6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux6Guest'
      oracleLinux6_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux6_64Guest'
      oracleLinux7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux7Guest'
      oracleLinux7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux7_64Guest'
      oracleLinux8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux8_64Guest'
      oracleLinux9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux9_64Guest'
      oracleLinux10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oracleLinux10_64Guest'
      suseGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'suseGuest'
      suse64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'suse64Guest'
      slesGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'slesGuest'
      sles64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles64Guest'
      sles10Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles10Guest'
      sles10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles10_64Guest'
      sles11Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles11Guest'
      sles11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles11_64Guest'
      sles12Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles12Guest'
      sles12_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles12_64Guest'
      sles15_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles15_64Guest'
      sles16_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sles16_64Guest'
      nld9Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'nld9Guest'
      oesGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'oesGuest'
      sjdsGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'sjdsGuest'
      mandrakeGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'mandrakeGuest'
      mandrivaGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'mandrivaGuest'
      mandriva64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'mandriva64Guest'
      turboLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'turboLinuxGuest'
      turboLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'turboLinux64Guest'
      ubuntuGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'ubuntuGuest'
      ubuntu64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'ubuntu64Guest'
      debian4Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian4Guest'
      debian4_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian4_64Guest'
      debian5Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian5Guest'
      debian5_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian5_64Guest'
      debian6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian6Guest'
      debian6_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian6_64Guest'
      debian7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian7Guest'
      debian7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian7_64Guest'
      debian8Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian8Guest'
      debian8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian8_64Guest'
      debian9Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian9Guest'
      debian9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian9_64Guest'
      debian10Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian10Guest'
      debian10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian10_64Guest'
      debian11Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian11Guest'
      debian11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian11_64Guest'
      debian12Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian12Guest'
      debian12_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian12_64Guest'
      debian13Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian13Guest'
      debian13_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'debian13_64Guest'
      asianux3Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux3Guest'
      asianux3_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux3_64Guest'
      asianux4Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux4Guest'
      asianux4_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux4_64Guest'
      asianux5_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux5_64Guest'
      asianux7_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux7_64Guest'
      asianux8_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux8_64Guest'
      asianux9_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'asianux9_64Guest'
      miraclelinux_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'miraclelinux_64Guest'
      pardus_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'pardus_64Guest'
      opensuseGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'opensuseGuest'
      opensuse64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'opensuse64Guest'
      fedoraGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'fedoraGuest'
      fedora64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'fedora64Guest'
      coreos64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'coreos64Guest'
      vmwarePhoton64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmwarePhoton64Guest'
      other24xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other24xLinuxGuest'
      other26xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other26xLinuxGuest'
      otherLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'otherLinuxGuest'
      other3xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other3xLinuxGuest'
      other4xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other4xLinuxGuest'
      other5xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other5xLinuxGuest'
      other6xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other6xLinuxGuest'
      other7xLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other7xLinuxGuest'
      genericLinuxGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'genericLinuxGuest'
      other24xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other24xLinux64Guest'
      other26xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other26xLinux64Guest'
      other3xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other3xLinux64Guest'
      other4xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other4xLinux64Guest'
      other5xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other5xLinux64Guest'
      other6xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other6xLinux64Guest'
      other7xLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'other7xLinux64Guest'
      otherLinux64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'otherLinux64Guest'
      solaris6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris6Guest'
      solaris7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris7Guest'
      solaris8Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris8Guest'
      solaris9Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris9Guest'
      solaris10Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris10Guest'
      solaris10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris10_64Guest'
      solaris11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'solaris11_64Guest'
      fusionos_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'fusionos_64Guest'
      prolinux_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'prolinux_64Guest'
      kylinlinux_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'kylinlinux_64Guest'
      flatcar_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'flatcar_64Guest'
      os2Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'os2Guest'
      eComStationGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'eComStationGuest'
      eComStation2Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'eComStation2Guest'
      netware4Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'netware4Guest'
      netware5Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'netware5Guest'
      netware6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'netware6Guest'
      openServer5Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'openServer5Guest'
      openServer6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'openServer6Guest'
      unixWare7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'unixWare7Guest'
      darwinGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwinGuest'
      darwin64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin64Guest'
      darwin10Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin10Guest'
      darwin10_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin10_64Guest'
      darwin11Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin11Guest'
      darwin11_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin11_64Guest'
      darwin12_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin12_64Guest'
      darwin13_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin13_64Guest'
      darwin14_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin14_64Guest'
      darwin15_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin15_64Guest'
      darwin16_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin16_64Guest'
      darwin17_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin17_64Guest'
      darwin18_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin18_64Guest'
      darwin19_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin19_64Guest'
      darwin20_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin20_64Guest'
      darwin21_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin21_64Guest'
      darwin22_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin22_64Guest'
      darwin23_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'darwin23_64Guest'
      vmkernelGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernelGuest'
      vmkernel5Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel5Guest'
      vmkernel6Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel6Guest'
      vmkernel65Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel65Guest'
      vmkernel7Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel7Guest'
      vmkernel8Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel8Guest'
      vmkernel9Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'vmkernel9Guest'
      amazonlinux2_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'amazonlinux2_64Guest'
      amazonlinux3_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'amazonlinux3_64Guest'
      crxPod1Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'crxPod1Guest'
      crxSys1Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'crxSys1Guest'
      rockylinux_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'rockylinux_64Guest'
      almalinux_64Guest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'almalinux_64Guest'
      otherGuest: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'otherGuest'
      otherGuest64: _typing.ClassVar['GuestOsDescriptor.GuestOsIdentifier'] = 'otherGuest64'

   class FirmwareType(pyVmomi.VmomiSupport.Enum):
      """
      Firmware types
      
      Attributes:
          bios: BIOS firmware
          efi: Extensible Firmware Interface
          csm: Compatibility Support Module for EFI
      """
      bios: _typing.ClassVar['GuestOsDescriptor.FirmwareType'] = 'bios'
      efi: _typing.ClassVar['GuestOsDescriptor.FirmwareType'] = 'efi'
      csm: _typing.ClassVar['GuestOsDescriptor.FirmwareType'] = 'csm'

   class SupportLevel(pyVmomi.VmomiSupport.Enum):
      """
      Guest OS support level
      
      Attributes:
          experimental: This operating system is not supported,
              but may be supported in the future.
          legacy: This operating system is not fully supported,
              but may have been supported in the past.
          terminated: No longer supported.
          supported: Fully supported.
          unsupported: This operating system is not supported.
          deprecated: Support for this operating system will be terminated in the future.
              
              Please migrate to using a different operating system.
          techPreview: This operating system may not be supported yet,
              please check VMware compatibility guide.
      """
      experimental: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'experimental'
      legacy: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'legacy'
      terminated: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'terminated'
      supported: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'supported'
      unsupported: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'unsupported'
      deprecated: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'deprecated'
      techPreview: _typing.ClassVar['GuestOsDescriptor.SupportLevel'] = 'techPreview'

   id: str
   family: str
   fullName: str
   supportedMaxCPUs: int
   numSupportedPhysicalSockets: int
   numSupportedCoresPerSocket: int
   supportedMinMemMB: int
   supportedMaxMemMB: int
   recommendedMemMB: int
   recommendedColorDepth: int
   supportedDiskControllerList: list[type] = []
   recommendedSCSIController: _typing.Optional[type] = None
   recommendedDiskController: type
   supportedNumDisks: int
   recommendedDiskSizeMB: int
   recommendedCdromController: type
   supportedEthernetCard: list[type] = []
   recommendedEthernetCard: _typing.Optional[type] = None
   supportsSlaveDisk: _typing.Optional[bool] = None
   cpuFeatureMask: list[pyVmomi.vim.host.CpuIdInfo] = []
   smcRequired: bool
   supportsWakeOnLan: bool
   supportsVMI: bool
   supportsMemoryHotAdd: bool
   supportsCpuHotAdd: bool
   supportsCpuHotRemove: bool
   supportedFirmware: list[str] = []
   recommendedFirmware: str
   supportedUSBControllerList: list[type] = []
   recommendedUSBController: _typing.Optional[type] = None
   supports3D: bool
   recommended3D: bool
   smcRecommended: bool
   ich7mRecommended: bool
   usbRecommended: bool
   supportLevel: str
   supportedForCreate: bool
   vRAMSizeInKB: pyVmomi.vim.option.IntOption
   numSupportedFloppyDevices: int
   wakeOnLanEthernetCard: list[type] = []
   supportsPvscsiControllerForBoot: bool
   diskUuidEnabled: bool
   supportsHotPlugPCI: bool
   supportsSecureBoot: _typing.Optional[bool] = None
   defaultSecureBoot: _typing.Optional[bool] = None
   persistentMemorySupported: _typing.Optional[bool] = None
   supportedMinPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   supportedMaxPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   recommendedPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   persistentMemoryHotAddSupported: _typing.Optional[bool] = None
   persistentMemoryHotRemoveSupported: _typing.Optional[bool] = None
   persistentMemoryColdGrowthSupported: _typing.Optional[bool] = None
   persistentMemoryColdGrowthGranularityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   persistentMemoryHotGrowthSupported: _typing.Optional[bool] = None
   persistentMemoryHotGrowthGranularityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   numRecommendedPhysicalSockets: _typing.Optional[int] = None
   numRecommendedCoresPerSocket: _typing.Optional[int] = None
   vvtdSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vbsSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vsgxSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vsgxRemoteAttestationSupported: _typing.Optional[bool] = None
   supportsTPM20: _typing.Optional[bool] = None
   recommendedTPM20: _typing.Optional[bool] = None
   vwdtSupported: _typing.Optional[bool] = None


class GuestQuiesceSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object type encapsulates configuration settings
   when creating a virtual machine quiesced snapshot.
   
   Attributes:
       timeout: The property to indicate maximum time in minutes for snapshot operation
           to be performed on the virtual machine.
           
           The timeout can not be less than 5 minutes or more than 240 minutes.
   """
   timeout: _typing.Optional[int] = None


class IdeDiskDeviceInfo(DiskDeviceInfo):
   """
   The IdeDiskDeviceInfo class contains detailed information about a specific
   IDE disk hardware device.
   
   These devices are for the
   vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo and
   vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo backings.
   """
   class PartitionInfo(pyVmomi.vmodl.DynamicData):
      """
      Describes the partition sizes
      
      Attributes:
          id: Identification of the partition
          capacity: Size of partition
      """
      id: int
      capacity: int

   partitionTable: list[IdeDiskDeviceInfo.PartitionInfo] = []


class IndependentFilterSpec(BaseIndependentFilterSpec):
   """
   The IndependentFilterSpec data object is used to specify the independent
   filters to be associated with virtual machine disks.
   
   Attributes:
       filterName: Name/id of the IO filter.
       filterClass: IO filter class.
       filterCapabilities: Capabilities defined by the above filter.
           
           Basically this key value pair define the configurable properties
           of the independent filters. Users can specify desired values.
   
   Since: vSphere API Release 7.0.2.1
   """
   filterName: str
   filterClass: _typing.Optional[str] = None
   filterCapabilities: list[pyVmomi.vim.KeyValue] = []


class InstantCloneSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for creating an Instant Clone of a powered-on virtual machine.
   
   Attributes:
       name: The name of the cloned virtual machine.
       location: A type of `pyVmomi.vim.vm.RelocateSpec` that specifies the location of
           resources the newly created virtual machine will use.
           
           The location might be empty or specify:
           - The folder where the virtual machine should be located. If not
             specified, the root VM folder of the source VM will be used.
           - A datastore where the InstantCloned virtual machine will be located
             on the physical storage.
           - A resource pool determines where compute resources will be
             available to the clone.
           - A device change specification. The only allowed device changes
             are edits of VirtualEthernetCard and filebacked Serial/Parallel
             ports.
             
           All other settings are NOT supported.
       config: A list of key value pairs that will be passed to the destination VM.
           
           These pairs should be used to provide user-defined customization to
           differentiate the destination VM from the source VM. Values will be
           queryable via destination VM's `pyVmomi.vim.vm.ConfigInfo.extraConfig`.
       biosUuid: 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string
           in \"12345678-abcd-1234-cdef-123456789abc\" format.
   """
   name: str
   location: RelocateSpec
   config: list[pyVmomi.vim.option.OptionValue] = []
   biosUuid: _typing.Optional[str] = None


class LegacyNetworkSwitchInfo(pyVmomi.vmodl.DynamicData):
   """
   The LegacyNetworkSwitchInfo data object type contains information about
   the legacy network switches available on the host.
   - VMware Server - Options available for the \"custom\" NetworkBackingType.
   - ESX Server - The \"esxnet\" NetworkBackingType.
   
   Attributes:
       name: The name of the network switch.
   """
   name: str


class Message(pyVmomi.vmodl.DynamicData):
   """
   Message data which is intended to be displayed according
   to the locale of a client.
   
   A `pyVmomi.vim.vm.Message` contains both a formatted, localized version of the
   text and the data needed to perform localization in conjunction
   with localization catalogs.
   
   Clients of the VIM API may use
   `pyVmomi.vim.SessionManager`.`pyVmomi.vim.SessionManager.setLocale`
   to cause the server to emit localized `pyVmomi.vim.vm.Message.text`, or may perform
   client-side localization based on message catalogs provided by the
   `pyVmomi.vim.LocalizationManager`.
   
   Message variables are always integers, e.g. {1} and {2}, which are
   1-based indexes into `pyVmomi.vim.vm.Message.argument`.
   - The corresponding argument may be a recursive lookup:
     - `pyVmomi.vim.vm.Message.argument` = [\"button.cancel\", \"msg.revert\"]
     - CATALOG(locmsg, `pyVmomi.vim.vm.Message.id`) = \"Select '{1}' to {2}\"
     - CATALOG(locmsg, button.cancel) = \"Cancel\"
     - CATALOG(locmsg, msg.revert) = \"revert\"
     - \\==> `pyVmomi.vim.vm.Message.text` = \"Select 'Cancel' to revert\"
   - If the recursive lookup fails, the argument is a plain string.
     - `pyVmomi.vim.vm.Message.argument` = [\"127.0.0.1\"]
     - CATALOG(locmsg, `pyVmomi.vim.vm.Message.id`) = \"IP address is {1}\"
     - \\==> `pyVmomi.vim.vm.Message.text` \"IP address is 127.0.0.1\"
       
   See Also: `pyVmomi.vim.LocalizationManager`
   
   Attributes:
       id: A unique identifier for this particular message.
           
           This field is a key for looking up format strings in the locmsg
           catalog.
       argument: Substitution arguments for variables in the localized message.
           
           Substitution variables in the format string identified by `pyVmomi.vim.vm.Message.id`
           are 1-based indexes into this array. Substitution variable {1}
           corresponds to argument[0], etc.
       text: Text in session locale.
           
           Use `pyVmomi.vim.SessionManager`.`pyVmomi.vim.SessionManager.setLocale` to
           change the session locale.
   """
   id: str
   argument: list[object] = []
   text: _typing.Optional[str] = None


class NetworkInfo(TargetInfo):
   """
   NetworkInfo describes a network that a device backing
   can attached to.
   
   Attributes:
       network: Information about the network
       vswitch: Key of parent vSwitch of the network
   """
   network: pyVmomi.vim.Network.Summary
   vswitch: _typing.Optional[str] = None


class NetworkShaperInfo(pyVmomi.vmodl.DynamicData):
   """
   Network traffic shaping specification.
   
   Traffic shaping is used to configure the network utilization
   characteristics of a virtual machine.
   
   Attributes:
       enabled: Is the shaper enabled?
       peakBps: Peak bandwidth, in bits per second.
       averageBps: Average bandwidth, in bits per second.
       burstSize: Burst size, in bytes.
   """
   enabled: _typing.Optional[bool] = None
   peakBps: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   averageBps: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   burstSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class OpaqueNetworkInfo(TargetInfo):
   """
   This class describes an opaque network that a device backing
   can attached to.
   
   Attributes:
       network: Information about the opaque network
       networkReservationSupported: Indicates whether network bandwidth reservation is supported on
           the opaque network
   """
   network: pyVmomi.vim.OpaqueNetwork.Summary
   networkReservationSupported: _typing.Optional[bool] = None

class ParallelInfo(TargetInfo):
   """
   ParallelInfo class contains information about a physical parallel
   drive on the host.
   """
   pass


class PciPassthroughInfo(TargetInfo):
   """
   Description of a generic PCI device that can be attached to a virtual machine.
   
   Attributes:
       pciDevice: Details of the PCI device, including vendor, class and
           device identification information.
       systemId: The ID of the system the PCI device is attached to.
   """
   pciDevice: pyVmomi.vim.host.PciDevice
   systemId: str

class PciSharedGpuPassthroughInfo(TargetInfo):
   """
   Description of a gpu PCI device that can be shared with a virtual machine.
   
   Attributes:
       vgpu: The VGPU corresponding to this GPU passthrough device.
   """
   vgpu: str


class PrecisionClockInfo(TargetInfo):
   """
   The PrecisionClockInfo data object type describes available host
   clock resources, which can be used as backing reference for
   virtual precision clock devices.
   
   Attributes:
       systemClockProtocol: The current host system clock synchronization protocol.
           
           Used for specifying protocol in
           `pyVmomi.vim.vm.device.VirtualPrecisionClock.SystemClockBackingInfo`.
   """
   systemClockProtocol: _typing.Optional[str] = None


class ProfileDetails(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vm.ProfileDetails` data object type provides details of the policy
   associated with a virtual machine and it's virtual disks.
   
   Attributes:
       profile: Storage profile associated with Virtual Machine's home directory.
       diskProfileDetails: An optional list that allows specifying details of the policy associated
           with virtual disks.
   """
   class DiskProfileDetails(pyVmomi.vmodl.DynamicData):
      """
      Details of the policies associated with Virtual Disks.
      
      Attributes:
          diskId: Virtual disk ID.
          profile: Storage profile associated with the Virtual Disk.
      """
      diskId: int
      profile: list[ProfileSpec] = []

   profile: list[ProfileSpec] = []
   diskProfileDetails: list[ProfileDetails.DiskProfileDetails] = []


class ProfileRawData(pyVmomi.vmodl.DynamicData):
   """
   The extensible data object type encapsulates additional data specific
   to Virtual Machine and its devices.
   
   This data is provided by vSphere Extensions which are integral part
   of vSphere.
   
   The data is not persisted in Virtual Machine configuration file but is
   stored and managed by extensions.
   
   Storage Profile Based Management (SPBM) will be one of the consumers of
   this data structure. SPBM will provide detailed information about
   Virtual Machine storage requirements.
   
   Attributes:
       extensionKey: vSphere Extension Identifier
       objectData: Extension-specific additional data to be associated
           with Virtual machine and its devices.
   """
   extensionKey: str
   objectData: _typing.Optional[str] = None


class PropertyRelation(pyVmomi.vmodl.DynamicData):
   """
   Data object which represents relations between a
   property and its target value and the required values
   of any other properties in the vm configuration so
   that the target value can be set.
   
   Attributes:
       key: The target property and its value
       relations: The related properties and their values
   """
   key: pyVmomi.vmodl.DynamicProperty
   relations: list[pyVmomi.vmodl.DynamicProperty] = []


class QuestionInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes the question that is currently
   blocking a virtual machine.
   
   Attributes:
       id: Identifier with an opaque value that specifies the pending question.
       text: Text that describes the pending question.
       choice: List of key-value pairs that specify possible answers.
       message: The message data for the individual messages that comprise the question.
           
           Only available on servers that support localization.
   """
   id: str
   text: str
   choice: pyVmomi.vim.option.ChoiceOption
   message: list[Message] = []


class RelocateSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for moving or copying a virtual machine to a different datastore
   or host.
   
   Attributes:
       service: The service endpoint of vCenter where the virtual machine should be
           located.
           
           If not specified, the current vCenter service is used. If the
           virtual machine is relocated to a different vCenter service, the
           destination host, pool, and datastore parameters have to be explicitly
           specified by default when the task is submitted.
       folder: The folder where the virtual machine should be located.
           
           If not specified,
           the root VM folder of the destination datacenter will be used.
       datastore: The datastore where the virtual machine should be located.
           
           If
           not specified, the current datastore is used.
       diskMoveType: Manner in which to move the virtual disk to the `pyVmomi.vim.vm.RelocateSpec.datastore`.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.RelocateSpec.DiskMoveOptions`.
           
           This property applies to all the disks which the virtual machine has,
           but can be overridden on a per-disk basis using
           `pyVmomi.vim.vm.RelocateSpec.DiskLocator.diskMoveType` prior to vSphere
           API 6.0 or using
           `pyVmomi.vim.vm.device.VirtualDiskSpec.diskMoveType` in vSphere API
           6.0 and later.
           
           This property can only be set if
           `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported` is true.
           
           If left unset then
           `moveAllDiskBackingsAndDisallowSharing`
           is assumed.
       pool: The resource pool to which this virtual machine should be attached.
           - For a relocate or clone operation to a virtual machine, if the
             argument is not supplied, the current resource pool of virtual
             machine is used.
           - For a clone operation from a template to a virtual machine,
             this argument is required.
           - If the virtual machine is relocated to a different vCenter service,
             and a resource pool is not specified, the destination host must be
             specified.
           - If a resource pool is specified, the virtual machine is powered
             on, and the target pool represents a cluster without DRS enabled,
             an InvalidArgument exception is thrown.
           - If the virtual machine is relocated to a different datacenter
             within the vCenter service, the resource pool has to be specified
             and cannot be unset.
       host: The target host for the virtual machine.
           
           If not specified,
           - if resource pool is not specified, current host is used.
           - if resource pool is specified, and the target pool represents
             a stand-alone host, the host is used.
           - if resource pool is specified, the virtual machine is powered on,
             and the target pool represents a DRS-enabled cluster, a host
             selected by DRS is used.
           - if resource pool is specified, the virtual machine is powered on,
             and the target pool represents a cluster without DRS enabled,
             an InvalidArgument exception is thrown.
           - if a resource pool is specified, the target pool represents a
             cluster, and this is a clone or the virtual machine is powered
             off, a random compatible host is chosen.
           - A destination host must be specified if the virtual machine is
             relocated to a different vCenter service, and a resource pool is
             not specified.
       disk: An optional list that allows specifying the datastore location
           for each virtual disk.
       transform: Transformation to perform on the disks.
           
           The backend is free to ignore
           this hint if it is not valid for the current operation. This can be
           used by clients, for example, to create sparse disks for templates.
       deviceChange: An optional list of virtual device specs that allow specifying the new
           device locations for the relocate operation.
           
           The supported device changes are:
           - For `pyVmomi.vim.vm.device.VirtualEthernetCard`, it has to be used
             in `pyVmomi.vim.vm.device.VirtualDeviceSpec.device` to specify the
             target network backing.
           - For `pyVmomi.vim.vm.device.VirtualDisk`, it can be used to specify
             vFlash cache configuration, or the storage profile for destination
             disks. The storage profiles are used to either upgrade the virtual
             disk's storage to a persistent memory, or keep the virtual disk
             in persistent memory when moving the virtual machine's overall
             storage.
           - All other specification are ignored.
       profile: Storage profile requirement for Virtual Machine's home directory.
           
           Profiles are solution specific.
           Storage Profile Based Management(SPBM) is a vSphere server extension.
           The API users who want to provision VMs using Storage Profiles, need to
           interact with SPBM.
           This is an optional parameter and if user doesn't specify profile,
           the default behavior will apply.
       cryptoSpec: Virtual Machine cryptographic options.
           
           Encryption requirement for the virtual machine's metadata
           files (non-disk files).
       tagSpecs: Specification of the vSphere tags that need to be modified for this
           virtual machine.
           
           Each TagSpec refers to:
           \\- Operation to be performed, i.e., attach a new tag to a VM with this
           RelocateSpec or detach an existing tag from a VM with this
           RelocateSpec.
           \\- Information required to uniquely identify the vSphere tag that needs
           to be attached or detached.
           
           When this field is specified in the RelocateSpec during
           `pyVmomi.vim.VirtualMachine.clone` or
           `pyVmomi.vim.VirtualMachine.relocate`,
           the tags specified in tagSpecs will be automatically attached or
           detached (based on the operation type) from the new VM.
           
           Since: vSphere API Release 9.1.0.0
       vmPlacementPolicies: An optional list of `pyVmomi.vim.vm.VmPlacementPolicy` for this VM.
           
           Each policy
           describes a constraint or preference that can influence where, when
           and how this VM should be placed.
           
           If this RelocateSpec is specified during an operation (such as while
           finding a suitable placement for a VM before to relocate that VM), then
           the placement policies specified here will be automatically enforced
           without requiring the client to separately create any vSphere placement
           policy (such as vSphere compute-policies) and associate this VM with it.
           For more details, see `pyVmomi.vim.vm.VmPlacementPolicy` and different types of
           placement policies derived from it.
           
           Note: These placement policies are only applicable when a VM is managed
           by Supervisor. They will be automatically populated by Supervisor based
           on the placement constraints defined in Supervisor. This field will be
           ignored except when set by Supervisor.
           
           Since: vSphere API Release 9.1.0.0
       skipExtensionCompatibilityChecks: Whether to skip enforcement of the `pyVmomi.vim.vm.ExtensionCompatibilityConstraint` registered on the virtual machine for
           this relocate operation.
           
           Intended for a managing extension's service accounts, so they can relocate
           the VMs they manage without being blocked by the constraints they
           registered. Honored only when the caller holds the
           VirtualMachine.ExtensionCompatibility.Bypass privilege on the virtual machine;
           otherwise the operation is rejected. Built-in compatibility checks (host
           compatibility, SPBM, and so on) are still enforced.
           
           Since: vSphere API Release 9.1.2.0
   """
   class Transformation(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: as of vSphere API 5.0.The set of transformations that can be performed on the virtual disks
      as part of the copy.
      """
      flat: _typing.ClassVar['RelocateSpec.Transformation'] = 'flat'
      sparse: _typing.ClassVar['RelocateSpec.Transformation'] = 'sparse'

   class DiskLocator(pyVmomi.vmodl.DynamicData):
      """
      The DiskLocator data object type specifies a virtual disk device (by ID) and
      a datastore locator for the disk's storage.
      
      Attributes:
          diskId: Device ID of the virtual disk.
          datastore: Target datastore.
          diskMoveType: Manner in which to move the virtual disk to the `pyVmomi.vim.vm.RelocateSpec.DiskLocator.datastore`.
              
              The set of possible values is described
              in `pyVmomi.vim.vm.RelocateSpec.DiskMoveOptions`.
              
              This property can only be set if `pyVmomi.vim.host.Capability.deltaDiskBackingsSupported` is true.
              
              If left unset then `moveAllDiskBackingsAndDisallowSharing`
              is assumed.
          diskBackingInfo: Backing information for the virtual disk at the destination.
              
              This can be used, for instance, to change the format of the
              virtual disk. If the specified backing is invalid or not
              supported at the destination, `pyVmomi.vim.fault.InvalidDeviceBacking` is thrown. Specific property
              changes may be ignored if they are not supported.
              
              Supported BackingInfo types and properties:
              - `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo`
                - thinProvisioned
                - eagerlyScrub
              - `pyVmomi.vim.vm.device.VirtualDisk.SeSparseBackingInfo`
                (ESX 5.1 or later)
          profile: Virtual Disk Profile requirement.
              
              Profiles are solution specific.
              Profile Based Storage Management is a vSphere server extension.
              The API users who want to provision VMs using Storage Profiles, need to
              interact with it.
              This is an optional parameter and if user doesn't specify profile,
              the default behavior will apply.
          backing: Cryptographic option of the current disk.
          filterSpec: List of independent filters `pyVmomi.vim.vm.IndependentFilterSpec`
              to be configured on the virtual disk after the relocate.
              
              Since: vSphere API Release 7.0.2.1
      """
      class BackingSpec(pyVmomi.vmodl.DynamicData):
         """
         ``pyVmomi.vim.vm.RelocateSpec.DiskLocator.BackingSpec`` is a data
         object type for cryptographic information about the backing of a
         device.
         
         The member `pyVmomi.vim.vm.RelocateSpec.DiskLocator.BackingSpec.parent` refers the parent in the chain of
         `pyVmomi.vim.vm.device.VirtualDevice.BackingInfo` objects.
         """
         parent: _typing.Optional[RelocateSpec.DiskLocator.BackingSpec] = None
         crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None

      diskId: int
      datastore: pyVmomi.vim.Datastore
      diskMoveType: _typing.Optional[str] = None
      diskBackingInfo: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []
      backing: _typing.Optional[RelocateSpec.DiskLocator.BackingSpec] = None
      filterSpec: list[BaseIndependentFilterSpec] = []

   class DiskMoveOptions(pyVmomi.VmomiSupport.Enum):
      """
      Specifies how a virtual disk is moved or copied to a
      datastore.
      
      In all cases after the move or copy the virtual machine's current running point
      will be placed on the target datastore. The current running point is defined
      as the disk backing which the virtual machine is currently
      writing to. This end state can be achieved in multiple
      ways, and the supported options are described in this
      enumeration.
      
      These options are only relevant when the backing of the
      specified disk is a `pyVmomi.vim.vm.device.VirtualDevice.FileBackingInfo`.
      
      Since disk backings may become shared as the result of
      either a `pyVmomi.vim.VirtualMachine.clone` or
      a `pyVmomi.vim.VirtualMachine.relocate`,
      `pyVmomi.vim.VirtualMachine.promoteDisks` has been provided as
      a way to unshare such disk backings.
      
      See Also: `pyVmomi.vim.vm.device.VirtualDisk.SparseVer1BackingInfo.parent`, `pyVmomi.vim.vm.device.VirtualDisk.SparseVer2BackingInfo.parent`, `pyVmomi.vim.vm.device.VirtualDisk.FlatVer1BackingInfo.parent`, `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo.parent`, `pyVmomi.vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.parent`, `pyVmomi.vim.vm.RelocateSpec.diskMoveType`, `pyVmomi.vim.vm.RelocateSpec.DiskLocator.diskMoveType`
      
      Attributes:
          moveAllDiskBackingsAndAllowSharing: All of the virtual disk's backings should be moved to the new datastore.
              
              If a disk backing is not the child-most backing of this virtual machine,
              and there exists a read-only disk backing with the same content ID
              on the target datastore, then this disk backing may not be copied. Instead
              it is acceptable to attach to the read-only disk backing at the target
              datastore. A read-only disk backing is defined as a virtual disk
              backing which no virtual machine is currently writing to.
          moveAllDiskBackingsAndDisallowSharing: All of the virtual disk's backings should be moved to the new datastore.
              
              It is not acceptable to attach to a disk backing with the same content ID
              on the destination datastore. During a `pyVmomi.vim.VirtualMachine.clone` any delta disk backings will be consolidated.
          moveChildMostDiskBacking: Move only the child-most disk backing.
              
              Any parent disk backings should
              be left in their current locations.
              
              This option only differs from `moveAllDiskBackingsAndAllowSharing` and
              `moveAllDiskBackingsAndDisallowSharing` when the virtual
              disk has a parent backing.
              
              Note that in the case of a `pyVmomi.vim.VirtualMachine.clone`,
              this means that the parent disks will now be shared. This is safe as any
              parent disks are always read-only.
              Note that in the case of a `pyVmomi.vim.VirtualMachine.relocate` operation,
              only the virtual disks in the current virtual machine configuration are moved.
          createNewChildDiskBacking: Create a new child disk backing on the destination datastore.
              
              None of the
              virtual disk's existing files should be moved from their current locations.
              
              Note that in the case of a `pyVmomi.vim.VirtualMachine.clone`,
              this means that the original virtual machine's disks are now all being shared.
              This is only safe if the clone was taken from a snapshot point, because
              snapshot points are always read-only. Thus for a clone this
              option is only valid `pyVmomi.vim.vm.CloneSpec.snapshot`.
              createNewChildDiskBacking is not a supported operation for
              `pyVmomi.vim.VirtualMachine.relocate` operations unless all disks are moving.
          moveAllDiskBackingsAndConsolidate: All of the virtual disk's backings should be moved to the new datastore.
              
              During a `pyVmomi.vim.VirtualMachine.clone` or a
              `pyVmomi.vim.VirtualMachine.migrate`, any delta disk backings will be
              consolidated.
      """
      moveAllDiskBackingsAndAllowSharing: _typing.ClassVar['RelocateSpec.DiskMoveOptions'] = 'moveAllDiskBackingsAndAllowSharing'
      moveAllDiskBackingsAndDisallowSharing: _typing.ClassVar['RelocateSpec.DiskMoveOptions'] = 'moveAllDiskBackingsAndDisallowSharing'
      moveChildMostDiskBacking: _typing.ClassVar['RelocateSpec.DiskMoveOptions'] = 'moveChildMostDiskBacking'
      createNewChildDiskBacking: _typing.ClassVar['RelocateSpec.DiskMoveOptions'] = 'createNewChildDiskBacking'
      moveAllDiskBackingsAndConsolidate: _typing.ClassVar['RelocateSpec.DiskMoveOptions'] = 'moveAllDiskBackingsAndConsolidate'

   service: _typing.Optional[pyVmomi.vim.ServiceLocator] = None
   folder: _typing.Optional[pyVmomi.vim.Folder] = None
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   diskMoveType: _typing.Optional[str] = None
   pool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   disk: list[RelocateSpec.DiskLocator] = []
   transform: _typing.Optional[RelocateSpec.Transformation] = None
   deviceChange: list[pyVmomi.vim.vm.device.VirtualDeviceSpec] = []
   profile: list[ProfileSpec] = []
   cryptoSpec: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   tagSpecs: list[pyVmomi.vim.TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []
   skipExtensionCompatibilityChecks: _typing.Optional[bool] = None


class ReplicationConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   The ReplicationConfigSpec object type encapsulates the replication
   configuration parameters for a virtual machine.
   
   It consists of two
   parts: 1) a set of virtual machine-wide replication properties; 2)
   a set of properties per replicated virtual disk. ReplicationSetting
   is passed as an argument for initial replication configuration
   `pyVmomi.vim.HbrManager.enableReplication` as well as for
   re-configuration of a replicated VM's properties `pyVmomi.vim.HbrManager.reconfigureReplication`.
   
   Attributes:
       generation: A generation number (>=0) that reflects the \"freshness\" of the
           ReplicationConfigSpec on which a re-configuration is based.
           
           The
           generation number is used to detect and disallow concurrent
           updates to a VM's replication settings.
           For initial replication enablement, generation = 0. The
           replication settings of every replication re-configuration
           operation must reflect the latest generation number known to the
           caller. It takes an explicit call to get the latest replication
           settings to find out what the latest generation number is. The
           update algorithm of the generation number is opaque to the
           caller; e.g., the caller cannot assume that the generation
           numbers are incremented by one every time replication is
           (re)configured, not even that they are changing monotonically.
       vmReplicationId: An opaque identifier that uniquely identifies a replicated VM
           between primary and secondary sites.
       destination: The IP address of the HBR Server in the secondary site
           where this VM is replicated to.
           
           Note: If net encryption is enabled, this is the address of the
           encryption tunnelling agent.
       port: The port on the HBR Server in the secondary site where this VM
           is replicated to.
           
           Note: If net encryption is enabled, this is the port of the
           encryption tunneling agent.
       rpo: The Recovery Point Objective specified for this VM, in minutes.
           
           Currently, valid values are in the range of 1 minute to 1440
           minutes (24 hours).
       quiesceGuestEnabled: Flag that indicates whether or not to quiesce the file system or
           applications in the guest OS before a consistent replica is
           created.
       paused: Flag that indicates whether or not the vm or group has been paused for
           replication.
       oppUpdatesEnabled: Flag that indicates whether or not to perform opportunistic
           updates in-between consistent replicas.
       netCompressionEnabled: Flag that indicates whether or not compression should
           be used when sending traffic over the network.
           
           The primary will negotiate the best compression with
           the server on the secondary if this is enabled.
       netEncryptionEnabled: Flag that indicates whether or not encryption should
           be used when sending traffic over the network.
           
           The primary will use the remoteCertificateThumbprint
           to verify the identity of the remote server.
       encryptionDestination: The IP address of the remote HBR server, target for encrypted LWD.
           
           This field is required when net encryption is enabled, ignored otherwise.
       additionalEncryptionDestination: Since: vSphere API Release 9.1.0.0
       encryptionPort: The port on the remote HBR server, target for encrypted LWD.
           
           This field is only relevant when net encryption is enabled.
       remoteCertificateThumbprint: The SHA256 thumbprint of the remote server certificate.
           
           This field is only relevant when net encryption is enabled.
       dataSetsReplicationEnabled: Flag that indicates whether DataSets files are replicated or not.
           
           Since: vSphere API Release 8.0.0.0
       useHbrProxyHttpPreamble: Flag that indicates whether to use HTTP preamble for HBRProxy when
           connecting to the remote site.
           
           If unset, defaults to false.
           
           Since: vSphere API Release 9.1.0.0
       disk: The set of the disks of this VM that are configured for
           replication.
   """
   class DiskSettings(pyVmomi.vmodl.DynamicData):
      """
      The ReplicationConfigSpec.DiskSettings object type encapsulates
      the replication properties of a replicated disk of a replicated
      virtual machine.
      
      Attributes:
          key: The disk's device key in the VM's configuration.
              
              Used to
              uniquely identify the disk to be configured for replication
              in the primary VM.
          diskReplicationId: An opaque identifier that uniquely identifies a replicated
              disk between primary and secondary sites.
      """
      key: int
      diskReplicationId: str

   generation: pyVmomi.VmomiSupport.long
   vmReplicationId: str
   destination: str
   port: int
   rpo: pyVmomi.VmomiSupport.long
   quiesceGuestEnabled: bool
   paused: bool
   oppUpdatesEnabled: bool
   netCompressionEnabled: _typing.Optional[bool] = None
   netEncryptionEnabled: _typing.Optional[bool] = None
   encryptionDestination: _typing.Optional[str] = None
   additionalEncryptionDestination: list[str] = []
   encryptionPort: _typing.Optional[int] = None
   remoteCertificateThumbprint: _typing.Optional[str] = None
   dataSetsReplicationEnabled: _typing.Optional[bool] = None
   useHbrProxyHttpPreamble: _typing.Optional[bool] = None
   disk: list[ReplicationConfigSpec.DiskSettings] = []


class RuntimeInfo(pyVmomi.vmodl.DynamicData):
   """
   The RuntimeInfo data object type provides information about
   the execution state and history of a virtual machine.
   
   Attributes:
       device: Per-device runtime info.
           
           This array will be empty if the host
           software does not provide runtime info for any of the device
           types currently in use by the virtual machine.
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       host: The host that is responsible for running a virtual machine.
           
           This property is null if the virtual machine is not running and is
           not assigned to run on a particular host.
       connectionState: Indicates whether or not the virtual machine is available for management.
       powerState: The current power state of the virtual machine.
       vmFailoverInProgress: Represents if the vm is currently being failed over by FDM
           
           Since: vSphere API Release 7.0.2.0
       faultToleranceState: The fault tolerance state of the virtual machine.
       dasVmProtection: The vSphere HA protection state for a virtual machine.
           
           Property
           is unset if vSphere HA is not enabled.
       toolsInstallerMounted: Flag to indicate whether or not the VMware Tools installer
           is mounted as a CD-ROM.
       suspendTime: The timestamp when the virtual machine was most recently suspended.
           
           This property is updated every time the virtual machine is suspended.
       bootTime: The timestamp when the virtual machine was most recently powered on.
           
           This property is updated when the virtual machine is powered on
           from the poweredOff state, and is cleared when the virtual machine is
           powered off. This property is not updated when a virtual machine is resumed
           from a suspended state.
       suspendInterval: The total time the virtual machine has been suspended
           since it was initially powered on.
           
           This time excludes the current period,
           if the virtual machine is currently suspended. This property is updated
           when the virtual machine resumes, and is reset to zero when the virtual machine
           is powered off.
       question: The current question, if any, that is blocking the virtual machine's execution.
       memoryOverhead: The amount of memory resource (in bytes) that will be used by
           the virtual machine above its guest memory requirements.
           
           This value is set if and only if the virtual machine is registered
           on a host that supports memory resource allocation features.
           
           For powered off VMs, this is the minimum overhead required to
           power on the VM on the registered host.
           
           For powered on VMs, this is the current overhead reservation, a
           value which is almost always larger than the minimum overhead, and
           which grows with time.
       maxCpuUsage: Current upper-bound on CPU usage.
           
           The upper-bound is based on the host
           the virtual machine is current running on, as well as limits configured
           on the virtual machine itself or any parent resource pool.
           Valid while the virtual machine is running.
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       maxMemoryUsage: Current upper-bound on memory usage.
           
           The upper-bound is based on memory
           configuration of the virtual machine, as well as limits configured
           on the virtual machine itself or any parent resource pool.
           Valid while the virtual machine is running.
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       numMksConnections: Number of active MKS connections to this virtual machine.
       recordReplayState: Record / replay state of this virtual machine.
       cleanPowerOff: For a powered off virtual machine, indicates whether the virtual
           machine's last shutdown was an orderly power off or not.
           
           Unset if
           the virtual machine is running or suspended.
       needSecondaryReason: If set, indicates the reason the virtual machine needs a secondary.
       onlineStandby: This property indicates whether the guest has gone into one of the
           s1, s2 or s3 standby modes, false indicates the guest is awake.
       minRequiredEVCModeKey: For a powered-on or suspended virtual machine in a cluster with Enhanced
           VMotion Compatibility (EVC) enabled, this identifies the least-featured
           EVC mode (among those for the appropriate CPU vendor) that could admit
           the virtual machine.
           
           See `pyVmomi.vim.EVCMode`. Until vSphere 6.5, this
           property will be unset if the virtual machine is powered off or is not in
           an EVC cluster.
           
           This property may be used as a general indicator of the CPU feature
           baseline currently in use by the virtual machine. However, the virtual
           machine may be suppressing some of the features present in the CPU
           feature baseline of the indicated mode, either explicitly (in the
           virtual machine's configured
           `pyVmomi.vim.vm.ConfigInfo.cpuFeatureMask`) or implicitly
           (in the default masks for the
           `pyVmomi.vim.vm.GuestOsDescriptor` appropriate for the
           virtual machine's configured guest OS).
       consolidationNeeded: Whether any disk of the virtual machine requires consolidation.
           
           This can happen for example when a snapshot is deleted but its
           associated disk is not committed back to the base disk.
           Use `pyVmomi.vim.VirtualMachine.consolidateDisks` to consolidate if
           needed.
       offlineFeatureRequirement: These requirements must have equivalent host capabilities
           `pyVmomi.vim.host.ConfigInfo.featureCapability` in order to power on.
       featureRequirement: These requirements must have equivalent host capabilities
           `pyVmomi.vim.host.ConfigInfo.featureCapability` in order to power on,
           resume, or migrate to the host.
       featureMask: The masks applied to an individual virtual machine as a result of its
           configuration.
       vFlashCacheAllocation: Specifies the total allocated vFlash resource for the vFlash caches associated with VM's
           VMDKs when VM is powered on, in bytes.
       paused: Whether the virtual machine is paused, or not.
       snapshotInBackground: Whether a snapshot operation is in progress in the background, or not.
       quiescedForkParent: This flag indicates whether a parent virtual machine is in a fork ready
           state.
           
           A persistent instant clone child can be created only when this flag
           is true. While a non-persistent instant clone child can be created
           independent of this flag, it can only be powered on if this flag is true.
       instantCloneFrozen: Whether the virtual machine is frozen for instant clone, or not.
       cryptoState: Encryption state of the virtual machine.
           
           Valid values are enumerated by the
           `pyVmomi.vim.VirtualMachine.CryptoState` type.
       suspendedToMemory: Whether the virtual machine is suspended to memory, or not.
           
           Since: vSphere API Release 7.0.2.0
       opNotificationTimeout: Operation notification timeout in seconds.
           
           Specifies the maximum time duration the application may take to
           prepare for the operation after it has been notified.
           This property is set only for powered on VMs.
           
           Since: vSphere API Release 8.0.0.1
       iommuActive: Indicates whether there is active IOMMU domain in the current VM.
           
           Since: vSphere API Release 8.0.1.0
       consolidateWorkTotal: If consolidationNeeded is true, then this field is an upper
           estimate of the number of total bytes of work needed to
           consolidate all disks in the VM.
           
           (This value can also be treated
           as an upper estimate of the amount of additional, temporary,
           free space required for consolidate to succeed.)
           
           Since: vSphere API Release 9.1.0.0
       consolidateWorkDone: If consolidateNeeded is true, and a consolidate was begun but
           was interrupted, this field estimates how many bytes of work
           were performed already.
           
           Such consolidates can be resumed at
           this point under certain circumstances.
           
           Since: vSphere API Release 9.1.0.0
       diskChainBroken: If true, at least one disk chain in this VM is broken.
           
           The
           `pyVmomi.vim.vm.device.VirtualDisk.diskChainBrokenIssue` field
           in the broken disk(s) describes the nature of the breakage.
           If it's unset or false, no disk chain in this VM is broken.
           
           Since: vSphere API Release 9.1.0.0
   """
   class DasProtectionState(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.vm.RuntimeInfo.DasProtectionState` object describes the
      vSphere HA protection state of a virtual machine (VM).
      
      Attributes:
          dasProtected: Whether vSphere HA is protecting a virtual machine (VM).
              
              If a
              VM is protected, vSphere HA will enforce any availability
              features that have been enabled for this VM. For
              example, if the VM is running on a host
              that fails and the VM is configured to be restarted on a failure,
              then vSphere HA will attempt to restart the VM on another host.
              Similarly, if you enable VM/Application Health Monitoring
              for this VM, vSphere HA will monitor the heartbeats of the
              VM and reset the VM when needed, as dictated by the configured
              policy settings.
      """
      dasProtected: bool

   device: list[DeviceRuntimeInfo] = []
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   connectionState: pyVmomi.vim.VirtualMachine.ConnectionState
   powerState: pyVmomi.vim.VirtualMachine.PowerState
   vmFailoverInProgress: _typing.Optional[bool] = None
   faultToleranceState: pyVmomi.vim.VirtualMachine.FaultToleranceState
   dasVmProtection: _typing.Optional[RuntimeInfo.DasProtectionState] = None
   toolsInstallerMounted: bool
   suspendTime: _typing.Optional[_datetime.datetime] = None
   bootTime: _typing.Optional[_datetime.datetime] = None
   suspendInterval: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   question: _typing.Optional[QuestionInfo] = None
   memoryOverhead: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxCpuUsage: _typing.Optional[int] = None
   maxMemoryUsage: _typing.Optional[int] = None
   numMksConnections: int
   recordReplayState: pyVmomi.vim.VirtualMachine.RecordReplayState
   cleanPowerOff: _typing.Optional[bool] = None
   needSecondaryReason: _typing.Optional[str] = None
   onlineStandby: bool
   minRequiredEVCModeKey: _typing.Optional[str] = None
   consolidationNeeded: bool
   offlineFeatureRequirement: list[FeatureRequirement] = []
   featureRequirement: list[FeatureRequirement] = []
   featureMask: list[pyVmomi.vim.host.FeatureMask] = []
   vFlashCacheAllocation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   paused: _typing.Optional[bool] = None
   snapshotInBackground: _typing.Optional[bool] = None
   quiescedForkParent: _typing.Optional[bool] = None
   instantCloneFrozen: _typing.Optional[bool] = None
   cryptoState: _typing.Optional[str] = None
   suspendedToMemory: _typing.Optional[bool] = None
   opNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   iommuActive: _typing.Optional[bool] = None
   consolidateWorkTotal: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   consolidateWorkDone: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   diskChainBroken: _typing.Optional[bool] = None


class ScheduledHardwareUpgradeInfo(pyVmomi.vmodl.DynamicData):
   """
   Data object type containing settings for the scheduled hardware upgrades.
   
   Attributes:
       upgradePolicy: Scheduled hardware upgrade policy setting for the virtual machine.
       versionKey: Key for target hardware version to be used on next scheduled upgrade
           in the format of `pyVmomi.vim.vm.ConfigOptionDescriptor.key`.
       scheduledHardwareUpgradeStatus: Status for last attempt to run scheduled hardware upgrade.
       fault: Contains information about the failure of last attempt to run
           scheduled hardware upgrade.
   """
   class HardwareUpgradePolicy(pyVmomi.VmomiSupport.Enum):
      """
      The policy setting used to determine when to perform scheduled
      upgrades for a virtual machine.
      
      Attributes:
          never: No scheduled upgrades.
          onSoftPowerOff: Run scheduled upgrades only on normal guest OS shutdown.
          always: Always run scheduled upgrades.
      """
      never: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy'] = 'never'
      onSoftPowerOff: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy'] = 'onSoftPowerOff'
      always: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy'] = 'always'

   class HardwareUpgradeStatus(pyVmomi.VmomiSupport.Enum):
      """
      Status for last attempt to run scheduled hardware upgrade.
      
      Attributes:
          none: No scheduled upgrade ever happened.
          pending: Upgrade is scheduled, but was not run yet.
          success: Upgrade succeeded.
          failed: Upgrade failed.
              
              For more information about the failure
      """
      none: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus'] = 'none'
      pending: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus'] = 'pending'
      success: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus'] = 'success'
      failed: _typing.ClassVar['ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus'] = 'failed'

   upgradePolicy: _typing.Optional[str] = None
   versionKey: _typing.Optional[str] = None
   scheduledHardwareUpgradeStatus: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ScsiDiskDeviceInfo(DiskDeviceInfo):
   """
   The ScsiDiskDeviceInfo class contains detailed information about a specific
   scsi disk hardware device.
   
   These devices are for the
   vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.
   
   Attributes:
       disk: Detailed information about the disk.
       transportHint: Transport identifier hint used to identify the device.
           
           To definitively
           correlate this device with a host physical disk, use the disk property.
           This identifier is intended as a hint to end users to identify the
           disk device.
       lunNumber: LUN number hint used to identify the SCSI device.
           
           To definitively
           correlate this device with a host physical disk, use the disk property.
           This identifier is intended as a hint to end users to identify the
           disk device.
   """
   disk: _typing.Optional[pyVmomi.vim.host.ScsiDisk] = None
   transportHint: _typing.Optional[str] = None
   lunNumber: _typing.Optional[int] = None


class ScsiPassthroughInfo(TargetInfo):
   """
   Description of a generic SCSI device, including information about
   the device ID.
   
   Attributes:
       scsiClass: The class of the generic SCSI device.
       vendor: The vendor name.
       physicalUnitNumber: Unit number of the generic device on the physical host.
   """
   class ScsiClass(pyVmomi.VmomiSupport.Enum):
      """Possible SCSI classes."""
      disk: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'disk'
      tape: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'tape'
      printer: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'printer'
      processor: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'processor'
      worm: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'worm'
      cdrom: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'cdrom'
      scanner: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'scanner'
      optical: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'optical'
      media: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'media'
      com: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'com'
      raid: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'raid'
      unknown: _typing.ClassVar['ScsiPassthroughInfo.ScsiClass'] = 'unknown'

   scsiClass: str
   vendor: str
   physicalUnitNumber: int

class SerialInfo(TargetInfo):
   """
   SerialInfo class contains information about a physical serial
   drive on the host.
   """
   pass


class SgxInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the virtual software guard extension (vSGX)
   configuration of this virtual machine.
   
   Attributes:
       epcSize: Size of vEPC, in megabytes.
       flcMode: FLC mode for the virtual machine.
           
           The set of possible values are
           described in `pyVmomi.vim.vm.SgxInfo.FlcModes`. If no value is specified,
           then \"unlocked\" will be used.
       lePubKeyHash: Public key hash of the provider launch enclave.
           
           This is the SHA256
           digest of the SIGSTRUCT.MODULUS(MR_SIGNER) of the provider launch
           enclave. This hash must only be provided when the launch enclave mode is
           \"locked\", for the other cases the hash is ignored.
       requireAttestation: Indicates whether or not a virtual machine requires remote
           attestation.
           
           Since: vSphere API Release 8.0.0.1
   """
   class FlcModes(pyVmomi.VmomiSupport.Enum):
      """
      Flexible Launch Enclave (FLC) modes.
      
      Attributes:
          locked: FLC is available in the guest.
              
              The \"launch Enclave MSRs\" are locked and
              initialized with the provided public key hash.
          unlocked: FLC is available in the guest.
              
              The \"launch enclave MSRs\" are writeable
              and initialized with Intel's public key hash.
      """
      locked: _typing.ClassVar['SgxInfo.FlcModes'] = 'locked'
      unlocked: _typing.ClassVar['SgxInfo.FlcModes'] = 'unlocked'

   epcSize: pyVmomi.VmomiSupport.long
   flcMode: _typing.Optional[str] = None
   lePubKeyHash: _typing.Optional[str] = None
   requireAttestation: _typing.Optional[bool] = None


class SgxTargetInfo(TargetInfo):
   """
   Description of Intel Software Guard Extensions information.
   
   Attributes:
       maxEpcSize: Maximum size, in bytes, of EPC available on the compute resource.
       flcModes: FLC modes available in the compute resource.
           
           The set of possible values
           are described in `pyVmomi.vim.vm.SgxInfo.FlcModes`.
       lePubKeyHashes: Public key hashes of the provider launch enclaves available in the
           compute resource.
       requireAttestationSupported: Whether the host/cluster supports requiring SGX remote attestation.
           
           Since: vSphere API Release 8.0.0.1
   """
   maxEpcSize: pyVmomi.VmomiSupport.long
   flcModes: list[str] = []
   lePubKeyHashes: list[str] = []
   requireAttestationSupported: _typing.Optional[bool] = None


class Snapshot(pyVmomi.vim.ExtensibleManagedObject):
   """
   The Snapshot managed object type specifies the interface to individual snapshots
   of a virtual machine.
   
   Although these are managed objects, they are subordinate to
   their virtual machine.
   """
   @property
   def config(self) -> ConfigInfo:
      """
      Information about the configuration of this virtual machine when this snapshot was
      taken.
      
      The datastore paths for the virtual machine disks point to the head of the disk
      chain that represents the disk at this given snapshot. The fileInfo.fileLayout
      field is not set.
      """
      ...
   @property
   def childSnapshot(self) -> list[Snapshot]:
      """All snapshots for which this snapshot is the parent."""
      ...
   @property
   def vm(self) -> pyVmomi.vim.VirtualMachine:
      """The virtual machine for which the snapshot was taken."""
      ...

   def Revert(self, host: _typing.Optional[pyVmomi.vim.HostSystem], suppressPowerOn: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Change the execution state of the virtual machine to the state of this snapshot.
      
      Args:
          host: (optional) Choice of host for the virtual machine, in case this
              operation causes the virtual machine to power on.
              
              If a snapshot was taken while a virtual machine was powered on, and this operation
              is invoked after the virtual machine was powered off, the operation causes the
              virtual machine to power on to reach the snapshot state. This parameter can be
              used to specify a choice of host where the virtual machine should power on.
              
              If this parameter is not set and the vBalance feature is configured for automatic
              load balancing, a host is automatically selected. Otherwise, the virtual machine
              keeps its existing host affiliation.
          suppressPowerOn: (optional) If set to true, the virtual
              machine will not be powered on regardless of the power state when
              the snapshot was created. Default to false.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InsufficientResourcesFault: if this operation would violate a resource
              usage policy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed in the current state
              of the virtual machine. For example, the virtual machine's configuration
              is not available.
          pyVmomi.vim.fault.FileFault: if there is a problem accessing the virtual machine on the
              filesystem.
          pyVmomi.vim.fault.VmConfigFault: if a configuration issue prevents the power-on. Typically, a
              more specific fault, such as UnsupportedVmxLocation, is thrown.
      """
      ...
   def Remove(self, removeChildren: bool, consolidate: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Removes this snapshot and deletes any associated storage.
      
      Args:
          removeChildren: Flag to specify removal of the entire snapshot subtree.
          consolidate: (optional) If set to true, the virtual disk associated
              with this snapshot will be merged with other disk if possible. Defaults to true.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
      """
      ...
   def Rename(self, name: _typing.Optional[str], description: _typing.Optional[str]) -> None:
      """
      Rename this snapshot with either a new name or a new description or both.
      
      At least one of these must be specified when calling the rename method.
      
      Args:
          name: New name for the snapshot.
          description: New description for the snapshot.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if the specified snapshot name is not valid.
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed in the current state
              of the virtual machine. For example, the virtual machine's configuration
              is not available.
      """
      ...
   def ExportSnapshot(self) -> pyVmomi.vim.HttpNfcLease:
      """
      Obtains an export lease on this snapshot.
      
      The export lease contains
      a list of URLs for the virtual disks for this snapshot, as well as
      a ticket giving access to the URLs.
      
      See `pyVmomi.vim.HttpNfcLease` for information on how to use the lease.
      
      Returns:
          The export lease on this `pyVmomi.vim.vm.Snapshot`. The
          export task continues running until the lease is completed by the
          caller.
      
      Raises:
          pyVmomi.vim.fault.TaskInProgress: if the virtual machine is busy.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed because of the
              virtual machine's current state. For example, if the virtual machine
              configuration information is not available.
          pyVmomi.vim.fault.FileFault: if there is an error accessing the virtual machine files.
      """
      ...


class SnapshotInfo(pyVmomi.vmodl.DynamicData):
   """
   The SnapshotInfo data object type provides all the information about the
   hierarchy of snapshots in a virtual machine.
   
   Attributes:
       currentSnapshot: Current snapshot of the virtual machine
           
           This property is set by calling
           `pyVmomi.vim.vm.Snapshot.revert` or
           `pyVmomi.vim.VirtualMachine.createSnapshot`.
           This property will be empty when the working snapshot is at the root
           of the snapshot tree.
       rootSnapshotList: Data for the entire set of snapshots for one virtual machine.
   """
   currentSnapshot: _typing.Optional[Snapshot] = None
   rootSnapshotList: list[SnapshotTree] = []


class SnapshotSelectionSpec(pyVmomi.vmodl.DynamicData):
   """
   This data type defines the filtering specification for removing snapshots
   from virtual machine.
   
   Attributes:
       retentionDays: This is the property to select snapshots older than X days.
   
   Since: vSphere API Release 8.0.3.0
   """
   retentionDays: _typing.Optional[int] = None


class SnapshotTree(pyVmomi.vmodl.DynamicData):
   """
   SnapshotTree encapsulates all the read-only data produced by the snapshot.
   
   Attributes:
       snapshot: The managed object for this snapshot.
       vm: The virtual machine for which the snapshot was taken.
       name: Name of the snapshot.
       description: Description of the snapshot.
       id: The unique identifier that distinguishes this snapshot from
           other snapshots of the virtual machine.
       createTime: The date and time the snapshot was taken.
       state: The power state of the virtual machine when this snapshot was taken.
       quiesced: Flag to indicate whether or not the snapshot was created with
           the \"quiesce\" option, ensuring a consistent state of the file system.
       backupManifest: The relative path from the snapshotDirectory pointing to the backup
           manifest.
           
           Available for certain quiesced snapshots only.
       childSnapshotList: The snapshot data for all snapshots for which this snapshot is the parent.
       replaySupported: Flag to indicate whether this snapshot is associated with a recording
           session on the virtual machine that can be replayed.
   """
   snapshot: Snapshot
   vm: pyVmomi.vim.VirtualMachine
   name: str
   description: str
   id: int
   createTime: _datetime.datetime
   state: pyVmomi.vim.VirtualMachine.PowerState
   quiesced: bool
   backupManifest: _typing.Optional[str] = None
   childSnapshotList: list[SnapshotTree] = []
   replaySupported: _typing.Optional[bool] = None

class SoundInfo(TargetInfo):
   """
   SoundInfo class contains information about a physical sound
   card on the host.
   """
   pass


class SriovDevicePoolInfo(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       key: To be used for extending to other device types
   """
   key: str


class SriovInfo(PciPassthroughInfo):
   """
   Description of a SRIOV device that can be attached to a virtual machine.
   
   Attributes:
       virtualFunction: Indicates whether corresponding PCI device is a virtual function
           instantiated by a SR-IOV capable device.
       pnic: The name of the physical nic that is represented by a SR-IOV
           capable physical function.
       devicePool: SRIOV DevicePool information
   """
   virtualFunction: bool
   pnic: _typing.Optional[str] = None
   devicePool: _typing.Optional[SriovDevicePoolInfo] = None


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   """
   This class is networking specific SR-IOV device pool info
   
   Attributes:
       switchKey: vSwitch key
       switchUuid: DVSwitch Uuid
   """
   switchKey: _typing.Optional[str] = None
   switchUuid: _typing.Optional[str] = None


class StorageInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about the amount of storage used by a virtual machine across
   datastores that it is located on.
   
   Attributes:
       perDatastoreUsage: Storage space used by this virtual machine on all datastores that it
           is located on.
           
           Total storage space committed to this virtual machine across all datastores is
           simply an aggregate of the property
           `pyVmomi.vim.vm.StorageInfo.UsageOnDatastore.committed`.
       timestamp: Time when values in this structure were last updated.
   """
   class UsageOnDatastore(pyVmomi.vmodl.DynamicData):
      """
      Storage space used by this virtual machine on a particular datastore.
      
      Attributes:
          datastore: Reference to datastore for which information is being provided.
          committed: Storage space, in bytes, on this datastore that is actually being used by
              the virtual machine.
              
              It includes space actually occupied by disks, logs, snapshots,
              configuration files etc. Files of the virtual machine which are present
              on a different datastore (e.g. a virtual disk on another datastore) are not
              included here. `pyVmomi.vim.vm.FileLayoutEx` provides a detailed
              break-up of the committed space.
          uncommitted: Additional storage space, in bytes, potentially used by the virtual machine
              on this datastore.
              
              Additional space may be needed for example when lazily allocated disks grow,
              or storage for swap is allocated when powering on the virtual machine.
              
              If the virtual machine is running off delta disks (for example because
              a snapshot was taken), then only the potential growth of the currently
              used delta-disks is considered.
          unshared: Storage space, in bytes, occupied by the virtual machine on this datastore
              that is not shared with any other virtual machine.
      """
      datastore: pyVmomi.vim.Datastore
      committed: pyVmomi.VmomiSupport.long
      uncommitted: pyVmomi.VmomiSupport.long
      unshared: pyVmomi.VmomiSupport.long

   perDatastoreUsage: list[StorageInfo.UsageOnDatastore] = []
   timestamp: _datetime.datetime


class SubnetInfo(TargetInfo):
   """
   Attributes:
       id: The ID of the subnet
       subnetFolderInfo: The subnet folder info
       vpcFolderInfo: The VPC folder info
       projectFolderInfo: The project folder info
       rootFolderInfo: The root folder info.
           
           root folder can be either \"Virtual Private Clouds\" or \"NSX Managed Folders\"
   
   Since: vSphere API Release 9.0.0.0
   """
   class FolderInfo(pyVmomi.vmodl.DynamicData):
      """Since: vSphere API Release 9.0.0.0"""
      name: str
      folder: pyVmomi.vim.Folder

   id: str
   subnetFolderInfo: SubnetInfo.FolderInfo
   vpcFolderInfo: SubnetInfo.FolderInfo
   projectFolderInfo: _typing.Optional[SubnetInfo.FolderInfo] = None
   rootFolderInfo: SubnetInfo.FolderInfo


class Summary(pyVmomi.vmodl.DynamicData):
   """
   The summary data object type encapsulates a typical set of virtual machine
   information that is useful for list views and summary pages.
   
   VirtualCenter can retrieve this information very efficiently,
   even for large sets of virtual machines.
   
   Attributes:
       vm: Reference to the virtual machine managed object.
       runtime: Runtime and state information of a running virtual machine.
           
           Most of this information is also available when a virtual machine is powered off.
           In that case, it contains information from the last run, if available.
       guest: Guest operating system and VMware Tools information.
           
           See `pyVmomi.vim.VirtualMachine.guest` for more information.
       config: Basic configuration information about the virtual machine.
           
           This information
           is not available when the virtual machine is unavailable, for instance, when
           it is being created or deleted.
       storage: Storage information of the virtual machine.
           
           It can be explicitly refreshed
           with the `pyVmomi.vim.VirtualMachine.refreshStorageInfo` operation.
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       quickStats: A set of statistics that are typically updated with near real-time regularity.
           
           This data object type does not support notification, for scalability reasons.
           Therefore, changes in QuickStats do not generate property collector updates. To
           monitor statistics values, use the statistics and alarms modules instead.
       overallStatus: Overall alarm status on this node.
           
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       customValue: Custom field values.
   """
   class ConfigSummary(pyVmomi.vmodl.DynamicData):
      """
      A subset of virtual machine configuration.
      
      Attributes:
          name: Name of the virtual machine.
          template: Flag to determine whether or not this virtual machine is a template.
          vmPathName: Path name to the configuration file for the virtual machine
          memorySizeMB: Memory size of the virtual machine, in megabytes.
          cpuReservation: Configured CPU reservation in MHz
          memoryReservation: Configured Memory reservation in MB
          numCpu: Number of processors in the virtual machine.
          numEthernetCards: Number of virtual network adapters.
          numVirtualDisks: Number of virtual disks attached to the virtual machine.
          uuid: Virtual machine BIOS identification.
          instanceUuid: VC-specific identifier of the virtual machine
          guestId: Guest operating system identifier (short name).
          guestFullName: Guest operating system name configured on the virtual machine.
          annotation: Description for the virtual machine.
          product: Product information.
              
              References to properties in the URLs are expanded.
          installBootRequired: Whether the VM requires a reboot to finish installation.
              
              False if no vApp
              meta-data is configured.
          ftInfo: Fault Tolerance settings for this virtual machine.
              
              This property will be populated only for fault tolerance virtual
              machines and will be left unset for all other virtual machines.
              See `pyVmomi.vim.vm.FaultToleranceConfigInfo` for a description.
          managedBy: Specifies that this VM is managed by a VC Extension.
              
              See the
              `pyVmomi.vim.vm.ConfigSpec.managedBy` property in the ConfigSpec
              for more details.
          tpmPresent: Is TPM present in a VM?
          numVmiopBackings: Number of VMIOP backed devices attached to the virtual machine.
          hwVersion: The hardware version string for this virtual machine.
      """
      name: str
      template: bool
      vmPathName: str
      memorySizeMB: _typing.Optional[int] = None
      cpuReservation: _typing.Optional[int] = None
      memoryReservation: _typing.Optional[int] = None
      numCpu: _typing.Optional[int] = None
      numEthernetCards: _typing.Optional[int] = None
      numVirtualDisks: _typing.Optional[int] = None
      uuid: _typing.Optional[str] = None
      instanceUuid: _typing.Optional[str] = None
      guestId: _typing.Optional[str] = None
      guestFullName: _typing.Optional[str] = None
      annotation: _typing.Optional[str] = None
      product: _typing.Optional[pyVmomi.vim.vApp.ProductInfo] = None
      installBootRequired: _typing.Optional[bool] = None
      ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
      managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
      tpmPresent: _typing.Optional[bool] = None
      numVmiopBackings: _typing.Optional[int] = None
      hwVersion: _typing.Optional[str] = None

   class QuickStats(pyVmomi.vmodl.DynamicData):
      """
      A set of statistics that are typically updated with near real-time regularity.
      
      This data object type does not support notification, for scalability reasons.
      Therefore, changes in QuickStats do not generate property collector updates. To
      monitor statistics values, use the statistics and alarms modules instead.
      
      Attributes:
          overallCpuUsage: Basic CPU performance statistics, in MHz.
              
              Valid while the virtual machine is running.
          overallCpuDemand: Basic CPU performance statistics, in MHz.
              
              Valid while the virtual machine is running.
          overallCpuReadiness: Percentage of time that the virtual machine was ready, but could not
              get scheduled to run on the physical CPU.
              
              Valid while the virtual machine is running.
          guestMemoryUsage: Guest memory utilization statistics, in MB.
              
              This
              is also known as active guest memory. The number
              can be between 0 and the configured memory size of
              the virtual machine. Valid while the virtual machine is
              running.
          hostMemoryUsage: Host memory utilization statistics, in MB.
              
              This
              is also known as consumed host memory. This is between 0 and
              the configured resource limit. Valid while the virtual machine is
              running. This includes the overhead memory of the VM.
          guestHeartbeatStatus: Guest operating system heartbeat metric.
              
              See `pyVmomi.vim.VirtualMachine.guestHeartbeatStatus` for a description.
          distributedCpuEntitlement: This is the amount of CPU resource, in MHz, that this VM is entitled to, as
              calculated by DRS.
              
              Valid only for a VM managed by DRS.
          distributedMemoryEntitlement: This is the amount of memory, in MB, that this VM is entitled to, as
              calculated by DRS.
              
              Valid only for a VM managed by DRS.
          staticCpuEntitlement: The static CPU resource entitlement for a virtual machine.
              
              This value is
              calculated based on this virtual machine's resource reservations, shares
              and limit, and doesn't take into account current usage. This is the worst
              case CPU allocation for this virtual machine, that is, the amount of CPU
              resource this virtual machine would receive if all virtual machines running
              in the cluster went to maximum consumption. Units are MHz.
          staticMemoryEntitlement: The static memory resource entitlement for a virtual machine.
              
              This value is
              calculated based on this virtual machine's resource reservations, shares
              and limit, and doesn't take into account current usage. This is the worst
              case memory allocation for this virtual machine, that is, the amount of
              memory this virtual machine would receive if all virtual machines running
              in the cluster went to maximum consumption. Units are MB.
          grantedMemory: Amount of host physical memory that is mapped for a virtual machine,
              in MB.
              
              The number can be between 0 and the configured memory size of
              the virtual machine. Valid while the virtual machine is running.
          privateMemory: The portion of memory, in MB, that is granted to this VM from non-shared
              host memory.
          sharedMemory: The portion of memory, in MB, that is granted to this VM from host memory
              that is shared between VMs.
          swappedMemory: The portion of memory, in MB, that is granted to this VM from the host's swap
              space.
              
              This is a sign that there is memory pressure on the host.
          balloonedMemory: The size of the balloon driver in the VM, in MB.
              
              The host will inflate the
              balloon driver to reclaim physical memory from the VM. This is a sign that
              there is memory pressure on the host.
          consumedOverheadMemory: The amount of consumed overhead memory, in MB, for this VM.
          ftLogBandwidth: The network bandwidth used for logging between the
              primary and secondary fault tolerance VMs.
              
              The unit is kilobytes per second.
          ftSecondaryLatency: The amount of time in wallclock that the VCPU of the secondary fault
              tolerance VM is behind the VCPU of the primary VM.
              
              The unit is millisecond.
          ftLatencyStatus: The latency status of the fault tolerance VM.
              
              ftLatencyStatus is determined by the value of ftSecondaryLatency.
              ftLatencyStatus is:
              green, if ftSecondaryLatency is less than or equal to 2 seconds;
              yellow, if ftSecondaryLatency is greater than 2 seconds,
              and less than or equal to 6 seconds;
              red, if ftSecondaryLatency is greater than 6 seconds;
              gray, if ftSecondaryLatency is unknown.
          compressedMemory: The amount of compressed memory currently consumed by VM, in Kb.
          uptimeSeconds: The system uptime of the VM in seconds.
          ssdSwappedMemory: The amount of memory swapped to fast disk device such as
              SSD, in KB.
          activeMemory: The amount of memory that was recently touched by the VM, in MB.
              
              Since: vSphere API Release 7.0.3.0
          memoryTierStats: Stats for each physical memory tier.
              
              A physical memory tier consists of one or
              more logical memory tiers of the same `pyVmomi.vim.host.MemoryTierType`. For
              example, the logical tiers can be tier0 (DRAM), tier1 (DRAM), and tier2 (PMEM),
              while the physical tiers are just DRAM and PMEM.
              
              Since: vSphere API Release 7.0.3.0
      """
      class MemoryTierStats(pyVmomi.vmodl.DynamicData):
         """
         Attributes:
             memoryTierType: The memory tier type.
                 
                 See `pyVmomi.vim.host.MemoryTierType` for supported
                 values.
             readBandwidth: Memory access bandwidth usage for the reads of the VM on this tier in
                 MBps.
         
         Since: vSphere API Release 7.0.3.0
         """
         memoryTierType: str
         readBandwidth: pyVmomi.VmomiSupport.long

      overallCpuUsage: _typing.Optional[int] = None
      overallCpuDemand: _typing.Optional[int] = None
      overallCpuReadiness: _typing.Optional[int] = None
      guestMemoryUsage: _typing.Optional[int] = None
      hostMemoryUsage: _typing.Optional[int] = None
      guestHeartbeatStatus: pyVmomi.vim.ManagedEntity.Status
      distributedCpuEntitlement: _typing.Optional[int] = None
      distributedMemoryEntitlement: _typing.Optional[int] = None
      staticCpuEntitlement: _typing.Optional[int] = None
      staticMemoryEntitlement: _typing.Optional[int] = None
      grantedMemory: _typing.Optional[int] = None
      privateMemory: _typing.Optional[int] = None
      sharedMemory: _typing.Optional[int] = None
      swappedMemory: _typing.Optional[int] = None
      balloonedMemory: _typing.Optional[int] = None
      consumedOverheadMemory: _typing.Optional[int] = None
      ftLogBandwidth: _typing.Optional[int] = None
      ftSecondaryLatency: _typing.Optional[int] = None
      ftLatencyStatus: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None
      compressedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      uptimeSeconds: _typing.Optional[int] = None
      ssdSwappedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      activeMemory: _typing.Optional[int] = None
      memoryTierStats: list[Summary.QuickStats.MemoryTierStats] = []

   class GuestSummary(pyVmomi.vmodl.DynamicData):
      """
      A subset of virtual machine guest information.
      
      Attributes:
          guestId: Guest operating system identifier (short name), if known.
          guestFullName: Guest operating system name configured on the virtual machine.
          toolsStatus: Current status of VMware Tools in the guest operating system, if known.
          toolsVersionStatus: Current version status of VMware Tools in the guest operating system,
              if known.
          toolsVersionStatus2: Current version status of VMware Tools in the guest operating system,
              if known.
          toolsRunningStatus: Current running status of VMware Tools in the guest operating system,
              if known.
          hostName: Hostname of the guest operating system, if known.
          ipAddress: Primary IP address assigned to the guest operating system, if known.
          hwVersion: The hardware version string for this virtual machine.
      """
      guestId: _typing.Optional[str] = None
      guestFullName: _typing.Optional[str] = None
      toolsStatus: _typing.Optional[GuestInfo.ToolsStatus] = None
      toolsVersionStatus: _typing.Optional[str] = None
      toolsVersionStatus2: _typing.Optional[str] = None
      toolsRunningStatus: _typing.Optional[str] = None
      hostName: _typing.Optional[str] = None
      ipAddress: _typing.Optional[str] = None
      hwVersion: _typing.Optional[str] = None

   class StorageSummary(pyVmomi.vmodl.DynamicData):
      """
      A subset of the storage information of this virtual machine.
      
      See `pyVmomi.vim.vm.StorageInfo` for a detailed storage break-up.
      
      Attributes:
          committed: Total storage space, in bytes, committed to this virtual machine across
              all datastores.
              
              Essentially an aggregate of the property
              `pyVmomi.vim.vm.StorageInfo.UsageOnDatastore.committed` across all
              datastores that this virtual machine is located on.
          uncommitted: Additional storage space, in bytes, potentially used by this virtual machine
              on all datastores.
              
              Essentially an aggregate of the property
              `pyVmomi.vim.vm.StorageInfo.UsageOnDatastore.uncommitted` across all
              datastores that this virtual machine is located on.
          unshared: Total storage space, in bytes, occupied by the virtual machine across
              all datastores, that is not shared with any other virtual machine.
          timestamp: Time when values in this structure were last updated.
      """
      committed: pyVmomi.VmomiSupport.long
      uncommitted: pyVmomi.VmomiSupport.long
      unshared: pyVmomi.VmomiSupport.long
      timestamp: _datetime.datetime

   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   runtime: RuntimeInfo
   guest: _typing.Optional[Summary.GuestSummary] = None
   config: Summary.ConfigSummary
   storage: _typing.Optional[Summary.StorageSummary] = None
   quickStats: Summary.QuickStats
   overallStatus: pyVmomi.vim.ManagedEntity.Status
   customValue: list[pyVmomi.vim.CustomFieldsManager.Value] = []


class ToolsConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   ToolsConfigInfo is a data object type containing settings for the VMware Tools
   software running in the guest operating system.
   
   Attributes:
       toolsVersion: Version of VMware Tools installed on the guest operating system.
       toolsInstallType: Installation type of VMware Tools in the guest operating system.
           
           The set of possible values is described in
           `pyVmomi.vim.vm.GuestInfo.ToolsInstallType`
       afterPowerOn: Flag to specify whether or not scripts should run
           after the virtual machine powers on.
       afterResume: Flag to specify whether or not scripts should run
           after the virtual machine resumes.
       beforeGuestStandby: Flag to specify whether or not scripts should run
           before the virtual machine suspends.
       beforeGuestShutdown: Flag to specify whether or not scripts should run
           before the virtual machine powers off.
       beforeGuestReboot: Flag to specify whether or not scripts should run
           before the virtual machine reboots.
       toolsUpgradePolicy: Tools upgrade policy setting for the virtual machine.
       pendingCustomization: When set, this indicates that a customization operation is pending on the VM.
           
           The value represents the filename of the customization package on the host.
       customizationKeyId: When set, provides the id of the key used to encrypt the customization
           package attached to the VM.
       syncTimeWithHostAllowed: Indicates whether or not the tools program is allowed to synchronize
           guest time with host time.
           
           When set to `false`, disallows
           tool periodic time synchronization as well as guest time step corrections
           due to one-off events like resume from suspend.
           
           Since: vSphere API Release 7.0.1.0
       syncTimeWithHost: Flag to specify whether or not the tools program will periodically
           synchronize guest time with host time.
           
           Periodical synchronization is
           only allowed if `pyVmomi.vim.vm.ToolsConfigInfo.syncTimeWithHostAllowed`
           is not set to `false`.
       lastInstallInfo: Information about the last tools upgrade attempt if applicable.
           
           This information is maintained by the server and is ignored if set by the client.
   """
   class UpgradePolicy(pyVmomi.VmomiSupport.Enum):
      """
      The policy setting used to determine when tools are auto-upgraded for
      a virtual machine
      
      Attributes:
          manual: No auto-upgrades for tools will be performed for this
              virtual machine.
              
              Users must manually invoke the UpgradeTools
              operation to update the tools.
          upgradeAtPowerCycle: When the virtual machine is power-cycled, the system checks
              for a newer version of tools when the VM comes back up.
              
              If it
              is available, a tools upgrade is automatically performed on the
              virtual machine and it is rebooted if necessary.
      """
      manual: _typing.ClassVar['ToolsConfigInfo.UpgradePolicy'] = 'manual'
      upgradeAtPowerCycle: _typing.ClassVar['ToolsConfigInfo.UpgradePolicy'] = 'upgradeAtPowerCycle'

   class ToolsLastInstallInfo(pyVmomi.vmodl.DynamicData):
      """
      Describes status of last tools upgrade attempt
      
      Attributes:
          counter: Number of attempts that have been made to upgrade the version of tools
              installed on this virtual machine.
          fault: Error that happened, if any, during last attempt to upgrade tools.
      """
      counter: int
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   toolsVersion: _typing.Optional[int] = None
   toolsInstallType: _typing.Optional[str] = None
   afterPowerOn: _typing.Optional[bool] = None
   afterResume: _typing.Optional[bool] = None
   beforeGuestStandby: _typing.Optional[bool] = None
   beforeGuestShutdown: _typing.Optional[bool] = None
   beforeGuestReboot: _typing.Optional[bool] = None
   toolsUpgradePolicy: _typing.Optional[str] = None
   pendingCustomization: _typing.Optional[str] = None
   customizationKeyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
   syncTimeWithHostAllowed: _typing.Optional[bool] = None
   syncTimeWithHost: _typing.Optional[bool] = None
   lastInstallInfo: _typing.Optional[ToolsConfigInfo.ToolsLastInstallInfo] = None


class UsbInfo(TargetInfo):
   """
   This data object contains information about a physical USB device
   on the host.
   
   Attributes:
       description: A user visible name of the USB device.
       vendor: The vendor ID of the USB device.
       product: The product ID of the USB device.
       physicalPath: An autoconnect pattern which describes the device's physical
           path.
           
           This is the path to the specific port on the host where the
           USB device is attached.
       family: The device class families.
           
           For possible values see
           `pyVmomi.vim.vm.UsbInfo.Family`
       speed: The possible device speeds detected by server.
           
           For possible values see
           `pyVmomi.vim.vm.UsbInfo.Speed`
       summary: Summary information about the virtual machine that is currently
           using this device, if any.
   """
   class Speed(pyVmomi.VmomiSupport.Enum):
      """
      Device speed.
      
      Attributes:
          low: This device operates at low speed (1.5Mb/s).
          full: This device operates at full speed (12Mb/s).
          high: This device can operate at high speed (480Mb/s)
          superSpeed: This device can operate at super speed (4.8Gb/s)
          superSpeedPlus: This device can operate at super speed plus (10Gb/s)
          superSpeed20Gbps: This device can operate at super speed gen 2x2 (20Gb/s)
              
              Since: vSphere API Release 7.0.3.2
          unknownSpeed: This device's speed is unknown.
      """
      low: _typing.ClassVar['UsbInfo.Speed'] = 'low'
      full: _typing.ClassVar['UsbInfo.Speed'] = 'full'
      high: _typing.ClassVar['UsbInfo.Speed'] = 'high'
      superSpeed: _typing.ClassVar['UsbInfo.Speed'] = 'superSpeed'
      superSpeedPlus: _typing.ClassVar['UsbInfo.Speed'] = 'superSpeedPlus'
      superSpeed20Gbps: _typing.ClassVar['UsbInfo.Speed'] = 'superSpeed20Gbps'
      unknownSpeed: _typing.ClassVar['UsbInfo.Speed'] = 'unknownSpeed'

   class Family(pyVmomi.VmomiSupport.Enum):
      """
      Device class family.
      
      Attributes:
          audio: Audio capable device.
          hid: Human interface device.
          hid_bootable: Bootable human interface device, this is a subset of HID devices.
          physical: Physical interface device.
          communication: Communication device.
          imaging: Still imaging device.
          printer: Printer device.
          storage: Mass storage device.
          hub: USB hubs.
          smart_card: Smart card device.
          security: Content security device.
          video: Video device.
          wireless: Wireless controller.
          bluetooth: Standard bluetooth adapter that uses HCI protocol,
              this is a subset of wireless controllers.
          wusb: Wireless device related to the Wireless USB standard,
              this is a subset of wireless controllers,
          pda: Palm PDA, and Microsoft ActiveSync PDA.
          vendor_specific: Device that has an interface using a vendor-specific protocol.
          other: Other miscellaneous device.
          unknownFamily: There was an error in determining this device's classes
              accurately.
      """
      audio: _typing.ClassVar['UsbInfo.Family'] = 'audio'
      hid: _typing.ClassVar['UsbInfo.Family'] = 'hid'
      hid_bootable: _typing.ClassVar['UsbInfo.Family'] = 'hid_bootable'
      physical: _typing.ClassVar['UsbInfo.Family'] = 'physical'
      communication: _typing.ClassVar['UsbInfo.Family'] = 'communication'
      imaging: _typing.ClassVar['UsbInfo.Family'] = 'imaging'
      printer: _typing.ClassVar['UsbInfo.Family'] = 'printer'
      storage: _typing.ClassVar['UsbInfo.Family'] = 'storage'
      hub: _typing.ClassVar['UsbInfo.Family'] = 'hub'
      smart_card: _typing.ClassVar['UsbInfo.Family'] = 'smart_card'
      security: _typing.ClassVar['UsbInfo.Family'] = 'security'
      video: _typing.ClassVar['UsbInfo.Family'] = 'video'
      wireless: _typing.ClassVar['UsbInfo.Family'] = 'wireless'
      bluetooth: _typing.ClassVar['UsbInfo.Family'] = 'bluetooth'
      wusb: _typing.ClassVar['UsbInfo.Family'] = 'wusb'
      pda: _typing.ClassVar['UsbInfo.Family'] = 'pda'
      vendor_specific: _typing.ClassVar['UsbInfo.Family'] = 'vendor_specific'
      other: _typing.ClassVar['UsbInfo.Family'] = 'other'
      unknownFamily: _typing.ClassVar['UsbInfo.Family'] = 'unknownFamily'

   description: str
   vendor: int
   product: int
   physicalPath: str
   family: list[str] = []
   speed: list[str] = []
   summary: _typing.Optional[Summary] = None


class UsbScanCodeSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object contains information about which USB HID codes
   to send to the Virtual Machine's keyboard.
   """
   class ModifierType(pyVmomi.vmodl.DynamicData):
      """
      The types of key modifiers to apply to each code.
      
      Attributes:
          leftControl: Left control key
          leftShift: Left shift key
          leftAlt: Left alt key
          leftGui: Left gui key
          rightControl: Right control key
          rightShift: Right shift key
          rightAlt: Right alt key
          rightGui: Right gui key
      """
      leftControl: _typing.Optional[bool] = None
      leftShift: _typing.Optional[bool] = None
      leftAlt: _typing.Optional[bool] = None
      leftGui: _typing.Optional[bool] = None
      rightControl: _typing.Optional[bool] = None
      rightShift: _typing.Optional[bool] = None
      rightAlt: _typing.Optional[bool] = None
      rightGui: _typing.Optional[bool] = None

   class KeyEvent(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          usbHidCode: USB HID code of the event
          modifiers: Modifiers to apply to the USB HID code
      """
      usbHidCode: int
      modifiers: _typing.Optional[UsbScanCodeSpec.ModifierType] = None

   keyEvents: list[UsbScanCodeSpec.KeyEvent] = []


class VFlashModuleInfo(TargetInfo):
   """
   VFlashModuleInfo class contains information about a vFlash module
   on the host.
   
   Attributes:
       vFlashModule: Information about the vFlash module
   """
   vFlashModule: pyVmomi.vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption


class VMotionStunTimeInfo(TargetInfo):
   """
   Description of VMotion Stun Time.
   
   Attributes:
       migrationBW: Migration bandwidth in Mbps
       stunTime: Stun Time in seconds
   
   Since: vSphere API Release 8.0.2.0
   """
   migrationBW: pyVmomi.VmomiSupport.long
   stunTime: pyVmomi.VmomiSupport.long


class VcpuConfig(pyVmomi.vmodl.DynamicData):
   """
   Vcpu configuration.
   
   Attributes:
       latencySensitivity: Latency sensitivity specification for this vcpu.
           
           The latency sensitivity can be configured per-vcpu only when the VM
           `pyVmomi.vim.vm.ConfigSpec.latencySensitivity` is
           configured to `high`
           in the same ConfigSpec.
           Setting `pyVmomi.vim.vm.ConfigSpec.latencySensitivity`,
           but not setting the vcpu's LatencySensitivity would apply the VM's
           latency sensitivity level to all the vcpus of the VM.
           The latency sensitivity of the vcpu should not exceed the
           latency sensitivity level of the VM.
           The only allowed levels for vcpu Latency sensitivity
           are `high` or
           `normal`
   """
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None


class VendorDeviceGroupInfo(TargetInfo):
   """
   Description of a PCI vendor device group device.
   
   Attributes:
       deviceGroupName: Name of Vendor Device Group.
       deviceGroupDescription: Description of Vendor Device Group.
       componentDeviceInfo: Array describing component devices of this Vendor Device Group.
           
           There is one entry per componentDevice in the deviceGroupSpec.
   
   Since: vSphere API Release 8.0.0.1
   """
   class ComponentDeviceInfo(pyVmomi.vmodl.DynamicData):
      """
      Class describing a component device within this vendor device group.
      
      Attributes:
          type: Type of this component.
              
              See `pyVmomi.vim.vm.VendorDeviceGroupInfo.ComponentDeviceInfo.ComponentType` for supported types.
          vendorName: Name of component device vendor.
          deviceName: Name of component device.
          isConfigurable: True if this device may be configured by user or UI.
          device: VirtualDevice template for this device.
      
      Since: vSphere API Release 8.0.0.1
      """
      class ComponentType(pyVmomi.VmomiSupport.Enum):
         """
         Type of component device.
         
         Since: vSphere API Release 8.0.0.1
         """
         pciPassthru: _typing.ClassVar['VendorDeviceGroupInfo.ComponentDeviceInfo.ComponentType'] = 'pciPassthru'
         nvidiaVgpu: _typing.ClassVar['VendorDeviceGroupInfo.ComponentDeviceInfo.ComponentType'] = 'nvidiaVgpu'
         sriovNic: _typing.ClassVar['VendorDeviceGroupInfo.ComponentDeviceInfo.ComponentType'] = 'sriovNic'
         dvx: _typing.ClassVar['VendorDeviceGroupInfo.ComponentDeviceInfo.ComponentType'] = 'dvx'

      type: str
      vendorName: str
      deviceName: str
      isConfigurable: bool
      device: pyVmomi.vim.vm.device.VirtualDevice

   deviceGroupName: str
   deviceGroupDescription: _typing.Optional[str] = None
   componentDeviceInfo: list[VendorDeviceGroupInfo.ComponentDeviceInfo] = []


class VgpuDeviceInfo(TargetInfo):
   """
   Description of PCI vGPU device and its capabilities.
   
   Attributes:
       deviceName: The vGPU device name.
       deviceVendorId: A well-known unique identifier for the device.
           
           It concatenates the
           16-bit PCI vendor id in lower bits followed by 16-bit PCI device id.
       maxFbSizeInGib: The maximum framebuffer size in gibibytes.
       timeSlicedCapable: Indicate whether device is time-sliced capable.
       migCapable: Indicate whether device is Multiple Instance GPU capable.
       computeProfileCapable: Indicate whether device is compute profile capable.
       quadroProfileCapable: Indicate whether device is quadro profile capable.
   
   Since: vSphere API Release 7.0.3.0
   """
   deviceName: str
   deviceVendorId: pyVmomi.VmomiSupport.long
   maxFbSizeInGib: pyVmomi.VmomiSupport.long
   timeSlicedCapable: bool
   migCapable: bool
   computeProfileCapable: bool
   quadroProfileCapable: bool


class VgpuProfileInfo(TargetInfo):
   """
   Description of PCI vGPU profile and its attributes.
   
   Attributes:
       profileName: The vGPU profile name.
       deviceVendorId: A well-known unique identifier for the device that supports this
           profile.
           
           It concatenates the 16-bit PCI vendor id in lower bits
           followed by 16-bit PCI device id.
       fbSizeInGib: The profile framebuffer size in gibibytes.
       profileSharing: Indicate how this profile is shared within device.
       profileClass: Indicate class for this profile.
       stunTimeEstimates: VMotion stun time information for this profile.
           
           Since: vSphere API Release 8.0.2.0
   
   Since: vSphere API Release 7.0.3.0
   """
   class ProfileSharing(pyVmomi.VmomiSupport.Enum):
      """
      Possible values for profile sharing.
      
      Attributes:
          timeSliced: Time-sliced
          mig: Multi-instance GPU partitioning
      
      Since: vSphere API Release 7.0.3.0
      """
      timeSliced: _typing.ClassVar['VgpuProfileInfo.ProfileSharing'] = 'timeSliced'
      mig: _typing.ClassVar['VgpuProfileInfo.ProfileSharing'] = 'mig'

   class ProfileClass(pyVmomi.VmomiSupport.Enum):
      """
      Possible values for profile class.
      
      Since: vSphere API Release 7.0.3.0
      """
      compute: _typing.ClassVar['VgpuProfileInfo.ProfileClass'] = 'compute'
      quadro: _typing.ClassVar['VgpuProfileInfo.ProfileClass'] = 'quadro'

   profileName: str
   deviceVendorId: pyVmomi.VmomiSupport.long
   fbSizeInGib: pyVmomi.VmomiSupport.long
   profileSharing: str
   profileClass: str
   stunTimeEstimates: list[VMotionStunTimeInfo] = []


class VirtualDeviceGroups(pyVmomi.vmodl.DynamicData):
   """
   The VirtualDeviceGroups data object
   type contains information about the backing that maps the
   virtual device onto a physical device for a Vendor Device Group device.
   
   Vendor Device Groups allow third-parties to define collections of
   devices that must be allocated to a virtual machine as a unit.
   Typically, this is because the set of devices are related in
   a some way, e.g. a physical link connects the devices.
   
   Attributes:
       deviceGroup: Information about device groups used by this VM.
           
           When adding a group, all devices that form the group
           must be added in the same request.
           When removing group, also all devices participating
           in the group must be removed.
           Modifying existing device group membership is not allowed.
   
   Since: vSphere API Release 8.0.0.1
   """
   class DeviceGroup(pyVmomi.vmodl.DynamicData):
      """
      Base device group type.
      
      Attributes:
          groupInstanceKey: Group instance key.
              
              Unique integer referencing
              device group. During group creation client should
              use a temporary negative number. Once group is
              added to the virtual machine, server generates non-negative
              integer that stays constant during group lifetime.
              See `pyVmomi.vim.vm.device.VirtualDevice.key` for details.
          deviceInfo: Provides a label and summary information for the device.
      """
      groupInstanceKey: int
      deviceInfo: _typing.Optional[pyVmomi.vim.Description] = None

   class VendorDeviceGroup(VirtualDeviceGroups.DeviceGroup):
      """
      Vendor device group.
      
      These groups are defined in the
      ``pyVmomi.vim.vm.VendorDeviceGroupInfo``.
      When this group is added, all devices that form the group
      must be added in the same request.
      Modification of membership in the group is not allowed,
      devices cannot be added or removed.
      When group is removed, all devices that form the group
      must be removed in the same request.
      
      Attributes:
          deviceGroupName: The name of the vendor device group from
              ``pyVmomi.vim.vm.VendorDeviceGroupInfo``.
      """
      deviceGroupName: str

   deviceGroup: list[VirtualDeviceGroups.DeviceGroup] = []


class VirtualDeviceSwap(pyVmomi.vmodl.DynamicData):
   """
   Device Swap: Report current status of device swap feature.
   
   Since: vSphere API Release 8.0.0.1
   """
   class DeviceSwapStatus(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          none: No operation active.
          scheduled: Device swap will be performed on next restart.
          inprogress: Device swap is in progress.
          failed: Device swap failed.
          completed: Device swap successfully completed.
      
      Since: vSphere API Release 8.0.0.1
      """
      none: _typing.ClassVar['VirtualDeviceSwap.DeviceSwapStatus'] = 'none'
      scheduled: _typing.ClassVar['VirtualDeviceSwap.DeviceSwapStatus'] = 'scheduled'
      inprogress: _typing.ClassVar['VirtualDeviceSwap.DeviceSwapStatus'] = 'inprogress'
      failed: _typing.ClassVar['VirtualDeviceSwap.DeviceSwapStatus'] = 'failed'
      completed: _typing.ClassVar['VirtualDeviceSwap.DeviceSwapStatus'] = 'completed'

   class DeviceSwapInfo(pyVmomi.vmodl.DynamicData):
      """
      Information for the device swap operation.
      
      Attributes:
          enabled: Is the swap operation enabled for this virtual machine.
          applicable: Is the swap operation applicable to this virtual machine?
              Operation is applicable if it is enabled for the virtual
              machine, for the host or cluster in which virtual machine
              resides, operating system supports device swap, and
              virtual machine has controllers that need to be replaced.
              
              This field is read-only and cannot be modified.
          status: Status of the operation.
              
              One of
              `pyVmomi.vim.vm.VirtualDeviceSwap.DeviceSwapStatus`
              This field is read-only and cannot be modified.
      
      Since: vSphere API Release 8.0.0.1
      """
      enabled: _typing.Optional[bool] = None
      applicable: _typing.Optional[bool] = None
      status: _typing.Optional[str] = None

   lsiToPvscsi: _typing.Optional[VirtualDeviceSwap.DeviceSwapInfo] = None


class VirtualHardware(pyVmomi.vmodl.DynamicData):
   """
   The VirtualHardware data object type contains the complete configuration
   of the hardware in a virtual machine.
   
   Attributes:
       numCPU: Number of virtual CPUs present in this virtual machine.
       numCoresPerSocket: Number of cores used to distribute virtual CPUs among sockets
           in this virtual machine.
           
           This field should be ignored for powered off VM with
           autoCoresPerSocket equals TRUE, because the virtual socket size
           will be assigned during power-on.
           This field could be unset for releases prior to 7.0 U3, and it
           implies numCoresPerSocket is 1.
           In other cases, this field represents the actual virtual socket
           size seen by the virtual machine.
       autoCoresPerSocket: Cores per socket is automatically determined.
           
           Since: vSphere API Release 8.0.0.1
       memoryMB: Memory size, in MB.
       virtualICH7MPresent: Does this virtual machine have Virtual Intel I/O Controller Hub 7
       virtualSMCPresent: Does this virtual machine have System Management Controller
       device: The set of virtual devices belonging to the virtual machine.
           
           This list is unordered.
       motherboardLayout: One of motherboardLayout choices.
           
           Default is i440bxHostBridge. See
           `pyVmomi.vim.vm.VirtualHardware.motherboardLayout`
           
           Since: vSphere API Release 8.0.0.1
       simultaneousThreads: Number of SMT (Simultaneous multithreading) threads.
           
           If unset, then system defaults are in use.
           
           Since: vSphere API Release 8.0.0.1
   """
   class MotherboardLayout(pyVmomi.VmomiSupport.Enum):
      """
      Motherboard layout of the VM.
      
      Attributes:
          i440bxHostBridge: Single i440BX host bridge.
          acpiHostBridges: Multiple ACPI host bridges.
      
      Since: vSphere API Release 8.0.0.1
      """
      i440bxHostBridge: _typing.ClassVar['VirtualHardware.MotherboardLayout'] = 'i440bxHostBridge'
      acpiHostBridges: _typing.ClassVar['VirtualHardware.MotherboardLayout'] = 'acpiHostBridges'

   numCPU: int
   numCoresPerSocket: _typing.Optional[int] = None
   autoCoresPerSocket: _typing.Optional[bool] = None
   memoryMB: int
   virtualICH7MPresent: _typing.Optional[bool] = None
   virtualSMCPresent: _typing.Optional[bool] = None
   device: list[pyVmomi.vim.vm.device.VirtualDevice] = []
   motherboardLayout: _typing.Optional[str] = None
   simultaneousThreads: _typing.Optional[int] = None


class VirtualHardwareOption(pyVmomi.vmodl.DynamicData):
   """
   The VirtualHardwareOption data object contains the options available
   for all virtual devices.
   
   Attributes:
       hwVersion: The virtual hardware version.
       virtualDeviceOption: Array of virtual device options valid for this virtual
           machine configuration.
           
           The list is unordered.
       deviceListReadonly: Whether the set of virtual devices can be changed, e.g., can devices
           be added or removed.
           
           This does not preclude changing devices.
       numCPU: List of acceptable values for the number of CPUs supported by this
           `pyVmomi.vim.vm.ConfigOption`.
           
           This is usually superseded by the information available in the
           guest operating system descriptors.
           The guest operating system descriptor describes a maximum CPU
           count, but the acceptable values are still constrained to the
           set specified here. The default value is stored at index 0 in the list.
       numCoresPerSocket: The minimum, maximum and default number of cores per socket that
           can be used when distributing virtual CPUs.
       autoCoresPerSocket: Whether auto cores per socket is supported.
           
           Since: vSphere API Release 8.0.0.1
       numCpuReadonly: Can the number of virtual CPUs be changed
       memoryMB: The minimum, maximum, and default memory options, in MB, per virtual machine,
           for this VirtualHardwareOption.
           
           These
           values are typically overruled by the supported and recommended
           values specified in the `pyVmomi.vim.vm.GuestOsDescriptor` class.
       numPCIControllers: The minimum, maximum, and default number of PCI controllers for
           this virtual machine configuration.
       numIDEControllers: The minimum, maximum, and default number of IDE controllers for
           this virtual machine configuration.
           
           Note: SCSI controllers sit
           on the PCI controller so their options (minimum, maximum, and default values)
           are contained inside the
           `pyVmomi.vim.vm.device.VirtualPCIControllerOption`
           class.
       numUSBControllers: The minimum, maximum, and default number of USB controllers for
           this virtual machine configuration.
       numUSBXHCIControllers: The minimum, maximum, and default number of XHCI (USB 3.0) controllers for
           this virtual machine configuration.
       numSIOControllers: The minimum, maximum, and default number of SIO controllers for
           this virtual machine configuration.
       numPS2Controllers: The minimum, maximum, and default number of PS2 controllers for
           this virtual machine configuration.
       licensingLimit: List of property names which limits are given be a licensing
           restriction of the underlying product, e.g., a limit that is
           not derived based on the product or hardware features.
           
           For example, the property name \"numCPU\"
       numSupportedWwnPorts: The minimum, maximum and default number of NPIV WorldWideNode names
           supported for this virtual machine configuration.
       numSupportedWwnNodes: The minimum, maximum and default number of NPIV WorldWidePort names
           supported for this virtual machine configuration.
       resourceConfigOption: Default value and value range for `pyVmomi.vim.ResourceConfigOption`
       numNVDIMMControllers: The minimum, maximum and default number of virtual NVDIMM controllers
           for this virtual machine configuration.
       numTPMDevices: The minimum, maximum, and default number of virtual TPMs.
       numWDTDevices: The minimum, maximum, and default number of virtual watchdog timers.
       numPrecisionClockDevices: The minimum, maximum and default number of PrecisionClock devices.
       epcMemoryMB: The minimum, maximum and default value of Intel's Secure Guard Extensions
           Enclave Page Cache (EPC) memory.
       acpiHostBridgesFirmware: Empty for HWv17 & older, [\"efi\"] for HWv18.
           
           Since: vSphere API Release 8.0.0.1
       numCpuSimultaneousThreads: The minimum, maximum and default number of CPU simultaneous threads.
           
           Since: vSphere API Release 8.0.0.1
       numNumaNodes: The minimum, maximum and default number of NUMA nodes.
           
           Since: vSphere API Release 8.0.0.1
       numDeviceGroups: Maximum number of device groups.
           
           Since: vSphere API Release 8.0.0.1
       deviceGroupTypes: Supported device group types.
           
           Since: vSphere API Release 8.0.0.1
   """
   hwVersion: int
   virtualDeviceOption: list[pyVmomi.vim.vm.device.VirtualDeviceOption] = []
   deviceListReadonly: bool
   numCPU: list[int] = []
   numCoresPerSocket: pyVmomi.vim.option.IntOption
   autoCoresPerSocket: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   numCpuReadonly: bool
   memoryMB: pyVmomi.vim.option.LongOption
   numPCIControllers: pyVmomi.vim.option.IntOption
   numIDEControllers: pyVmomi.vim.option.IntOption
   numUSBControllers: pyVmomi.vim.option.IntOption
   numUSBXHCIControllers: pyVmomi.vim.option.IntOption
   numSIOControllers: pyVmomi.vim.option.IntOption
   numPS2Controllers: pyVmomi.vim.option.IntOption
   licensingLimit: list[pyVmomi.VmomiSupport.PropertyPath] = []
   numSupportedWwnPorts: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numSupportedWwnNodes: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   resourceConfigOption: pyVmomi.vim.ResourceConfigOption
   numNVDIMMControllers: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numTPMDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numWDTDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numPrecisionClockDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   epcMemoryMB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   acpiHostBridgesFirmware: list[str] = []
   numCpuSimultaneousThreads: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numNumaNodes: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numDeviceGroups: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   deviceGroupTypes: list[type] = []


class VirtualNuma(pyVmomi.vmodl.DynamicData):
   """
   This data object describes the virtual NUMA configuration for
   this virtual machine and configured through ConfigSpec.
   
   Attributes:
       coresPerNumaNode: Cores per vNUMA node for this VM.
           
           The number of vNUMA nodes is
           calculated by total number of cores divided by corePerNumaNode.
           If set to be zero, it clears any manual override and autosize
           vNUMA node.
           If set to be non zero, VM uses the value as vNUMA node size.
           If unset, the VM continue to follow the behavior in last poweron.
       exposeVnumaOnCpuHotadd: Capability to expose virtual NUMA when CPU hotadd is enabled.
           
           If set to true, ESXi will consider exposing virtual NUMA to
           the VM when CPU hotadd is enabled.
           If set to false, ESXi will enforce the VM to have single
           virtual NUMA node when CPU hotadd is enabled.
           If unset, the VM continue to follow the behavior in last poweron.
   
   Since: vSphere API Release 8.0.0.1
   """
   coresPerNumaNode: _typing.Optional[int] = None
   exposeVnumaOnCpuHotadd: _typing.Optional[bool] = None


class VirtualNumaInfo(pyVmomi.vmodl.DynamicData):
   """
   vNUMA: This is read-only data for ConfigInfo since this portion is
   not configurable.
   
   Attributes:
       coresPerNumaNode: Cores per NUMA node.
           
           When this virtual machine is powered off and \"autoCoresPerNumaNode\"
           is True, coresPerNumaNode will be assigned during power-on and this
           field should be ignored.
           In other cases, this field represents the virtual NUMA node size
           seen by the guest.
       autoCoresPerNumaNode: Whether coresPerNode is determined automatically.
       vnumaOnCpuHotaddExposed: Whether virtual NUMA topology is exposed when CPU hotadd is
           enabled.
   
   Since: vSphere API Release 8.0.0.1
   """
   coresPerNumaNode: _typing.Optional[int] = None
   autoCoresPerNumaNode: _typing.Optional[bool] = None
   vnumaOnCpuHotaddExposed: _typing.Optional[bool] = None


class VirtualPMem(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere 9.0 APIs with no replacement.Virtual Persistent Memory configuration for the VM.
   
   Attributes:
       snapshotMode: An enum describing behavior of NVDIMM devices when a VM snapshot is taken
           and restored.
           
           If unset, taking a VM snapshot will fail when the VM is
           configured with NVDIMMs. See `pyVmomi.vim.vm.VirtualPMem.SnapshotMode` for supported values.
           The snapshot mode applies to all NVDIMMs configured for the VM.
           Property is currently only applicable to VMs with virtual NVDIMMs and not
           applicable to vPMem disks.
           Setting this property will fail if the VM has existing snapshots.
   
   Since: vSphere API Release 7.0.3.0
   """
   class SnapshotMode(pyVmomi.VmomiSupport.Enum):
      """
      The set of supported snapshot modes for VMs configured with NVDIMMs.
      
      Attributes:
          independent_persistent: The data on virtual NVDIMMs are not affected by snapshot reverts.
              
              Writes to virtual NVDIMMs after a snapshot is taken cannot be
              reverted to the snapshotted state.
          independent_eraseonrevert: Virtual NVDIMMs are erased and recreated upon snapshot reverts.
      
      Since: vSphere API Release 7.0.3.0
      """
      independent_persistent: _typing.ClassVar['VirtualPMem.SnapshotMode'] = 'independent_persistent'
      independent_eraseonrevert: _typing.ClassVar['VirtualPMem.SnapshotMode'] = 'independent_eraseonrevert'

   snapshotMode: _typing.Optional[str] = None


class VmImportSpec(pyVmomi.vim.ImportSpec):
   """
   A VmImportSpec is used by `pyVmomi.vim.ResourcePool.importVApp` when importing entities.
   
   It provides all information needed to import a `pyVmomi.vim.VirtualMachine`. So far,
   this coincides with `pyVmomi.vim.vm.ConfigSpec`.
   
   A VmImportSpec can be contained in a `pyVmomi.vim.vApp.VAppImportSpec` as part of
   the ImportSpec for an entity.
   
   See also `pyVmomi.vim.ImportSpec`.
   
   Attributes:
       configSpec: Configuration for the virtual machine.
       resPoolEntity: If specified, this resource pool will be used as the parent resource pool and the
           virtual machine will be made a linked child to the parent vApp.
           
           This field is ignored
           for the root node in an ImportSpec tree.
   """
   configSpec: ConfigSpec
   resPoolEntity: _typing.Optional[pyVmomi.vim.ResourcePool] = None


class VmPlacementPolicy(pyVmomi.vmodl.DynamicData):
   """
   Describes the constraints and/or preferences that can influence where a VM
   needs to be placed.
   
   A `pyVmomi.vim.vm.VmPlacementPolicy` for a VM can be specified in VM's
   `pyVmomi.vim.vm.ConfigSpec` or `pyVmomi.vim.vm.RelocateSpec` and that policy will be enforced
   when that VM's placement decision is made. The placement policies specified
   via `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` are enforced whenever a VM with
   that ConfigSpec needs to be placed for creation or power-on. Similarly,
   placement policies specified via `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies`
   are enforced whenever a VM with that RelocateSpec needs to be placed for
   relocating.
   
   This allows clients to express placement constraints/preferences directly as
   a part of `pyVmomi.vim.vm.ConfigSpec` or `pyVmomi.vim.vm.RelocateSpec` instead of requiring the
   clients to first create separate vCenter constructs for expressing the same
   constraint/preference. For example, if a VM's `pyVmomi.vim.vm.ConfigSpec` or
   `pyVmomi.vim.vm.RelocateSpec` has an affinity or anti-affinity towards other VMs
   (see `pyVmomi.vim.vm.VmVmAffinity` and `pyVmomi.vim.vm.VmVmAntiAffinity`), then vSphere DRS and
   vSphere HA can interpret and enforce that desired affinity/anti-affinity
   without requiring the client to first create a cluster level
   `pyVmomi.vim.cluster.AffinityRuleSpec` or
   `pyVmomi.vim.cluster.AntiAffinityRuleSpec` and then associate the VM with it.
   
   Placement policies can be of different types. This base class only defines
   the common properties that the different types of policies can have. The
   specific constraints and/or preferences that dictate how exactly a VM's
   placement can be impacted are described in each sub-type of policy derived
   from this base `pyVmomi.vim.vm.VmPlacementPolicy` class.
   
   Note: `pyVmomi.vim.vm.VmPlacementPolicy` is only applicable for VMs managed by
   Supervisor and they will be automatically populated by Supervisor based on
   the placement constraints defined in Supervisor. These placement policies
   will be ignored except when set by Supervisor.
   
   Since: vSphere API Release 9.1.0.0
   """
   class VmPlacementPolicyStrictness(pyVmomi.VmomiSupport.Enum):
      """
      Specifies the strictness of a placement policy to be enforced while
      placing a VM at different stages of a VM's lifecycle.
      
      This field may not apply to all types of placement policies derived from
      `pyVmomi.vim.vm.VmPlacementPolicy`.
      
      Attributes:
          PreferredDuringPlacementPreferredDuringExecution: A VmPlacementPolicy with this strictness is enforced on a best-effort
              basis whenever a VM linked with this policy (via that VM's
              `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
              `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies`) needs to be placed.
              
              Below is a detailed explanation:
              If an operation requires specifying a VM's `pyVmomi.vim.vm.ConfigSpec` or
              `pyVmomi.vim.vm.RelocateSpec` and there is a VmPlacementPolicy specified in
              that `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
              `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies` with this
              VmPlacementPolicyStrictness, then it means the following:
              
              (1) This VmPlacementPolicy will be considered as \"preferred\". This
              means that if a VM with this VmPlacementPolicy cannot be successfully
              placed on any host due to this policy, then the policy will be dropped
              and a placement recommendation can still be generated even if it
              results in violating that policy. This is denoted by the
              \"PreferredDuringPlacement\" part of this strictness value.
              
              (2) This VmPlacementPolicy will be enforced for that operation as well
              as beyond that when that VM is in execution. For example, when the VM
              needs to be relocated for putting its host into maintenance mode, then
              this VmPlacementPolicy will be enforced on a best-effort basis.
              Similarly, when the VM needs to be restarted as part of vSphere HA
              failover, then this VmPlacementPolicy will be enforced on a best-effort
              basis.
              This is denoted by the \"PreferredDuringExecution\" part of this
              strictness value. Note that if a VM needs to be relocated by DRS for
              load-balancing, then any VmPlacementPolicy is considered as \"Required\"
              and DRS load-balancing is not included in the \"PreferredDuringExecution\"
              part of this strictness value.
          RequiredDuringPlacementPreferredDuringExecution: A VmPlacementPolicy with this strictness is enforced on a strict
              basis while placing the VM for the operation where this policy has
              been specified via `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
              `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies`).
              
              After that, the same policy
              will be enforced on a best-effort basis.
              
              Below is a detailed explanation:
              If an operation requires specifying a VM's `pyVmomi.vim.vm.ConfigSpec` or
              `pyVmomi.vim.vm.RelocateSpec` and there is a VmPlacementPolicy specified in
              that `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
              `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies` with this
              VmPlacementPolicyStrictness, then it means the following:
              
              (1) This VmPlacementPolicy will be considered as \"required\" while
              computing the placement for that operation. This means that if a VM
              with this VmPlacementPolicy cannot be successfully placed on any host
              due to this policy, then the policy will still be honored and no
              placement recommendation will be generated for that operation. The
              policy must be satisfied to find a successful placement target for
              the VM for that operation. This is denoted by the
              \"RequiredDuringPlacement\" part of this strictness value.
              
              (2) This VmPlacementPolicy will be enforced for that operation as well
              as beyond that when that VM is in execution. For example, when the VM
              needs to be relocated for putting its host into maintenance mode, then
              this VmPlacementPolicy will be enforced on a best-effort basis.
              Similarly, when the VM needs to be restarted as part of vSphere HA
              failover, then this VmPlacementPolicy will be enforced on a best-effort
              basis.
              This is denoted by the \"PreferredDuringExecution\" part of this
              strictness value. Note that if a VM needs to be relocated by DRS for
              load-balancing, then any VmPlacementPolicy is considered as \"Required\"
              and DRS load-balancing is not included in the \"PreferredDuringExecution\"
              part of this strictness value.
      
      Since: vSphere API Release 9.1.0.0
      """
      PreferredDuringPlacementPreferredDuringExecution: _typing.ClassVar['VmPlacementPolicy.VmPlacementPolicyStrictness'] = 'PreferredDuringPlacementPreferredDuringExecution'
      RequiredDuringPlacementPreferredDuringExecution: _typing.ClassVar['VmPlacementPolicy.VmPlacementPolicyStrictness'] = 'RequiredDuringPlacementPreferredDuringExecution'

   class VmPlacementPolicyTopology(pyVmomi.VmomiSupport.Enum):
      """
      Defines the infrastructure topology for which a VM placement policy
      should be enforced.
      
      For example, for any policy that defines affinity or anti-affinity
      between VMs, the topology defines the granularity of the infrastructure
      at which the affinity or anti-affinity needs to be enforced.
      If 2 VMs are anti-affined, then:
      \\- Topology of host means those 2 VMs should be placed on 2 different hosts.
      \\- Topology of zone means those 2 VMs should be placed in 2 different zones.
      
      Note:
      \\- This field may not apply to all types of placement policies derived from
      `pyVmomi.vim.vm.VmPlacementPolicy`.
      
      Attributes:
          Host: Any VM placement policy with this `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` will
              be enforced at the granularity of ESXi host.
              
              For example, a VM-VM affinity policy with this
              `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` would imply that the associated VMs
              need to be placed on the same ESXi host.
          ClusterComputeResource: Any VM placement policy with this `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` will be
              enforced at the granularity of a vCenter compute cluster.
              
              For example, a VM-VM affinity policy with this
              `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` would imply that the associated VMs
              need to be placed in the same vCenter compute cluster.
          VSphereZone: Any VM placement policy with this `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` will be
              enforced at the granularity of vSphere Zone.
              
              For example, a VM-VM affinity policy with this
              `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology` would imply that the associated VMs
              need to be placed in the same vSphere Zone.
      
      Since: vSphere API Release 9.1.0.0
      """
      Host: _typing.ClassVar['VmPlacementPolicy.VmPlacementPolicyTopology'] = 'Host'
      ClusterComputeResource: _typing.ClassVar['VmPlacementPolicy.VmPlacementPolicyTopology'] = 'ClusterComputeResource'
      VSphereZone: _typing.ClassVar['VmPlacementPolicy.VmPlacementPolicyTopology'] = 'VSphereZone'


class VmToVmGroupsAntiAffinity(VmPlacementPolicy):
   """
   Specification of a placement policy that anti-affines this VM (for which
   this placement policy is being specified) with multiple groups of VMs.
   
   This policy allows specifying multiple groups of VMs such that this VM is
   anti-affined with every VM of the other VM groups. Each of these other
   groups is identified by a unique vSphere tag. Effectively, this VM will
   be anti-affined with any VM that has any of those other tags.
   
   However, note that while the policy will anti-affine a given VM with
   multiple \"other\" groups of VMs, there is no implied affinity or
   anti-affinity:
   1\\) Within the VMs of any one of those \"other\" groups.
   2\\) Between the VMs of any two of those \"other\" groups.
   Below example will explain this in more detail.
   
   Consider a VM that needs to be anti-affined with a VM that has either
   tag-2 or tag-3 attached to it. This can be expressed by specifying
   `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` policy in this VM's
   `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
   `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies` and it would imply:
   \\- This VM will be anti-affined with every VM that has tag-2.
   \\- This VM will be anti-affined with every VM that has tag-3.
   \\- Any VM that has either tag-2 or tag-3 will be anti-affined with
   this VM.
   \\- To enforce the above anti-affinity while placing this VM, or any VM
   with tag-2 or tag-3, a compute-policy will be automatically created
   in this vCenter.
   \\- To associate the compute-policy representing this VmToVmGroupsAntiAffinity
   VmPlacementPolicy with this VM, one of the tags associated with this
   VM will be used.
   \\- In this example, one of this VM's tags, let's say tag-1, could be
   used to link this VM with such a compute-policy. Then this compute-
   policy would mean that any VM with \"tag-1\" will be anti-affined with
   any VM with \"tag-2\" or \"tag-3\".
   \\- VMs that have \"tag-2\" will not have any affinity/anti-affinity among
   themselves.
   \\- VMs that have \"tag-3\" will not have any affinity/anti-affinity among
   themselves.
   \\- VMs that have \"tag-2\" will not have any affinity/anti-affinity with
   VMs that have \"tag-3\". Likewise for VMs with \"tag-3\".
   
   Note:
   \\- This placement policy is different than `pyVmomi.vim.vm.VmVmAntiAffinity`
   because `pyVmomi.vim.vm.VmVmAntiAffinity` allows specifying only 1 VM group
   and all the VMs within that group become anti-affined with each other,
   whereas, this placement policy allows anti-affining a given VM (with
   a given tag) with multiple groups VMs (represented via different tags).
   
   Attributes:
       selfTag: Tag identifying this VM to associate this `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity`
           placement policy with this VM.
           
           When a `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement policy is specified for a
           VM, then one of the tags attached to this VM needs to link this VM with
           the corresponding compute-policy representing this
           `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement policy. This is needed because
           when a VM is placed by vSphere DRS or HA, the compute-policies to be
           enforced are derived from the tag(s) attached to that VM.
           For example, consider a VM with tag-1 needs to be anti-affined with VMs
           of tag-2 and tag-3. When this placement policy needs to be specified for
           this VM, then tag-1 can be used as this VM's tag and the placement
           policy would say: [tag-1] ANTI-AFFINE [tag-2, tag-3].
           
           If left unset, system will automatically generate a new vSphere tag
           and attach to this VM.
       antiAffinedVmGroupTags: Tags identifying the \"other\" VM groups that need to be anti-affined with
           this VM.
           
           A VM with any tag from the list of tags in `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity.antiAffinedVmGroupTags`
           will be anti-affined with the VM that has `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity.selfTag` tag.
           any VM that has any of the other tags in
           
           This field must have at least one value that must be different from the
           value of `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity.selfTag`. If this field is left unset or empty, then
           this `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement policy will be ignored while
           placing this VM.
       policyStrictness: Specifies the strictness of this `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement
           policy while placing a VM for which this policy has been specified.
           
           For details, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyStrictness`
           
           If this field is left unset, then the default value of
           `PreferredDuringPlacementPreferredDuringExecution`
           will be assumed.
       policyTopology: Specifies the topology for enforcing this `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity`
           placement policy while placing a VM for which this policy is specified.
           
           For possible values, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology`.
           
           For example:
           \\- If this is set to
           `VSphereZone`
           for a `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement, then the groups of VMs
           anti-affined by this policy should be placed in different vSphere Zones.
           \\- If this is set to
           `Host`,
           for a `pyVmomi.vim.vm.VmToVmGroupsAntiAffinity` placement, then the groups of VMs
           anti-affined by this policy should be placed on different ESXi hosts.
           
           If this field is left unset, then the default value of
           `Host` will be assumed.
   
   Since: vSphere API Release 9.1.0.0
   """
   selfTag: _typing.Optional[pyVmomi.vim.TagId] = None
   antiAffinedVmGroupTags: list[pyVmomi.vim.TagId] = []
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class VmVmAffinity(VmPlacementPolicy):
   """
   Specification of a VM placement policy that affines a group of
   VMs among themselves.
   
   Attributes:
       affinedVmsTag: Name of the vSphere tag identifying the VMs that need to be affined
           with each other.
           
           When this type of placement policy is specified for a VM
           (via `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
           `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies`), then that VM is affined with
           all the other VMs that have `pyVmomi.vim.vm.VmVmAffinity.affinedVmsTag` a vSphere tag.
           This means that DRS will attempt to place all the VMs with
           `pyVmomi.vim.vm.VmVmAffinity.affinedVmsTag` on the same target host/cluster/vSphereZone
           (where the topology of the target is specified by
           `pyVmomi.vim.vm.VmVmAffinity.policyTopology`).
           
           Example: VmVmAffinity placement policy with `pyVmomi.vim.vm.VmVmAffinity.affinedVmsTag`
           equal to \"test-workloads\" would mean that all the VMs that have a
           vSphere tag with the name \"test-workloads\" should be placed on the
           same target host/cluster/vSphereZone (as indicated by
           `pyVmomi.vim.vm.VmVmAffinity.policyTopology`).
       policyStrictness: Specifies the strictness of this VmVmAffinity placement
           policy while placing a VM for which this policy is specified.
           
           For details, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyStrictness`
           
           If this field is left unset, then the default value of
           `PreferredDuringPlacementPreferredDuringExecution`
           will be assumed.
       policyTopology: Specifies the topology for enforcing this VmVmAffinity placement
           policy while placing a VM for which this policy is specified.
           
           For possible values, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology`.
           
           For example:
           \\- If this is set to
           `VSphereZone`,
           the VMs that have `pyVmomi.vim.vm.VmVmAffinity.affinedVmsTag`
           tag attached to them should be placed in the same vSphere Zone.
           \\- If this is set to
           `Host`,
           the VMs that have `pyVmomi.vim.vm.VmVmAffinity.affinedVmsTag`
           tag attached to them should be placed on the same ESXi host.
           
           If this field is left unset, then the default value of
           `Host` will be assumed.
   
   Since: vSphere API Release 9.1.0.0
   """
   affinedVmsTag: pyVmomi.vim.TagId
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class VmVmAntiAffinity(VmPlacementPolicy):
   """
   Specification of a VM placement policy that anti-affines a group of
   VMs among themselves.
   
   Attributes:
       antiAffinedVmsTag: Name of the vSphere tag identifying the VMs that need to be anti-affined
           with each other.
           
           When this type of placement policy is specified for a VM,
           (via `pyVmomi.vim.vm.ConfigSpec.vmPlacementPolicies` or
           `pyVmomi.vim.vm.RelocateSpec.vmPlacementPolicies`), then that VM is anti-affined
           to all the other VMs that have `pyVmomi.vim.vm.VmVmAntiAffinity.antiAffinedVmsTag`. This means
           that DRS will attempt to place all the VMs with
           `pyVmomi.vim.vm.VmVmAntiAffinity.antiAffinedVmsTag` tag on different target hosts/clusters/
           vSphereZones (where the topology of the target is specified by
           `pyVmomi.vim.vm.VmVmAntiAffinity.policyTopology`).
           
           For example - VmVmAntiAffinity placement policy with
           `pyVmomi.vim.vm.VmVmAntiAffinity.antiAffinedVmsTag` equal to \"prod-workloads\" would mean that
           all the VMs that have a vSphere tag with the name \"prod-workloads\" should
           be placed on different target hosts/clusters/vSphereZones (as indicated by
           `pyVmomi.vim.vm.VmVmAntiAffinity.policyTopology`).
       policyStrictness: Specifies the strictness of this VmVmAntiAffinity placement
           policy while placing a VM for which this policy is specified.
           
           For
           details, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyStrictness`
           
           If this field is left unset, then the default value of
           `PreferredDuringPlacementPreferredDuringExecution`
           will be assumed.
       policyTopology: Specifies the topology for enforcing this VmVmAntiAffinity placement
           policy while placing a VM for which this policy is specified.
           
           For possible values, see
           `pyVmomi.vim.vm.VmPlacementPolicy.VmPlacementPolicyTopology`.
           
           For example:
           \\- If this is set to
           `VSphereZone`, the VMs
           that have `pyVmomi.vim.vm.VmVmAntiAffinity.antiAffinedVmsTag` tag attached to them should be
           placed in different vSphere Zones.
           \\- If this is set to
           `Host`, the VMs that
           have `pyVmomi.vim.vm.VmVmAntiAffinity.antiAffinedVmsTag` tag attached to them should be placed
           on different ESXi hosts (but they may be placed in the same vSphere Zone).
           
           If this field is left unset, then the default value of
           `Host` will be assumed.
   
   Since: vSphere API Release 9.1.0.0
   """
   antiAffinedVmsTag: pyVmomi.vim.TagId
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class WindowsQuiesceSpec(GuestQuiesceSpec):
   """
   This data object type encapsulates configuration settings
   when creating a virtual machine quiesced snapshot.
   
   Attributes:
       vssBackupType: The property to indicate what type of VSS backup operation is going
           to be performed on the virtual machine.
           
           See VSS_BACKUP_TYPE on MSDN:
           https://msdn.microsoft.com/en-us/library/aa384679(v=vs.85).aspx
       vssBootableSystemState: The property to indicate if a bootable system state during VSS backup
           to be performed on the virtual machine.
       vssPartialFileSupport: The property to indicate if partial file support is enabled during VSS
           backup to be performed on the virtual machine.
       vssBackupContext: The property to indicate what context of VSS backup operation to be
           performed on the virtual machine.
           
           For the list of supported values,
           see `pyVmomi.vim.vm.WindowsQuiesceSpec.VssBackupContext`
   """
   class VssBackupContext(pyVmomi.VmomiSupport.Enum):
      """
      The VSS Snapshot Context
      VSS_SNAPSHOT_CONTEXT values not listed below are not implemented.
      
      Attributes:
          ctx_auto: The context value indicates auto selection of VSS snapshot context.
              
              The ctx_backup may make Windows VSS-aware applications quiescing during
              backup. The ctx_auto makes VMTools select ctx_file_share_backup context
              if ctx_backup is not available.
          ctx_backup: Indicate VSS_CTX_BACKUP.
          ctx_file_share_backup: Indicate VSS_CTX_FILE_SHARE_BACKUP.
      """
      ctx_auto: _typing.ClassVar['WindowsQuiesceSpec.VssBackupContext'] = 'ctx_auto'
      ctx_backup: _typing.ClassVar['WindowsQuiesceSpec.VssBackupContext'] = 'ctx_backup'
      ctx_file_share_backup: _typing.ClassVar['WindowsQuiesceSpec.VssBackupContext'] = 'ctx_file_share_backup'

   vssBackupType: _typing.Optional[int] = None
   vssBootableSystemState: _typing.Optional[bool] = None
   vssPartialFileSupport: _typing.Optional[bool] = None
   vssBackupContext: _typing.Optional[str] = None
