
vim.host.FileAccess
===================
  This data object type contains a single access control entry for a file permissions list.
:extends: vmodl.DynamicData_

Attributes:
    who (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       User or group to which the access applies.
    what (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Rights given to the user or group.
