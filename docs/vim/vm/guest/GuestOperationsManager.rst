
vim.vm.guest.GuestOperationsManager
===================================
  GuestOperationsManager is the managed object that provides APIs to manipulate the guest operating system files and process. Each class of APIs is separated into its own manager.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------
    authManager (`vim.vm.guest.AuthManager <vim/vm/guest/AuthManager.rst>`_):
      privilege: System.Anonymous
       A singleton managed object that provides methods for guest authentication operations.
    fileManager (`vim.vm.guest.FileManager <vim/vm/guest/FileManager.rst>`_):
      privilege: System.Anonymous
       A singleton managed object that provides methods for guest file operations.
    processManager (`vim.vm.guest.ProcessManager <vim/vm/guest/ProcessManager.rst>`_):
      privilege: System.Anonymous
       A singleton managed object that provides methods for guest process operations.


Methods
-------


