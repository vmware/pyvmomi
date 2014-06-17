.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.TargetTransport: ../../../vim/host/TargetTransport.rst

.. _vim.host.ScsiTopology.Lun: ../../../vim/host/ScsiTopology/Lun.rst


vim.host.ScsiTopology.Target
============================
  This data object type describes the SCSI target that is associated with a list of logical units.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       The identifier for the SCSI target
    target (`int`_):

       The target identifier.
    lun (`vim.host.ScsiTopology.Lun`_, optional):

       The list of SCSI logical units with which a target is associated.
    transport (`vim.host.TargetTransport`_, optional):

       SCSI Transport information about the target.
