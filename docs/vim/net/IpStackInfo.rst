.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.net.IpStackInfo.NetToMedia: ../../vim/net/IpStackInfo/NetToMedia.rst

.. _vim.net.IpStackInfo.DefaultRouter: ../../vim/net/IpStackInfo/DefaultRouter.rst


vim.net.IpStackInfo
===================
  Protocol version independent reporting data object for IP stack.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    neighbor (`vim.net.IpStackInfo.NetToMedia`_, optional):

       Zero, one or more entries of neighbors discovered using ARP or NDP. This information is used to help diagnose connectivity or performance issues. This property maps to RFC 4293 ipNetToPhysicalTable.
    defaultRouter (`vim.net.IpStackInfo.DefaultRouter`_, optional):

       Zero one or more entries of discovered IP routers that are directly reachable from a an interface on this system. This property maps to RFC 4293 ipDefaultRouterTable.
