
vim.fault.IscsiFaultVnicIsLastPath
==================================
    :extends:

        `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_

  This fault indicates that the given Virtual NIC is associated with the only path to the storage. Any attempt to unbind this from iSCSI HBA would result in storage being inaccessible.

Attributes:

    vnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_)




