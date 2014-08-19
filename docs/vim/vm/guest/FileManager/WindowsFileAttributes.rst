
vim.vm.guest.FileManager.WindowsFileAttributes
==============================================
  Different attributes for a Windows guest file.
:extends: vim.vm.guest.FileManager.FileAttributes_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    hidden (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The file is hidden. If this property is not specified when passing a `GuestWindowsFileAttributes <vim/vm/guest/FileManager/WindowsFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the file will not be set as a hidden file.
    readOnly (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The file is read-only. If this property is not specified when passing a `GuestWindowsFileAttributes <vim/vm/guest/FileManager/WindowsFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ , the file will not be set as a read-only file.
    createTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The date and time the file was created. This property gives information about files when returned from `ListFilesInGuest <vim/vm/guest/FileManager.rst#listFiles>`_ or `InitiateFileTransferFromGuest <vim/vm/guest/FileManager.rst#initiateFileTransferFromGuest>`_ as part of a `GuestWindowsFileAttributes <vim/vm/guest/FileManager/WindowsFileAttributes.rst>`_ object. This property will be ignored when passing a `GuestWindowsFileAttributes <vim/vm/guest/FileManager/WindowsFileAttributes.rst>`_ object to `InitiateFileTransferToGuest <vim/vm/guest/FileManager.rst#initiateFileTransferToGuest>`_ or `ChangeFileAttributesInGuest <vim/vm/guest/FileManager.rst#changeFileAttributes>`_ .
