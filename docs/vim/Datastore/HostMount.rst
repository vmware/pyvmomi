
vim.Datastore.HostMount
=======================
  Host-specific datastore information.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.HostSystem <vim/HostSystem.rst>`_):

       The host associated with this datastore.
    mountInfo (`vim.host.MountInfo <vim/host/MountInfo.rst>`_):

       Host-specific information about the mount.
