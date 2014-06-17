.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../../vmodl/LocalizableMessage.rst

.. _vim.profile.ProfilePropertyPath: ../../../vim/profile/ProfilePropertyPath.rst


vim.fault.ProfileUpdateFailed.UpdateFailure
===========================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    profilePath (`vim.profile.ProfilePropertyPath`_):

       Location in the profile which has the error
    errMsg (`vmodl.LocalizableMessage`_):

       Message which explains the problem encountered
