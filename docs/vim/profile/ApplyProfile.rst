
vim.profile.ApplyProfile
========================
  The `ApplyProfile <vim/profile/ApplyProfile.rst>`_ data object is the base class for all data objects that define profile configuration data.ApplyProfiledefines ESX configuration data storage and it supports recursive profile definition for the profile plug-in architecture.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the profile is enabled.
    policy ([`vim.profile.Policy <vim/profile/Policy.rst>`_], optional):

       The list of policies comprising the profile. A `ProfilePolicy <vim/profile/Policy.rst>`_ stores one or more configuration data values in a `PolicyOption <vim/profile/PolicyOption.rst>`_ . The policy option is one of the configuration options from the `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ . `possibleOption <vim/profile/PolicyMetadata.rst#possibleOption>`_ list.
    profileTypeName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Identifies the profile type.
    profileVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Profile engine version.
    property ([`vim.profile.ApplyProfileProperty <vim/profile/ApplyProfileProperty.rst>`_], optional):

       List of subprofiles for this profile. This list can change depending on which profile plug-ins are available in the system. Subprofiles can be nested to arbitrary depths to represent host capabilities.
