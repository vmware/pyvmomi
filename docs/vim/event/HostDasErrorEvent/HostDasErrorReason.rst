.. _vim.event.HostDasErrorEvent: ../../../vim/event/HostDasErrorEvent.rst

.. _vim.event.HostDasErrorEvent.HostDasErrorReason: ../../../vim/event/HostDasErrorEvent/HostDasErrorReason.rst

vim.event.HostDasErrorEvent.HostDasErrorReason
==============================================
  :contained by: `vim.event.HostDasErrorEvent`_

  :type: `vim.event.HostDasErrorEvent.HostDasErrorReason`_

  :name: other

values:
--------

healthCheckScriptFailed
   Health check script failed

isolationAddressUnpingable
   HA isolation address unpingable

agentShutdown
   HA agent was shutdown

communicationInitFailed
   HA communication initialization failed

other
   Other reason

timeout
   Timeout while communicating with HA agent

configFailed
   Error while configuring/unconfiguring HA

agentFailed
   HA agent has an error
