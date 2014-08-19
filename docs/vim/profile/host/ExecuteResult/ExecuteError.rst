
vim.profile.host.ExecuteResult.ExecuteError
===========================================
  The `ProfileExecuteError <vim/profile/host/ExecuteResult/ExecuteError.rst>`_ data object describes an error encountered during host profile execution.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    path (`vim.profile.ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_, optional):

       Path to the profile or policy with which the error is associated.
    message (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):

       Message describing the error.
