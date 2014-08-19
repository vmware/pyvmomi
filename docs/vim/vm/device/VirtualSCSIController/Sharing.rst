vim.vm.device.VirtualSCSIController.Sharing
===========================================
  Sharing describes three possible ways of sharing the SCSI bus: One of these values is assigned to the sharedBus object to determine if or how the SCSI bus is shared.
  :contained by: `vim.vm.device.VirtualSCSIController <vim/vm/device/VirtualSCSIController.rst>`_

  :type: `vim.vm.device.VirtualSCSIController.Sharing <vim/vm/device/VirtualSCSIController/Sharing.rst>`_

  :name: physicalSharing

values:
--------

virtualSharing
   The virtual SCSI bus is shared between two or more virtual machines. In this case, no physical machine is involved.

noSharing
   The virtual SCSI bus is not shared.

physicalSharing
   The virtual SCSI bus is shared between two or more virtual machines residing on different physical hosts.
