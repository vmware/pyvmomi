
vim.fault.CannotChangeVsanClusterUuid
=====================================
    :extends:

        `vim.fault.VsanFault <vim/fault/VsanFault.rst>`_

  Fault thrown for cases that a VSAN cluster UUID may not be changed. For example, the VSAN cluster UUID for a host may not be changed so long as that host is enabled for VSAN. The VSAN cluster UUID for a given `ClusterComputeResource <vim/ClusterComputeResource.rst>`_ may not be changed so long as that vim.ClusterComputeResource is enabled for VSAN.See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ 

Attributes:




