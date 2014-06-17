.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.NasConfigFault: ../../vim/fault/NasConfigFault.rst


vim.fault.NasConnectionLimitReached
===================================
    :extends:

        `vim.fault.NasConfigFault`_

  This fault is thrown when an operation to configure a CIFS volume fails because the request exceeds the maximum allowed connections on this host for the specified remote path.

Attributes:

    remoteHost (`str`_)

    remotePath (`str`_)




