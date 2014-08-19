
vim.vm.device.VirtualSCSIControllerOption
=========================================
  The VirtualSCSIControllerOption data object type contains the options for a virtual SCSI controller defined by the `VirtualSCSIController <vim/vm/device/VirtualSCSIController.rst>`_ data object type.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    numSCSIDisks (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       Three properties (numSCSIDisks.min, numSCSIDisks.max, and numSCSIDisks.defaultValue) define the minimum, maximum, and default number of SCSI VirtualDisk instances available at any given time in the SCSI controller. The number of SCSI VirtualDisk instances is also limited by the number of available slots in the SCSI controller.
    numSCSICdroms (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       Three properties (numSCSICdroms.min, numSCSICdroms.max, and numSCSICdroms.defaultValue) define the minimum, maximum, and default number of SCSI VirtualCdrom instances available in the SCSI controller. The number of SCSI VirtualCdrom instances is also limited by the number of available slots in the SCSI controller.
    numSCSIPassthrough (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       Three properties (numSCSIPassthrough.min, numSCSIPassthrough.max, and numSCSIPassthrough.defaultValue) define the minimum, maximum, and default number of VirtualSCSIPassthrough instances available have at any given time in the SCSI controller. The number of VirtualSCSIPassthrough instances is also limited by the number of available slots in the SCSI controller.
    sharing ([`vim.vm.device.VirtualSCSIController.Sharing <vim/vm/device/VirtualSCSIController/Sharing.rst>`_]):

       Supported shared bus modes.
    defaultSharedIndex (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Index into sharing array specifying the default value.
    hotAddRemove (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       All SCSI controllers support hot adding and removing of devices. This support can't be toggled in the current implementation. Therefore, this option is ignored when reconfiguring a SCSI controller and is always set to "true" when reading an existing configuration.
    scsiCtlrUnitNumber (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The unit number of the SCSI controller. The SCSI controller sits on its own bus, so that this field defines which slot the controller will use.
