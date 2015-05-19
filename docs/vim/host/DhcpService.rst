.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.DhcpService.Specification: ../../vim/host/DhcpService/Specification.rst


vim.host.DhcpService
====================
  A dynamic host control protocol (DHCP) service instance serves IP addresses to a single virtual network subnet. The instances may be handled collectively by a single server. This decision can be made during implementation.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    key (`str`_):

       The instance ID of the DHCP service.
    spec (`vim.host.DhcpService.Specification`_):

       Configurable properties for the DHCP service.
