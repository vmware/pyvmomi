.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore.Info: ../../vim/Datastore/Info.rst

.. _vim.host.VmfsVolume: ../../vim/host/VmfsVolume.rst


vim.host.VmfsDatastoreInfo
==========================
  Information details about a VMFS datastore.
:extends: vim.Datastore.Info_

Attributes:
    maxPhysicalRDMFileSize (`long`_):

       Maximum raw device mapping size (physical compatibility)
    maxVirtualRDMFileSize (`long`_):

       Maximum raw device mapping size (virtual compatibility)
    vmfs (`vim.host.VmfsVolume`_, optional):

       The VMFS volume information for the datastore. May not be available when the datastore is not accessible.
