vim.fault.VmFaultToleranceConfigIssue.ReasonForIssue
====================================================
  :contained by: `vim.fault.VmFaultToleranceConfigIssue <vim/fault/VmFaultToleranceConfigIssue.rst>`_

  :type: `vim.fault.VmFaultToleranceConfigIssue.ReasonForIssue <vim/fault/VmFaultToleranceConfigIssue/ReasonForIssue.rst>`_

  :name: hasVFlashConfiguration

values:
--------

hasLocalDisk
   The virtual machine has one or more disks on local datastore

missingVMotionNic
   No VMotion license or VMotion nic is not configured on the host

video3dEnabled
   The virtual machine video device has 3D enabled

noConfig
   No configuration information is available for the virtual machine

hasNestedHVConfiguration
   Nested HV and FT are mutually exclusive. Disallow turning on FT when nested HV configuration is enabled on VM.

hasUnsupportedDisk
   hasUnsupportedDisk

recordReplayNotSupported
   The virtual machine does not support record/replay. Vm::Capability.RecordReplaySupported is false.

haNotEnabled
   HA is not enabled on the cluster

thinDisk
   The virtual machine has thin provisioned disks

replayNotSupported
   It is not possible to turn on Fault Tolerance on this powered-on VM. The support for record/replay should be enabled or Fault Tolerance turned on, when this VM is powered off.

hasSnapshots
   The virtual machine has one or more snapshots

ftUnsupportedProduct
   The host ftSupported flag is not set because of it is a VMware Server 2.0

esxAgentVm
   The virtual machine is an ESX agent VM

templateVm
   The virtual machine is a template

multipleVCPU
   The virtual machine has more than one virtual CPU

missingFTLoggingNic
   FT logging nic is not configured on the host

ftSecondaryVm
   The virtual machine is a fault tolerance secondary virtual machine

hostInactive
   The host is not active

hasVFlashConfiguration
   The virtual machine has a vFlash memory device or/and disks with vFlash cache configured.

moreThanOneSecondary
   There is already a secondary virtual machine for the primary virtual machine

ftUnsupportedHardware
   The host ftSupported flag is not set because of hardware issues

verifySSLCertificateFlagNotSet
   The "check host certificate" flag is not set
