.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.ProfileStructure: ../../vim/profile/ProfileStructure.rst


vim.profile.ProfileStructureProperty
====================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    propertyName (`str`_):

       Name of the property where this ProfileStructureProperty is being used
    array (`bool`_):

       Flag indicating if this property is an Array of profiles
    element (`vim.profile.ProfileStructure`_):

       Details about the profile contained within this property
