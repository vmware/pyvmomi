.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ClusterComputeResource: ../../vim/ClusterComputeResource.rst

.. _CannotMoveVsanEnabledHost: ../../vim/fault/CannotMoveVsanEnabledHost.rst

.. _vim.fault.CannotMoveVsanEnabledHost: ../../vim/fault/CannotMoveVsanEnabledHost.rst


vim.fault.VsanClusterUuidMismatch
=================================
    :extends:

        `vim.fault.CannotMoveVsanEnabledHost`_

  Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into a `ClusterComputeResource`_ whose VSAN cluster UUID does not match.See `CannotMoveVsanEnabledHost`_ 

Attributes:

    hostClusterUuid (`str`_)

    destinationClusterUuid (`str`_)




