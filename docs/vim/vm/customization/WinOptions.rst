.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.customization.Options: ../../../vim/vm/customization/Options.rst

.. _vim.vm.customization.WinOptions.SysprepRebootOption: ../../../vim/vm/customization/WinOptions/SysprepRebootOption.rst


vim.vm.customization.WinOptions
===============================
  Optional operations supported by the customization process for Windows.
:extends: vim.vm.customization.Options_

Attributes:
    changeSID (`bool`_):

       The customization process should modify the machine's security identifier (SID). For Vista OS, SID will always be modified.
    deleteAccounts (`bool`_):

       If deleteAccounts is true, then all user accounts are removed from the system as part of the customization. Mini-setup creates a new Administrator account with a blank password.
    reboot (`vim.vm.customization.WinOptions.SysprepRebootOption`_, optional):

       A value of type SysprepRebootOption specifying the action that should be taken after running sysprep. Defaults to "reboot".
