
vim.VirtualMachine.DiskChangeInfo
=================================
  Data structure to describe areas in a disk associated with this VM that have been modified since a well-defined point in the past. Returned by `QueryChangedDiskAreas <vim/VirtualMachine.rst#queryChangedDiskAreas>`_ . This data structure describes a subset of the disk identified by startOffset and length. All areas that have been modified within this interval are listed under changedArea.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    startOffset (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Start offset (in bytes) of disk area described by this data structure.
    length (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Length (in bytes) of disk area described by this data structure.
    changedArea ([`vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent <vim/VirtualMachine/DiskChangeInfo/DiskChangeExtent.rst>`_], optional):

       Modified disk areas. Might be empty if no parts of the disk between startOffset and startOffset + length were modified.
