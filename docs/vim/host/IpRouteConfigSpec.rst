
vim.host.IpRouteConfigSpec
==========================
  Dataobject specifying the configuration for IpRoute
:extends: vim.host.IpRouteConfig_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    gatewayDeviceConnection (`vim.host.VirtualNicConnection <vim/host/VirtualNicConnection.rst>`_, optional):

       Choose a gateway device based on what the VirtualNic is connected to. This applies to service console gateway only, it is ignored otherwise.
    ipV6GatewayDeviceConnection (`vim.host.VirtualNicConnection <vim/host/VirtualNicConnection.rst>`_, optional):

       The ipv6 gateway device based on what the VirtualNic is connected to. This applies to service console gateway only, it is ignored otherwise.
