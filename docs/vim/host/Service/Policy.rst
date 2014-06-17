.. _vim.host.Service: ../../../vim/host/Service.rst

.. _vim.host.Service.Policy: ../../../vim/host/Service/Policy.rst

vim.host.Service.Policy
=======================
  Set of valid service policy strings.
  :contained by: `vim.host.Service`_

  :type: `vim.host.Service.Policy`_

  :name: off

values:
--------

on
   Service should be started when the host starts up.

automatic
   Service should run if and only if it has open firewall ports.

off
   Service should not be started when the host starts up.
