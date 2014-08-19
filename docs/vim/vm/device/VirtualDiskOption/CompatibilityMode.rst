vim.vm.device.VirtualDiskOption.CompatibilityMode
=================================================
  All known compatibility modes for raw disk mappings. Valid compatibility modes are:
   * virtualMode
   * physicalMode
   * 
  :contained by: `vim.vm.device.VirtualDiskOption <vim/vm/device/VirtualDiskOption.rst>`_

  :type: `vim.vm.device.VirtualDiskOption.CompatibilityMode <vim/vm/device/VirtualDiskOption/CompatibilityMode.rst>`_

  :name: physicalMode

values:
--------

physicalMode
   A disk device backed by a physical compatibility mode raw disk mapping cannot use disk modes, and commands are passed straight through to the LUN indicated by the raw disk mapping.

virtualMode
   A disk device backed by a virtual compatibility mode raw disk mapping can use disk modes.See `VirtualDiskMode <vim/vm/device/VirtualDiskOption/DiskMode.rst>`_ 
