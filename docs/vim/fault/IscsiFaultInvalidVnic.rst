
vim.fault.IscsiFaultInvalidVnic
===============================
    :extends:

        `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_

  This fault indicates an attempt is made to bind a Virtual NIC to an iSCSI adapter where the Virtual NIC has no association with the adapter. For ex: The uplink for the given Virtual NIC is not valid for the iSCSI HBA.

Attributes:

    vnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_)




