.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.NtpConfig: ../../vim/host/NtpConfig.rst


vim.host.DateTimeConfig
=======================
  This data object represents the dateTime configuration of the host.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    timeZone (`str`_, optional):

       The time zone of the host. Must be one of the values of `key`_ 
    ntpConfig (`vim.host.NtpConfig`_, optional):

       The NTP configuration on the host.
