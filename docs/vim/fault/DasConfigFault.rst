
vim.fault.DasConfigFault
========================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  This fault indicates that some error has occurred during the configuration of the host for HA. This may be subclassed by a more specific fault.

Attributes:

    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    output (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    event (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




