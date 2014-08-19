
vim.fault.InventoryHasStandardAloneHosts
========================================
    :extends:

        `vmodl.fault.NotEnoughLicenses <vmodl/fault/NotEnoughLicenses.rst>`_

  A InventoryHasStandardAloneHosts fault is thrown if an assignment operation tries to downgrade a license that does have allow hosts licensed with StandardAlone license in the inventory.

Attributes:

    hosts (`str <https://docs.python.org/2/library/stdtypes.html>`_)




