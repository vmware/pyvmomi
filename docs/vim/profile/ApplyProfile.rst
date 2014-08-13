.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ApplyProfile: ../../vim/profile/ApplyProfile.rst

.. _PolicyOption: ../../vim/profile/PolicyOption.rst

.. _ProfilePolicy: ../../vim/profile/Policy.rst

.. _possibleOption: ../../vim/profile/PolicyMetadata.rst#possibleOption

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.Policy: ../../vim/profile/Policy.rst

.. _ProfilePolicyMetadata: ../../vim/profile/PolicyMetadata.rst

.. _vim.profile.ApplyProfileProperty: ../../vim/profile/ApplyProfileProperty.rst


vim.profile.ApplyProfile
========================
  The `ApplyProfile`_ data object is the base class for all data objects that define profile configuration data.ApplyProfiledefines ESX configuration data storage and it supports recursive profile definition for the profile plug-in architecture.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    enabled (`bool`_):

       Indicates whether the profile is enabled.
    policy ([`vim.profile.Policy`_], optional):

       The list of policies comprising the profile. A `ProfilePolicy`_ stores one or more configuration data values in a `PolicyOption`_ . The policy option is one of the configuration options from the `ProfilePolicyMetadata`_ . `possibleOption`_ list.
    profileTypeName (`str`_, optional):

       Identifies the profile type.
    profileVersion (`str`_, optional):

       Profile engine version.
    property ([`vim.profile.ApplyProfileProperty`_], optional):

       List of subprofiles for this profile. This list can change depending on which profile plug-ins are available in the system. Subprofiles can be nested to arbitrary depths to represent host capabilities.
