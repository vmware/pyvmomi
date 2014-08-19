vim.fault.DasConfigFault.DasConfigFaultReason
=============================================
  :contained by: `vim.fault.DasConfigFault <vim/fault/DasConfigFault.rst>`_

  :type: `vim.fault.DasConfigFault.DasConfigFaultReason <vim/fault/DasConfigFault/DasConfigFaultReason.rst>`_

  :name: VSanNotSupportedOnHost

values:
--------

HostNetworkMisconfiguration
   There is a problem with the host network configuration.

InsufficientPrivileges
   The privileges were insuffient for the operation.

NoDatastoresConfigured
   No datastores defined for this host

VSanNotSupportedOnHost
   Host in vSAN cluster does not support vSAN.

Other
   The HA configuration failed for other reasons.

NoPrimaryAgentAvailable
   There was no running primary agent available to contact. Check that your other hosts don't have HA errors

HostMisconfiguration
   There is a problem with the host configuration.
