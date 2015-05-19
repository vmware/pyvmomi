.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.HostBusAdapter: ../../../vim/host/HostBusAdapter.rst

.. _vim.host.ScsiTopology.Target: ../../../vim/host/ScsiTopology/Target.rst


vim.host.ScsiTopology.Interface
===============================
  This data object type describes the SCSI interface that is associated with a list of targets.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       The identifier for the SCSI interface
    adapter (`vim.host.HostBusAdapter`_):

       The link to data for this SCSI interface.
    target ([`vim.host.ScsiTopology.Target`_], optional):

       The list of targets to which the SCSI interface is associated.
