.. _vim.dvs.VmwareDistributedVirtualSwitch: ../../../vim/dvs/VmwareDistributedVirtualSwitch.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.PvlanPortType: ../../../vim/dvs/VmwareDistributedVirtualSwitch/PvlanPortType.rst

vim.dvs.VmwareDistributedVirtualSwitch.PvlanPortType
====================================================
  The PVLAN port types.
  :contained by: `vim.dvs.VmwareDistributedVirtualSwitch`_

  :type: `vim.dvs.VmwareDistributedVirtualSwitch.PvlanPortType`_

  :name: community

values:
--------

promiscuous
   The port can communicate with all other ports within the same PVLAN, including the isolated and community ports .

isolated
   The port can only communicate with the promiscuous ports within the same PVLAN, any other traffics are blocked.

community
   The ports communicates with other community ports and with promiscuous ports within the same PVLAN. any other traffics are blocked.
