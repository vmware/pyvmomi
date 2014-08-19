vim.net.IpStackInfo.EntryType
=============================
  IP Stack keeps state on entries in IpNetToMedia table to perform physical address lookups for IP addresses. Here are the standard states perSee RFC
  :contained by: `vim.net.IpStackInfo <vim/net/IpStackInfo.rst>`_

  :type: `vim.net.IpStackInfo.EntryType <vim/net/IpStackInfo/EntryType.rst>`_

  :name: manual

values:
--------

manual
   This entry was set manually.

other
   This implementation is reporting something other than what states are listed below.

dynamic
   This entry has been learned using ARP or NDP.

invalid
   The IP Stack has marked this entry as not useable.
