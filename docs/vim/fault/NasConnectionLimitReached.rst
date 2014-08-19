
vim.fault.NasConnectionLimitReached
===================================
    :extends:

        `vim.fault.NasConfigFault <vim/fault/NasConfigFault.rst>`_

  This fault is thrown when an operation to configure a CIFS volume fails because the request exceeds the maximum allowed connections on this host for the specified remote path.

Attributes:

    remoteHost (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    remotePath (`str <https://docs.python.org/2/library/stdtypes.html>`_)




