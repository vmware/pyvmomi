
vim.OvfManager.FileItem
=======================
  An FileItem represents a file that must be uploaded by the caller when the inventory objects has been created in VI. These objects are created by `ResourcePool.importVApp <vim/ResourcePool.rst#importVApp>`_ .Files can either be new files, in which case the "create" flag will be true, or updates to existing files in VI. The latter is used to support the OVF parentRef mechanism for Disks.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    deviceId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Uniquely identifies the device (disk, CD-ROM etc.) within the entity hierarchy.When `ResourcePool.importVApp <vim/ResourcePool.rst#importVApp>`_ is called to create the `VirtualMachine <vim/VirtualMachine.rst>`_ s and `VirtualApp <vim/VirtualApp.rst>`_ s, it returns a map, device ID -> URL, of where to upload the backing files.
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The path of the item to upload, relative to the path of the OVF descriptor.
    compressionMethod (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The compression method as specified by the OVF specification (for example "gzip" or "bzip2").
    chunkSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The chunksize as specified by the OVF specification. If this attribute is set, the "path" attribute is a prefix to each chunk of the complete file. For example, if chunksize is 2000000000 bytes, the actual files might be: myfile.000000000 (2000000000 bytes) myfile.000000001 (2000000000 bytes) myfile.000000002 (1500000000 bytes)
    size (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The complete size of the file, if it is specified in the OVF descriptor.
    cimType (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The CIM type of the device for which this file provides backing.For example, the value 17 means "Disk drive".
    create (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the item is not expected to exist in the infrastructure and should therefore be created by the caller (for example using HTTP PUT).
