
vim.fault.ProfileUpdateFailed.UpdateFailure
===========================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    profilePath (`vim.profile.ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_):

       Location in the profile which has the error
    errMsg (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):

       Message which explains the problem encountered
