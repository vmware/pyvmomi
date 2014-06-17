.. _str: https://docs.python.org/2/library/stdtypes.html

.. _port: ../../../vim/vsan/host/ConfigInfo/NetworkInfo.rst#port

.. _UpdateVsan_Task: ../../../vim/host/VsanSystem.rst#update

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _VsanHostIpConfig: ../../../vim/vsan/host/IpConfig.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VsanHostConfigInfoNetworkInfo: ../../../vim/vsan/host/ConfigInfo/NetworkInfo.rst

.. _VsanHostConfigInfoNetworkInfoPortConfig: ../../../vim/vsan/host/ConfigInfo/NetworkInfo/PortConfig.rst


vim.vsan.host.IpConfig
======================
  An `VsanHostIpConfig`_ is a pair of multicast IP addresses for use by the VSAN service. For VSAN there is one such IpConfig pair per "virtual network" as represented by `VsanHostConfigInfoNetworkInfoPortConfig`_ .See `VsanHostConfigInfoNetworkInfo`_ See `port`_ See `VsanHostConfigInfoNetworkInfoPortConfig`_ See `UpdateVsan_Task`_ 
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    upstreamIpAddress (`str`_):

       Agent-to-master multicast IP address.
    downstreamIpAddress (`str`_):

       Master-to-agent multicast IP address.
