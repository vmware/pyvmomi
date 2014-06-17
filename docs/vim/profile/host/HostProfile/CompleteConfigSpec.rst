.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _config: ../../../../vim/profile/Profile.rst#config

.. _HostProfile: ../../../../vim/profile/host/HostProfile.rst

.. _referenceHost: ../../../../vim/profile/host/HostProfile.rst#referenceHost

.. _vim.HostSystem: ../../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _ProfileExpression: ../../../../vim/profile/Expression.rst

.. _defaultComplyProfile: ../../../../vim/profile/host/HostProfile/ConfigInfo.rst#defaultComplyProfile

.. _disabledExpressionList: ../../../../vim/profile/host/HostProfile/ConfigInfo.rst#disabledExpressionList

.. _disabledExpressionListChanged: ../../../../vim/profile/host/HostProfile/CompleteConfigSpec.rst#disabledExpressionListChanged

.. _HostProfileCompleteConfigSpec: ../../../../vim/profile/host/HostProfile/CompleteConfigSpec.rst

.. _vim.profile.ComplianceProfile: ../../../../vim/profile/ComplianceProfile.rst

.. _vim.profile.host.HostApplyProfile: ../../../../vim/profile/host/HostApplyProfile.rst

.. _vim.profile.host.HostProfile.ConfigSpec: ../../../../vim/profile/host/HostProfile/ConfigSpec.rst


vim.profile.host.HostProfile.CompleteConfigSpec
===============================================
  The `HostProfileCompleteConfigSpec`_ data object specifies the complete configuration for a host profile.
:extends: vim.profile.host.HostProfile.ConfigSpec_
:since: `vSphere API 4.0`_

Attributes:
    applyProfile (`vim.profile.host.HostApplyProfile`_, optional):

       Profile that contains configuration data for the host.
    customComplyProfile (`vim.profile.ComplianceProfile`_, optional):

       User defined compliance profile. Reserved for future use.
    disabledExpressionListChanged (`bool`_):

       Flag indicating if this configuration specification contains changes in the `disabledExpressionList`_ . If False, the Profile Engine ignores the contents of the disabled expression list.
    disabledExpressionList (`str`_, optional):

       List of expressions to be disabled. Each entry in the list specifies a `ProfileExpression`_ . `id`_ . All expressions are enabled by default.If you set `disabledExpressionListChanged`_ to True, the Profile Engine uses the contents of this list to replace the contents of the `HostProfile`_ . `config`_ . `disabledExpressionList`_ .The expression list is contained in the `defaultComplyProfile`_ . The Profile Engine automatically generates the default compliance profile when you create a host profile.
    validatorHost (`vim.HostSystem`_, optional):

       Host for profile validation. This can be a host on which the profile is intended to be used. If you do not specify a validator host, the Profile Engine uses the `HostProfile`_ . `referenceHost`_ to validate the profile.
