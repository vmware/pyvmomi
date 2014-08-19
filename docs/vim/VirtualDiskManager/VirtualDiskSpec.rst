
vim.VirtualDiskManager.VirtualDiskSpec
======================================
  Specification used to create or clone a virtual disk
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    diskType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of the new virtual disk.See `VirtualDiskType <vim/VirtualDiskManager/VirtualDiskType.rst>`_ 
    adapterType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of the virtual disk adapter for the new virtual disk.See `VirtualDiskAdapterType <vim/VirtualDiskManager/VirtualDiskAdapterType.rst>`_ 
