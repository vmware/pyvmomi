
vim.dvs.HostMember
==================
  The `DistributedVirtualSwitchHostMember <vim/dvs/HostMember.rst>`_ data object represents an ESXi host that is a member of a distributed virtual switch. When you add a host to a switch ( `DistributedVirtualSwitchHostMemberConfigSpec <vim/dvs/HostMember/ConfigSpec.rst>`_ . `host <vim/dvs/HostMember/ConfigSpec.rst#host>`_ ), the Server creates a proxy switch ( `HostProxySwitch <vim/host/HostProxySwitch.rst>`_ ). The host member object contains information about the configuration and state of the proxy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    runtimeState (`vim.dvs.HostMember.RuntimeState <vim/dvs/HostMember/RuntimeState.rst>`_, optional):

       Host member runtime state.
    config (`vim.dvs.HostMember.ConfigInfo <vim/dvs/HostMember/ConfigInfo.rst>`_):

       Host member configuration.
    productInfo (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):

       Vendor, product and version information for the proxy switch module.
    uplinkPortKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Port keys of the uplink ports created for the host member. These ports will be deleted after the host leaves the switch.
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The host DistributedVirtualSwitch component status. See `HostComponentState <vim/dvs/HostMember/HostComponentState.rst>`_ for valid values.
    statusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Additional information regarding the host's current status.
