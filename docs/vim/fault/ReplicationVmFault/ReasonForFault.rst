vim.fault.ReplicationVmFault.ReasonForFault
===========================================
  :contained by: `vim.fault.ReplicationVmFault <vim/fault/ReplicationVmFault.rst>`_

  :type: `vim.fault.ReplicationVmFault.ReasonForFault <vim/fault/ReplicationVmFault/ReasonForFault.rst>`_

  :name: invalidInstanceId

values:
--------

invalidInstanceId
   The specified instanceId does not match the `VirtualMachine <vim/VirtualMachine.rst>`_ instanceId

notConfigured
    `VirtualMachine <vim/VirtualMachine.rst>`_ is not configured for replication

poweredOn
    `VirtualMachine <vim/VirtualMachine.rst>`_ is powered on

poweredOff
    `VirtualMachine <vim/VirtualMachine.rst>`_ is powered off (and is not undergoing offline replication)

offlineReplicating
    `VirtualMachine <vim/VirtualMachine.rst>`_ is in the process of creating an an offline instance.

suspended
    `VirtualMachine <vim/VirtualMachine.rst>`_ is suspended (and is not undergoing offline replication)

invalidState
    `VirtualMachine <vim/VirtualMachine.rst>`_ is in an invalid state
