.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.InsufficientResourcesFault: ../../vim/fault/InsufficientResourcesFault.rst


vim.fault.VmFaultToleranceTooManyVMsOnHost
==========================================
    :extends:

        `vim.fault.InsufficientResourcesFault`_

  This fault is returned when a host has more than the recommended number of Fault Tolerance VMs running on it.

Attributes:

    hostName (`str`_): is optional.

    maxNumFtVms (`int`_)




