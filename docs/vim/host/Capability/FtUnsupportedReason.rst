.. _vim.host.Capability: ../../../vim/host/Capability.rst

.. _ftCompatibilityIssues: ../../../vim/host/Capability.rst#ftCompatibilityIssues

.. _vim.host.Capability.FtUnsupportedReason: ../../../vim/host/Capability/FtUnsupportedReason.rst

vim.host.Capability.FtUnsupportedReason
=======================================
  Set of possible values for `ftCompatibilityIssues`_ 
  :contained by: `vim.host.Capability`_

  :type: `vim.host.Capability.FtUnsupportedReason`_

  :name: haAgentIssue

values:
--------

missingFTLoggingNic
   FT logging nic is not configured on the host

missingVMotionNic
   VMotion nic is not configured on the host

haAgentIssue
   Host does not have HA agent running properly

vMotionNotLicensed
   No VMotion license

ftNotLicensed
   Host does not have proper FT license
