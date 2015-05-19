.. _vim.fault.ReplicationVmConfigFault: ../../../vim/fault/ReplicationVmConfigFault.rst

.. _vim.fault.ReplicationVmConfigFault.ReasonForFault: ../../../vim/fault/ReplicationVmConfigFault/ReasonForFault.rst

vim.fault.ReplicationVmConfigFault.ReasonForFault
=================================================
  :contained by: `vim.fault.ReplicationVmConfigFault`_

  :type: `vim.fault.ReplicationVmConfigFault.ReasonForFault`_

  :name: replicationConfigurationFailed

values:
--------

invalidPriorConfiguration
   The existing replication configuration of the VM is broken (applicable to re-configuration only).

replicationAlreadyEnabled
   Attempting to re-enable replication for the VM

replicationConfigurationFailed
   Failed to commit the new replication properties for the VM.

cannotRetrieveVmReplicationConfiguration
   Could not retrieve the VM configuration

invalidGenerationNumber
   Invalid generation number in VM's configuration

incompatibleHwVersion
   Incompatible VM hardware version

outOfBoundsRpoValue
   Invalid RPO value (out of bounds)

invalidDestinationPort
   Invalid destination port

invalidVmReplicationId
   Invalid VM Replication ID string

reconfigureVmReplicationIdNotAllowed
   Attempting to re-configure the VM replication ID

invalidDestinationIpAddress
   Invalid destination IP address

replicationNotEnabled
   Attempting to re-configure or disable replication for a VM for which replication has not been enabled.

invalidExtraVmOptions
   Malformed extra options list

staleGenerationNumber
   Mis-matching generation number (stale)
