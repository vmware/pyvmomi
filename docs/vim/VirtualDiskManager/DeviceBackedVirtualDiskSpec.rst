.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ScsiLun: ../../vim/host/ScsiLun.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.VirtualDiskManager.VirtualDiskSpec: ../../vim/VirtualDiskManager/VirtualDiskSpec.rst


vim.VirtualDiskManager.DeviceBackedVirtualDiskSpec
==================================================
  Specification used to create a host device backed virtual disk
:extends: vim.VirtualDiskManager.VirtualDiskSpec_
:since: `VI API 2.5`_

Attributes:
    device (`str`_):

       The deviceName of the backing deviceSee `ScsiLun`_ 
