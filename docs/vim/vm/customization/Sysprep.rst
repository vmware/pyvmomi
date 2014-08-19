
vim.vm.customization.Sysprep
============================
  An object representation of a Windowssysprep.infanswer file. The sysprep type encloses all the individual keys listed in asysprep.inffile. For more detailed information, see the document `Windows 2000 Unattended Setup Guide <http://www.microsoft.com/technet/prodtechnol/Windows2000Pro/deploy/unattend/default.mspx>`_ .
:extends: vim.vm.customization.IdentitySettings_

Attributes:
    guiUnattended (`vim.vm.customization.GuiUnattended <vim/vm/customization/GuiUnattended.rst>`_):

       An object representation of the sysprep GuiUnattended key.
    userData (`vim.vm.customization.UserData <vim/vm/customization/UserData.rst>`_):

       An object representation of the sysprep UserData key.
    guiRunOnce (`vim.vm.customization.GuiRunOnce <vim/vm/customization/GuiRunOnce.rst>`_, optional):

       An object representation of the sysprep GuiRunOnce key.
    identification (`vim.vm.customization.Identification <vim/vm/customization/Identification.rst>`_):

       An object representation of the sysprep Identification key.
    licenseFilePrintData (`vim.vm.customization.LicenseFilePrintData <vim/vm/customization/LicenseFilePrintData.rst>`_, optional):

       An object representation of the sysprep LicenseFilePrintData key. Required only for Windows 2000 Server and Windows Server 2003.
