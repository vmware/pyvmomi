
vim.event.VmFaultToleranceStateChangedEvent
===========================================
  This event records a fault tolerance state change. A default alarm will be triggered upon this event, which would change the vm state: the vm state is red if the newState is needSecondary; the vm state is yellow if the newState is disabled; the vm state is green if the newState is notConfigured, starting, enabled or running
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    oldState (`vim.VirtualMachine.FaultToleranceState <vim/VirtualMachine/FaultToleranceState.rst>`_):

       The old fault toleeance state.
    newState (`vim.VirtualMachine.FaultToleranceState <vim/VirtualMachine/FaultToleranceState.rst>`_):

       The new fault tolerance state.
