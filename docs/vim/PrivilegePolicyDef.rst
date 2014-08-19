
vim.PrivilegePolicyDef
======================
  Describes a basic privilege policy.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    createPrivilege (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of privilege required for creation.
    readPrivilege (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of privilege required for reading.
    updatePrivilege (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of privilege required for updating.
    deletePrivilege (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of privilege required for deleting.
