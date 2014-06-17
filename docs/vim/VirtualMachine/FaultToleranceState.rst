.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.VirtualMachine.FaultToleranceState: ../../vim/VirtualMachine/FaultToleranceState.rst

vim.VirtualMachine.FaultToleranceState
======================================
  The FaultToleranceState type defines a simple set of states for a fault tolerant virtual machine: disabled, starting, and enabled.
  :contained by: `vim.VirtualMachine`_

  :type: `vim.VirtualMachine.FaultToleranceState`_

  :name: running

values:
--------

notConfigured
   This state indicates that the virtual machine has not been configured for fault tolerance.

needSecondary
   For a virtual machine that is the primary in a fault tolerant group, this state indicates that the virtual machine is powered on and has at least one enabled secondary, but no secondary is currenly active. This state is not valid for a virtual machine that is a secondary in a fault tolerant group.

enabled
   For a virtual machine that is the primary in a fault tolerant group, this state indicates that the virtual machine is not currently powered on, but has at least one enabled secondary For a virtual machine that is the secondary in a fault tolerant group, this state indicates that the secondary is enabled, but is not currently powered on.

disabled
   For a virtual machine that is the primary in a fault tolerant group, this state indicates that the virtual machine has at least one registered secondary, but no secondary is enabled. For a virtual machine that is the secondary in a fault tolerant group, this state indicates that the secondary is disabled.

running
   This state indicates that the virtual machine is running with fault tolerance protection.

starting
   For a virtual machine that is the primary in a fault tolerant group, this state indicates that the virtual machine is powered on and has at least one secondary that is synchronizing its state with the primary. For a virtual machine that is the secondary in a fault tolerant group, this state indicates that the secondary is powered on and is synchronizing its state with the primary virtual machine.
