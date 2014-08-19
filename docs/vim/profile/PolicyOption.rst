
vim.profile.PolicyOption
========================
  The `PolicyOption <vim/profile/PolicyOption.rst>`_ data object represents one or more configuration values. A policy option is one of the configuration options from the `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ . `possibleOption <vim/profile/PolicyMetadata.rst#possibleOption>`_ list.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifier for the policy option. This value matches one of the keys from the list of possible options in the policy metadata ( `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ . `possibleOption <vim/profile/PolicyMetadata.rst#possibleOption>`_ []. `id <vim/profile/PolicyOptionMetadata.rst#id>`_ . `key <vim/ElementDescription.rst#key>`_ ).
    parameter ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       Parameters for the policy option. This list must include all parameters that are not marked as optional in the policy option metadata parameter list ( `ProfilePolicyMetadata <vim/profile/PolicyMetadata.rst>`_ . `possibleOption <vim/profile/PolicyMetadata.rst#possibleOption>`_ []. `parameter <vim/profile/PolicyOptionMetadata.rst#parameter>`_ []. `optional <vim/profile/ParameterMetadata.rst#optional>`_ ).
