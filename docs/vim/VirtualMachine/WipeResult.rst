
vim.VirtualMachine.WipeResult
=============================
  Data structure used by wipeDisk to return the amount of disk space that can be saved on an Flex-SE disk if a subsequent shrinkDisk API is invoked on that disk.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    diskId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The disk id for the disk that was wiped.
    shrinkableDiskSpace (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The amount of shrinkable disk space in kB.
