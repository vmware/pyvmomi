.. _vim.StoragePod: ../../../vim/StoragePod.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.cluster.RuleInfo: ../../../vim/cluster/RuleInfo.rst

.. _StorageDrsConfigInfo: ../../../vim/storageDrs/ConfigInfo.rst

.. _vim.storageDrs.VmConfigInfo: ../../../vim/storageDrs/VmConfigInfo.rst

.. _vim.storageDrs.PodSelectionSpec.DiskLocator: ../../../vim/storageDrs/PodSelectionSpec/DiskLocator.rst


vim.storageDrs.PodSelectionSpec.VmPodConfig
===========================================
  Initial VM configuration for the specified pod. This configuration will be saved to the pod config `StorageDrsConfigInfo`_ when the placement recommendations are applied.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    storagePod (`vim.StoragePod`_):

       The pod that this initial configuration applies to. Since there could be multiple pods in a single placement request, we may need to specify multiple initial VM configurations, one per pod.
    disk (`vim.storageDrs.PodSelectionSpec.DiskLocator`_, optional):

       Array of PodDiskLocator objects.
    vmConfig (`vim.storageDrs.VmConfigInfo`_, optional):

       The VM configuration for the VM that is being placed.
    interVmRule (`vim.cluster.RuleInfo`_, optional):

       The initial interVmRules that should during placement of this virtual machine. It may not always be possible to specify that the virtual machine being placed is part of the rule because the virtual machine may not have been created yet. So for simplicity, we assume the virtual machine being placed is always implicitly part of any rule specified. It will be explicitly added to the rule before it is saved to the pod config.
