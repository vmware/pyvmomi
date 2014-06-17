.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.host.DatastoreBrowser.FileInfo.Details
==========================================
  The FileInfo.Details data object type is a set of flags for a search request. This search request specifies which details to return for each matching file. This data object type is here to ensure that there is one flag corresponding to each FileInfo property other than the path name, which a search always returns.
:extends: vmodl.DynamicData_

Attributes:
    fileType (`bool`_):

       The flag to indicate whether or not the files that match this query specification are returned along with file type information. This field must be set to return specific details about the file type.
    fileSize (`bool`_):

       The flag to indicate whether or not the size of the file is returned.
    modification (`bool`_):

       The flag to indicate whether or not to return the date and time the file was last modified.
    fileOwner (`bool`_):

       The flag to indicate whether or not to return the file owner.
