.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.net.IpConfigInfo: ../../../vim/net/IpConfigInfo.rst

.. _vim.net.DnsConfigInfo: ../../../vim/net/DnsConfigInfo.rst

.. _vim.net.NetBIOSConfigInfo: ../../../vim/net/NetBIOSConfigInfo.rst


vim.vm.GuestInfo.NicInfo
========================
  
:extends: vmodl.DynamicData_

Attributes:
    network (`str`_, optional):

       Name of the virtual switch portgroup or dvPort connected to this adapter.
    ipAddress (`str`_, optional):

    macAddress (`str`_, optional):

       MAC address of the adapter.
    connected (`bool`_):

       Flag indicating whether or not the virtual device is connected.
    deviceConfigId (`int`_):

       Link to the corresponding virtual device.
    dnsConfig (`vim.net.DnsConfigInfo`_, optional):

       DNS configuration of the adapter. This property is set only when Guest OS supports it. See StackInfo dnsConfig for system wide settings.
    ipConfig (`vim.net.IpConfigInfo`_, optional):

       IP configuration settings of the adapter See StackInfo ipStackConfig for system wide settings.
    netBIOSConfig (`vim.net.NetBIOSConfigInfo`_, optional):

       NetBIOS configuration of the adapter
