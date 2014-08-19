
vim.profile.PolicyMetadata
==========================
  The `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ data object represents the metadata information for a `ProfilePolicy <vim/profile/Policy.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`vim.ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_):

       Identifier for the policy.
    possibleOption ([`vim.profile.PolicyOptionMetadata <vim/profile/PolicyOptionMetadata.rst>`_]):

       Possible policy options that can be set for a policy of the given kind. `HostProfile <vim/profile/host/HostProfile.rst>`_ s and subprofiles will contain selected policy options from this list. See `PolicyOption <vim/profile/PolicyOption.rst>`_ .
