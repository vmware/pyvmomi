
vim.vm.UsbInfo
==============
  This data object contains information about a physical USB device on the host.
:extends: vim.vm.TargetInfo_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A user visible name of the USB device.
    vendor (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The vendor ID of the USB device.
    product (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The product ID of the USB device.
    physicalPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       An autoconnect pattern which describes the device's physical path. This is the path to the specific port on the host where the USB device is attached.
    family ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The device class families. For possible values see `VirtualMachineUsbInfoFamily <vim/vm/UsbInfo/Family.rst>`_ 
    speed ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The possible device speeds detected by server. For possible values see `VirtualMachineUsbInfoSpeed <vim/vm/UsbInfo/Speed.rst>`_ 
    summary (`vim.vm.Summary <vim/vm/Summary.rst>`_, optional):

       Summary information about the virtual machine that is currently using this device, if any.
