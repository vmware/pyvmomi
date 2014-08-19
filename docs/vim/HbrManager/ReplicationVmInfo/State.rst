vim.HbrManager.ReplicationVmInfo.State
======================================
  Describes the current state of a replicated `VirtualMachine <vim/VirtualMachine.rst>`_ 
  :contained by: `vim.HbrManager.ReplicationVmInfo <vim/HbrManager/ReplicationVmInfo.rst>`_

  :type: `vim.HbrManager.ReplicationVmInfo.State <vim/HbrManager/ReplicationVmInfo/State.rst>`_

  :name: error

values:
--------

none
   The `VirtualMachine <vim/VirtualMachine.rst>`_ has no current replication state. This is a virtual machine that is configured for replication, but is powered off and not undergoing offline replication.

syncing
   One or more of the `VirtualMachine <vim/VirtualMachine.rst>`_ disks is in the process of an initial synchronization with the remote site.

paused
   The `VirtualMachine <vim/VirtualMachine.rst>`_ replication is paused.

idle
   The `VirtualMachine <vim/VirtualMachine.rst>`_ is being replicated but is not currently in the process of having a consistent instance created.

error
   The `VirtualMachine <vim/VirtualMachine.rst>`_ is unable to replicate due to errors.XXX Currently unused.

active
   The `VirtualMachine <vim/VirtualMachine.rst>`_ is in the process of having a consistent instance created.
