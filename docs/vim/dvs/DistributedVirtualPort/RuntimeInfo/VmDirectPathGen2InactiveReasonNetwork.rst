.. _DVPortStatus: ../../../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst

.. _DVSFeatureCapability: ../../../../vim/DistributedVirtualSwitch/FeatureCapability.rst

.. _vmDirectPathGen2Supported: ../../../../vim/DistributedVirtualSwitch/FeatureCapability.rst#vmDirectPathGen2Supported

.. _vmDirectPathGen2InactiveReasonNetwork: ../../../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonNetwork

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo: ../../../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork: ../../../../vim/dvs/DistributedVirtualPort/RuntimeInfo/VmDirectPathGen2InactiveReasonNetwork.rst

vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork
================================================================================
  Set of possible values for `DVPortStatus`_ . `vmDirectPathGen2InactiveReasonNetwork`_ .
  :contained by: `vim.dvs.DistributedVirtualPort.RuntimeInfo`_

  :type: `vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork`_

  :name: portNptDisabledForPort

values:
--------

portNptNoVirtualFunctionsAvailable
   At least some of the physical NICs used as uplinks for this port support VMDirectPath Gen 2, but all available network-passthrough resources are in use by other ports.

portNptNoCompatibleNics
   None of the physical NICs used as uplinks for this port support VMDirectPath Gen 2.See `vmDirectPathGen2Supported`_ 

portNptIncompatibleDvs
   The switch for which this port is defined does not support VMDirectPath Gen 2. See `DVSFeatureCapability`_ . `vmDirectPathGen2Supported`_ .

portNptDisabledForPort
   VMDirectPath Gen 2 has been explicitly disabled for this port.
