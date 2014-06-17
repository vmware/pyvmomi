.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.customization.NameGenerator: ../../../vim/vm/customization/NameGenerator.rst

.. _Windows 2000 Unattended Setup Guide: http://www.microsoft.com/technet/prodtechnol/Windows2000Pro/deploy/unattend/default.mspx


vim.vm.customization.UserData
=============================
  Personal data pertaining to the owner of the virtual machine.The UserData data object type maps to the UserData key in thesysprep.infanswer file. These values are transferred directly into thesysprep.inffile that VirtualCenter stores on the target virtual disk. For more detailed information, see the document `Windows 2000 Unattended Setup Guide`_ .
:extends: vmodl.DynamicData_

Attributes:
    fullName (`str`_):

       User's full name.
    orgName (`str`_):

       User's organization.
    computerName (`vim.vm.customization.NameGenerator`_):

       The computer name of the (Windows) virtual machine. Computer name may contain letters (A-Z), numbers(0-9) and hyphens (-) but no spaces or periods (.). The name may not consists entirely of digits. On Vista computer name is restricted to 15 characters in length. If the computer name is longer than 15 characters, it will be truncated to 15 characters.
    productId (`str`_):

       Microsoft Sysprep requires that a valid serial number be included in the answer file when mini-setup runs. This serial number is ignored if the original guest operating system was installed using a volume-licensed CD.
