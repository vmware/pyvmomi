.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.MountInfo: ../../vim/host/MountInfo.rst


vim.Datastore.HostMount
=======================
  Host-specific datastore information.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.HostSystem`_):

       The host associated with this datastore.
    mountInfo (`vim.host.MountInfo`_):

       Host-specific information about the mount.
