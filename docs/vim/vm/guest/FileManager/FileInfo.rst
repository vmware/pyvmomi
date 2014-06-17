.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _GuestFileType: ../../../../vim/vm/guest/FileManager/FileInfo/FileType.rst

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.vm.guest.FileManager.FileAttributes: ../../../../vim/vm/guest/FileManager/FileAttributes.rst


vim.vm.guest.FileManager.FileInfo
=================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    path (`str`_):

       The complete path to the file
    type (`str`_):

       The file type, one of `GuestFileType`_ 
    size (`long`_):

       The file size in bytes
    attributes (`vim.vm.guest.FileManager.FileAttributes`_):

       Different attributes of a file.
