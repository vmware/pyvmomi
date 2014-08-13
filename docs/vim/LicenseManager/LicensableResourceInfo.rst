.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst


vim.LicenseManager.LicensableResourceInfo
=========================================
  Encapsulates information about all licensable resources on the host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    resource ([`vmodl.KeyAnyValue`_]):

       List of currently supported resources. The type of every value is long. The key can be one of ResourceKey or arbitrary string.NOTE: The values in this property may not be accurate for pre-5.0 hosts when returned by vCenter 5.0
