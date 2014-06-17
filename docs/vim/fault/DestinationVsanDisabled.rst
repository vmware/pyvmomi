.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ClusterComputeResource: ../../vim/ClusterComputeResource.rst

.. _CannotMoveVsanEnabledHost: ../../vim/fault/CannotMoveVsanEnabledHost.rst

.. _vim.fault.CannotMoveVsanEnabledHost: ../../vim/fault/CannotMoveVsanEnabledHost.rst


vim.fault.DestinationVsanDisabled
=================================
    :extends:

        `vim.fault.CannotMoveVsanEnabledHost`_

  Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into a `ClusterComputeResource`_ which is disabled for VSAN.See `CannotMoveVsanEnabledHost`_ 

Attributes:

    destinationCluster (`str`_)




