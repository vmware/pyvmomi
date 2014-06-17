.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.NtpConfig
==================
  Configuration information for the NTP (Network Time Protocol) service.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    server (`str`_, optional):

       List of time servers, specified as either IP addresses or fully qualified domain names (FQDNs).
