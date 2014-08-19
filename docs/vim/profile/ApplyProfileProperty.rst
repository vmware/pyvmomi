
vim.profile.ApplyProfileProperty
================================
  The `ProfileApplyProfileProperty <vim/profile/ApplyProfileProperty.rst>`_ data object defines one or more subprofiles.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    propertyName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the property.
    array (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether this property is an array of profiles.
    profile ([`vim.profile.ApplyProfile <vim/profile/ApplyProfile.rst>`_], optional):

       Subprofiles that define policies and nested subprofiles.
