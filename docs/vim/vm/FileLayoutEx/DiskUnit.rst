
vim.vm.FileLayoutEx.DiskUnit
============================
  Information about a single unit of a virtual disk, such as the base-disk or a delta-disk.A disk-unit consists of at least one descriptor file, and zero or more extent files.Sometimes, a disk-unit is also referred to as abacking.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    fileKey ([`int <https://docs.python.org/2/library/stdtypes.html>`_]):

       Array of keys of the files that make up the disk unit. Values here correspond to property `key <vim/vm/FileLayoutEx/FileInfo.rst#key>`_ in `file <vim/vm/FileLayoutEx.rst#file>`_ .At least one entry always exists in this array. Property `type <vim/vm/FileLayoutEx/FileInfo.rst#type>`_ of the referenced file can be used to distinguish the disk descriptor (type `diskDescriptor <vim/vm/FileLayoutEx/FileType.rst#diskDescriptor>`_ ) from the extents.
