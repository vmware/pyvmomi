vim.host.InternetScsiHba.DiscoveryProperties.SlpDiscoveryMethod
===============================================================
  The available SLP discovery methods.
  :contained by: `vim.host.InternetScsiHba.DiscoveryProperties <vim/host/InternetScsiHba/DiscoveryProperties.rst>`_

  :type: `vim.host.InternetScsiHba.DiscoveryProperties.SlpDiscoveryMethod <vim/host/InternetScsiHba/DiscoveryProperties/SlpDiscoveryMethod.rst>`_

  :name: slpManual

values:
--------

slpAutoMulticast
   Use the well known multicast address to find DAs.

slpDhcp
   Use DHCP to find the SLP DAs.

slpManual
   User specified address for a DA.

slpAutoUnicast
   Use broadcasting to find SLP DAs. Only DAs on the current subnet will be found.
