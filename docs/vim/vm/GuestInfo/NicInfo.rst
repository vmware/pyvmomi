
vim.vm.GuestInfo.NicInfo
========================
  
:extends: vmodl.DynamicData_

Attributes:
    network (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the virtual switch portgroup or dvPort connected to this adapter.
    ipAddress ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

    macAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       MAC address of the adapter.
    connected (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether or not the virtual device is connected.
    deviceConfigId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Link to the corresponding virtual device.
    dnsConfig (`vim.net.DnsConfigInfo <vim/net/DnsConfigInfo.rst>`_, optional):

       DNS configuration of the adapter. This property is set only when Guest OS supports it. See StackInfo dnsConfig for system wide settings.
    ipConfig (`vim.net.IpConfigInfo <vim/net/IpConfigInfo.rst>`_, optional):

       IP configuration settings of the adapter See StackInfo ipStackConfig for system wide settings.
    netBIOSConfig (`vim.net.NetBIOSConfigInfo <vim/net/NetBIOSConfigInfo.rst>`_, optional):

       NetBIOS configuration of the adapter
