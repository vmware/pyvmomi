.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DatastoreBrowser.FileInfo: ../../../vim/host/DatastoreBrowser/FileInfo.rst


vim.host.DatastoreBrowser.SearchResults
=======================================
  This data object type contains the results of a search method for one datastore. A search method typically returns a set of these objects as an array.
:extends: vmodl.DynamicData_

Attributes:
    datastore (`vim.Datastore`_, optional):

       Datastore contains the results.
    folderPath (`str`_, optional):

       Relative path to the top-level folder.
    file (`vim.host.DatastoreBrowser.FileInfo`_, optional):

       Set of matching files, if any.
