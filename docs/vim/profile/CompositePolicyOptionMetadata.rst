
vim.profile.CompositePolicyOptionMetadata
=========================================
  The `ProfileCompositePolicyOptionMetadata <vim/profile/CompositePolicyOptionMetadata.rst>`_ data object represents the metadata information for a composite `PolicyOption <vim/profile/PolicyOption.rst>`_ . The user will retrieve metadata information about a composite policy and then combine policy options to produce the composite policy option.
:extends: vim.profile.PolicyOptionMetadata_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    option ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of optional policy option identifiers that could be combined in this composite policy option. The policy options should already be part of the possible policy options for the policy. See the `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ . `possibleOption <vim/profile/PolicyMetadata.rst#possibleOption>`_ list.
