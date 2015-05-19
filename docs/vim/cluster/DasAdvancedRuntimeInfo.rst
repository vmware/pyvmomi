.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.cluster.DasHostInfo: ../../vim/cluster/DasHostInfo.rst

.. _vim.cluster.DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo: ../../vim/cluster/DasAdvancedRuntimeInfo/HeartbeatDatastoreInfo.rst


vim.cluster.DasAdvancedRuntimeInfo
==================================
  Base class for advanced runtime information related to the high availability service for a cluster.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    dasHostInfo (`vim.cluster.DasHostInfo`_, optional):

       The information pertaining to the HA agents on the hosts
    heartbeatDatastoreInfo ([`vim.cluster.DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo`_], optional):

       The map of a datastore to the set of hosts that are using the datastore for storage heartbeating.
