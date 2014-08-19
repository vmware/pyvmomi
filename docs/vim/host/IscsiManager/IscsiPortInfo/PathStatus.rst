vim.host.IscsiManager.IscsiPortInfo.PathStatus
==============================================
  :contained by: `vim.host.IscsiManager.IscsiPortInfo <vim/host/IscsiManager/IscsiPortInfo.rst>`_

  :type: `vim.host.IscsiManager.IscsiPortInfo.PathStatus <vim/host/IscsiManager/IscsiPortInfo/PathStatus.rst>`_

  :name: lastActive

values:
--------

active
   All paths on this Virtual NIC are standby paths from SCSI stack perspective.

standBy
   One or more paths on the Virtual NIC are active paths to storage. Unbinding this Virtual NIC will cause storage path transitions.

notUsed
   There are no paths on this Virtual NIC

lastActive
   One or more paths on the Virtual NIC is the last active path to a particular storage device.
