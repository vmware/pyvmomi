
vim.fault.NasSessionCredentialConflict
======================================
    :extends:

        `vim.fault.NasConfigFault <vim/fault/NasConfigFault.rst>`_

  This fault is thrown when an operation to configure a CIFS volume fails when attempting to log on more than once with the same user name.

Attributes:

    remoteHost (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    remotePath (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




