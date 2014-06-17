.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.NasConfigFault: ../../vim/fault/NasConfigFault.rst


vim.fault.NasSessionCredentialConflict
======================================
    :extends:

        `vim.fault.NasConfigFault`_

  This fault is thrown when an operation to configure a CIFS volume fails when attempting to log on more than once with the same user name.

Attributes:

    remoteHost (`str`_)

    remotePath (`str`_)

    userName (`str`_)




