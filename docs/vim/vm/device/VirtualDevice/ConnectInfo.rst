
vim.vm.device.VirtualDevice.ConnectInfo
=======================================
  The `VirtualDeviceConnectInfo <vim/vm/device/VirtualDevice/ConnectInfo.rst>`_ data object type contains information about connectable virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    startConnected (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Specifies whether or not to connect the device when the virtual machine starts.
    allowGuestControl (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Enables guest control over whether the connectable device is connected.
    connected (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the device is currently connected. Valid only while the virtual machine is running.
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the current status of the connectable device. Valid only while the virtual machine is running. The set of possible values is described in `VirtualDeviceConnectInfoStatus <vim/vm/device/VirtualDevice/ConnectInfo/Status.rst>`_ 
