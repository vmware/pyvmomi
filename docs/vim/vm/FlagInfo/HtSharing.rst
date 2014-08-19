vim.vm.FlagInfo.HtSharing
=========================
  Set of possible values for `htSharing <vim/vm/FlagInfo.rst#htSharing>`_ .
  :contained by: `vim.vm.FlagInfo <vim/vm/FlagInfo.rst>`_

  :type: `vim.vm.FlagInfo.HtSharing <vim/vm/FlagInfo/HtSharing.rst>`_

  :name: internal

values:
--------

none
   VCPUs should not share cores with each other or with VCPUs from other virtual machines. That is, each VCPU from this virtual machine should always get a whole core to itself, with the other logical CPU on that core being placed into the "halted" state.

internal
   Similar to "none", in that VCPUs from this virtual machine will not be allowed to share cores with VCPUs from other virtual machines. However, other VCPUs from the same virtual machine will be allowed to share cores together. This configuration option is only permitted for SMP virtual machines. If applied to a uniprocessor virtual machine, it will be converted to the "none" sharing option.

any
   VCPUs may freely share cores at any time with any other VCPUs (default for all virtual machines on a hyperthreaded system).
