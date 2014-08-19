vim.VirtualMachine.PowerState
=============================
  The PowerState type defines a simple set of states for a virtual machine: poweredOn, poweredOff, and suspended. This type does not model substates, such as when a task is running to change the virtual machine state. If the virtual machine is in a state with a task in progress, it transitions to a new state when the task completes. For example, a virtual machine continues to be in the poweredOn state while a suspend task is running, and changes to the suspended state once the task finishes.As a consequence of this approach, clients interested in monitoring the status of a virtual machine should typically track the `activeTask <vim/ManagedEntity.rst#recentTask>`_ data object in addition to the `powerState <vim/vm/RuntimeInfo.rst#powerState>`_ object.
  :contained by: `vim.VirtualMachine <vim/VirtualMachine.rst>`_

  :type: `vim.VirtualMachine.PowerState <vim/VirtualMachine/PowerState.rst>`_

  :name: suspended

values:
--------

poweredOn
   The virtual machine is currently powered on.

poweredOff
   The virtual machine is currently powered off.

suspended
   The virtual machine is currently suspended.
