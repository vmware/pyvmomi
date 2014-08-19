
vim.profile.host.AnswerFile
===========================
  The `AnswerFile <vim/profile/host/AnswerFile.rst>`_ data object contains host-specific information that a host will use in combination with a `HostProfile <vim/profile/host/HostProfile.rst>`_ for configuration. Answer files are stored on the vCenter Server, along with host profiles. An answer file is always associated with a particular host.To supply host-specific data:
   * Specify deferred parameters when you call the
   * `HostProfile <vim/profile/host/HostProfile.rst>`_
   * .
   * `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_
   * method. The host profile engine will verify the set of parameters for the additional configuration data.
   * Use the complete required input list (
   * `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_
   * .
   * `requireInput <vim/profile/host/ExecuteResult.rst#requireInput>`_
   * []) as user input for the
   * `HostProfileManager <vim/profile/host/ProfileManager.rst>`_
   * .
   * `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_
   * method. When you apply the profile, the vCenter Server saves the additional configuration data in the
   * `userInput <vim/profile/host/AnswerFile.rst#userInput>`_
   * list.
   * Use the
   * `HostProfileManager <vim/profile/host/ProfileManager.rst>`_
   * .
   * `UpdateAnswerFile_Task <vim/profile/host/ProfileManager.rst#updateAnswerFile>`_
   * method. This method will update an existing answer file or create a new one.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    userInput ([`vim.profile.DeferredPolicyOptionParameter <vim/profile/DeferredPolicyOptionParameter.rst>`_], optional):

       List containing host-specific configuration data.
    createdTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time at which the answer file was created.
    modifiedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time at which the answer file was last modified.
