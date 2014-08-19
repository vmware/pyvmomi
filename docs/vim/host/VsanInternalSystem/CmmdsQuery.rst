
vim.host.VsanInternalSystem.CmmdsQuery
======================================
  All fields in the CMMDS Query spec are optional, but at least one needs specified to make a valid query.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       CMMDS type, e.g. DOM_OBJECT, LSOM_OBJECT, POLICY, DISK etc.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       UUID of the entry.
    owner (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       UUID of the owning node.
