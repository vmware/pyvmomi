
vim.fault.MismatchedBundle
==========================
    :extends:

        `vim.fault.VimFault <vim/fault/VimFault.rst>`_

  A MismatchedBundle fault is thrown when the bundle supplied for `RestoreFirmwareConfiguration <vim/host/FirmwareSystem.rst#restoreConfiguration>`_ does not match the specifications of the host

Attributes:

    bundleUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    hostUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    bundleBuildNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_)

    hostBuildNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_)




