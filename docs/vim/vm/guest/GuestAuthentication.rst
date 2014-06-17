.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.guest.GuestAuthentication
================================
  GuestAuthentication is an abstract base class for authentication in the guest.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    interactiveSession (`bool`_):

       This is set to true if the client wants an interactive session in the guest.
