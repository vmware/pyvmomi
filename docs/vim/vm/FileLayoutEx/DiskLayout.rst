
vim.vm.FileLayoutEx.DiskLayout
==============================
  Layout of a virtual disk, including the base- and delta- disks.A virtual disk typically is made up of a chain of disk-units.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifier for the virtual disk in `device <vim/vm/VirtualHardware.rst#device>`_ .
    chain ([`vim.vm.FileLayoutEx.DiskUnit <vim/vm/FileLayoutEx/DiskUnit.rst>`_], optional):

       The disk-unit chain that makes up this virtual disk.
