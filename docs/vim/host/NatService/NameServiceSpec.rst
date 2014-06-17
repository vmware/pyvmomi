.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.NatService.NameServiceSpec
===================================
  This data object type specifies the information for the name servers.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    dnsAutoDetect (`bool`_):

       The flag to indicate whether or not the DNS server should be automatically detected or specified explicitly.
    dnsPolicy (`str`_):

       The policy to use when multiple DNS addresses are available on the host.
    dnsRetries (`int`_):

       The number of retries before giving up on a DNS request from a virtual network.
    dnsTimeout (`int`_):

       The time (in seconds) before retrying a DNS request to an external network.
    dnsNameServer (`str`_, optional):

       The list of DNS servers.
    nbdsTimeout (`int`_):

       The time (in seconds) allotted for queries to the NetBIOS Datagram Server (NBDS).
    nbnsRetries (`int`_):

       Number of retries for each query to the NBNS.
    nbnsTimeout (`int`_):

       The time (in seconds) allotted for queries to the NBNS.
