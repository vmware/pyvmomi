
vim.vm.guest.FileManager.FileAttributes
=======================================
  Different attributes for a guest file.
   * Check
   * `GuestPosixFileAttributes <vim/vm/guest/FileManager/PosixFileAttributes.rst>`_
   * for Posix guest files.
   * Check
   * `GuestWindowsFileAttributes <vim/vm/guest/FileManager/WindowsFileAttributes.rst>`_
   * for Windows guest files.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    modificationTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The date and time the file was last modified. If this property is not specified when passing a `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the default value will be the time when the file is created inside the guest.
    accessTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The date and time the file was last accessed. If this property is not specified when passing a `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the default value will be the time when the file is created inside the guest.
    symlinkTarget (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The target for the file if it's a symbolic link. This is currently only set for Linux guest operating systems, but may be supported in the future on Windows guest operating systems that support symbolic links. This property gives information about files when returned from `ListFilesInGuest <vim/vm/guest/FileManager.rst#listFiles>`_ or `InitiateFileTransferFromGuest <vim/vm/guest/FileManager.rst#initiateFileTransferFromGuest>`_ as part of a `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ object. This property will be ignored when passing a `GuestFileAttributes <vim/vm/guest/FileManager/FileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ or `ChangeFileAttributesInGuest <vim/vm/guest/FileManager.rst#changeFileAttributes>`_ .
