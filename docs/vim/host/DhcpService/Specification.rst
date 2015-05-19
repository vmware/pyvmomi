.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.DhcpService.Specification
==================================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    virtualSwitch (`str`_):

       The name of the virtual switch to which DHCP service is connected.
    defaultLeaseDuration (`int`_):

       The default DHCP lease duration (minutes).
    leaseBeginIp (`str`_):

       The start of the IP address range served by the DHCP service.
    leaseEndIp (`str`_):

       The end of the IP address range served by the DHCP service.
    maxLeaseDuration (`int`_):

       The maximum DHCP lease duration (minutes).
    unlimitedLease (`bool`_):

       A flag to indicate whether or not unlimited DHCP lease durations are allowed.
    ipSubnetAddr (`str`_):

       Subnet served by DHCP service.
    ipSubnetMask (`str`_):

       Subnet mask of network served by DHCP service.
