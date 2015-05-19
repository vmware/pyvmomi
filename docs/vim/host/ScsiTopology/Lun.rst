.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.ScsiLun: ../../../vim/host/ScsiLun.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.ScsiTopology.Lun
=========================
  This data object type describes the SCSI logical unit.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       The identifier for the SCSI Lun
    lun (`int`_):

       The logical unit number of the SCSI logical unit.
    scsiLun (`vim.host.ScsiLun`_):

       The link to data for this SCSI logical unit.
