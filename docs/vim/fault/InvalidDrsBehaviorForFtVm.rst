.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst


vim.fault.InvalidDrsBehaviorForFtVm
===================================
    :extends:

        `vmodl.fault.InvalidArgument`_

  This fault is thrown when an attempt is made to set the DRS behavior of an FT VM to an unsupported value. Currently, the only supported behavior isDRS Disabled.

Attributes:

    vm (`str`_)

    vmName (`str`_)




