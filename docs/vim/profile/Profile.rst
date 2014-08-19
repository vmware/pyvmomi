
vim.profile.Profile
===================
  TheProfilemanaged object is the base class for host and cluster profiles.


:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    config (`vim.profile.Profile.ConfigInfo <vim/profile/Profile/ConfigInfo.rst>`_):
      privilege: Profile.Edit
       Configuration data for the profile.
    description (`vim.profile.Profile.Description <vim/profile/Profile/Description.rst>`_):
       Localizable description of the profile
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Name of the profile.
    createdTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):
       Time at which the profile was created.
    modifiedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):
       Time at which the profile was last modified.
    entity ([`vim.ManagedEntity <vim/ManagedEntity.rst>`_]):
       List of managed entities associated with the profile.
    complianceStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Overall compliance of entities associated with this profile. If one of the entities is out of compliance, the profile isnonCompliant. If all entities are in compliance, the profile iscompliant. If the compliance status of one of the entities is not known, compliance status of the profile isunknown. See `ComplianceResultStatus <vim/profile/ComplianceResult/Status.rst>`_ .


Methods
-------


RetrieveDescription():
   Returns the localizable description for the profile.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:


  Returns:
    `vim.profile.Profile.Description <vim/profile/Profile/Description.rst>`_:
         Profile divided into sections containing element descriptions and messages.

  Raises:

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


DestroyProfile():
   Destroy the profile.


  Privilege:
               Profile.Delete



  Args:


  Returns:
    None
         


AssociateProfile(entity):
   Associate a profile with a managed entity. You can check the compliance of entities associated with a profile by calling the `CheckProfileCompliance_Task <vim/profile/Profile.rst#checkCompliance>`_ method.


  Privilege:
               Profile.Edit



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The entity(s) to associate with the profile. If an entity is already associated with the profile, the association is maintained and the vCenter Server does not perform any action.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidType <vmodl/fault/InvalidType.rst>`_: 
       If the entity is of an unexpeted type.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the association conflicts with existing association.


DissociateProfile(entity):
   Remove the association between a profile and a managed entity.


  Privilege:
               Profile.Edit



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):
       List of entities. The vCenter Server will remove the associations that the profile has with the entities in the list. If unset, the Server removes all the associations that the profile has with any managed entities in the inventory. If the specified entity is not associated with the profile, the Server does not perform any action.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the dissociation conflicts with existing association.


CheckProfileCompliance(entity):
   Check compliance of an entity against a Profile.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):
       If specified, the compliance check is performed on this entity. If the entity is not specified, the vCenter Server runs a compliance check on all the entities associated with the profile. The entity does not have to be associated with the profile.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         The compliance result.

  Raises:

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


ExportProfile():
   Export the profile in a serialized form. To use the serialized string to create a profile, specify a `ProfileSerializedCreateSpec <vim/profile/Profile/SerializedCreateSpec.rst>`_ when you call the `HostProfileManager <vim/profile/host/ProfileManager.rst>`_ . `CreateProfile <vim/profile/ProfileManager.rst#createProfile>`_ method.


  Privilege:
               Profile.Export



  Args:


  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         Serialized form of the profile.


