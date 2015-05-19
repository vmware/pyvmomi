.. _vim.host.PortGroup: ../../../vim/host/PortGroup.rst

.. _vim.host.PortGroup.PortConnecteeType: ../../../vim/host/PortGroup/PortConnecteeType.rst

vim.host.PortGroup.PortConnecteeType
====================================
  The type of component connected to a port group.
  :contained by: `vim.host.PortGroup`_

  :type: `vim.host.PortGroup.PortConnecteeType`_

  :name: unknown

values:
--------

unknown
   This port group serves an entity of unspecified kind.

host
   The VMkernel is connected to this port group.

systemManagement
   A system management entity (service console) is connected to this port group.

virtualMachine
   A virtual machine is connected to this port group.
