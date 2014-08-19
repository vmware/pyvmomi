
vim.fault.AnswerFileUpdateFailed.UpdateFailure
==============================================
  DataObject which represents the errors that ocurred when an answer file update was performed.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    userInputPath (`vim.profile.ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_):

       The user input that has the error
    errMsg (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):

       Message which explains the error
