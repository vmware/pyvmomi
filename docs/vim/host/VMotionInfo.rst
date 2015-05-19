.. _vim.host.IpConfig: ../../vim/host/IpConfig.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VMotionSystem.NetConfig: ../../vim/host/VMotionSystem/NetConfig.rst


vim.host.VMotionInfo
====================
  This data object type describes VMotion host configuration data objects.
:extends: vmodl.DynamicData_
**deprecated**


Attributes:
    netConfig (`vim.host.VMotionSystem.NetConfig`_, optional):

       VMotion network configuration.
    ipConfig (`vim.host.IpConfig`_, optional):

       IP configuration of the VMotion VirtualNic.
