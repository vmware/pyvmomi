.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.VirtualMachine.StorageRequirement
=====================================
  Describes the storage requirement to perform a consolidation operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    datastore (`vim.Datastore`_):

       The datastore.
    freeSpaceRequiredInKb (`long`_):

       Space required.
