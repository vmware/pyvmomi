.. _vim.host.NasVolume: ../../vim/host/NasVolume.rst

.. _vim.Datastore.Info: ../../vim/Datastore/Info.rst


vim.host.NasDatastoreInfo
=========================
  Information details about a network-attached storage (NAS) datastore.
:extends: vim.Datastore.Info_

Attributes:
    nas (`vim.host.NasVolume`_, optional):

       The NFS mount information for the datastore. May not be available when the datastore is not accessible.
