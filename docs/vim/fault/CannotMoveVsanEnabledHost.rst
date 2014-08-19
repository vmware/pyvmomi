
vim.fault.CannotMoveVsanEnabledHost
===================================
    :extends:

        `vim.fault.VsanFault <vim/fault/VsanFault.rst>`_

  Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into an unsuitable `ClusterComputeResource <vim/ClusterComputeResource.rst>`_ . The destination vim.ClusterComputeResource may be disabled for VSAN, or may be using VSAN with a different cluster UUID.See `AddHost_Task <vim/ClusterComputeResource.rst#addHost>`_ See `MoveHostInto_Task <vim/ClusterComputeResource.rst#moveHostInto>`_ See `MoveInto_Task <vim/ClusterComputeResource.rst#moveInto>`_ See `VsanClusterUuidMismatch <vim/fault/VsanClusterUuidMismatch.rst>`_ See `DestinationVsanDisabled <vim/fault/DestinationVsanDisabled.rst>`_ 

Attributes:




