.. _str: https://docs.python.org/2/library/stdtypes.html

.. _host: ../../vim/dvs/HostMember/ConfigSpec.rst#host

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _HostProxySwitch: ../../vim/host/HostProxySwitch.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostComponentState: ../../vim/dvs/HostMember/HostComponentState.rst

.. _vim.dvs.ProductSpec: ../../vim/dvs/ProductSpec.rst

.. _vim.dvs.HostMember.ConfigInfo: ../../vim/dvs/HostMember/ConfigInfo.rst

.. _vim.dvs.HostMember.RuntimeState: ../../vim/dvs/HostMember/RuntimeState.rst

.. _DistributedVirtualSwitchHostMember: ../../vim/dvs/HostMember.rst

.. _DistributedVirtualSwitchHostMemberConfigSpec: ../../vim/dvs/HostMember/ConfigSpec.rst


vim.dvs.HostMember
==================
  The `DistributedVirtualSwitchHostMember`_ data object represents an ESXi host that is a member of a distributed virtual switch. When you add a host to a switch ( `DistributedVirtualSwitchHostMemberConfigSpec`_ . `host`_ ), the Server creates a proxy switch ( `HostProxySwitch`_ ). The host member object contains information about the configuration and state of the proxy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    runtimeState (`vim.dvs.HostMember.RuntimeState`_, optional):

       Host member runtime state.
    config (`vim.dvs.HostMember.ConfigInfo`_):

       Host member configuration.
    productInfo (`vim.dvs.ProductSpec`_, optional):

       Vendor, product and version information for the proxy switch module.
    uplinkPortKey (`str`_, optional):

       Port keys of the uplink ports created for the host member. These ports will be deleted after the host leaves the switch.
    status (`str`_):

       The host DistributedVirtualSwitch component status. See `HostComponentState`_ for valid values.
    statusDetail (`str`_, optional):

       Additional information regarding the host's current status.
