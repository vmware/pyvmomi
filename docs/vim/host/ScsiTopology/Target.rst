
vim.host.ScsiTopology.Target
============================
  This data object type describes the SCSI target that is associated with a list of logical units.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the SCSI target
    target (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The target identifier.
    lun ([`vim.host.ScsiTopology.Lun <vim/host/ScsiTopology/Lun.rst>`_], optional):

       The list of SCSI logical units with which a target is associated.
    transport (`vim.host.TargetTransport <vim/host/TargetTransport.rst>`_, optional):

       SCSI Transport information about the target.
