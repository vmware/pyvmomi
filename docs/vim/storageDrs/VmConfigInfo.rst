.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _StoragePod: ../../vim/StoragePod.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _defaultIntraVmAffinity: ../../vim/storageDrs/PodConfigInfo.rst#defaultIntraVmAffinity

.. _StorageDrsPodConfigInfoBehavior: ../../vim/storageDrs/PodConfigInfo/Behavior.rst

.. _vim.storageDrs.VirtualDiskAntiAffinityRuleSpec: ../../vim/storageDrs/VirtualDiskAntiAffinityRuleSpec.rst


vim.storageDrs.VmConfigInfo
===========================
  Storage DRS configuration for a single virtual machine. This makes it possible to override the default behavior for an individual virtual machine.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    vm (`vim.VirtualMachine`_, optional):

       Reference to the virtual machine. Can be NULL during initial placement.
    enabled (`bool`_, optional):

       Flag to indicate whether or not VirtualCenter is allowed to perform any storage migration or initial placement recommendations for this virtual machine on the pod `StoragePod`_ . If this flag is false, the virtual machine is effectively excluded from storage DRS.If no individual DRS specification exists for a virtual machine, this property defaults to true.
    behavior (`str`_, optional):

       Specifies the particular storage DRS behavior for this virtual machine. For supported values, see `StorageDrsPodConfigInfoBehavior`_ .
    intraVmAffinity (`bool`_, optional):

       Specifies whether or not to have the affinity rule for the virtual disks of this virtual machine. If not set, the default value is derived from the pod-wide default `defaultIntraVmAffinity`_ .
    intraVmAntiAffinity (`vim.storageDrs.VirtualDiskAntiAffinityRuleSpec`_, optional):

       Specifies the disks for this virtual machine that should be placed on different datastores. A VM cannot have both an affinity and an anti-affinity rule at the same time. Virtual machine disks that are not in this rule are unconstrained and can be placed either on the same datastore or on a different datastore as other disks from this virtual machine.
