.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.InvalidIpmiMacAddress
===============================
    :extends:

        `vim.fault.VimFault`_

  A InvalidIpmiMacAddress fault is thrown when the IPMI mac address provided by the user doesn't match with the observed mac address on the host.

Attributes:

    userProvidedMacAddress (`str`_)

    observedMacAddress (`str`_)




