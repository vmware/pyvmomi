.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.GuestInfo.NamespaceGenerationInfo
========================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    key (`str`_):

       The namespace name as the unique key.
    generationNo (`int`_):

       Namespace generation number. Generation number is changed whenever there is new unread event pending from the guest to the VMODL.
