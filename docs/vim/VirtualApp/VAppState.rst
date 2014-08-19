vim.VirtualApp.VAppState
========================
  The VAppState type defines the set of states a vApp can be in. The transitory states between started and stopped is modeled explicitly, since the starting or stopping of a vApp is typically a time-consuming process that might take minutes to complete.
  :contained by: `vim.VirtualApp <vim/VirtualApp.rst>`_

  :type: `vim.VirtualApp.VAppState <vim/VirtualApp/VAppState.rst>`_

  :name: stopping

values:
--------

started
   The vApp is currently powered on .

starting
   The vApp is in the process of starting.

stopped
   The vApp is currently powered off or suspended.

stopping
   The vApp is in the process of stopping.
