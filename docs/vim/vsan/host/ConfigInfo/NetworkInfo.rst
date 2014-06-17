.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig: ../../../../vim/vsan/host/ConfigInfo/NetworkInfo/PortConfig.rst


vim.vsan.host.ConfigInfo.NetworkInfo
====================================
  Host-local VSAN network configuration. This data object is used both for specifying and retrieving network configuration for a host participating in the VSAN service.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    port (`vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig`_, optional):

       Set of PortConfig entries for use by the VSAN service, one per "virtual network" as used by VSAN.
