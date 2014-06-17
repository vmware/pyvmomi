.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Summary: ../../vim/vm/Summary.rst

.. _vim.host.Summary: ../../vim/host/Summary.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.ConnectInfo.NetworkInfo: ../../vim/host/ConnectInfo/NetworkInfo.rst

.. _vim.host.ConnectInfo.LicenseInfo: ../../vim/host/ConnectInfo/LicenseInfo.rst

.. _vim.host.ConnectInfo.DatastoreInfo: ../../vim/host/ConnectInfo/DatastoreInfo.rst


vim.host.ConnectInfo
====================
  This data object type contains information about a single host that can be used by the connection wizard. This can be returned without adding the host to VirtualCenter.
:extends: vmodl.DynamicData_

Attributes:
    serverIp (`str`_, optional):

       The IP address of the VirtualCenter already managing this host, if any.
    inDasCluster (`bool`_, optional):

       If the host is already being managed by a vCenter Server, this property reports true if the host is also part of a vSphere HA enabled cluster. If this is the case, remove or disconnect the host from this cluster before adding it to another vCenter Server.
    host (`vim.host.Summary`_):

       Summary information about the host. The status fields and managed object reference is not set when an object of this type is created. These fields and references are typically set later when these objects are associated with a host.
    vm (`vim.vm.Summary`_, optional):

       The list of virtual machines on the host.
    vimAccountNameRequired (`bool`_, optional):

       Whether or not the host requires a vimAccountName and password to be set in the ConnectSpec. This is normally only required for VMware Server hosts.
    clusterSupported (`bool`_, optional):

       Whether or not the host supports clustering capabilities such as HA or DRS and therefore can be added to a cluster. If false, the host must be added as a standalone host.
    network (`vim.host.ConnectInfo.NetworkInfo`_, optional):

       The list of network information for networks configured on this host.
    datastore (`vim.host.ConnectInfo.DatastoreInfo`_, optional):

       The list of datastores on the host.
    license (`vim.host.ConnectInfo.LicenseInfo`_, optional):

       License manager information on the host
