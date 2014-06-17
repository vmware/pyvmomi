.. _str: https://docs.python.org/2/library/stdtypes.html

.. _spec: ../../vim/host/NasVolume/Specification.rst

.. _vim.fault.NasConfigFault: ../../vim/fault/NasConfigFault.rst


vim.fault.InvalidNasCredentials
===============================
    :extends:

        `vim.fault.NasConfigFault`_

  This fault is thrown when an operation to configure a CIFS volume fails because the credentials specified in the `spec`_ are incorrect.

Attributes:

    userName (`str`_)




