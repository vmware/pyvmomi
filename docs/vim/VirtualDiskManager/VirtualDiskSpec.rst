.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _VirtualDiskType: ../../vim/VirtualDiskManager/VirtualDiskType.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _VirtualDiskAdapterType: ../../vim/VirtualDiskManager/VirtualDiskAdapterType.rst


vim.VirtualDiskManager.VirtualDiskSpec
======================================
  Specification used to create or clone a virtual disk
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    diskType (`str`_):

       The type of the new virtual disk.See `VirtualDiskType`_ 
    adapterType (`str`_):

       The type of the virtual disk adapter for the new virtual disk.See `VirtualDiskAdapterType`_ 
