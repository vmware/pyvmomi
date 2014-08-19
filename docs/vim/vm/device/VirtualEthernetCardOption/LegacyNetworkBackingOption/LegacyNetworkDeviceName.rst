vim.vm.device.VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName
==========================================================================================
  Possible device names for legacy network backing option are listed below. Note: This is not an exhaustive list. It is possible to specify a specific device as well. For example, on ESX hosts, the device name could be specified as "vmnic[0-9]" or vmnet_[0-9]. For VMware Server Windows hosts, the device name could be specified as "vmnet[0-9]" and for VMware Server Linux hosts, the device name could be specified as "/dev/vmnet[0-9]" depending on what devices are available on that particular host.
  :contained by: `vim.vm.device.VirtualEthernetCardOption.LegacyNetworkBackingOption <vim/vm/device/VirtualEthernetCardOption/LegacyNetworkBackingOption.rst>`_

  :type: `vim.vm.device.VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName <vim/vm/device/VirtualEthernetCardOption/LegacyNetworkBackingOption/LegacyNetworkDeviceName.rst>`_

  :name: hostonly

values:
--------

hostonly
   hostonly

nat
   nat

bridged
   bridged
