.. _enabled: ../../vim/host/AuthenticationStoreInfo.rst#enabled

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _HostLocalAuthentication: ../../vim/host/LocalAuthentication.rst

.. _HostAuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst

.. _vim.host.AuthenticationStore: ../../vim/host/AuthenticationStore.rst

.. _HostActiveDirectoryAuthentication: ../../vim/host/ActiveDirectoryAuthentication.rst

.. _vim.host.AuthenticationManagerInfo: ../../vim/host/AuthenticationManagerInfo.rst


vim.host.AuthenticationManager
==============================
  The `HostAuthenticationManager`_ managed object provides access to Active Directory configuration information for an ESX host. It also provides access to methods for adding a host to or removing a host from an Active Directory domain.The vSphere API supports Microsoft Active Directory management of authentication for ESX hosts. To integrate an ESX host into an Active Directory environment, you use an Active Directory account that has the authority to add a computer to a domain. The ESX Server locates the Active Directory domain controller. When you add a host to a domain, you only need to specify the domain and the account user name and password.There are two approaches that you can use to add an ESX host to or remove a host from an Active Directory domain.
   * `JoinDomain_Task`_
   * and
   * `LeaveCurrentDomain_Task`_
   * methods - Your vSphere client application can call these methods directly to add the host to or remove the host from a domain.
   * Host configuration - Use the
   * `HostActiveDirectory`_
   * data object to specify Active Directory configuration, either adding the host to or removing the host from a domain. To apply the Active Directory configuration, use the
   * `HostProfileManager`_
   * method (
   * `ApplyHostConfig_Task`_
   * ) to apply the
   * `HostConfigSpec`_
   * . When the ESX Server processes the configuration, it will invoke the join or leave method.To take advantage of ESX host membership in an Active Directory domain, grant permissions on the ESX host to Active Directory users and groups who should have direct access to management of the ESX host. Use the `UserDirectory`_ . `RetrieveUserGroups`_ method to obtain information about Active Directory users and groups. After retrieving the Active Directory data, you can use the `AuthorizationManager`_ . `SetEntityPermissions`_ method to set the `principal`_ property to the appropriate user or group.By default, the ESX host assigns the Administrator role to the "ESX Admins" group. If the group does not exist when the host joins the domain, the host will not assign the role. In this case, you must create the "ESX Admins" group in the Active Directory. The host will periodically check the domain controller for the group and will assign the role when the group exists.


:since: `vSphere API 4.1`_


Attributes
----------
    info (`vim.host.AuthenticationManagerInfo`_):
       Information about Active Directory membership.
    supportedStore ([`vim.host.AuthenticationStore`_]):
       An array that can contain managed object references to local and Active Directory authentication managed objects.supportedStoredata implies a connection to a system that stores information about accounts. ThesupportedStorearray can include the following objects:
        * 
        * `HostLocalAuthentication`_
        * - Local authentication refers to user accounts on the ESX host. Local authentication is always enabled.
        * 
        * `HostActiveDirectoryAuthentication`_
        * - Active Directory authentication refers to computer accounts and user accounts on the domain controller. This object indicates the domain membership status for the host and defines the join and leave methods for Active Directory membership.
        * If
        * supportedStore
        * references a
        * `HostActiveDirectoryAuthentication`_
        * object, the host is capable of joining a domain. However, if you try to add a host to a domain when the
        * `HostAuthenticationStoreInfo`_
        * .
        * `enabled`_
        * property is
        * True
        * (accessed through the
        * info
        * property), the join method will throw a fault.


Methods
-------


