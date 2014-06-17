.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../../../vmodl/LocalizableMessage.rst

.. _vim.profile.ProfilePropertyPath: ../../../../vim/profile/ProfilePropertyPath.rst


vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError
=============================================================
  The AnswerFileStatusError data object describes an answer file error and identifies the profile or policy option with which the error is associated.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    userInputPath (`vim.profile.ProfilePropertyPath`_):

       Path to a profile or a policy option for host-specific data.
    errMsg (`vmodl.LocalizableMessage`_):

       Message describing the error.
