.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _userInput: ../../../vim/profile/host/AnswerFile.rst#userInput

.. _AnswerFile: ../../../vim/profile/host/AnswerFile.rst

.. _HostProfile: ../../../vim/profile/host/HostProfile.rst

.. _requireInput: ../../../vim/profile/host/ExecuteResult.rst#requireInput

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostProfileManager: ../../../vim/profile/host/ProfileManager.rst

.. _ExecuteHostProfile: ../../../vim/profile/host/HostProfile.rst#execute

.. _ApplyHostConfig_Task: ../../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _ProfileExecuteResult: ../../../vim/profile/host/ExecuteResult.rst

.. _UpdateAnswerFile_Task: ../../../vim/profile/host/ProfileManager.rst#updateAnswerFile

.. _vim.profile.DeferredPolicyOptionParameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst


vim.profile.host.AnswerFile
===========================
  The `AnswerFile`_ data object contains host-specific information that a host will use in combination with a `HostProfile`_ for configuration. Answer files are stored on the vCenter Server, along with host profiles. An answer file is always associated with a particular host.To supply host-specific data:
   * Specify deferred parameters when you call the
   * `HostProfile`_
   * .
   * `ExecuteHostProfile`_
   * method. The host profile engine will verify the set of parameters for the additional configuration data.
   * Use the complete required input list (
   * `ProfileExecuteResult`_
   * .
   * `requireInput`_
   * []) as user input for the
   * `HostProfileManager`_
   * .
   * `ApplyHostConfig_Task`_
   * method. When you apply the profile, the vCenter Server saves the additional configuration data in the
   * `userInput`_
   * list.
   * Use the
   * `HostProfileManager`_
   * .
   * `UpdateAnswerFile_Task`_
   * method. This method will update an existing answer file or create a new one.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    userInput ([`vim.profile.DeferredPolicyOptionParameter`_], optional):

       List containing host-specific configuration data.
    createdTime (`datetime`_):

       Time at which the answer file was created.
    modifiedTime (`datetime`_):

       Time at which the answer file was last modified.
