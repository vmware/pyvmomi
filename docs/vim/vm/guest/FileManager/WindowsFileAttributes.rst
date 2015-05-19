.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _ListFilesInGuest: ../../../../vim/vm/guest/FileManager.rst#listFiles

.. _GuestWindowsFileAttributes: ../../../../vim/vm/guest/FileManager/WindowsFileAttributes.rst

.. _ChangeFileAttributesInGuest: ../../../../vim/vm/guest/FileManager.rst#changeFileAttributes

.. _InitiateFileTransferToGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferToGuest

.. _InitiateFileTransferFromGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferFromGuest

.. _vim.vm.guest.FileManager.FileAttributes: ../../../../vim/vm/guest/FileManager/FileAttributes.rst


vim.vm.guest.FileManager.WindowsFileAttributes
==============================================
  Different attributes for a Windows guest file.
:extends: vim.vm.guest.FileManager.FileAttributes_
:since: `vSphere API 5.0`_

Attributes:
    hidden (`bool`_, optional):

       The file is hidden. If this property is not specified when passing a `GuestWindowsFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the file will not be set as a hidden file.
    readOnly (`bool`_, optional):

       The file is read-only. If this property is not specified when passing a `GuestWindowsFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the file will not be set as a read-only file.
    createTime (`datetime`_, optional):

       The date and time the file was created. This property gives information about files when returned from `ListFilesInGuest`_ or `InitiateFileTransferFromGuest`_ as part of a `GuestWindowsFileAttributes`_ object. This property will be ignored when passing a `GuestWindowsFileAttributes`_ object to `InitiateFileTransferToGuest`_ or `ChangeFileAttributesInGuest`_ .
