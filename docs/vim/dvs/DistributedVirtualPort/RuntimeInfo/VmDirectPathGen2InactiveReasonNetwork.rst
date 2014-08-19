vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork
================================================================================
  Set of possible values for `DVPortStatus <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_ . `vmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonNetwork>`_ .
  :contained by: `vim.dvs.DistributedVirtualPort.RuntimeInfo <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_

  :type: `vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo/VmDirectPathGen2InactiveReasonNetwork.rst>`_

  :name: portNptDisabledForPort

values:
--------

portNptNoVirtualFunctionsAvailable
   At least some of the physical NICs used as uplinks for this port support VMDirectPath Gen 2, but all available network-passthrough resources are in use by other ports.

portNptNoCompatibleNics
   None of the physical NICs used as uplinks for this port support VMDirectPath Gen 2.See `vmDirectPathGen2Supported <vim/host/PhysicalNic.rst#vmDirectPathGen2Supported>`_ 

portNptIncompatibleDvs
   The switch for which this port is defined does not support VMDirectPath Gen 2. See `DVSFeatureCapability <vim/DistributedVirtualSwitch/FeatureCapability.rst>`_ . `vmDirectPathGen2Supported <vim/DistributedVirtualSwitch/FeatureCapability.rst#vmDirectPathGen2Supported>`_ .

portNptDisabledForPort
   VMDirectPath Gen 2 has been explicitly disabled for this port.
