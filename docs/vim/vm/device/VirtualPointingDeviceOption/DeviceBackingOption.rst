.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _vim.vm.device.VirtualDeviceOption.DeviceBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/DeviceBackingOption.rst


vim.vm.device.VirtualPointingDeviceOption.DeviceBackingOption
=============================================================
  The DeviceBackingOption data object type represents the options for a pointing device backing a VirtualPointingDevice data object type.
:extends: vim.vm.device.VirtualDeviceOption.DeviceBackingOption_

Attributes:
    hostPointingDevice (`vim.option.ChoiceOption`_):

       This object defines the supported mouse types, including the default supported mouse type, with the following properties:
        * hostPointingDevices.value
        * : This array defines the supported mouse types.
        * hostPointingDevices.choiceDescription
        * : This array provides the descriptions for the supported mouse types defined by hostPointingDevices.value.
        * hostPointingDevices.defaultIndex
        * : This integer points to an index in the hostPointingDevices.value array. This is the mouse type supported by default.
        * 
