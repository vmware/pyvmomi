.. _str: https://docs.python.org/2/library/stdtypes.html

.. _inputPath: ../../../vim/profile/DeferredPolicyOptionParameter.rst#inputPath

.. _parameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst#parameter

.. _AnswerFile: ../../../vim/profile/host/AnswerFile.rst

.. _HostProfile: ../../../vim/profile/host/HostProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _inapplicablePath: ../../../vim/profile/host/ExecuteResult.rst#inapplicablePath

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostProfileManager: ../../../vim/profile/host/ProfileManager.rst

.. _ExecuteHostProfile: ../../../vim/profile/host/HostProfile.rst#execute

.. _vim.host.ConfigSpec: ../../../vim/host/ConfigSpec.rst

.. _ApplyHostConfig_Task: ../../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _ProfileExecuteResult: ../../../vim/profile/host/ExecuteResult.rst

.. _ProfileExecuteResultStatus: ../../../vim/profile/host/ExecuteResult/Status.rst

.. _ProfileDeferredPolicyOptionParameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst

.. _vim.profile.DeferredPolicyOptionParameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst

.. _vim.profile.host.ExecuteResult.ExecuteError: ../../../vim/profile/host/ExecuteResult/ExecuteError.rst


vim.profile.host.ExecuteResult
==============================
  The `ProfileExecuteResult`_ data object contains the results from a `HostProfile`_ . `ExecuteHostProfile`_ operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    status (`str`_):

       Status of the profile execution operation. The value is a string that contains one of the `ProfileExecuteResultStatus`_ enumerations.
    configSpec (`vim.host.ConfigSpec`_, optional):

       Host configuration specification. This data is valid only if thestatusvalue issuccess. See `ProfileExecuteResultStatus`_ .Use this data object when you apply the configuration to a host. See theconfigSpecparameter to the `HostProfileManager`_ . `ApplyHostConfig_Task`_ method.
    inapplicablePath (`str`_, optional):

       List of property paths. Each path identifies a policy that does not apply to this host. For example, if the precheck policies for a port group are not satisfied, the port group will not be created when you apply the profile to the host. Based on this information, the client might not display that part of the profile tree.
    requireInput (`vim.profile.DeferredPolicyOptionParameter`_, optional):

       List that describes the required input for host configuration and identifies any policy options that still require parameter data. Each entry in the list specifies the path to a policy and a parameter list. If the call to `ExecuteHostProfile`_ includes deferred parameters, therequireInputentries (requireInput[]. `parameter`_ []) will be populated with the parameter data that was passed to the execute method. For policies that still require input data, the parameter list in the corresponding entry will be null.A vSphere client that displays a GUI can use this information to show the host-specific configuration policy options. The client can highlight required input fields and ask the user for data in increments instead of collecting all of the input at once. For example, in the first pass, the client collects a minimum of user input and sends that to the Server. The Server evaluates the profile and might decide to invalidate a particular part of the subtree or enable a new subtree in the profile. This would result in a new set of invalid paths ( `inapplicablePath`_ []) and required input property paths ( `ProfileDeferredPolicyOptionParameter`_ . `inputPath`_ ). The client can make a series of calls to the method until it achieves a success status.When `ExecuteHostProfile`_ returns a success status, therequireInputlist contains the complete list of parameters, consisting of the following data:
        * Deferred parameter values resolved through successive calls to
        * `ExecuteHostProfile`_
        * .
        * Default parameter values from the host configuration.
        * User-specified values that override the defaults.You can specify the returnedrequireInputlist in theuserInputparameter to the `HostProfileManager`_ . `ApplyHostConfig_Task`_ method. The Server will use the list to update the `AnswerFile`_ associated with the host.
    error (`vim.profile.host.ExecuteResult.ExecuteError`_, optional):

       List of errors that were encountered during execute. This field will be set if status is set to error.
