
vim.host.DatastoreBrowser.FileInfo
==================================
  This data object type contains rudimentary information about a file in a datastore. The information here is not meant to cover all information in traditional file systems, but rather to provide sufficient information for files that are associated with virtual machines. Derived types describe the known file types for a datastore.
:extends: vmodl.DynamicData_

Attributes:
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The path relative to the folder path in the search results.
    fileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The size of the file in bytes.
    modification (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The last date and time the file was modified.
    owner (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user name of the owner of the file.
