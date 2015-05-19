.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.ProfileStructureProperty: ../../vim/profile/ProfileStructureProperty.rst


vim.profile.ProfileStructure
============================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    profileTypeName (`str`_):

       Identifier for the profile type
    child ([`vim.profile.ProfileStructureProperty`_], optional):

       SubProfile properties available for this profile
