.. _vim.vm.FlagInfo: ../../../vim/vm/FlagInfo.rst

.. _virtualMmuUsage: ../../../vim/vm/FlagInfo.rst#virtualMmuUsage

.. _vim.vm.FlagInfo.VirtualMmuUsage: ../../../vim/vm/FlagInfo/VirtualMmuUsage.rst

vim.vm.FlagInfo.VirtualMmuUsage
===============================
  Set of possible values for `virtualMmuUsage`_ .
  :contained by: `vim.vm.FlagInfo`_

  :type: `vim.vm.FlagInfo.VirtualMmuUsage`_

  :name: off

values:
--------

on
   Use nested paging hardware support if the physical hardware supports it.

automatic
   Determine automatically whether to use nested page table hardware support.

off
   Do not use nested page table hardware support.
