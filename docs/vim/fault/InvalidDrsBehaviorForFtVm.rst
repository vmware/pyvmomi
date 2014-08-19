
vim.fault.InvalidDrsBehaviorForFtVm
===================================
    :extends:

        `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_

  This fault is thrown when an attempt is made to set the DRS behavior of an FT VM to an unsupported value. Currently, the only supported behavior isDRS Disabled.

Attributes:

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




