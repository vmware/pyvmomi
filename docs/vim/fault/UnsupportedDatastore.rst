
vim.fault.UnsupportedDatastore
==============================
    :extends:

        `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_

  The virtual machine is not supported on the target datastore. This fault is thrown by provisioning operations when an attempt is made to create a virtual machine on an unsupported datastore (for example, creating a non-legacy virtual machine on a legacy datastore).

Attributes:

    datastore (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




