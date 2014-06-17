.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.Timedout: ../../vim/fault/Timedout.rst


vim.fault.PowerOnFtSecondaryTimedout
====================================
    :extends:

        `vim.fault.Timedout`_

  PowerOnFtSecondaryTimedout exception is thrown when Virtual Center fails the operation to power on a Fault Tolerance secondary virtual machine because it is taking longer than expected.

Attributes:

    vm (`str`_)

    vmName (`str`_)

    timeout (`int`_)




