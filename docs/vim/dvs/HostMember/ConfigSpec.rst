.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _CreateDVS_Task: ../../../vim/Folder.rst#createDistributedVirtualSwitch

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _HostProxySwitch: ../../../vim/host/HostProxySwitch.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _ReconfigureDvs_Task: ../../../vim/DistributedVirtualSwitch.rst#reconfigure

.. _vim.dvs.KeyedOpaqueBlob: ../../../vim/dvs/KeyedOpaqueBlob.rst

.. _DistributedVirtualSwitch: ../../../vim/DistributedVirtualSwitch.rst

.. _vim.dvs.HostMember.Backing: ../../../vim/dvs/HostMember/Backing.rst


vim.dvs.HostMember.ConfigSpec
=============================
  Specification to create or reconfigure ESXi host membership in a `DistributedVirtualSwitch`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    operation (`str`_):

       Host member operation type. See `ConfigSpecOperation`_ for valid values.
    host (`vim.HostSystem`_):

       Identifies a host member of a `DistributedVirtualSwitch`_ for a `CreateDVS_Task`_ or `DistributedVirtualSwitch`_ . `ReconfigureDvs_Task`_ operation.
    backing (`vim.dvs.HostMember.Backing`_, optional):

       Specifies the physical NICs to use as backing for the proxy switch on the host.
    maxProxySwitchPorts (`int`_, optional):

       Maximum number of ports allowed in the `HostProxySwitch`_ .ESXi 5.0 and earlier hosts: If you are reconfiguring an existing host membership, that is, the proxy switch already exists, you must reboot the host for the new setting to take effect.
    vendorSpecificConfig ([`vim.dvs.KeyedOpaqueBlob`_], optional):

       Opaque binary blob that stores vendor specific configuration.
