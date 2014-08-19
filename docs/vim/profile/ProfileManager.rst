
vim.profile.ProfileManager
==========================
  This Class is responsible for managing Profiles.


:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    profile ([`vim.profile.Profile <vim/profile/Profile.rst>`_]):
      privilege: Profile.View
       A list of profiles known to this ProfileManager.


Methods
-------


CreateProfile(createSpec):
   Create a profile from the specified CreateSpec.


  Privilege:
               Profile.Create



  Args:
    createSpec (`vim.profile.Profile.CreateSpec <vim/profile/Profile/CreateSpec.rst>`_):
       Specification for the profile being created. Usually a derived class CreateSpec can be used to create the Profile.




  Returns:
    `vim.profile.Profile <vim/profile/Profile.rst>`_:
         Profile created from the specified createSpec.

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       If a profile with the specified name already exists.

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the specified reference host is incompatible or no reference host has been specifed.


QueryPolicyMetadata(policyName, profile):
   Get the Metadata information for the policyNames. PolicyNames are available with the defaultProfile obtained by invoking the method createDefaultProfile.


  Privilege:
               System.View



  Args:
    policyName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Retrieve metadata for the specified policyNames. If policyName is not specified, metadata for all policies will be returned.


    profile (`vim.profile.Profile <vim/profile/Profile.rst>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    [`vim.profile.PolicyMetadata <vim/profile/PolicyMetadata.rst>`_]:
         The metadata information for the policy.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If policyName is invalid.

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


FindAssociatedProfile(entity):
   Get the profile(s) to which this entity is associated. The list of profiles will only include profiles known to this profileManager.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       Entity for which profile is being looked up.




  Returns:
    [`vim.profile.Profile <vim/profile/Profile.rst>`_]:
         


