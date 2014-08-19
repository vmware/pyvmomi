
vim.fault.NoPermissionOnNasVolume
=================================
    :extends:

        `vim.fault.NasConfigFault <vim/fault/NasConfigFault.rst>`_

  This fault is thrown when an operation to configure a NAS volume fails because of insufficient user permissions. For CIFS volumes, this implies that the user specified in the `spec <vim/host/NasVolume/Specification.rst>`_ does not have access to the network resource.

Attributes:

    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




