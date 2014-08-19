
vim.profile.host.HostProfile.CompleteConfigSpec
===============================================
  The `HostProfileCompleteConfigSpec <vim/profile/host/HostProfile/CompleteConfigSpec.rst>`_ data object specifies the complete configuration for a host profile.
:extends: vim.profile.host.HostProfile.ConfigSpec_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    applyProfile (`vim.profile.host.HostApplyProfile <vim/profile/host/HostApplyProfile.rst>`_, optional):

       Profile that contains configuration data for the host.
    customComplyProfile (`vim.profile.ComplianceProfile <vim/profile/ComplianceProfile.rst>`_, optional):

       User defined compliance profile. Reserved for future use.
    disabledExpressionListChanged (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating if this configuration specification contains changes in the `disabledExpressionList <vim/profile/host/HostProfile/CompleteConfigSpec.rst#disabledExpressionList>`_ . If False, the Profile Engine ignores the contents of the disabled expression list.
    disabledExpressionList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       List of expressions to be disabled. Each entry in the list specifies a `ProfileExpression <vim/profile/Expression.rst>`_ . `id <vim/profile/Expression.rst#id>`_ . All expressions are enabled by default.If you set `disabledExpressionListChanged <vim/profile/host/HostProfile/CompleteConfigSpec.rst#disabledExpressionListChanged>`_ to True, the Profile Engine uses the contents of this list to replace the contents of the `HostProfile <vim/profile/host/HostProfile.rst>`_ . `config <vim/profile/Profile.rst#config>`_ . `disabledExpressionList <vim/profile/host/HostProfile/ConfigInfo.rst#disabledExpressionList>`_ .The expression list is contained in the `defaultComplyProfile <vim/profile/host/HostProfile/ConfigInfo.rst#defaultComplyProfile>`_ . The Profile Engine automatically generates the default compliance profile when you create a host profile.
    validatorHost (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       Host for profile validation. This can be a host on which the profile is intended to be used. If you do not specify a validator host, the Profile Engine uses the `HostProfile <vim/profile/host/HostProfile.rst>`_ . `referenceHost <vim/profile/host/HostProfile.rst#referenceHost>`_ to validate the profile.
