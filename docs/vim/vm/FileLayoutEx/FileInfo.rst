.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VirtualMachineFileLayoutExFileType: ../../../vim/vm/FileLayoutEx/FileType.rst


vim.vm.FileLayoutEx.FileInfo
============================
  Basic information about a file.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`int`_):

       Key to reference this file.
    name (`str`_):

       Name of the file, including the complete datastore path.
    type (`str`_):

       Type of the file. `VirtualMachineFileLayoutExFileType`_ lists all valid values.
    size (`long`_):

       Size of the file in bytes.
    uniqueSize (`long`_, optional):

       Size of the file in bytes corresponding to the file blocks that were allocated uniquely. In other words, if the underlying storage supports sharing of file blocks across disk files, the property corresponds to the size of the file blocks that were allocated only in context of this file, i.e. it does not include shared blocks that were allocated in other files. This property will be unset if the underlying implementation is unable to compute this information. One example of this is when the file resides on a NAS datastore whose underlying storage doesn't support this metric. In some cases the field might be set but the value could be over-estimated due to the inability of the NAS based storage to provide an accurate value.
