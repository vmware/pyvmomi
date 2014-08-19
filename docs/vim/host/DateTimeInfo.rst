
vim.host.DateTimeInfo
=====================
  This data object represents the dateTime configuration of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    timeZone (`vim.host.DateTimeSystem.TimeZone <vim/host/DateTimeSystem/TimeZone.rst>`_):

       The time zone of the host.
    ntpConfig (`vim.host.NtpConfig <vim/host/NtpConfig.rst>`_, optional):

       The NTP configuration on the host.
