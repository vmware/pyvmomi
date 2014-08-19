
vim.fault.VsanClusterUuidMismatch
=================================
    :extends:

        `vim.fault.CannotMoveVsanEnabledHost <vim/fault/CannotMoveVsanEnabledHost.rst>`_

  Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into a `ClusterComputeResource <vim/ClusterComputeResource.rst>`_ whose VSAN cluster UUID does not match.See `CannotMoveVsanEnabledHost <vim/fault/CannotMoveVsanEnabledHost.rst>`_ 

Attributes:

    hostClusterUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    destinationClusterUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_)




