
vim.fault.InvalidIpmiMacAddress
===============================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  A InvalidIpmiMacAddress fault is thrown when the IPMI mac address provided by the user doesn't match with the observed mac address on the host.

Attributes:

    userProvidedMacAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    observedMacAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_)




