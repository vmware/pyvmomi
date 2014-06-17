.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.profile.Profile.ConfigInfo
==============================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    name (`str`_):

       Name of the profile
    annotation (`str`_, optional):

       User Provided description of the profile
    enabled (`bool`_):

       Flag indicating if the Profile is enabled
