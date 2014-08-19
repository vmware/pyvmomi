
vim.host.FlagInfo
=================
  The FlagInfo data object type encapsulates the flag settings for a host. These properties are optional since the same structure is used to change the values during an edit or create operation.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    backgroundSnapshotsEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether background snapshots are enabled.
