.. _int: https://docs.python.org/2/library/stdtypes.html

.. _file: ../../../vim/vm/FileLayoutEx.rst#file

.. _type: ../../../vim/vm/FileLayoutEx/FileInfo.rst#type

.. _diskDescriptor: ../../../vim/vm/FileLayoutEx/FileType.rst#diskDescriptor

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.FileLayoutEx.DiskUnit
============================
  Information about a single unit of a virtual disk, such as the base-disk or a delta-disk.A disk-unit consists of at least one descriptor file, and zero or more extent files.Sometimes, a disk-unit is also referred to as abacking.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    fileKey ([`int`_]):

       Array of keys of the files that make up the disk unit. Values here correspond to property `key`_ in `file`_ .At least one entry always exists in this array. Property `type`_ of the referenced file can be used to distinguish the disk descriptor (type `diskDescriptor`_ ) from the extents.
