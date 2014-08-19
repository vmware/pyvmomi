
vim.vm.guest.GuestAuthentication
================================
  GuestAuthentication is an abstract base class for authentication in the guest.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    interactiveSession (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       This is set to true if the client wants an interactive session in the guest.
