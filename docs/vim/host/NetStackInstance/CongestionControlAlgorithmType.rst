.. _vim.host.NetStackInstance: ../../../vim/host/NetStackInstance.rst

.. _vim.host.NetStackInstance.CongestionControlAlgorithmType: ../../../vim/host/NetStackInstance/CongestionControlAlgorithmType.rst

vim.host.NetStackInstance.CongestionControlAlgorithmType
========================================================
  Define TCP congestion control algorithm used by an instance
  :contained by: `vim.host.NetStackInstance`_

  :type: `vim.host.NetStackInstance.CongestionControlAlgorithmType`_

  :name: cubic

values:
--------

cubic
   Cubic Algorithm. See http://tools.ietf.org/id/draft-rhee-tcp-cubic-00.txt for detail.

newreno
   New Reno Algorithm. See http://tools.ietf.org/html/rfc3782 for detail.
