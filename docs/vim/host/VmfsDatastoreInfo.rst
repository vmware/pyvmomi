
vim.host.VmfsDatastoreInfo
==========================
  Information details about a VMFS datastore.
:extends: vim.Datastore.Info_

Attributes:
    maxPhysicalRDMFileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum raw device mapping size (physical compatibility)
    maxVirtualRDMFileSize (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum raw device mapping size (virtual compatibility)
    vmfs (`vim.host.VmfsVolume <vim/host/VmfsVolume.rst>`_, optional):

       The VMFS volume information for the datastore. May not be available when the datastore is not accessible.
