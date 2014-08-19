
vim.profile.host.ExecuteResult
==============================
  The `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ data object contains the results from a `HostProfile <vim/profile/host/HostProfile.rst>`_ . `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Status of the profile execution operation. The value is a string that contains one of the `ProfileExecuteResultStatus <vim/profile/host/ExecuteResult/Status.rst>`_ enumerations.
    configSpec (`vim.host.ConfigSpec <vim/host/ConfigSpec.rst>`_, optional):

       Host configuration specification. This data is valid only if thestatusvalue issuccess. See `ProfileExecuteResultStatus <vim/profile/host/ExecuteResult/Status.rst>`_ .Use this data object when you apply the configuration to a host. See theconfigSpecparameter to the `HostProfileManager <vim/profile/host/ProfileManager.rst>`_ . `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_ method.
    inapplicablePath ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of property paths. Each path identifies a policy that does not apply to this host. For example, if the precheck policies for a port group are not satisfied, the port group will not be created when you apply the profile to the host. Based on this information, the client might not display that part of the profile tree.
    requireInput ([`vim.profile.DeferredPolicyOptionParameter <vim/profile/DeferredPolicyOptionParameter.rst>`_], optional):

       List that describes the required input for host configuration and identifies any policy options that still require parameter data. Each entry in the list specifies the path to a policy and a parameter list. If the call to `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ includes deferred parameters, therequireInputentries (requireInput[]. `parameter <vim/profile/DeferredPolicyOptionParameter.rst#parameter>`_ []) will be populated with the parameter data that was passed to the execute method. For policies that still require input data, the parameter list in the corresponding entry will be null.A vSphere client that displays a GUI can use this information to show the host-specific configuration policy options. The client can highlight required input fields and ask the user for data in increments instead of collecting all of the input at once. For example, in the first pass, the client collects a minimum of user input and sends that to the Server. The Server evaluates the profile and might decide to invalidate a particular part of the subtree or enable a new subtree in the profile. This would result in a new set of invalid paths ( `inapplicablePath <vim/profile/host/ExecuteResult.rst#inapplicablePath>`_ []) and required input property paths ( `ProfileDeferredPolicyOptionParameter <vim/profile/DeferredPolicyOptionParameter.rst>`_ . `inputPath <vim/profile/DeferredPolicyOptionParameter.rst#inputPath>`_ ). The client can make a series of calls to the method until it achieves a success status.When `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ returns a success status, therequireInputlist contains the complete list of parameters, consisting of the following data:
        * Deferred parameter values resolved through successive calls to
        * `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_
        * .
        * Default parameter values from the host configuration.
        * User-specified values that override the defaults.You can specify the returnedrequireInputlist in theuserInputparameter to the `HostProfileManager <vim/profile/host/ProfileManager.rst>`_ . `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_ method. The Server will use the list to update the `AnswerFile <vim/profile/host/AnswerFile.rst>`_ associated with the host.
    error ([`vim.profile.host.ExecuteResult.ExecuteError <vim/profile/host/ExecuteResult/ExecuteError.rst>`_], optional):

       List of errors that were encountered during execute. This field will be set if status is set to error.
