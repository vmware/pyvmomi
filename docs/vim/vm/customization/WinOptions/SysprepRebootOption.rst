vim.vm.customization.WinOptions.SysprepRebootOption
===================================================
  A enum constant specifying what should be done to the guest vm after running sysprep.
  :contained by: `vim.vm.customization.WinOptions <vim/vm/customization/WinOptions.rst>`_

  :type: `vim.vm.customization.WinOptions.SysprepRebootOption <vim/vm/customization/WinOptions/SysprepRebootOption.rst>`_

  :name: shutdown

values:
--------

shutdown
   Shutdown the machine after running sysprep. This puts the vm in a sealed state.

reboot
   Reboot the machine after running sysprep. This will cause values specified in the sysprep.inf to be applied immediately.

noreboot
   Take no action. Leave the guest os running after running sysprep. This option can be used to look at values for debugging purposes after running sysprep.
