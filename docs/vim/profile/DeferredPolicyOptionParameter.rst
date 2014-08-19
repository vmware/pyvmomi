
vim.profile.DeferredPolicyOptionParameter
=========================================
  The `ProfileDeferredPolicyOptionParameter <vim/profile/DeferredPolicyOptionParameter.rst>`_ data object contains information about a single deferred parameter for host configuration.
   * The Server verifies deferred parameter data when it calls the
   * `HostProfile <vim/profile/host/HostProfile.rst>`_
   * .
   * `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_
   * method.
   * The client supplies deferred parameter data for host configuration when it calls the
   * `HostProfileManager <vim/profile/host/ProfileManager.rst>`_
   * .
   * `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_
   * method.
   * The vCenter Server stores deferred parameter data in answer files (
   * `AnswerFile <vim/profile/host/AnswerFile.rst>`_
   * .
   * `userInput <vim/profile/host/AnswerFile.rst#userInput>`_
   * ).
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    inputPath (`vim.profile.ProfilePropertyPath <vim/profile/ProfilePropertyPath.rst>`_):

       Complete path to the `PolicyOption <vim/profile/PolicyOption.rst>`_ that defines the parameters.
    parameter ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       List that contains values for the policy parameters.During parameter verification, this property is unspecified if the client has not provided the values for this parameter. See `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ . `requireInput <vim/profile/host/ExecuteResult.rst#requireInput>`_ .
