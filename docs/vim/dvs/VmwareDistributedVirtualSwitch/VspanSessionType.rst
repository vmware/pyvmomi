vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionType
=======================================================
  Distributed Port Mirroring session types.
  :contained by: `vim.dvs.VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_

  :type: `vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionType <vim/dvs/VmwareDistributedVirtualSwitch/VspanSessionType.rst>`_

  :name: encapsulatedRemoteMirrorSource

values:
--------

encapsulatedRemoteMirrorSource
   In encapsulatedRemoteMirrorSource session, Distributed Ports can be used as source entities, and Ip address can be used as destination entities.

remoteMirrorDest
   In remoteMirrorDest session, vlan Ids can be used as source entities, and Distributed Ports can be used as destination entities.

remoteMirrorSource
   In remoteMirrorSource session, Distributed Ports can be used as source entities, and uplink ports name can be used as destination entities.

dvPortMirror
   In dvPortMirror session, Distributed Ports can be used as both source and destination entities.

mixedDestMirror
   In mixedDestMirror session, Distributed Ports can be used as source entities, and both Distributed Ports and Uplink Ports Name can be used as destination entities.
