.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.customization.Password: ../../../vim/vm/customization/Password.rst

.. _Windows 2000 Unattended Setup Guide: http://www.microsoft.com/technet/prodtechnol/Windows2000Pro/deploy/unattend/default.mspx


vim.vm.customization.Identification
===================================
  The Identification data object type provides information needed to join a workgroup or domain.The Identification data object type maps to the Identification key in thesysprep.infanswer file. These values are transferred into thesysprep.inffile that VirtualCenter stores on the target virtual disk. For more detailed information, see the document `Windows 2000 Unattended Setup Guide`_ .
:extends: vmodl.DynamicData_

Attributes:
    joinWorkgroup (`str`_, optional):

       The workgroup that the virtual machine should join. If this value is supplied, then the domain name and authentication fields must be empty.
    joinDomain (`str`_, optional):

       The domain that the virtual machine should join. If this value is supplied, then domainAdmin and domainAdminPassword must also be supplied, and the workgroup name must be empty.
    domainAdmin (`str`_, optional):

       This is the domain user account used for authentication if the virtual machine is joining a domain. The user does not need to be a domain administrator, but the account must have the privileges required to add computers to the domain.
    domainAdminPassword (`vim.vm.customization.Password`_, optional):

       This is the password for the domain user account used for authentication if the virtual machine is joining a domain.
