vim.vm.device.VirtualDiskOption.DiskMode
========================================
  The list of known disk modes.The list of supported disk modes varies by the backing type. The "persistent" mode is supported by every backing type.
  :contained by: `vim.vm.device.VirtualDiskOption <vim/vm/device/VirtualDiskOption.rst>`_

  :type: `vim.vm.device.VirtualDiskOption.DiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_

  :name: append

values:
--------

independent_persistent
   Same as persistent, but not affected by snapshots.

persistent
   Changes are immediately and permanently written to the virtual disk.

independent_nonpersistent
   Same as nonpersistent, but not affected by snapshots.

undoable
   Changes are made to a redo log, but you are given the option to commit or undo.

nonpersistent
   Changes to virtual disk are made to a redo log and discarded at power off.

append
   Changes are appended to the redo log; you revoke changes by removing the undo log.
