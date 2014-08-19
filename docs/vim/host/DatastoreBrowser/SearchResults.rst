
vim.host.DatastoreBrowser.SearchResults
=======================================
  This data object type contains the results of a search method for one datastore. A search method typically returns a set of these objects as an array.
:extends: vmodl.DynamicData_

Attributes:
    datastore (`vim.Datastore <vim/Datastore.rst>`_, optional):

       Datastore contains the results.
    folderPath (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Relative path to the top-level folder.
    file ([`vim.host.DatastoreBrowser.FileInfo <vim/host/DatastoreBrowser/FileInfo.rst>`_], optional):

       Set of matching files, if any.
