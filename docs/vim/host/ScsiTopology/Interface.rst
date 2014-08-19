
vim.host.ScsiTopology.Interface
===============================
  This data object type describes the SCSI interface that is associated with a list of targets.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the SCSI interface
    adapter (`vim.host.HostBusAdapter <vim/host/HostBusAdapter.rst>`_):

       The link to data for this SCSI interface.
    target ([`vim.host.ScsiTopology.Target <vim/host/ScsiTopology/Target.rst>`_], optional):

       The list of targets to which the SCSI interface is associated.
