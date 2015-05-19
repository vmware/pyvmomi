.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.BoolOption: ../../../vim/option/BoolOption.rst

.. _vim.option.ChoiceOption: ../../../vim/option/ChoiceOption.rst

.. _vim.vm.device.VirtualDeviceOption: ../../../vim/vm/device/VirtualDeviceOption.rst


vim.vm.device.VirtualEthernetCardOption
=======================================
  This data object type contains the options for the virtual ethernet card data object type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    supportedOUI (`vim.option.ChoiceOption`_):

       The valid Organizational Unique Identifiers (OUIs) supported by this virtual Ethernet card.Supported OUIs for statically assigned MAC addresses:"00:50:56"
    macType (`vim.option.ChoiceOption`_):

       The supported MAC address types.
    wakeOnLanEnabled (`vim.option.BoolOption`_):

       Flag to indicate whether or not wake-on-LAN is settable on this device.
    vmDirectPathGen2Supported (`bool`_):

       Flag to indicate whether VMDirectPath Gen 2 is available on this device.
