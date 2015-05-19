.. _int: https://docs.python.org/2/library/stdtypes.html

.. _GuestFileInfo: ../../../../vim/vm/guest/FileManager/FileInfo.rst

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.vm.guest.FileManager.FileInfo: ../../../../vim/vm/guest/FileManager/FileInfo.rst


vim.vm.guest.FileManager.ListFileInfo
=====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    files ([`vim.vm.guest.FileManager.FileInfo`_], optional):

       A list of `GuestFileInfo`_ data objects containing information for all the matching files.
    remaining (`int`_):

       The number of files left to be returned. If non-zero, then the next set of files can be returned by calling ListFiles again with the index set to the number of results already returned.
