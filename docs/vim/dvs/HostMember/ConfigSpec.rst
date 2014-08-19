
vim.dvs.HostMember.ConfigSpec
=============================
  Specification to create or reconfigure ESXi host membership in a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Host member operation type. See `ConfigSpecOperation <vim/ConfigSpecOperation.rst>`_ for valid values.
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       Identifies a host member of a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ for a `CreateDVS_Task <vim/Folder.rst#createDistributedVirtualSwitch>`_ or `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ . `ReconfigureDvs_Task <vim/DistributedVirtualSwitch.rst#reconfigure>`_ operation.
    backing (`vim.dvs.HostMember.Backing <vim/dvs/HostMember/Backing.rst>`_, optional):

       Specifies the physical NICs to use as backing for the proxy switch on the host.
    maxProxySwitchPorts (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Maximum number of ports allowed in the `HostProxySwitch <vim/host/HostProxySwitch.rst>`_ .ESXi 5.0 and earlier hosts: If you are reconfiguring an existing host membership, that is, the proxy switch already exists, you must reboot the host for the new setting to take effect.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob <vim/dvs/KeyedOpaqueBlob.rst>`_], optional):

       Opaque binary blob that stores vendor specific configuration.
