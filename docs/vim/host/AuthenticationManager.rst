
vim.host.AuthenticationManager
==============================
  The `HostAuthenticationManager <vim/host/AuthenticationManager.rst>`_ managed object provides access to Active Directory configuration information for an ESX host. It also provides access to methods for adding a host to or removing a host from an Active Directory domain.The vSphere API supports Microsoft Active Directory management of authentication for ESX hosts. To integrate an ESX host into an Active Directory environment, you use an Active Directory account that has the authority to add a computer to a domain. The ESX Server locates the Active Directory domain controller. When you add a host to a domain, you only need to specify the domain and the account user name and password.There are two approaches that you can use to add an ESX host to or remove a host from an Active Directory domain.
   * `JoinDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#joinDomain>`_
   * and
   * `LeaveCurrentDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#leaveCurrentDomain>`_
   * methods - Your vSphere client application can call these methods directly to add the host to or remove the host from a domain.
   * Host configuration - Use the
   * `HostActiveDirectory <vim/host/ActiveDirectorySpec.rst>`_
   * data object to specify Active Directory configuration, either adding the host to or removing the host from a domain. To apply the Active Directory configuration, use the
   * `HostProfileManager <vim/profile/host/ProfileManager.rst>`_
   * method (
   * `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_
   * ) to apply the
   * `HostConfigSpec <vim/host/ConfigSpec.rst>`_
   * . When the ESX Server processes the configuration, it will invoke the join or leave method.To take advantage of ESX host membership in an Active Directory domain, grant permissions on the ESX host to Active Directory users and groups who should have direct access to management of the ESX host. Use the `UserDirectory <vim/UserDirectory.rst>`_ . `RetrieveUserGroups <vim/UserDirectory.rst#retrieveUserGroups>`_ method to obtain information about Active Directory users and groups. After retrieving the Active Directory data, you can use the `AuthorizationManager <vim/AuthorizationManager.rst>`_ . `SetEntityPermissions <vim/AuthorizationManager.rst#setEntityPermissions>`_ method to set the `principal <vim/AuthorizationManager/Permission.rst#principal>`_ property to the appropriate user or group.By default, the ESX host assigns the Administrator role to the "ESX Admins" group. If the group does not exist when the host joins the domain, the host will not assign the role. In this case, you must create the "ESX Admins" group in the Active Directory. The host will periodically check the domain controller for the group and will assign the role when the group exists.


:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


Attributes
----------
    info (`vim.host.AuthenticationManagerInfo <vim/host/AuthenticationManagerInfo.rst>`_):
       Information about Active Directory membership.
    supportedStore ([`vim.host.AuthenticationStore <vim/host/AuthenticationStore.rst>`_]):
       An array that can contain managed object references to local and Active Directory authentication managed objects.supportedStoredata implies a connection to a system that stores information about accounts. ThesupportedStorearray can include the following objects:
        * 
        * `HostLocalAuthentication <vim/host/LocalAuthentication.rst>`_
        * - Local authentication refers to user accounts on the ESX host. Local authentication is always enabled.
        * 
        * `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_
        * - Active Directory authentication refers to computer accounts and user accounts on the domain controller. This object indicates the domain membership status for the host and defines the join and leave methods for Active Directory membership.
        * If
        * supportedStore
        * references a
        * `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_
        * object, the host is capable of joining a domain. However, if you try to add a host to a domain when the
        * `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_
        * .
        * `enabled <vim/host/AuthenticationStoreInfo.rst#enabled>`_
        * property is
        * True
        * (accessed through the
        * info
        * property), the join method will throw a fault.


Methods
-------


