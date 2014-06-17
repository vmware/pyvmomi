.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.dvs.PortStatistics: ../../../vim/dvs/PortStatistics.rst

.. _vim.dvs.KeyedOpaqueBlob: ../../../vim/dvs/KeyedOpaqueBlob.rst

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo: ../../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst


vim.dvs.DistributedVirtualPort.State
====================================
  The state of a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo`_, optional):

       Run time information of the port. This property is set only when the port is running.
    stats (`vim.dvs.PortStatistics`_):

       Statistics of the port.
    vendorSpecificState (`vim.dvs.KeyedOpaqueBlob`_, optional):

       Opaque binary blob that stores vendor-specific runtime state data.
