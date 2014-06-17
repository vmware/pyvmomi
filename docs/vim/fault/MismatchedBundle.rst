.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VimFault: ../../vim/fault/VimFault.rst

.. _RestoreFirmwareConfiguration: ../../vim/host/FirmwareSystem.rst#restoreConfiguration


vim.fault.MismatchedBundle
==========================
    :extends:

        `vim.fault.VimFault`_

  A MismatchedBundle fault is thrown when the bundle supplied for `RestoreFirmwareConfiguration`_ does not match the specifications of the host

Attributes:

    bundleUuid (`str`_)

    hostUuid (`str`_)

    bundleBuildNumber (`int`_)

    hostBuildNumber (`int`_)




