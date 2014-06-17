.. _str: https://docs.python.org/2/library/stdtypes.html

.. _AutoLogon: ../../../vim/vm/customization/GuiUnattended.rst#autoLogon

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _Windows 2000 Unattended Setup Guide: http://www.microsoft.com/technet/prodtechnol/Windows2000Pro/deploy/unattend/default.mspx


vim.vm.customization.GuiRunOnce
===============================
  The commands listed in the GuiRunOnce data object type are executed when a user logs on the first time after customization completes. The logon may be driven by the `AutoLogon`_ setting.The GuiRunOnce data object type maps to the GuiRunOnce key in thesysprep.infanswer file. These values are transferred into thesysprep.inffile that VirtualCenter stores on the target virtual disk. For more detailed information, see the document `Windows 2000 Unattended Setup Guide`_ .
:extends: vmodl.DynamicData_

Attributes:
    commandList (`str`_):

       A list of commands to run at first user logon, after guest customization.
