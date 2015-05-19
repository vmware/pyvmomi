.. _VirtualMachine: ../../../vim/VirtualMachine.rst

.. _vim.HbrManager.ReplicationVmInfo: ../../../vim/HbrManager/ReplicationVmInfo.rst

.. _vim.HbrManager.ReplicationVmInfo.State: ../../../vim/HbrManager/ReplicationVmInfo/State.rst

vim.HbrManager.ReplicationVmInfo.State
======================================
  Describes the current state of a replicated `VirtualMachine`_ 
  :contained by: `vim.HbrManager.ReplicationVmInfo`_

  :type: `vim.HbrManager.ReplicationVmInfo.State`_

  :name: error

values:
--------

none
   The `VirtualMachine`_ has no current replication state. This is a virtual machine that is configured for replication, but is powered off and not undergoing offline replication.

syncing
   One or more of the `VirtualMachine`_ disks is in the process of an initial synchronization with the remote site.

paused
   The `VirtualMachine`_ replication is paused.

idle
   The `VirtualMachine`_ is being replicated but is not currently in the process of having a consistent instance created.

error
   The `VirtualMachine`_ is unable to replicate due to errors.XXX Currently unused.

active
   The `VirtualMachine`_ is in the process of having a consistent instance created.
