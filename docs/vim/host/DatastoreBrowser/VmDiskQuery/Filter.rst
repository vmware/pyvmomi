.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDisk: ../../../../vim/vm/device/VirtualDisk.rst

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _VirtualIDEController: ../../../../vim/vm/device/VirtualIDEController.rst

.. _VirtualSCSIController: ../../../../vim/vm/device/VirtualSCSIController.rst


vim.host.DatastoreBrowser.VmDiskQuery.Filter
============================================
  The filter for the virtual disk primary file.
:extends: vmodl.DynamicData_

Attributes:
    diskType (`str`_, optional):

       If this optional property is set, only the virtual disk primary files that match one of the specified disk types are selected. If no disk types are specified, this search criteria is ignored.The specified disk type is one of the backing information types for a virtual disk.See `VirtualDisk`_ 
    matchHardwareVersion (`int`_, optional):

       If this optional property is set, only virtual disk primary files that match one of the specified hardware versions are selected. If no versions are specified, this search criteria is ignored.
    controllerType (`str`_, optional):

       If this optional property is set, only virtual disk files that have a controller type that matches one of the controller types specified are returned. If no controller types are specified, this search criteria is ignored.The specified controller type is one of the controller types for a virtual disk.See `VirtualIDEController`_ See `VirtualSCSIController`_ 
    thin (`bool`_, optional):

       This optional property can be used to filter disks based on whether they are thin-provsioned or not: if set to true, only thin-provisioned disks are returned, and vice-versa.
