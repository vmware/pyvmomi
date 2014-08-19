
vim.profile.PolicyOptionMetadata
================================
  The `ProfilePolicyOptionMetadata <vim/profile/PolicyOptionMetadata.rst>`_ data object contains the metadata information for a `PolicyOption <vim/profile/PolicyOption.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`vim.ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_):

       Identifier for the policy option.
        * The
        * id.key
        * value (
        * `ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_
        * .
        * `key <vim/ElementDescription.rst#key>`_
        * ) identifies the policy option type.
        * The
        * id.label
        * property (
        * `ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_
        * .
        * `label <vim/Description.rst#label>`_
        * ) contains a brief localizable message describing the policy option.
        * The
        * id.summary
        * property (
        * `ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_
        * .
        * `summary <vim/Description.rst#summary>`_
        * ) contains a localizable summary of the policy option. Summary information can contain embedded variable names which can be replaced with values from the
        * parameter
        * property.
    parameter ([`vim.profile.ParameterMetadata <vim/profile/ParameterMetadata.rst>`_], optional):

       Metadata about the parameters for the policy option.
