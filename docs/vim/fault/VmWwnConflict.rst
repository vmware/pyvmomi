.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.InvalidVmConfig: ../../vim/fault/InvalidVmConfig.rst


vim.fault.VmWwnConflict
=======================
    :extends:

        `vim.fault.InvalidVmConfig`_

  Thrown if a user attempts to assign a WWN that is currently being used by other virtual machine or host.

Attributes:

    vm (`str`_): is optional.

    host (`str`_): is optional.

    name (`str`_): is optional.

    wwn (`long`_): is optional.




