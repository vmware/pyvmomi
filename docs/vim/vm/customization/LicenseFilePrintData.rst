.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _Windows 2000 Unattended Setup Guide: http://www.microsoft.com/technet/prodtechnol/Windows2000Pro/deploy/unattend/default.mspx

.. _vim.vm.customization.LicenseFilePrintData.AutoMode: ../../../vim/vm/customization/LicenseFilePrintData/AutoMode.rst


vim.vm.customization.LicenseFilePrintData
=========================================
  The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in thesysprep.infanswer file. These values are transferred into thesysprep.inffile that VirtualCenter stores on the target virtual disk. For more detailed information, see the document `Windows 2000 Unattended Setup Guide`_ .LicenseFilePrintData provides licensing information for Windows server operating systems.
:extends: vmodl.DynamicData_

Attributes:
    autoMode (`vim.vm.customization.LicenseFilePrintData.AutoMode`_):

       Server licensing mode
    autoUsers (`int`_, optional):

       This key is valid only if AutoMode = PerServer. The integer value indicates the number of client licenses purchased for the VirtualCenter server being installed.
