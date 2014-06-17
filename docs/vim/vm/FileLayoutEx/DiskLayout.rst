.. _int: https://docs.python.org/2/library/stdtypes.html

.. _device: ../../../vim/vm/VirtualHardware.rst#device

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.FileLayoutEx.DiskUnit: ../../../vim/vm/FileLayoutEx/DiskUnit.rst


vim.vm.FileLayoutEx.DiskLayout
==============================
  Layout of a virtual disk, including the base- and delta- disks.A virtual disk typically is made up of a chain of disk-units.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`int`_):

       Identifier for the virtual disk in `device`_ .
    chain (`vim.vm.FileLayoutEx.DiskUnit`_, optional):

       The disk-unit chain that makes up this virtual disk.
