
vim.host.SystemHealthInfo
=========================
  This data object provides information about the health of the phyical system. The data is retrieved from numeric sensor probes.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    numericSensorInfo ([`vim.host.NumericSensorInfo <vim/host/NumericSensorInfo.rst>`_], optional):

       Health information provided by the power probes.
