.. _VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vim.fault.ReplicationVmFault: ../../../vim/fault/ReplicationVmFault.rst

.. _vim.fault.ReplicationVmFault.ReasonForFault: ../../../vim/fault/ReplicationVmFault/ReasonForFault.rst

vim.fault.ReplicationVmFault.ReasonForFault
===========================================
  :contained by: `vim.fault.ReplicationVmFault`_

  :type: `vim.fault.ReplicationVmFault.ReasonForFault`_

  :name: invalidInstanceId

values:
--------

invalidInstanceId
   The specified instanceId does not match the `VirtualMachine`_ instanceId

notConfigured
    `VirtualMachine`_ is not configured for replication

poweredOn
    `VirtualMachine`_ is powered on

poweredOff
    `VirtualMachine`_ is powered off (and is not undergoing offline replication)

offlineReplicating
    `VirtualMachine`_ is in the process of creating an an offline instance.

suspended
    `VirtualMachine`_ is suspended (and is not undergoing offline replication)

invalidState
    `VirtualMachine`_ is in an invalid state
