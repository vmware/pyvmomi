.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vim.HostSystem.ConnectionState: ../../vim/HostSystem/ConnectionState.rst

vim.HostSystem.ConnectionState
==============================
  Defines a host's connection state.
  :contained by: `vim.HostSystem`_

  :type: `vim.HostSystem.ConnectionState`_

  :name: disconnected

values:
--------

connected
   Connected to the server. For ESX Server, this is always the setting.

disconnected
   The user has explicitly taken the host down. VirtualCenter does not expect to receive heartbeats from the host. The next time a heartbeat is received, the host is moved to the connected state again and an event is logged.

notResponding
   VirtualCenter is not receiving heartbeats from the server. The state automatically changes to connected once heartbeats are received again. This state is typically used to trigger an alarm on the host.
