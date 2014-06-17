.. _string: ../../str

.. _vim.fault.VmConfigFault: ../../vim/fault/VmConfigFault.rst


vim.fault.UnsupportedDatastore
==============================
    :extends:

        `vim.fault.VmConfigFault`_

  The virtual machine is not supported on the target datastore. This fault is thrown by provisioning operations when an attempt is made to create a virtual machine on an unsupported datastore (for example, creating a non-legacy virtual machine on a legacy datastore).

Attributes:

    datastore (`str`_): is optional.




