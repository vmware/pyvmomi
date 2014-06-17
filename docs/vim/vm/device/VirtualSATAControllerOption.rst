.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vim.option.IntOption: ../../../vim/option/IntOption.rst

.. _VirtualSATAController: ../../../vim/vm/device/VirtualSATAController.rst

.. _vim.vm.device.VirtualControllerOption: ../../../vim/vm/device/VirtualControllerOption.rst


vim.vm.device.VirtualSATAControllerOption
=========================================
  The VirtualSATAControllerOption data object type contains the options for a virtual SATA controller defined by the `VirtualSATAController`_ data object type.
:extends: vim.vm.device.VirtualControllerOption_
:since: `vSphere API 5.5`_

Attributes:
    numSATADisks (`vim.option.IntOption`_):

       Three properties (numSATADisks.min, numSATADisks.max, and numSATADisks.defaultValue) define the minimum, maximum, and default number of SATA VirtualDisk instances available at any given time in the SATA controller. The number of SATA VirtualDisk instances is also limited by the number of available slots in the SATA controller.
    numSATACdroms (`vim.option.IntOption`_):

       Three properties (numSATACdroms.min, numSATACdroms.max, and numSATACdroms.defaultValue) define the minimum, maximum, and default number of SATA VirtualCdrom instances available in the SATA controller. The number of SATA VirtualCdrom instances is also limited by the number of available slots in the SATA controller.
