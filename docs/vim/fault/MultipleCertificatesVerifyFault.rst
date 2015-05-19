.. _string: ../../str

.. _AddHost_Task: ../../vim/ClusterComputeResource.rst#addHost

.. _ReconnectHost_Task: ../../vim/HostSystem.rst#reconnect

.. _AddStandaloneHost_Task: ../../vim/Folder.rst#addStandaloneHost

.. _vim.fault.HostConnectFault: ../../vim/fault/HostConnectFault.rst


vim.fault.MultipleCertificatesVerifyFault
=========================================
    :extends:

        `vim.fault.HostConnectFault`_

  MultipleCertificatesVerifyFault is thrown by the host connect method `ReconnectHost_Task`_ as well as the methods to add a host to VirtualCenter ( `AddStandaloneHost_Task`_ and `AddHost_Task`_ ) if VirtualCenter detects that the host has different SSL certificates for different management ports. This can occur, for example, if an ESX 2.x host has different SSL certificates for the authd service (port 902) and the Management UI port (port 443). VirtualCenter is not able to manage such hosts. To fix this issue, the user should modify the host to ensure there is only one certificate for all services. Alternatively, different certificates are allowed as long as each certificate is verifiable (trusted) by the VirtualCenter server.

Attributes:

    thumbprintData (`str`_)




