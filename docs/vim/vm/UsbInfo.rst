.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.vm.Summary: ../../vim/vm/Summary.rst

.. _vim.vm.TargetInfo: ../../vim/vm/TargetInfo.rst

.. _VirtualMachineUsbInfoSpeed: ../../vim/vm/UsbInfo/Speed.rst

.. _VirtualMachineUsbInfoFamily: ../../vim/vm/UsbInfo/Family.rst


vim.vm.UsbInfo
==============
  This data object contains information about a physical USB device on the host.
:extends: vim.vm.TargetInfo_
:since: `VI API 2.5`_

Attributes:
    description (`str`_):

       A user visible name of the USB device.
    vendor (`int`_):

       The vendor ID of the USB device.
    product (`int`_):

       The product ID of the USB device.
    physicalPath (`str`_):

       An autoconnect pattern which describes the device's physical path. This is the path to the specific port on the host where the USB device is attached.
    family ([`str`_], optional):

       The device class families. For possible values see `VirtualMachineUsbInfoFamily`_ 
    speed ([`str`_], optional):

       The possible device speeds detected by server. For possible values see `VirtualMachineUsbInfoSpeed`_ 
    summary (`vim.vm.Summary`_, optional):

       Summary information about the virtual machine that is currently using this device, if any.
