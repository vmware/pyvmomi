.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _Sharing: ../../../vim/vm/device/VirtualSCSIController/Sharing.rst

.. _vim.vm.device.VirtualController: ../../../vim/vm/device/VirtualController.rst

.. _vim.vm.device.VirtualSCSIController.Sharing: ../../../vim/vm/device/VirtualSCSIController/Sharing.rst


vim.vm.device.VirtualSCSIController
===================================
  The VirtualSCSIController data object type represents a SCSI controller in a virtual machine.
:extends: vim.vm.device.VirtualController_

Attributes:
    hotAddRemove (`bool`_, optional):

       All SCSI controllers support hot adding and removing of devices. This support can't be toggled in the current implementation. Therefore, this option is ignored when reconfiguring a SCSI controller and is always set to "true" when reading an existing configuration.
    sharedBus (`vim.vm.device.VirtualSCSIController.Sharing`_):

       Mode for sharing the SCSI bus. The modes are physicalSharing, virtualSharing, and noSharing. See the `Sharing`_ data object type for an explanation of these modes.
    scsiCtlrUnitNumber (`int`_, optional):

       The unit number of the SCSI controller. The SCSI controller sits on its own bus, so this field defines which slot the controller is using.
