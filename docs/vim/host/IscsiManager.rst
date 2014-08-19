
vim.host.IscsiManager
=====================
  This managed object provides interfaces for mapping VMkernel NIC to iSCSI Host Bus Adapter.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------


Methods
-------


QueryVnicStatus(vnicDevice):
   Query the status of Virtual NIC association with the iSCSI.


  Privilege:
               Host.Config.Storage



  Args:
    vnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Virtual NIC device to check the status for




  Returns:
    `vim.host.IscsiManager.IscsiStatus <vim/host/IscsiManager/IscsiStatus.rst>`_:
         A status object IscsiStatus, containing list of the fault codes, providing the user with information as to whether Virtual NIC is used by iSCSI and list of compliance check failure codes if any. The returned IscsiStatus object will have an array of MethodFault objects providing following information:
          * Empty IscsiStatus (i.e reason unset) if Virtual NIC device is not used.
          * Fault code IscsiFaultVnicInUse if Virtual NIC is being used by iSCSI.
          * This will be followed with list of fault codes corresponding to the compliance check failures.

  Raises:

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.


QueryPnicStatus(pnicDevice):
   Query if Physical NIC device is used for iSCSI.


  Privilege:
               Host.Config.Storage



  Args:
    pnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Physical NIC device name to check the status for




  Returns:
    `vim.host.IscsiManager.IscsiStatus <vim/host/IscsiManager/IscsiStatus.rst>`_:
         A status object, IscsiStatus, indicating whether Physical NIC is used by iSCSI or not.
          * Empty IscsiStatus (i.e reason unset) if Physical NIC device is not used.
          * Fault code IscsiFaultPnicInUse if Physical NIC is being used.

  Raises:

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.


QueryBoundVnics(iScsiHbaName):
   Query the list of Virtual NICs that are bound to a given iSCSI HBA.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       iSCSI adapter name for which the method to be applied.




  Returns:
    [`vim.host.IscsiManager.IscsiPortInfo <vim/host/IscsiManager/IscsiPortInfo.rst>`_]:
         An array of IscsiPortInfo containing detailed information on the list of Virtual NICs bound to the adapter

  Raises:

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If the given HBA is not found


QueryCandidateNics(iScsiHbaName):
   Query the candidate Virtual NICs and Physical NICs that can be used for Port-Binding. For dependent offload adapters, the Virtual NIC should be attached to the physical NIC associated with the hardware function.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       iSCSI Adapter name for which the method to be applied.




  Returns:
    [`vim.host.IscsiManager.IscsiPortInfo <vim/host/IscsiManager/IscsiPortInfo.rst>`_]:
         Array of IscsiPortInfo containing detailed information on list of eligible Virtual NICs that can be bound to the adapter. This list will also include details on the eligible Physical NICs that are not associated with any Virtual NICs.

  Raises:

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If the given HBA is not found


BindVnic(iScsiHbaName, vnicDevice):
   Bind a Virtual NIC to be used for an iSCSI adapter


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       iSCSI adapter name for which the Virtual NIC to be added.


    vnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Virtual NIC that is to be bound to the iSCSI HBA




  Returns:
    None
         

  Raises:

    `vim.fault.IscsiFaultVnicAlreadyBound <vim/fault/IscsiFaultVnicAlreadyBound.rst>`_: 
       The given Virtual NIC is already bound to the HBA.

    `vim.fault.IscsiFaultVnicHasNoUplinks <vim/fault/IscsiFaultVnicHasNoUplinks.rst>`_: 
       The given Virtual NIC has no physical uplinks.

    `vim.fault.IscsiFaultVnicHasMultipleUplinks <vim/fault/IscsiFaultVnicHasMultipleUplinks.rst>`_: 
       The given Virtual NIC has multiple uplinks.

    `vim.fault.IscsiFaultVnicHasWrongUplink <vim/fault/IscsiFaultVnicHasWrongUplink.rst>`_: 
       The given Virtual NIC has the wrong uplink and it can't be used for iSCSI multi-pathing.

    `vim.fault.IscsiFaultVnicNotFound <vim/fault/IscsiFaultVnicNotFound.rst>`_: 
       The given Virtual NIC is not present on the system.

    `vim.fault.IscsiFaultInvalidVnic <vim/fault/IscsiFaultInvalidVnic.rst>`_: 
       The given Virtual NIC is not valid for the HBA.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       For platform error that occurs during the operation.

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If the given HBA is not found


UnbindVnic(iScsiHbaName, vnicDevice, force):
   Unbind Virtual NIC binding from an iSCSI adapter.


  Privilege:
               Host.Config.Storage



  Args:
    iScsiHbaName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       iSCSI adapter name for which the Virtual NIC to be removed.


    vnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Virtual NIC that is to be removed from the iSCSI HBA


    force (`bool <https://docs.python.org/2/library/stdtypes.html>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.IscsiFaultVnicNotBound <vim/fault/IscsiFaultVnicNotBound.rst>`_: 
       The given Virtual NIC is not bound to the adapter

    `vim.fault.IscsiFaultVnicHasActivePaths <vim/fault/IscsiFaultVnicHasActivePaths.rst>`_: 
       The given Virtual NIC is associated with "active" paths to the storage.

    `vim.fault.IscsiFaultVnicIsLastPath <vim/fault/IscsiFaultVnicIsLastPath.rst>`_: 
       The given Virtual NIC is associated with "only" paths to the storage.

    `vim.fault.PlatformConfigFault <vim/fault/PlatformConfigFault.rst>`_: 
       For platform error that occurs during the operation.

    `vim.fault.IscsiFault <vim/fault/IscsiFault.rst>`_: 
       For any problem that is not handled with a more specific fault.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       If the given HBA is not found


QueryMigrationDependencies(pnicDevice):
   Query the dependency table for a migration operation of a given Physical NIC.


  Privilege:
               Host.Config.Storage



  Args:
    pnicDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       List of Physical NICs to be migrated




  Returns:
    `vim.host.IscsiManager.IscsiMigrationDependency <vim/host/IscsiManager/IscsiMigrationDependency.rst>`_:
         Dependency table, as described in IscsiMigrationDependency, providing the user of all the Virtual NIC and iSCSI resources affected.


