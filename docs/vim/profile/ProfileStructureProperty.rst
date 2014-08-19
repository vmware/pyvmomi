
vim.profile.ProfileStructureProperty
====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    propertyName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the property where this ProfileStructureProperty is being used
    array (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating if this property is an Array of profiles
    element (`vim.profile.ProfileStructure <vim/profile/ProfileStructure.rst>`_):

       Details about the profile contained within this property
