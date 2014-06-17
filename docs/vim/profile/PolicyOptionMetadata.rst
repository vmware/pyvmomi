.. _label: ../../vim/Description.rst#label

.. _summary: ../../vim/Description.rst#summary

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ExtendedElementDescription: ../../vim/ExtendedElementDescription.rst

.. _ProfilePolicyOptionMetadata: ../../vim/profile/PolicyOptionMetadata.rst

.. _vim.profile.ParameterMetadata: ../../vim/profile/ParameterMetadata.rst

.. _vim.ExtendedElementDescription: ../../vim/ExtendedElementDescription.rst


vim.profile.PolicyOptionMetadata
================================
  The `ProfilePolicyOptionMetadata`_ data object contains the metadata information for a `PolicyOption`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`vim.ExtendedElementDescription`_):

       Identifier for the policy option.
        * The
        * id.key
        * value (
        * `ExtendedElementDescription`_
        * .
        * `key`_
        * ) identifies the policy option type.
        * The
        * id.label
        * property (
        * `ExtendedElementDescription`_
        * .
        * `label`_
        * ) contains a brief localizable message describing the policy option.
        * The
        * id.summary
        * property (
        * `ExtendedElementDescription`_
        * .
        * `summary`_
        * ) contains a localizable summary of the policy option. Summary information can contain embedded variable names which can be replaced with values from the
        * parameter
        * property.
    parameter (`vim.profile.ParameterMetadata`_, optional):

       Metadata about the parameters for the policy option.
