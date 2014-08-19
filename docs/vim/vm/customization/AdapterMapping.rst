
vim.vm.customization.AdapterMapping
===================================
  Data object type to associate a virtual network adapter with its IP settings.
:extends: vmodl.DynamicData_

Attributes:
    macAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The MAC address of a network adapter being customized. The client cannot change this value because the guest operating system has no control over the MAC address of a virtual network adapter.This property is optional. If it is not included, the customization process maps the settings from the list of AdapterMappings.IPSettings in the Specification.nicSettingMap to the virtual machine's network adapters, in PCI slot order. The first virtual network adapter on the PCI bus is assigned nicSettingMap[0].IPSettings, the second adapter is assigned nicSettingMap[1].IPSettings, and so on.
    adapter (`vim.vm.customization.IPSettings <vim/vm/customization/IPSettings.rst>`_):

       The IP settings for the associated virtual network adapter.
