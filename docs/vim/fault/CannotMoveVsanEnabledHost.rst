.. _AddHost_Task: ../../vim/ClusterComputeResource.rst#addHost

.. _MoveInto_Task: ../../vim/ClusterComputeResource.rst#moveInto

.. _MoveHostInto_Task: ../../vim/ClusterComputeResource.rst#moveHostInto

.. _vim.fault.VsanFault: ../../vim/fault/VsanFault.rst

.. _ClusterComputeResource: ../../vim/ClusterComputeResource.rst

.. _VsanClusterUuidMismatch: ../../vim/fault/VsanClusterUuidMismatch.rst

.. _DestinationVsanDisabled: ../../vim/fault/DestinationVsanDisabled.rst


vim.fault.CannotMoveVsanEnabledHost
===================================
    :extends:

        `vim.fault.VsanFault`_

  Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into an unsuitable `ClusterComputeResource`_ . The destination vim.ClusterComputeResource may be disabled for VSAN, or may be using VSAN with a different cluster UUID.See `AddHost_Task`_ See `MoveHostInto_Task`_ See `MoveInto_Task`_ See `VsanClusterUuidMismatch`_ See `DestinationVsanDisabled`_ 

Attributes:




