.. _vim.option.IntOption: ../../../vim/option/IntOption.rst

.. _vim.vm.device.VirtualControllerOption: ../../../vim/vm/device/VirtualControllerOption.rst


vim.vm.device.VirtualPCIControllerOption
========================================
  This data object type contains the options for a virtual PCI Controller.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    numSCSIControllers (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualSCSIController instances available at any given time in the PCI controller. The number of VirtualSCSIController instances is also limited by the number of available slots in the PCI controller.
    numEthernetCards (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualEthernetCard instances available, at any given time, in the PCI controller. The number of VirtualEthernetCard instances is also limited by the number of available slots in the PCI controller.
    numVideoCards (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualVideoCard instances available, at any given time, in the PCI controller. The number of VirtualVideoCard instances is also limited by the number of available slots in the PCI controller.
    numSoundCards (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualSoundCard instances available, at any given time, in the PCI controller. The number of VirtualSoundCard instances is also limited by the number of available slots in the PCI controller.
    numVmiRoms (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualVMIROM instances available, at any given time, in the PCI controller. This is also limited by the number of available slots in the PCI controller.
    numVmciDevices (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualVMCIDevice instances available, at any given time, in the PCI controller. This is also limited by the number of available slots in the PCI controller.
    numPCIPassthroughDevices (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualPCIPassthrough instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller.
    numSasSCSIControllers (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualLsiLogicSASController instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported SCSI controllers.
    numVmxnet3EthernetCards (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualVmxnet3 ethernet card instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported ethernet cards.
    numParaVirtualSCSIControllers (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of ParaVirtualScsiController instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported SCSI controllers.
    numSATAControllers (`vim.option.IntOption`_):

       Defines the minimum, maximum, and default number of VirtualSATAController instances available, at any given time, in the PCI controller. This is also limited by the number of available PCI Express slots in the PCI controller as well as the total number of supported SATA controllers.
