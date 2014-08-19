
vim.host.ActiveDirectoryAuthentication
======================================
  The `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_ managed object indicates domain membership status and provides methods for adding a host to and removing a host from a domain.


:extends: vim.host.DirectoryStore_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


Attributes
----------


Methods
-------


JoinDomain(domainName, userName, password):
   Adds the host to an Active Directory domain.If the `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_ . `enabled <vim/host/AuthenticationStoreInfo.rst#enabled>`_ property isTrue(accessed through theinfoproperty), the host has joined a domain. The vSphere API will throw theInvalidStatefault if you try to add a host to a domain when the host has already joined a domain.


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    domainName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of the domain to be joined.


    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name for an Active Directory account that has the authority to add hosts to the domain.


    password (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Password for theuserNameaccount.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host has already joined a domain.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the host configuration prevents the join operation from succeeding.

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       ifuserNameandpasswordare not valid user credentials.

    `vim.fault.ActiveDirectoryFault <vim/fault/ActiveDirectoryFault.rst>`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_ object is busy.

    `vim.fault.BlockedByFirewall <vim/fault/BlockedByFirewall.rst>`_: 
       if ports needed by the join operation are blocked by the firewall.

    `vim.fault.DomainNotFound <vim/fault/DomainNotFound.rst>`_: 
       if the domain controller fordomainNamecannot be reached.

    `vim.fault.NoPermissionOnAD <vim/fault/NoPermissionOnAD.rst>`_: 
       ifuserNamehas no right to add hosts to the domain.

    `vim.fault.InvalidHostName <vim/fault/InvalidHostName.rst>`_: 
       if the domain part of the host's FQDN doesn't match the domain being joined.

    `vim.fault.ClockSkew <vim/fault/ClockSkew.rst>`_: 
       if the clocks of the host and the domain controller differ by more than the allowed amount of time.


JoinDomainWithCAM(domainName, camServer):
   Adds the host to an Active Directory domain through CAM service.If the `HostAuthenticationStoreInfo <vim/host/AuthenticationStoreInfo.rst>`_ . `enabled <vim/host/AuthenticationStoreInfo.rst#enabled>`_ property isTrue(accessed through theinfoproperty), the host has joined a domain. The vSphere API will throw theInvalidStatefault if you try to add a host to a domain when the host has already joined a domain.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    domainName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of the domain to be joined.


    camServer (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of server providing the CAM service.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host has already joined a domain.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if the host configuration prevents the join operation from succeeding.

    `vim.fault.ActiveDirectoryFault <vim/fault/ActiveDirectoryFault.rst>`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the `HostActiveDirectoryAuthentication <vim/host/ActiveDirectoryAuthentication.rst>`_ object is busy.

    `vim.fault.BlockedByFirewall <vim/fault/BlockedByFirewall.rst>`_: 
       if ports needed by the join operation are blocked by the firewall.

    `vim.fault.DomainNotFound <vim/fault/DomainNotFound.rst>`_: 
       if the domain controller fordomainNamecannot be reached.

    `vim.fault.InvalidHostName <vim/fault/InvalidHostName.rst>`_: 
       if the domain part of the host's FQDN doesn't match the domain being joined.

    `vim.fault.ClockSkew <vim/fault/ClockSkew.rst>`_: 
       if the clocks of the host and the domain controller differ by more than the allowed amount of time.

    `vim.fault.InvalidCAMServer <vim/fault/InvalidCAMServer.rst>`_: 
       if camServer is not a valid IP address, or if camServer is not accessible.

    `vim.fault.InvalidCAMCertificate <vim/fault/InvalidCAMCertificate.rst>`_: 
       if the certificate of the given CAM server cannot be verified.

    `vim.fault.CAMServerRefusedConnection <vim/fault/CAMServerRefusedConnection.rst>`_: 
       if the specified CAM server is not reachable, or if the server denied access.


ImportCertificateForCAM(certPath, camServer):
   Import the CAM server's certificate to the local store of vmwauth.The certificate should have already been uploaded to ESXi file system.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    certPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       full path of the certificate on ESXi


    camServer (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       IP of server providing the CAM service.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the certificate file does not exist

    `vim.fault.ActiveDirectoryFault <vim/fault/ActiveDirectoryFault.rst>`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.InvalidCAMServer <vim/fault/InvalidCAMServer.rst>`_: 
       if camServer is not a valid IP address


LeaveCurrentDomain(force):
   Removes the host from the Active Directory domain to which it belongs.


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       IfTrue, any existing permissions on managed entities for Active Directory users will be deleted. IfFalseand such permissions exist, the operation will fail.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is not in a domain or there are active permissions for Active Directory users.

    `vim.fault.AuthMinimumAdminPermission <vim/fault/AuthMinimumAdminPermission.rst>`_: 
       if this change would leave the system with no Administrator permission on the root node.

    `vim.fault.ActiveDirectoryFault <vim/fault/ActiveDirectoryFault.rst>`_: 
       for any problem that is not handled with a specific fault.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if the ActiveDirectoryAuthentication object is busy.

    `vim.fault.NonADUserRequired <vim/fault/NonADUserRequired.rst>`_: 
       only non Active Directory users can initiate the leave domain operation.


