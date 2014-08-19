
vim.profile.host.HostApplyProfile
=================================
  The `HostApplyProfile <vim/profile/host/HostApplyProfile.rst>`_ data object provides access to subprofiles that contain configuration data for different host capabilities. The Profile Engine will use any configuration data that you supply to overwrite the host configuration. See the `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ and `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_ methods.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    memory (`vim.profile.host.HostMemoryProfile <vim/profile/host/HostMemoryProfile.rst>`_, optional):

       Memory configuration for the host. This may not be valid for all versions of the host.
    storage (`vim.profile.host.StorageProfile <vim/profile/host/StorageProfile.rst>`_, optional):

       Host storage configuration.
    network (`vim.profile.host.NetworkProfile <vim/profile/host/NetworkProfile.rst>`_, optional):

       Network configuration.
    datetime (`vim.profile.host.DateTimeProfile <vim/profile/host/DateTimeProfile.rst>`_, optional):

       Date and time configuration.
    firewall (`vim.profile.host.FirewallProfile <vim/profile/host/FirewallProfile.rst>`_, optional):

       Firewall configuration.
    security (`vim.profile.host.SecurityProfile <vim/profile/host/SecurityProfile.rst>`_, optional):

       Security Configuration of the host. The security subprofile can include data such as administrator passwords.
    service ([`vim.profile.host.ServiceProfile <vim/profile/host/ServiceProfile.rst>`_], optional):

       Host configuration for services. Use the `key <vim/profile/host/ServiceProfile.rst#key>`_ property to access a subprofile in the list.
    option ([`vim.profile.host.OptionProfile <vim/profile/host/OptionProfile.rst>`_], optional):

       List of subprofiles representing advanced configuration options. Use the `key <vim/profile/host/OptionProfile.rst#key>`_ property to access a subprofile in the list.
    userAccount ([`vim.profile.host.UserProfile <vim/profile/host/UserProfile.rst>`_], optional):

       List of subprofiles for user accounts to be configured on the host. Use the `key <vim/profile/host/UserProfile.rst#key>`_ property to access a subprofile in the list.
    usergroupAccount ([`vim.profile.host.UserGroupProfile <vim/profile/host/UserGroupProfile.rst>`_], optional):

       List of subprofiles for user groups to be configured on the host. Use the `key <vim/profile/host/UserGroupProfile.rst#key>`_ property to access a subprofile in the list.
    authentication (`vim.profile.host.AuthenticationProfile <vim/profile/host/AuthenticationProfile.rst>`_, optional):

       Authentication Configuration.
