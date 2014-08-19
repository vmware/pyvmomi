vim.VirtualMachine.MovePriority
===============================
  MovePriority is an enumeration of values that indicate the priority of the task that moves a virtual machine from one host to another or one storage location to another. Note this priority can affect both the source and target hosts.
  :contained by: `vim.VirtualMachine <vim/VirtualMachine.rst>`_

  :type: `vim.VirtualMachine.MovePriority <vim/VirtualMachine/MovePriority.rst>`_

  :name: defaultPriority

values:
--------

highPriority
   The task of moving this virtual machine is high priority.

lowPriority
   The task of moving this virtual machine is low priority.

defaultPriority
   The task of moving this virtual machine is the default priority.
