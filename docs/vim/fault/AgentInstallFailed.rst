.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.HostConnectFault: ../../vim/fault/HostConnectFault.rst


vim.fault.AgentInstallFailed
============================
    :extends:

        `vim.fault.HostConnectFault`_

  An AgentInstallFailed fault is thrown when VirtualCenter fails to install the VirtualCenter agent on a host. For example, a fault is thrown if the agent software cannot be uploaded to the host or an error occurred during the agent installation.

Attributes:

    reason (`str`_): is optional.

    statusCode (`int`_): is optional.

    installerOutput (`str`_): is optional.




