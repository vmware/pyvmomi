
vim.fault.AlreadyConnected
==========================
    :extends:

        `vim.fault.HostConnectFault <vim/fault/HostConnectFault.rst>`_

  AlreadyConnect fault is thrown by the host connect method if the host is already connected to a VirtualCenter server. This might occur if the host has been added more than once in the same VirtualCenter in different folders or compute resources.

Attributes:

    name (`str <https://docs.python.org/2/library/stdtypes.html>`_)




