
vim.UserDirectory
=================
  The `UserDirectory <vim/UserDirectory.rst>`_ managed object provides information about users and groups on a vSphere server and ESX hosts. The method `RetrieveUserGroups <vim/UserDirectory.rst#retrieveUserGroups>`_ returns a list of user account data. The method can perform a search operation based on specific criteria - user name, group name, sub-string or string matching, and, on Windows, domain. Use the results as input to the AuthorizationManager methods `SetEntityPermissions <vim/AuthorizationManager.rst#setEntityPermissions>`_ and `ResetEntityPermissions <vim/AuthorizationManager.rst#resetEntityPermissions>`_ .The content of the returned results depends on the server environment:
   * On a Windows host,
   * `RetrieveUserGroups <vim/UserDirectory.rst#retrieveUserGroups>`_
   * can search from the set of trusted domains on the host, including the primary domain of the system. A special domain (specified as an empty string -
   * ) refers to the users and groups local to the host.
   * On an ESX Server or a Linux host, the search operates on the users and groups defined in the /etc/passwd file. Always specify an empty string (
   * ) for the domain argument. If the /etc/passwd file contains Sun NIS or NIS+ users and groups, RetrieveUserGroups returns information about these accounts as well.
   * 




Attributes
----------
    domainList ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
      privilege: System.View
       List of Windows domains available for user searches, if the underlying system supports windows domain membership.


Methods
-------


RetrieveUserGroups(domain, searchStr, belongsToGroup, belongsToUser, exactMatch, findUsers, findGroups):
   Returns a list of `UserSearchResult <vim/UserSearchResult.rst>`_ objects describing the users and groups defined for the server.
    * On Windows, the search for users and groups is restricted to the given domain. If you omit the domain argument, then the search is performed on local users and groups.
    * On ESX Server (or Linux systems), the method returns the list of users and groups that are specified in the /etc/passwd file. If the password file contains Sun NIS or NIS+ users and groups, the returned list includes information about those as well.
    * 
    * You must hold the Authorization.ModifyPermissions privilege to invoke this method. If you hold the privilege on any ManagedEntity, you will have access to user and group information for the server.
    * 
    * As of vSphere API 5.1:
    * Local user groups on ESXi are not supported and this method will not return information about local groups on the ESXi host. Information about Active Directory groups is not affected.
    * Some special system users on ESXi like 'nfsnobody' and 'daemon' will be filtered out by this method.
    * 


  Privilege:
               dynamic



  Args:
    domain (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Domain to be searched. If not set, then the method searches the local machine.


    searchStr (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Case insensitive substring used to filter results; the search string is compared to the login and full name for users, and the name and description for groups. Leave this blank to match all users.


    belongsToGroup (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If present, the returned list contains only users or groups that directly belong to the specified group. Users or groups that have indirect membership will not be included in the list.


    belongsToUser (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       If present, the returned list contains only groups that directly contain the specified user. Groups that indirectly contain the user will not be included in the list.


    exactMatch (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Indicates the searchStr passed should match a user or group name exactly.


    findUsers (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       True, if users should be included in the result.


    findGroups (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       True, if groups should be included in the result.




  Returns:
    [`vim.UserSearchResult <vim/UserSearchResult.rst>`_]:
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If any of the domain, belongsToGroup, or belongsToUser arguments refer to entities that do not exist.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If you specify a domain for systems that do not support domains, such as an ESX Server. The method also throws NotSupported if you specify membership (belongsToGroup or belongsToUser) and the server does not support by-membership queries.


