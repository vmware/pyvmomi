.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.dvs.DistributedVirtualSwitchInfo: ../../../vim/dvs/DistributedVirtualSwitchInfo.rst

.. _vim.dvs.DistributedVirtualPortgroupInfo: ../../../vim/dvs/DistributedVirtualPortgroupInfo.rst


vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget
=======================================================
  Configuration specification for a DistributedVirtualSwitch or DistributedVirtualPortgroup.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    distributedVirtualPortgroup (`vim.dvs.DistributedVirtualPortgroupInfo`_, optional):

       List of any DistributedVirtualPortgroup available for host Virtual NIC connection.
    distributedVirtualSwitch (`vim.dvs.DistributedVirtualSwitchInfo`_, optional):

       List of any DistributedVirtualSwitch available for host Virtual NIC connection.
