.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DVSRollbackCapability: ../../vim/DistributedVirtualSwitch/RollbackCapability.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst


vim.DistributedVirtualSwitch.RollbackCapability
===============================================
  The `DVSRollbackCapability`_ data object describes the rollback capabilities for a `DistributedVirtualSwitch`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    rollbackSupported (`bool`_):

       Indicates whether rollback is supported on the distributed switch.
