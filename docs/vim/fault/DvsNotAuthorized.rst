.. _str: https://docs.python.org/2/library/stdtypes.html

.. _extensionKey: ../../vim/DistributedVirtualSwitch/ConfigInfo.rst#extensionKey

.. _vim.fault.DvsFault: ../../vim/fault/DvsFault.rst

.. _dvsOperationSupported: ../../vim/DistributedVirtualSwitch/Capability.rst#dvsOperationSupported


vim.fault.DvsNotAuthorized
==========================
    :extends:

        `vim.fault.DvsFault`_

  Thrown if `dvsOperationSupported`_ is false and `extensionKey`_ is not same as the extension key of the login-session.

Attributes:

    sessionExtensionKey (`str`_): is optional.

    dvsExtensionKey (`str`_): is optional.




