
vim.vm.customization.CustomIpV6Generator
========================================
  Use a command-line program configured with the VirtualCenter server.
:extends: vim.vm.customization.IpV6Generator_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    argument (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       An optional argument that is passed to the utility for this ipv6 address. The meaning of this field is user-defined, in the script.
