.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _ListFilesInGuest: ../../../../vim/vm/guest/FileManager.rst#listFiles

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _GuestFileAttributes: ../../../../vim/vm/guest/FileManager/FileAttributes.rst

.. _GuestPosixFileAttributes: ../../../../vim/vm/guest/FileManager/PosixFileAttributes.rst

.. _GuestWindowsFileAttributes: ../../../../vim/vm/guest/FileManager/WindowsFileAttributes.rst

.. _ChangeFileAttributesInGuest: ../../../../vim/vm/guest/FileManager.rst#changeFileAttributes

.. _InitiateFileTransferToGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferToGuest

.. _InitiateFileTransferFromGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferFromGuest


vim.vm.guest.FileManager.FileAttributes
=======================================
  Different attributes for a guest file.
   * Check
   * `GuestPosixFileAttributes`_
   * for Posix guest files.
   * Check
   * `GuestWindowsFileAttributes`_
   * for Windows guest files.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    modificationTime (`datetime`_, optional):

       The date and time the file was last modified. If this property is not specified when passing a `GuestFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the default value will be the time when the file is created inside the guest.
    accessTime (`datetime`_, optional):

       The date and time the file was last accessed. If this property is not specified when passing a `GuestFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the default value will be the time when the file is created inside the guest.
    symlinkTarget (`str`_, optional):

       The target for the file if it's a symbolic link. This is currently only set for Linux guest operating systems, but may be supported in the future on Windows guest operating systems that support symbolic links. This property gives information about files when returned from `ListFilesInGuest`_ or `InitiateFileTransferFromGuest`_ as part of a `GuestFileAttributes`_ object. This property will be ignored when passing a `GuestFileAttributes`_ object to `InitiateFileTransferToGuest`_ or `ChangeFileAttributesInGuest`_ .
