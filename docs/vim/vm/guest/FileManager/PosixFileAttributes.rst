
vim.vm.guest.FileManager.PosixFileAttributes
============================================
  Different attributes for Posix guest file.
:extends: vim.vm.guest.FileManager.FileAttributes_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    ownerId (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The owner ID. If this property is not specified when passing a `GuestPosixFileAttributes <vim/vm/guest/FileManager/PosixFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the default value will be the owner Id of the user who invoked the file transfer operation.
    groupId (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The group ID. If this property is not specified when passing a `GuestPosixFileAttributes <vim/vm/guest/FileManager/PosixFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the default value will be the group Id of the user who invoked the file transfer operation.
    permissions (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The file permissions in chmod(2) format. If this property is not specified when passing a `GuestPosixFileAttributes <vim/vm/guest/FileManager/PosixFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the file will be created with 0644 permissions.
