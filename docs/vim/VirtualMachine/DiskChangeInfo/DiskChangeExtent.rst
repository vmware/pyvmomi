
vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent
==================================================
  An area of the disk flagged as modified
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    start (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Start offset (in bytes) of modified area
    length (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Length (in bytes) of modified area
