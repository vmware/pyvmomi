.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.VsanInternalSystem.CmmdsQuery
======================================
  All fields in the CMMDS Query spec are optional, but at least one needs specified to make a valid query.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    type (`str`_, optional):

       CMMDS type, e.g. DOM_OBJECT, LSOM_OBJECT, POLICY, DISK etc.
    uuid (`str`_, optional):

       UUID of the entry.
    owner (`str`_, optional):

       UUID of the owning node.
