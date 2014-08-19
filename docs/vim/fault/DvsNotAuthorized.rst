
vim.fault.DvsNotAuthorized
==========================
    :extends:

        `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_

  Thrown if `dvsOperationSupported <vim/DistributedVirtualSwitch/Capability.rst#dvsOperationSupported>`_ is false and `extensionKey <vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey>`_ is not same as the extension key of the login-session.

Attributes:

    sessionExtensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    dvsExtensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




