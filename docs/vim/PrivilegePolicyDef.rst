.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst


vim.PrivilegePolicyDef
======================
  Describes a basic privilege policy.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    createPrivilege (`str`_):

       Name of privilege required for creation.
    readPrivilege (`str`_):

       Name of privilege required for reading.
    updatePrivilege (`str`_):

       Name of privilege required for updating.
    deletePrivilege (`str`_):

       Name of privilege required for deleting.
