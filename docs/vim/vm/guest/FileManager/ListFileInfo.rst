
vim.vm.guest.FileManager.ListFileInfo
=====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    files ([`vim.vm.guest.FileManager.FileInfo <vim/vm/guest/FileManager/FileInfo.rst>`_], optional):

       A list of `GuestFileInfo <vim/vm/guest/FileManager/FileInfo.rst>`_ data objects containing information for all the matching files.
    remaining (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of files left to be returned. If non-zero, then the next set of files can be returned by calling ListFiles again with the index set to the number of results already returned.
