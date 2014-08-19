
vim.LicenseAssignmentManager
============================
  


:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------


Methods
-------


UpdateAssignedLicense(entity, licenseKey, entityDisplayName):
   Update the license associated with an entity


  Privilege:
               Global.Licenses



  Args:
    entity (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       ID of the entity. E.g. HostSystem.


    licenseKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       A license.


    entityDisplayName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Display name for the entity




  Returns:
    `vim.LicenseManager.LicenseInfo <vim/LicenseManager/LicenseInfo.rst>`_:
         Returns information about the license specified in licenseKey

  Raises:

    `vim.fault.LicenseEntityNotFound <vim/fault/LicenseEntityNotFound.rst>`_: 
       vim.fault.LicenseEntityNotFound


RemoveAssignedLicense(entityId):
   Remove licenses associated with an entity


  Privilege:
               Global.Licenses



  Args:
    entityId (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       ID of the entity. E.g. HostSystem.




  Returns:
    None
         

  Raises:

    `vim.fault.LicenseEntityNotFound <vim/fault/LicenseEntityNotFound.rst>`_: 
       vim.fault.LicenseEntityNotFound


QueryAssignedLicenses(entityId):
   Get information about all the licenses associated with an entity


  Privilege:
               System.View



  Args:
    entityId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       ID of the entity. E.g. HostSystem.




  Returns:
    [`vim.LicenseAssignmentManager.LicenseAssignment <vim/LicenseAssignmentManager/LicenseAssignment.rst>`_]:
         


