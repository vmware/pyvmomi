vim.dvs.HostMember.HostComponentState
=====================================
  Describes the state of the host proxy switch.
  :contained by: `vim.dvs.HostMember <vim/dvs/HostMember.rst>`_

  :type: `vim.dvs.HostMember.HostComponentState <vim/dvs/HostMember/HostComponentState.rst>`_

  :name: down

values:
--------

disconnected
   The host is disconnected or it is not responding.

up
   The host proxy switch is up and running.

down
   The host proxy is down.

warning
   The host requires attention.

outOfSync
   The proxy switch configuration is not the same as the distributed virtual switch configuration in the vCenter Server.

pending
   The host proxy switch is waiting to be initialized.
