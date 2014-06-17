.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.InvalidDeviceSpec: ../../vim/fault/InvalidDeviceSpec.rst


vim.fault.InvalidController
===========================
    :extends:

        `vim.fault.InvalidDeviceSpec`_

  An InvalidController exception is thrown if a device refers to a controller that cannot be found. For example, an exception might be thrown if the client incorrectly passes a controller key, or if the client did not specify a controller where one is required (such as for disks or CD-ROMs).

Attributes:

    controllerKey (`int`_)




