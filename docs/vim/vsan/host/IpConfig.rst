
vim.vsan.host.IpConfig
======================
  An `VsanHostIpConfig <vim/vsan/host/IpConfig.rst>`_ is a pair of multicast IP addresses for use by the VSAN service. For VSAN there is one such IpConfig pair per "virtual network" as represented by `VsanHostConfigInfoNetworkInfoPortConfig <vim/vsan/host/ConfigInfo/NetworkInfo/PortConfig.rst>`_ .See `VsanHostConfigInfoNetworkInfo <vim/vsan/host/ConfigInfo/NetworkInfo.rst>`_ See `port <vim/vsan/host/ConfigInfo/NetworkInfo.rst#port>`_ See `VsanHostConfigInfoNetworkInfoPortConfig <vim/vsan/host/ConfigInfo/NetworkInfo/PortConfig.rst>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    upstreamIpAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Agent-to-master multicast IP address.
    downstreamIpAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Master-to-agent multicast IP address.
