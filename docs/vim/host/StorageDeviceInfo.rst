.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ScsiTopology: ../../vim/host/ScsiTopology.rst

.. _vim.host.ScsiLun: ../../vim/host/ScsiLun.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.ScsiTopology: ../../vim/host/ScsiTopology.rst

.. _vim.host.MultipathInfo: ../../vim/host/MultipathInfo.rst

.. _vim.host.HostBusAdapter: ../../vim/host/HostBusAdapter.rst

.. _vim.host.PlugStoreTopology: ../../vim/host/PlugStoreTopology.rst


vim.host.StorageDeviceInfo
==========================
  This data object type describes the storage subsystem configuration.
:extends: vmodl.DynamicData_

Attributes:
    hostBusAdapter (`vim.host.HostBusAdapter`_, optional):

       The list of host bus adapters available on the host.
    scsiLun (`vim.host.ScsiLun`_, optional):

       The list of SCSI logical units available on the host.
    scsiTopology (`vim.host.ScsiTopology`_, optional):

       Storage topology view of SCSI storage devices. This data object exists only if storage topology information is available. See the `ScsiTopology`_ data object type for more information.
    multipathInfo (`vim.host.MultipathInfo`_, optional):

       The multipath configuration that controls multipath policy for ScsiLuns. This data object exists only if path information is available and is configurable.
    plugStoreTopology (`vim.host.PlugStoreTopology`_, optional):

       The plug-store topology on the host system. This data object exists only if the plug-store system is available and configurable.
    softwareInternetScsiEnabled (`bool`_):

       Indicates if the software iSCSI initiator is enabled on this system
