
vim.host.ConfigSpec
===================
  The `HostConfigSpec <vim/host/ConfigSpec.rst>`_ data object provides access to data objects that specify configuration changes to be applied to an ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    nasDatastore ([`vim.host.NasVolume.Config <vim/host/NasVolume/Config.rst>`_], optional):

       Configurations to create NAS datastores.
    network (`vim.host.NetworkConfig <vim/host/NetworkConfig.rst>`_, optional):

       Network system information.
    nicTypeSelection ([`vim.host.VirtualNicManager.NicTypeSelection <vim/host/VirtualNicManager/NicTypeSelection.rst>`_], optional):

       Type selection for different VirtualNics.
    service ([`vim.host.ServiceConfig <vim/host/ServiceConfig.rst>`_], optional):

       Host service configuration.
    firewall (`vim.host.FirewallConfig <vim/host/FirewallConfig.rst>`_, optional):

       Firewall configuration.
    option ([`vim.option.OptionValue <vim/option/OptionValue.rst>`_], optional):

       Host configuration options as defined by the `OptionValue <vim/option/OptionValue.rst>`_ data object type.
    datastorePrincipal (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Datastore principal user.
    datastorePrincipalPasswd (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Password for the datastore principal.
    datetime (`vim.host.DateTimeConfig <vim/host/DateTimeConfig.rst>`_, optional):

       DateTime Configuration.
    storageDevice (`vim.host.StorageDeviceInfo <vim/host/StorageDeviceInfo.rst>`_, optional):

       Storage system information.
    license (`vim.host.LicenseSpec <vim/host/LicenseSpec.rst>`_, optional):

       License configuration for the host.
    security (`vim.host.SecuritySpec <vim/host/SecuritySpec.rst>`_, optional):

       Security specification.
    userAccount ([`vim.host.LocalAccountManager.AccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_], optional):

       List of users to create/update with new password.
    usergroupAccount ([`vim.host.LocalAccountManager.AccountSpecification <vim/host/LocalAccountManager/AccountSpecification.rst>`_], optional):

       List of users to create/update with new password.
    memory (`vim.host.MemorySpec <vim/host/MemorySpec.rst>`_, optional):

       Memory configuration for the host.
    activeDirectory ([`vim.host.ActiveDirectorySpec <vim/host/ActiveDirectorySpec.rst>`_], optional):

       Active Directory configuration change.
    genericConfig ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       Advanced configuration.
