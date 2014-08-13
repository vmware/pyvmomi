.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.NumericSensorInfo: ../../vim/host/NumericSensorInfo.rst


vim.host.SystemHealthInfo
=========================
  This data object provides information about the health of the phyical system. The data is retrieved from numeric sensor probes.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    numericSensorInfo ([`vim.host.NumericSensorInfo`_], optional):

       Health information provided by the power probes.
