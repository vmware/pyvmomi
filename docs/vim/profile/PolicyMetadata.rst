.. _HostProfile: ../../vim/profile/host/HostProfile.rst

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _ProfilePolicy: ../../vim/profile/Policy.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ProfilePolicyMetadata: ../../vim/profile/PolicyMetadata.rst

.. _vim.ExtendedElementDescription: ../../vim/ExtendedElementDescription.rst

.. _vim.profile.PolicyOptionMetadata: ../../vim/profile/PolicyOptionMetadata.rst


vim.profile.PolicyMetadata
==========================
  The `ProfilePolicyMetadata`_ data object represents the metadata information for a `ProfilePolicy`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`vim.ExtendedElementDescription`_):

       Identifier for the policy.
    possibleOption ([`vim.profile.PolicyOptionMetadata`_]):

       Possible policy options that can be set for a policy of the given kind. `HostProfile`_ s and subprofiles will contain selected policy options from this list. See `PolicyOption`_ .
