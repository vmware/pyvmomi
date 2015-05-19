.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _VirtualDeviceConnectInfo: ../../../../vim/vm/device/VirtualDevice/ConnectInfo.rst

.. _VirtualDeviceConnectInfoStatus: ../../../../vim/vm/device/VirtualDevice/ConnectInfo/Status.rst


vim.vm.device.VirtualDevice.ConnectInfo
=======================================
  The `VirtualDeviceConnectInfo`_ data object type contains information about connectable virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    startConnected (`bool`_):

       Specifies whether or not to connect the device when the virtual machine starts.
    allowGuestControl (`bool`_):

       Enables guest control over whether the connectable device is connected.
    connected (`bool`_):

       Indicates whether the device is currently connected. Valid only while the virtual machine is running.
    status (`str`_, optional):

       Indicates the current status of the connectable device. Valid only while the virtual machine is running. The set of possible values is described in `VirtualDeviceConnectInfoStatus`_ 
