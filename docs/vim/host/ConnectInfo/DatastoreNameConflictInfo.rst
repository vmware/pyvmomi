.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.ConnectInfo.DatastoreInfo: ../../../vim/host/ConnectInfo/DatastoreInfo.rst


vim.host.ConnectInfo.DatastoreNameConflictInfo
==============================================
  This data object type describes a datastore on the host that has the same name as a different datastore on VirtualCenter.
:extends: vim.host.ConnectInfo.DatastoreInfo_

Attributes:
    newDatastoreName (`str`_):

       To resolve a conflict with existing datastores, a suggested new name of the datastore can be provided.
