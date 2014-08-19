
vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig
===============================================
  A PortConfig represents a virtual network adapter and its configuration for use by the VSAN service.See `HostVirtualNic <vim/host/VirtualNic.rst>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    ipConfig (`vim.vsan.host.IpConfig <vim/vsan/host/IpConfig.rst>`_, optional):

        `VsanHostIpConfig <vim/vsan/host/IpConfig.rst>`_ for this PortConfig.
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Device name which identifies the network adapter for this PortConfig.See `device <vim/host/VirtualNic.rst#device>`_ 
