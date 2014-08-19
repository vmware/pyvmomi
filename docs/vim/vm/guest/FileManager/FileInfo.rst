
vim.vm.guest.FileManager.FileInfo
=================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The complete path to the file
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The file type, one of `GuestFileType <vim/vm/guest/FileManager/FileInfo/FileType.rst>`_ 
    size (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The file size in bytes
    attributes (`vim.vm.guest.FileManager.FileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_):

       Different attributes of a file.
