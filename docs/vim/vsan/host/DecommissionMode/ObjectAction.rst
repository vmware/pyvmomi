vim.vsan.host.DecommissionMode.ObjectAction
===========================================
  The action to take with regard to storage objects upon decommissioning a host from use with the VSAN service.
  :contained by: `vim.vsan.host.DecommissionMode <vim/vsan/host/DecommissionMode.rst>`_

  :type: `vim.vsan.host.DecommissionMode.ObjectAction <vim/vsan/host/DecommissionMode/ObjectAction.rst>`_

  :name: evacuateAllData

values:
--------

evacuateAllData
   VSAN data evacuation should be performed such that all storage object data is removed from the host.

ensureObjectAccessibility
   VSAN data reconfiguration should be performed to ensure storage object accessibility.

noAction
   No special action should take place regarding VSAN data.
