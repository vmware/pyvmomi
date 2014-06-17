.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst


vim.fault.DasConfigFault
========================
    :extends:

        `vim.fault.VimFault`_

  This fault indicates that some error has occurred during the configuration of the host for HA. This may be subclassed by a more specific fault.

Attributes:

    reason (`str`_): is optional.

    output (`str`_): is optional.

    event (`str`_): is optional.




