.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.host.IpRouteConfig: ../../vim/host/IpRouteConfig.rst

.. _vim.host.VirtualNicConnection: ../../vim/host/VirtualNicConnection.rst


vim.host.IpRouteConfigSpec
==========================
  Dataobject specifying the configuration for IpRoute
:extends: vim.host.IpRouteConfig_
:since: `vSphere API 4.0`_

Attributes:
    gatewayDeviceConnection (`vim.host.VirtualNicConnection`_, optional):

       Choose a gateway device based on what the VirtualNic is connected to. This applies to service console gateway only, it is ignored otherwise.
    ipV6GatewayDeviceConnection (`vim.host.VirtualNicConnection`_, optional):

       The ipv6 gateway device based on what the VirtualNic is connected to. This applies to service console gateway only, it is ignored otherwise.
