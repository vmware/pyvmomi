.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.NtpConfig: ../../vim/host/NtpConfig.rst

.. _vim.host.DateTimeSystem.TimeZone: ../../vim/host/DateTimeSystem/TimeZone.rst


vim.host.DateTimeInfo
=====================
  This data object represents the dateTime configuration of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    timeZone (`vim.host.DateTimeSystem.TimeZone`_):

       The time zone of the host.
    ntpConfig (`vim.host.NtpConfig`_, optional):

       The NTP configuration on the host.
