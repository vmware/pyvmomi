.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.FileAccess
===================
  This data object type contains a single access control entry for a file permissions list.
:extends: vmodl.DynamicData_

Attributes:
    who (`str`_):

       User or group to which the access applies.
    what (`str`_):

       Rights given to the user or group.
