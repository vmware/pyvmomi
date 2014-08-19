
vim.host.DateTimeConfig
=======================
  This data object represents the dateTime configuration of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    timeZone (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time zone of the host. Must be one of the values of `key <vim/host/DateTimeSystem/TimeZone.rst#key>`_ 
    ntpConfig (`vim.host.NtpConfig <vim/host/NtpConfig.rst>`_, optional):

       The NTP configuration on the host.
