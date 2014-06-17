.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.TargetInfo
=================
  The TargetInfo specified a value that can be used in the device backings to connect the virtual machine to a physical (or logical) host device.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       The identification of the endpoint on the host. The format of this depends on the kind of virtual device this endpoints is used for. For example, for a VirtualEthernetCard this would be a networkname, and for a VirtualCDROM it would be a device name.
    configurationTag (`str`_, optional):

       List of configurations that this device is available for. This is only filled out if more than one configuration is requested.
