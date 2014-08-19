vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo.State
======================================================
  Define the instance state type
  :contained by: `vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo <vim/host/RuntimeInfo/NetStackInstanceRuntimeInfo.rst>`_

  :type: `vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo.State <vim/host/RuntimeInfo/NetStackInstanceRuntimeInfo/State.rst>`_

  :name: activating

values:
--------

active
   The instance is running

inactive
   The instance is deleted or not running

activating
   Reserved state for future proofing asynchronous creation

deactivating
   The instance is in the progress of asynchronous deletion
