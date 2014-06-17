.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.AuthorizationManager.PrivilegeAvailability
==============================================
  This class defines whether a specific privilege is granted.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    privId (`str`_):

       The privilege ID.
    isGranted (`bool`_):

       True if the privilege is granted.
