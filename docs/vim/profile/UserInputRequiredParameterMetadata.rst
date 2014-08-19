
vim.profile.UserInputRequiredParameterMetadata
==============================================
  The `UserInputRequiredParameterMetadata <vim/profile/UserInputRequiredParameterMetadata.rst>`_ data object represents policy option metadata information for configuration data. The Profile Engine saves configuration data from the user input options in the host `AnswerFile <vim/profile/host/AnswerFile.rst>`_ . See the `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ and `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_ methods.
:extends: vim.profile.PolicyOptionMetadata_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    userInputParameter ([`vim.profile.ParameterMetadata <vim/profile/ParameterMetadata.rst>`_], optional):

       Metadata for user input options.
