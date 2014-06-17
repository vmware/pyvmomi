.. _str: https://docs.python.org/2/library/stdtypes.html

.. _OptionValue: ../../vim/option/OptionValue.rst

.. _HostConfigSpec: ../../vim/host/ConfigSpec.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.MemorySpec: ../../vim/host/MemorySpec.rst

.. _vim.host.LicenseSpec: ../../vim/host/LicenseSpec.rst

.. _vim.host.SecuritySpec: ../../vim/host/SecuritySpec.rst

.. _vim.host.NetworkConfig: ../../vim/host/NetworkConfig.rst

.. _vim.host.ServiceConfig: ../../vim/host/ServiceConfig.rst

.. _vim.option.OptionValue: ../../vim/option/OptionValue.rst

.. _vim.host.FirewallConfig: ../../vim/host/FirewallConfig.rst

.. _vim.host.DateTimeConfig: ../../vim/host/DateTimeConfig.rst

.. _vim.host.NasVolume.Config: ../../vim/host/NasVolume/Config.rst

.. _vim.host.StorageDeviceInfo: ../../vim/host/StorageDeviceInfo.rst

.. _vim.host.ActiveDirectorySpec: ../../vim/host/ActiveDirectorySpec.rst

.. _vim.host.VirtualNicManager.NicTypeSelection: ../../vim/host/VirtualNicManager/NicTypeSelection.rst

.. _vim.host.LocalAccountManager.AccountSpecification: ../../vim/host/LocalAccountManager/AccountSpecification.rst


vim.host.ConfigSpec
===================
  The `HostConfigSpec`_ data object provides access to data objects that specify configuration changes to be applied to an ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    nasDatastore (`vim.host.NasVolume.Config`_, optional):

       Configurations to create NAS datastores.
    network (`vim.host.NetworkConfig`_, optional):

       Network system information.
    nicTypeSelection (`vim.host.VirtualNicManager.NicTypeSelection`_, optional):

       Type selection for different VirtualNics.
    service (`vim.host.ServiceConfig`_, optional):

       Host service configuration.
    firewall (`vim.host.FirewallConfig`_, optional):

       Firewall configuration.
    option (`vim.option.OptionValue`_, optional):

       Host configuration options as defined by the `OptionValue`_ data object type.
    datastorePrincipal (`str`_, optional):

       Datastore principal user.
    datastorePrincipalPasswd (`str`_, optional):

       Password for the datastore principal.
    datetime (`vim.host.DateTimeConfig`_, optional):

       DateTime Configuration.
    storageDevice (`vim.host.StorageDeviceInfo`_, optional):

       Storage system information.
    license (`vim.host.LicenseSpec`_, optional):

       License configuration for the host.
    security (`vim.host.SecuritySpec`_, optional):

       Security specification.
    userAccount (`vim.host.LocalAccountManager.AccountSpecification`_, optional):

       List of users to create/update with new password.
    usergroupAccount (`vim.host.LocalAccountManager.AccountSpecification`_, optional):

       List of users to create/update with new password.
    memory (`vim.host.MemorySpec`_, optional):

       Memory configuration for the host.
    activeDirectory (`vim.host.ActiveDirectorySpec`_, optional):

       Active Directory configuration change.
    genericConfig (`vmodl.KeyAnyValue`_, optional):

       Advanced configuration.
