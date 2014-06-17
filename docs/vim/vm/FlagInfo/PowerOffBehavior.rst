.. _vim.vm.FlagInfo: ../../../vim/vm/FlagInfo.rst

.. _snapshotPowerOffBehavior: ../../../vim/vm/FlagInfo.rst#snapshotPowerOffBehavior

.. _vim.vm.FlagInfo.PowerOffBehavior: ../../../vim/vm/FlagInfo/PowerOffBehavior.rst

vim.vm.FlagInfo.PowerOffBehavior
================================
  Set of possible values for `snapshotPowerOffBehavior`_ .
  :contained by: `vim.vm.FlagInfo`_

  :type: `vim.vm.FlagInfo.PowerOffBehavior`_

  :name: prompt

values:
--------

prompt
   Prompt the user for instructions at power-off time.

powerOff
   Just power off the virtual machine.

revert
   Revert to the snapshot.
