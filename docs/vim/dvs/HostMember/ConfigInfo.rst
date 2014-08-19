
vim.dvs.HostMember.ConfigInfo
=============================
  The `DistributedVirtualSwitchHostMemberConfigInfo <vim/dvs/HostMember/ConfigInfo.rst>`_ data object contains membership configuration information for the ESXi host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):

       ESXi host. This property should always be set unless the user's setting does not have System.Read privilege on the object referred to by this property.
    maxProxySwitchPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of ports than can be created in the proxy switch.ESXi 5.0 and earlier hosts: If you change the maximum number of ports, you must reboot the host for the new value to take effect.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob <vim/dvs/KeyedOpaqueBlob.rst>`_], optional):

       Opaque binary blob that stores vendor specific configuration.
    backing (`vim.dvs.HostMember.Backing <vim/dvs/HostMember/Backing.rst>`_):

       Host membership backing, specifying physical NIC, portgroup, and port bindings for the proxy switch.
