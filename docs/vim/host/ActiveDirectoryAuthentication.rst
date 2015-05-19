.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _enabled: ../../vim/host/AuthenticationStoreInfo.rst#enabled

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.fault.ClockSkew: ../../vim/fault/ClockSkew.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.InvalidLogin: ../../vim/fault/InvalidLogin.rst

.. _vim.fault.FileNotFound: ../../vim/fault/FileNotFound.rst

.. _vim.host.DirectoryStore: ../../vim/host/DirectoryStore.rst

.. _vim.fault.DomainNotFound: ../../vim/fault/DomainNotFound.rst

.. _vim.fault.TaskInProgress: ../../vim/fault/TaskInProgress.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.fault.InvalidHostName: ../../vim/fault/InvalidHostName.rst

.. _vim.fault.NoPermissionOnAD: ../../vim/fault/NoPermissionOnAD.rst

.. _vim.fault.InvalidCAMServer: ../../vim/fault/InvalidCAMServer.rst

.. _vim.fault.NonADUserRequired: ../../vim/fault/NonADUserRequired.rst

.. _vim.fault.BlockedByFirewall: ../../vim/fault/BlockedByFirewall.rst

.. _HostAuthenticationStoreInfo: ../../vim/host/AuthenticationStoreInfo.rst

.. _vim.fault.ActiveDirectoryFault: ../../vim/fault/ActiveDirectoryFault.rst

.. _vim.fault.InvalidCAMCertificate: ../../vim/fault/InvalidCAMCertificate.rst

.. _vim.fault.AuthMinimumAdminPermission: ../../vim/fault/AuthMinimumAdminPermission.rst

.. _vim.fault.CAMServerRefusedConnection: ../../vim/fault/CAMServerRefusedConnection.rst


vim.host.ActiveDirectoryAuthentication
======================================
  The `HostActiveDirectoryAuthentication`_ managed object indicates domain membership status and provides methods for adding a host to and removing a host from a domain.


:extends: vim.host.DirectoryStore_
:since: `vSphere API 4.1`_


Attributes
----------


Methods
-------


JoinDomain(domainName, userName, password):
   Adds the host to an Active Directory domain.If the `HostAuthenticationStoreInfo`_ . `enabled`_ property isTrue(accessed through theinfoproperty), the host has joined a domain. The vSphere API will throw theInvalidStatefault if you try to add a host to a domain when the host has already joined a domain.


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    domainName (`str`_):
       Name of the domain to be joined.


    userName (`str`_):
       Name for an Active Directory account that has the authority to add hosts to the domain.


    password (`str`_):
       Password for theuserNameaccount.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host has already joined a domain.

    `vim.fault.HostConfigFault`_: 
       if the host configuration prevents the join operation from succeeding.

    `vim.fault.InvalidLogin`_: 
       ifuserNameandpasswordare not valid user credentials.

    `vim.fault.ActiveDirectoryFault`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.TaskInProgress`_: 
       if the `HostActiveDirectoryAuthentication`_ object is busy.

    `vim.fault.BlockedByFirewall`_: 
       if ports needed by the join operation are blocked by the firewall.

    `vim.fault.DomainNotFound`_: 
       if the domain controller fordomainNamecannot be reached.

    `vim.fault.NoPermissionOnAD`_: 
       ifuserNamehas no right to add hosts to the domain.

    `vim.fault.InvalidHostName`_: 
       if the domain part of the host's FQDN doesn't match the domain being joined.

    `vim.fault.ClockSkew`_: 
       if the clocks of the host and the domain controller differ by more than the allowed amount of time.


JoinDomainWithCAM(domainName, camServer):
   Adds the host to an Active Directory domain through CAM service.If the `HostAuthenticationStoreInfo`_ . `enabled`_ property isTrue(accessed through theinfoproperty), the host has joined a domain. The vSphere API will throw theInvalidStatefault if you try to add a host to a domain when the host has already joined a domain.
  since: `vSphere API 5.0`_


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    domainName (`str`_):
       Name of the domain to be joined.


    camServer (`str`_):
       Name of server providing the CAM service.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host has already joined a domain.

    `vim.fault.HostConfigFault`_: 
       if the host configuration prevents the join operation from succeeding.

    `vim.fault.ActiveDirectoryFault`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.TaskInProgress`_: 
       if the `HostActiveDirectoryAuthentication`_ object is busy.

    `vim.fault.BlockedByFirewall`_: 
       if ports needed by the join operation are blocked by the firewall.

    `vim.fault.DomainNotFound`_: 
       if the domain controller fordomainNamecannot be reached.

    `vim.fault.InvalidHostName`_: 
       if the domain part of the host's FQDN doesn't match the domain being joined.

    `vim.fault.ClockSkew`_: 
       if the clocks of the host and the domain controller differ by more than the allowed amount of time.

    `vim.fault.InvalidCAMServer`_: 
       if camServer is not a valid IP address, or if camServer is not accessible.

    `vim.fault.InvalidCAMCertificate`_: 
       if the certificate of the given CAM server cannot be verified.

    `vim.fault.CAMServerRefusedConnection`_: 
       if the specified CAM server is not reachable, or if the server denied access.


ImportCertificateForCAM(certPath, camServer):
   Import the CAM server's certificate to the local store of vmwauth.The certificate should have already been uploaded to ESXi file system.
  since: `vSphere API 5.0`_


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    certPath (`str`_):
       full path of the certificate on ESXi


    camServer (`str`_):
       IP of server providing the CAM service.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.FileNotFound`_: 
       if the certificate file does not exist

    `vim.fault.ActiveDirectoryFault`_: 
       for any problem that is not handled with a more specific fault.

    `vim.fault.InvalidCAMServer`_: 
       if camServer is not a valid IP address


LeaveCurrentDomain(force):
   Removes the host from the Active Directory domain to which it belongs.


  Privilege:
               Host.Config.AuthenticationStore



  Args:
    force (`bool`_):
       IfTrue, any existing permissions on managed entities for Active Directory users will be deleted. IfFalseand such permissions exist, the operation will fail.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host is not in a domain or there are active permissions for Active Directory users.

    `vim.fault.AuthMinimumAdminPermission`_: 
       if this change would leave the system with no Administrator permission on the root node.

    `vim.fault.ActiveDirectoryFault`_: 
       for any problem that is not handled with a specific fault.

    `vim.fault.TaskInProgress`_: 
       if the ActiveDirectoryAuthentication object is busy.

    `vim.fault.NonADUserRequired`_: 
       only non Active Directory users can initiate the leave domain operation.


