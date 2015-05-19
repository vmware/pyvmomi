.. _str: https://docs.python.org/2/library/stdtypes.html

.. _EntityType: ../../../vim/dvs/EntityBackup/EntityType.rst

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.fault.ImportOperationBulkFault.FaultOnImport
================================================
  The fault occurred on the entity during an import operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    entityType (`str`_, optional):

       The entity type on which import failed. See `EntityType`_ for valid values
    key (`str`_, optional):

       The key on which import failed
    fault (`vmodl.LocalizedMethodFault`_):

       The fault that occurred.
