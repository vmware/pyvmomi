.. _host: ../../../vim/dvs/HostMember/ConfigSpec.rst#host

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.dvs.HostMember.Backing: ../../../vim/dvs/HostMember/Backing.rst

.. _vim.dvs.HostMember.PnicSpec: ../../../vim/dvs/HostMember/PnicSpec.rst

.. _DistributedVirtualSwitchHostMemberConfigSpec: ../../../vim/dvs/HostMember/ConfigSpec.rst

.. _DistributedVirtualSwitchHostMemberPnicBacking: ../../../vim/dvs/HostMember/PnicBacking.rst


vim.dvs.HostMember.PnicBacking
==============================
  The `DistributedVirtualSwitchHostMemberPnicBacking`_ data object specifies a set of physical NICs to use for a proxy switch. When you add a host to a distributed virtual switch ( `DistributedVirtualSwitchHostMemberConfigSpec`_ . `host`_ ), the host creates a proxy switch that will use the pNICs as uplinks.
:extends: vim.dvs.HostMember.Backing_
:since: `vSphere API 4.0`_

Attributes:
    pnicSpec (`vim.dvs.HostMember.PnicSpec`_, optional):

       List of physical NIC specifications. Each entry identifies a pNIC to the proxy switch and optionally specifies uplink portgroup and port connections for the pNIC.
