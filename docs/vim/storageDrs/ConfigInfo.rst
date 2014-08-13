.. _StoragePod: ../../vim/StoragePod.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _StorageDrsConfigInfo: ../../vim/storageDrs/ConfigInfo.rst

.. _vim.storageDrs.VmConfigInfo: ../../vim/storageDrs/VmConfigInfo.rst

.. _vim.storageDrs.PodConfigInfo: ../../vim/storageDrs/PodConfigInfo.rst


vim.storageDrs.ConfigInfo
=========================
  The `StorageDrsConfigInfo`_ data object describes storage DRS configuration for a pod `StoragePod`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    podConfig (`vim.storageDrs.PodConfigInfo`_):

       Pod-wide configuration of the storage DRS service.
    vmConfig ([`vim.storageDrs.VmConfigInfo`_], optional):

       List of virtual machine configurations for the storage DRS service. Each entry applies to all the virtual disks of the virtual machine on this pod.If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.
