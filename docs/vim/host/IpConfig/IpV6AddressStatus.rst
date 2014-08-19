vim.host.IpConfig.IpV6AddressStatus
===================================
  :contained by: `vim.host.IpConfig <vim/host/IpConfig.rst>`_

  :type: `vim.host.IpConfig.IpV6AddressStatus <vim/host/IpConfig/IpV6AddressStatus.rst>`_

  :name: duplicate

values:
--------

tentative
   Indicates that the uniqueness of the address on the link is presently being verified.

deprecated
   Indicates that this is a valid but deprecated address that should no longer be used as a source address.

inaccessible
   Indicates that the address is not accessible because interface is not operational.

invalid
   Indicates that this isn't a valid.

duplicate
   Indicates the address has been determined to be non-unique on the link, this address will not be reachable.

preferred
   Indicates that this is a valid address.

unknown
   Indicates that the status cannot be determined.
