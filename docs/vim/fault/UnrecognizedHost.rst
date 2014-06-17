.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.UnrecognizedHost
==========================
    :extends:

        `vim.fault.VimFault`_

  A UnrecognizedHost is thrown if the VirtualCenter server fails to validate the identity of the host using host-key. If a reconnect is attempted on a host and if the host-key of the host has changed since the last successful connection attempt, (might be changed by another instance of VirtualCenter), VirtualCenter server will fail to recognize the host.

Attributes:

    hostName (`str`_)




