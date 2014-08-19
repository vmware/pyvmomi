
vim.host.ScsiTopology.Lun
=========================
  This data object type describes the SCSI logical unit.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the SCSI Lun
    lun (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The logical unit number of the SCSI logical unit.
    scsiLun (`vim.host.ScsiLun <vim/host/ScsiLun.rst>`_):

       The link to data for this SCSI logical unit.
