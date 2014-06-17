.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.CustomizationFault: ../../vim/fault/CustomizationFault.rst


vim.fault.NicSettingMismatch
============================
    :extends:

        `vim.fault.CustomizationFault`_

  The number of network adapter settings in the customization specification does not match the number of network adapters present in the virtual machine.

Attributes:

    numberOfNicsInSpec (`int`_)

    numberOfNicsInVM (`int`_)




