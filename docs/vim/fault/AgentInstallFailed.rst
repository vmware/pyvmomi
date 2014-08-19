
vim.fault.AgentInstallFailed
============================
    :extends:

        `vim.fault.HostConnectFault <vim/fault/HostConnectFault.rst>`_

  An AgentInstallFailed fault is thrown when VirtualCenter fails to install the VirtualCenter agent on a host. For example, a fault is thrown if the agent software cannot be uploaded to the host or an error occurred during the agent installation.

Attributes:

    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    statusCode (`int <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    installerOutput (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




