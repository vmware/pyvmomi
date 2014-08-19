
vim.host.ActiveDirectorySpec
============================
  The `HostActiveDirectory <vim/host/ActiveDirectorySpec.rst>`_ data object contains Active Directory configuration information for an ESX host.The vSphere API supports Microsoft Active Directory management of authentication for ESX hosts. To integrate an ESX host into an Active Directory environment, you use an Active Directory account that has the authority to add a computer to a domain. The ESX Server locates the Active Directory domain controller. When you use the host profile to configure authentication for an ESX host, you specify the configuration operation (add or remove). To add the host to a domain, specify the domain, and the authorized Active Directory account user name and password. You do not need to specify these parameters to remove the host from a domain because the host has the information it needs to perform the operation. When you call `ApplyHostConfig_Task <vim/profile/host/ProfileManager.rst#applyHostConfiguration>`_ to apply the configuration, the ESX Server will call the appropriate method ( `JoinDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#joinDomain>`_ or `LeaveCurrentDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#leaveCurrentDomain>`_ ) on your behalf.Before you call the method to apply the host profile, check to see that the `HostAuthenticationManager <vim/host/AuthenticationManager.rst>`_ . `supportedStore <vim/host/AuthenticationManager.rst#supportedStore>`_ array contains a `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_ object. The presence of the Active Directory authentication object indicates that a host is capable of joining a domain. However, if you try to add a host to a domain when the `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_ . `enabled <vim/host/AuthenticationStoreInfo.rst#enabled>`_ property isTrue, the join method will throw a fault.As an alternative to using the host profile to configure Active Directory authentication for an ESX host, your vSphere client application can call the `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_ join and leave methods directly to add the host to or remove the host from a domain.To take advantage of ESX host membership in an Active Directory domain, grant permissions on the ESX host to users and groups in Active Directory who should have direct access to management of the ESX host. Use the `UserDirectory <vim/UserDirectory.rst>`_ . `RetrieveUserGroups <vim/UserDirectory.rst#retrieveUserGroups>`_ method to obtain information about Active Directory users and groups. After retrieving the Active Directory data, you can use the `AuthorizationManager <vim/AuthorizationManager.rst>`_ . `SetEntityPermissions <vim/AuthorizationManager.rst#setEntityPermissions>`_ method to set the `principal <vim/AuthorizationManager/Permission.rst#principal>`_ property to the appropriate user or group.By default, the ESX host assigns the Administrator role to the "ESX Admins" group. If the group does not exist when the host joins the domain, the host will not assign the role. In this case, you must create the "ESX Admins" group in the Active Directory. The host will periodically check the domain controller for the group and will assign the role when the group exists.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Configuration change operation to apply to the host. You can specify the following values:
        * 
        * `add <vim/host/ConfigChange/Operation.rst#add>`_
        * : Add the host to the domain. The ESX Server will use the
        * `HostActiveDirectorySpec <vim/host/ActiveDirectorySpec/Specification.rst>`_
        * information (domain, account user name and password) to call
        * `JoinDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#joinDomain>`_
        * .
        * 
        * `remove <vim/host/ConfigChange/Operation.rst#remove>`_
        * : Remove the host from its current domain. The ESX Server will call
        * `LeaveCurrentDomain_Task <vim/host/ActiveDirectoryAuthentication.rst#leaveCurrentDomain>`_
        * , specifying
        * True
        * for the
        * force
        * parameter to delete existing permissions.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    spec (`vim.host.ActiveDirectorySpec.Specification <vim/host/ActiveDirectorySpec/Specification.rst>`_, optional):

       Active Directory domain access information (domain and account user name and password).
