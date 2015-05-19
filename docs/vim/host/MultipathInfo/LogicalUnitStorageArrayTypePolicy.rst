.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostMultipathInfoLogicalUnitStorageArrayTypePolicy: ../../../vim/host/MultipathInfo/LogicalUnitStorageArrayTypePolicy.rst


vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy
========================================================
  The `HostMultipathInfoLogicalUnitStorageArrayTypePolicy`_ data object describes a storage array type policy for for a device. This policy determines how device I/O and management is performed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    policy (`str`_):

       String indicating the storage array type policy.
