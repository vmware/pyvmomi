
vim.profile.Profile.CreateSpec
==============================
  Specification describing the parameters during Profile creation
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the profile
    annotation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       User Provided description of the profile
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating if the Profile is enabled
