.. _str: https://docs.python.org/2/library/stdtypes.html

.. _device: ../../../../../vim/host/VirtualNic.rst#device

.. _HostVirtualNic: ../../../../../vim/host/VirtualNic.rst

.. _vSphere API 5.5: ../../../../../vim/version.rst#vimversionversion9

.. _VsanHostIpConfig: ../../../../../vim/vsan/host/IpConfig.rst

.. _vmodl.DynamicData: ../../../../../vmodl/DynamicData.rst

.. _vim.vsan.host.IpConfig: ../../../../../vim/vsan/host/IpConfig.rst


vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig
===============================================
  A PortConfig represents a virtual network adapter and its configuration for use by the VSAN service.See `HostVirtualNic`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    ipConfig (`vim.vsan.host.IpConfig`_, optional):

        `VsanHostIpConfig`_ for this PortConfig.
    device (`str`_):

       Device name which identifies the network adapter for this PortConfig.See `device`_ 
