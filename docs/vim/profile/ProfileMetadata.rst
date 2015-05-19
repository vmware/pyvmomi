.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _profileTypeNames: ../../vim/profile/ProfileComponentMetadata.rst#profileTypeNames

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ProfileCategoryMetadata: ../../vim/profile/ProfileCategoryMetadata.rst

.. _vim.ExtendedDescription: ../../vim/ExtendedDescription.rst

.. _ProfileComponentMetadata: ../../vim/profile/ProfileComponentMetadata.rst

.. _vim.profile.ProfileMetadata.ProfileSortSpec: ../../vim/profile/ProfileMetadata/ProfileSortSpec.rst


vim.profile.ProfileMetadata
===========================
  This data object represents the metadata information of a Profile.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Type of the Profile
    profileTypeName (`str`_, optional):

       Type identifier for the ApplyProfile
    description (`vim.ExtendedDescription`_, optional):

       Property which describes the profile
    sortSpec ([`vim.profile.ProfileMetadata.ProfileSortSpec`_], optional):

       Property that determines a sorting order for display purposes. If the list contains more than one sort spec, then the precedence should be determined by the list order (i.e. sort first by the first spec in the list, then sort by the second spec in the list, etc).
    profileCategory (`str`_, optional):

       Identifies the profile category that this subprofile is a part of. The value of this string should correspond to the key value of a `ProfileCategoryMetadata`_ object's `key`_ in its `id`_ property.
    profileComponent (`str`_, optional):

       Property indicating that the subprofile described by thisProfileMetadataobject is declared in the `profileTypeNames`_ of the specified profile component. The value of this property should correspond to the key value of the `ProfileComponentMetadata`_ object's `key`_ in its `id`_ property. This property should not be present for subprofiles that are not directly declared in the `profileTypeNames`_ property of a `ProfileComponentMetadata`_ object.
