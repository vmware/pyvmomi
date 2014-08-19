
vim.host.DhcpService.Specification
==================================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    virtualSwitch (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual switch to which DHCP service is connected.
    defaultLeaseDuration (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The default DHCP lease duration (minutes).
    leaseBeginIp (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The start of the IP address range served by the DHCP service.
    leaseEndIp (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The end of the IP address range served by the DHCP service.
    maxLeaseDuration (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The maximum DHCP lease duration (minutes).
    unlimitedLease (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       A flag to indicate whether or not unlimited DHCP lease durations are allowed.
    ipSubnetAddr (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Subnet served by DHCP service.
    ipSubnetMask (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Subnet mask of network served by DHCP service.
