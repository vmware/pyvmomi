
vim.host.ConnectInfo.DatastoreExistsInfo
========================================
  This data object type describes a datastore on the host that matches an existing datastore on VirtualCenter that has a different name.
:extends: vim.host.ConnectInfo.DatastoreInfo_

Attributes:
    newDatastoreName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of a matching datastore on VirtualCenter. The datastore on the host will be renamed to this name.
