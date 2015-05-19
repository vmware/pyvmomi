.. _userInput: ../../vim/profile/host/AnswerFile.rst#userInput

.. _AnswerFile: ../../vim/profile/host/AnswerFile.rst

.. _HostProfile: ../../vim/profile/host/HostProfile.rst

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _requireInput: ../../vim/profile/host/ExecuteResult.rst#requireInput

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostProfileManager: ../../vim/profile/host/ProfileManager.rst

.. _ExecuteHostProfile: ../../vim/profile/host/HostProfile.rst#execute

.. _ApplyHostConfig_Task: ../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _ProfileExecuteResult: ../../vim/profile/host/ExecuteResult.rst

.. _vim.profile.ProfilePropertyPath: ../../vim/profile/ProfilePropertyPath.rst

.. _ProfileDeferredPolicyOptionParameter: ../../vim/profile/DeferredPolicyOptionParameter.rst


vim.profile.DeferredPolicyOptionParameter
=========================================
  The `ProfileDeferredPolicyOptionParameter`_ data object contains information about a single deferred parameter for host configuration.
   * The Server verifies deferred parameter data when it calls the
   * `HostProfile`_
   * .
   * `ExecuteHostProfile`_
   * method.
   * The client supplies deferred parameter data for host configuration when it calls the
   * `HostProfileManager`_
   * .
   * `ApplyHostConfig_Task`_
   * method.
   * The vCenter Server stores deferred parameter data in answer files (
   * `AnswerFile`_
   * .
   * `userInput`_
   * ).
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    inputPath (`vim.profile.ProfilePropertyPath`_):

       Complete path to the `PolicyOption`_ that defines the parameters.
    parameter ([`vmodl.KeyAnyValue`_], optional):

       List that contains values for the policy parameters.During parameter verification, this property is unspecified if the client has not provided the values for this parameter. See `ProfileExecuteResult`_ . `requireInput`_ .
