.. _AnswerFile: ../../vim/profile/host/AnswerFile.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _ExecuteHostProfile: ../../vim/profile/host/HostProfile.rst#execute

.. _ApplyHostConfig_Task: ../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _vim.profile.ParameterMetadata: ../../vim/profile/ParameterMetadata.rst

.. _vim.profile.PolicyOptionMetadata: ../../vim/profile/PolicyOptionMetadata.rst

.. _UserInputRequiredParameterMetadata: ../../vim/profile/UserInputRequiredParameterMetadata.rst


vim.profile.UserInputRequiredParameterMetadata
==============================================
  The `UserInputRequiredParameterMetadata`_ data object represents policy option metadata information for configuration data. The Profile Engine saves configuration data from the user input options in the host `AnswerFile`_ . See the `ExecuteHostProfile`_ and `ApplyHostConfig_Task`_ methods.
:extends: vim.profile.PolicyOptionMetadata_
:since: `vSphere API 4.0`_

Attributes:
    userInputParameter ([`vim.profile.ParameterMetadata`_], optional):

       Metadata for user input options.
