.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _HostApplyProfile: ../../../vim/profile/host/HostApplyProfile.rst

.. _ExecuteHostProfile: ../../../vim/profile/host/HostProfile.rst#execute

.. _ApplyHostConfig_Task: ../../../vim/profile/host/ProfileManager.rst#applyHostConfiguration

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.UserProfile: ../../../vim/profile/host/UserProfile.rst

.. _vim.profile.host.OptionProfile: ../../../vim/profile/host/OptionProfile.rst

.. _vim.profile.host.ServiceProfile: ../../../vim/profile/host/ServiceProfile.rst

.. _vim.profile.host.NetworkProfile: ../../../vim/profile/host/NetworkProfile.rst

.. _vim.profile.host.StorageProfile: ../../../vim/profile/host/StorageProfile.rst

.. _vim.profile.host.SecurityProfile: ../../../vim/profile/host/SecurityProfile.rst

.. _vim.profile.host.FirewallProfile: ../../../vim/profile/host/FirewallProfile.rst

.. _vim.profile.host.DateTimeProfile: ../../../vim/profile/host/DateTimeProfile.rst

.. _vim.profile.host.UserGroupProfile: ../../../vim/profile/host/UserGroupProfile.rst

.. _vim.profile.host.HostMemoryProfile: ../../../vim/profile/host/HostMemoryProfile.rst

.. _vim.profile.host.AuthenticationProfile: ../../../vim/profile/host/AuthenticationProfile.rst


vim.profile.host.HostApplyProfile
=================================
  The `HostApplyProfile`_ data object provides access to subprofiles that contain configuration data for different host capabilities. The Profile Engine will use any configuration data that you supply to overwrite the host configuration. See the `ExecuteHostProfile`_ and `ApplyHostConfig_Task`_ methods.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    memory (`vim.profile.host.HostMemoryProfile`_, optional):

       Memory configuration for the host. This may not be valid for all versions of the host.
    storage (`vim.profile.host.StorageProfile`_, optional):

       Host storage configuration.
    network (`vim.profile.host.NetworkProfile`_, optional):

       Network configuration.
    datetime (`vim.profile.host.DateTimeProfile`_, optional):

       Date and time configuration.
    firewall (`vim.profile.host.FirewallProfile`_, optional):

       Firewall configuration.
    security (`vim.profile.host.SecurityProfile`_, optional):

       Security Configuration of the host. The security subprofile can include data such as administrator passwords.
    service ([`vim.profile.host.ServiceProfile`_], optional):

       Host configuration for services. Use the `key`_ property to access a subprofile in the list.
    option ([`vim.profile.host.OptionProfile`_], optional):

       List of subprofiles representing advanced configuration options. Use the `key`_ property to access a subprofile in the list.
    userAccount ([`vim.profile.host.UserProfile`_], optional):

       List of subprofiles for user accounts to be configured on the host. Use the `key`_ property to access a subprofile in the list.
    usergroupAccount ([`vim.profile.host.UserGroupProfile`_], optional):

       List of subprofiles for user groups to be configured on the host. Use the `key`_ property to access a subprofile in the list.
    authentication (`vim.profile.host.AuthenticationProfile`_, optional):

       Authentication Configuration.
