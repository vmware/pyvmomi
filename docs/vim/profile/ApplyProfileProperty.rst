.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.ApplyProfile: ../../vim/profile/ApplyProfile.rst

.. _ProfileApplyProfileProperty: ../../vim/profile/ApplyProfileProperty.rst


vim.profile.ApplyProfileProperty
================================
  The `ProfileApplyProfileProperty`_ data object defines one or more subprofiles.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    propertyName (`str`_):

       Name of the property.
    array (`bool`_):

       Flag indicating whether this property is an array of profiles.
    profile ([`vim.profile.ApplyProfile`_], optional):

       Subprofiles that define policies and nested subprofiles.
