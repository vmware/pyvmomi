
vim.vm.device.VirtualDevice.URIBackingInfo
==========================================
  The `VirtualDeviceURIBackingInfo <vim/vm/device/VirtualDevice/URIBackingInfo.rst>`_ data object type defines information for using a network socket as backing for a virtual device.
:extends: vim.vm.device.VirtualDevice.BackingInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    serviceURI (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Identifies the local host or a system on the network, depending on the value of `direction <vim/vm/device/VirtualDevice/URIBackingInfo.rst#direction>`_ .
        * If you use the virtual machine as a server, the URI identifies the host on which the virtual machine runs. In this case, the host name part of the URI should be empty, or it should specify the address of the local host.
        * If you use the virtual machine as a client, the URI identifies the remote system on the network.
        * 
    direction (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The direction of the connection. For possible values see `VirtualDeviceURIBackingOptionDirection <vim/vm/device/VirtualDeviceOption/URIBackingOption/Direction.rst>`_ 
    proxyURI (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Identifies a proxy service that provides network access to the `serviceURI <vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI>`_ . If you specify a proxy URI, the virtual machine initiates a connection with the proxy service and forwards the `serviceURI <vim/vm/device/VirtualDevice/URIBackingInfo.rst#serviceURI>`_ and `direction <vim/vm/device/VirtualDevice/URIBackingInfo.rst#direction>`_ to the proxy.
