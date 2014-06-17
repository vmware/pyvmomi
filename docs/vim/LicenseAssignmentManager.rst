.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.LicenseManager.LicenseInfo: ../vim/LicenseManager/LicenseInfo.rst

.. _vim.fault.LicenseEntityNotFound: ../vim/fault/LicenseEntityNotFound.rst

.. _vim.LicenseAssignmentManager.LicenseAssignment: ../vim/LicenseAssignmentManager/LicenseAssignment.rst


vim.LicenseAssignmentManager
============================
  


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


UpdateAssignedLicense(entity, licenseKey, entityDisplayName):
   Update the license associated with an entity


  Privilege:
               Global.Licenses



  Args:
    entity (`str`_):
       ID of the entity. E.g. HostSystem.


    licenseKey (`str`_):
       A license.


    entityDisplayName (`str`_, optional):
       Display name for the entity




  Returns:
    `vim.LicenseManager.LicenseInfo`_:
         Returns information about the license specified in licenseKey

  Raises:

    `vim.fault.LicenseEntityNotFound`_: 
       vim.fault.LicenseEntityNotFound


RemoveAssignedLicense(entityId):
   Remove licenses associated with an entity


  Privilege:
               Global.Licenses



  Args:
    entityId (`str`_):
       ID of the entity. E.g. HostSystem.




  Returns:
    None
         

  Raises:

    `vim.fault.LicenseEntityNotFound`_: 
       vim.fault.LicenseEntityNotFound


QueryAssignedLicenses(entityId):
   Get information about all the licenses associated with an entity


  Privilege:
               System.View



  Args:
    entityId (`str`_, optional):
       ID of the entity. E.g. HostSystem.




  Returns:
    `vim.LicenseAssignmentManager.LicenseAssignment`_:
         


