
vim.net.DhcpConfigSpec
======================
  Dynamic Host Configuration Protocol Configuration for IP version 4 and version 6.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    ipv6 (`vim.net.DhcpConfigSpec.DhcpOptionsSpec <vim/net/DhcpConfigSpec/DhcpOptionsSpec.rst>`_, optional):

       Configure IPv6 DHCP client settings.
    ipv4 (`vim.net.DhcpConfigSpec.DhcpOptionsSpec <vim/net/DhcpConfigSpec/DhcpOptionsSpec.rst>`_, optional):

       Configure IPv4 DHCP client settings.
