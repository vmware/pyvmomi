
vim.host.DhcpService
====================
  A dynamic host control protocol (DHCP) service instance serves IP addresses to a single virtual network subnet. The instances may be handled collectively by a single server. This decision can be made during implementation.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The instance ID of the DHCP service.
    spec (`vim.host.DhcpService.Specification <vim/host/DhcpService/Specification.rst>`_):

       Configurable properties for the DHCP service.
