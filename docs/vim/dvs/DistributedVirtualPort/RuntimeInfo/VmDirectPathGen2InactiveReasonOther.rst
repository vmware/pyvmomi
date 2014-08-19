vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther
==============================================================================
  Set of possible values for `DVPortStatus <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_ . `vmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonOther>`_ .
  :contained by: `vim.dvs.DistributedVirtualPort.RuntimeInfo <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_

  :type: `vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo/VmDirectPathGen2InactiveReasonOther.rst>`_

  :name: portNptIncompatibleConnectee

values:
--------

portNptIncompatibleConnectee
   Configuration or state of the port's connectee prevents VMDirectPath Gen 2. See `vmDirectPathGen2InactiveReasonVm <vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2InactiveReasonVm>`_ and/or `vmDirectPathGen2InactiveReasonExtended <vim/vm/DeviceRuntimeInfo/VirtualEthernetCardRuntimeState.rst#vmDirectPathGen2InactiveReasonExtended>`_ in the appropriate element of the RuntimeInfo.device array of the virtual machine connected to this port.

portNptIncompatibleHost
   The host for which this port is defined does not support VMDirectPath Gen 2. See `HostCapability <vim/host/Capability.rst>`_ . `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ 
