.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../../vmodl/LocalizableMessage.rst

.. _vim.profile.ProfilePropertyPath: ../../../vim/profile/ProfilePropertyPath.rst


vim.fault.AnswerFileUpdateFailed.UpdateFailure
==============================================
  DataObject which represents the errors that occurred when an answer file update was performed.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    userInputPath (`vim.profile.ProfilePropertyPath`_):

       The user input that has the error
    errMsg (`vmodl.LocalizableMessage`_):

       Message which explains the error
