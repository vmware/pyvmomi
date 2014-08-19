
vim.vm.LegacyNetworkSwitchInfo
==============================
  The LegacyNetworkSwitchInfo data object type contains information about the legacy network switches available on the host.
   * VMware Server - Options available for the "custom" NetworkBackingType.
   * ESX Server - The "esxnet" NetworkBackingType.
   * 
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the network switch.
