
vim.profile.ProfileMetadata.ProfileSortSpec
===========================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    policyId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The id of the policy used to sort instances of the profile
    parameter (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The parameter to be used for sorting. Note that if the policy to be used for sorting has multiple possible policy options, all possible policy options defined for that policy type must have this parameter.
