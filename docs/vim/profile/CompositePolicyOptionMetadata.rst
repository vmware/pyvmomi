.. _str: https://docs.python.org/2/library/stdtypes.html

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _possibleOption: ../../vim/profile/PolicyMetadata.rst#possibleOption

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _ProfilePolicyMetadata: ../../vim/profile/PolicyMetadata.rst

.. _vim.profile.PolicyOptionMetadata: ../../vim/profile/PolicyOptionMetadata.rst

.. _ProfileCompositePolicyOptionMetadata: ../../vim/profile/CompositePolicyOptionMetadata.rst


vim.profile.CompositePolicyOptionMetadata
=========================================
  The `ProfileCompositePolicyOptionMetadata`_ data object represents the metadata information for a composite `PolicyOption`_ . The user will retrieve metadata information about a composite policy and then combine policy options to produce the composite policy option.
:extends: vim.profile.PolicyOptionMetadata_
:since: `vSphere API 4.0`_

Attributes:
    option (`str`_):

       List of optional policy option identifiers that could be combined in this composite policy option. The policy options should already be part of the possible policy options for the policy. See the `ProfilePolicyMetadata`_ . `possibleOption`_ list.
