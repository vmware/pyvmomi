
vim.VirtualDiskManager.DeviceBackedVirtualDiskSpec
==================================================
  Specification used to create a host device backed virtual disk
:extends: vim.VirtualDiskManager.VirtualDiskSpec_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The deviceName of the backing deviceSee `ScsiLun <vim/host/ScsiLun.rst>`_ 
