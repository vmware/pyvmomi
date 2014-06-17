.. _str: https://docs.python.org/2/library/stdtypes.html

.. _optional: ../../vim/profile/ParameterMetadata.rst#optional

.. _parameter: ../../vim/profile/PolicyOptionMetadata.rst#parameter

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _possibleOption: ../../vim/profile/PolicyMetadata.rst#possibleOption

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ProfilePolicyMetadata: ../../vim/profile/PolicyMetadata.rst


vim.profile.PolicyOption
========================
  The `PolicyOption`_ data object represents one or more configuration values. A policy option is one of the configuration options from the `ProfilePolicyMetadata`_ . `possibleOption`_ list.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`str`_):

       Identifier for the policy option. This value matches one of the keys from the list of possible options in the policy metadata ( `ProfilePolicyMetadata`_ . `possibleOption`_ []. `id`_ . `key`_ ).
    parameter (`vmodl.KeyAnyValue`_, optional):

       Parameters for the policy option. This list must include all parameters that are not marked as optional in the policy option metadata parameter list ( `ProfilePolicyMetadata`_ . `possibleOption`_ []. `parameter`_ []. `optional`_ ).
