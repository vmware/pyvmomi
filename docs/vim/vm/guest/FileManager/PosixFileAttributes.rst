.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _GuestPosixFileAttributes: ../../../../vim/vm/guest/FileManager/PosixFileAttributes.rst

.. _InitiateFileTransferToGuest: ../../../../vim/vm/guest/FileManager.rst#initiateFileTransferToGuest

.. _vim.vm.guest.FileManager.FileAttributes: ../../../../vim/vm/guest/FileManager/FileAttributes.rst


vim.vm.guest.FileManager.PosixFileAttributes
============================================
  Different attributes for Posix guest file.
:extends: vim.vm.guest.FileManager.FileAttributes_
:since: `vSphere API 5.0`_

Attributes:
    ownerId (`int`_, optional):

       The owner ID. If this property is not specified when passing a `GuestPosixFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the default value will be the owner Id of the user who invoked the file transfer operation.
    groupId (`int`_, optional):

       The group ID. If this property is not specified when passing a `GuestPosixFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the default value will be the group Id of the user who invoked the file transfer operation.
    permissions (`long`_, optional):

       The file permissions in chmod(2) format. If this property is not specified when passing a `GuestPosixFileAttributes`_ object to `InitiateFileTransferToGuest`_ , the file will be created with 0644 permissions.
