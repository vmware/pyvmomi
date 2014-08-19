
vim.profile.ProfileMetadata
===========================
  This data object represents the metadata information of a Profile.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of the Profile
    profileTypeName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Type identifier for the ApplyProfile
    description (`vim.ExtendedDescription <vim/ExtendedDescription.rst>`_, optional):

       Property which describes the profile
    sortSpec ([`vim.profile.ProfileMetadata.ProfileSortSpec <vim/profile/ProfileMetadata/ProfileSortSpec.rst>`_], optional):

       Property that determines a sorting order for display purposes. If the list contains more than one sort spec, then the precedence should be determined by the list order (i.e. sort first by the first spec in the list, then sort by the second spec in the list, etc).
    profileCategory (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Identifies the profile category that this subprofile is a part of. The value of this string should correspond to the key value of a `ProfileCategoryMetadata <vim/profile/ProfileCategoryMetadata.rst>`_ object's `key <vim/ElementDescription.rst#key>`_ in its `id <vim/profile/ProfileCategoryMetadata.rst#id>`_ property.
    profileComponent (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Property indicating that the subprofile described by thisProfileMetadataobject is declared in the `profileTypeNames <vim/profile/ProfileComponentMetadata.rst#profileTypeNames>`_ of the specified profile component. The value of this property should correspond to the key value of the `ProfileComponentMetadata <vim/profile/ProfileComponentMetadata.rst>`_ object's `key <vim/ElementDescription.rst#key>`_ in its `id <vim/profile/ProfileComponentMetadata.rst#id>`_ property. This property should not be present for subprofiles that are not directly declared in the `profileTypeNames <vim/profile/ProfileComponentMetadata.rst#profileTypeNames>`_ property of a `ProfileComponentMetadata <vim/profile/ProfileComponentMetadata.rst>`_ object.
