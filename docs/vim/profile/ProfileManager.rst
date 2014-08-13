.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.profile.Profile: ../../vim/profile/Profile.rst

.. _vim.fault.DuplicateName: ../../vim/fault/DuplicateName.rst

.. _vim.profile.PolicyMetadata: ../../vim/profile/PolicyMetadata.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.profile.Profile.CreateSpec: ../../vim/profile/Profile/CreateSpec.rst

.. _vim.fault.InvalidProfileReferenceHost: ../../vim/fault/InvalidProfileReferenceHost.rst


vim.profile.ProfileManager
==========================
  This Class is responsible for managing Profiles.


:since: `vSphere API 4.0`_


Attributes
----------
    profile ([`vim.profile.Profile`_]):
      privilege: Profile.View
       A list of profiles known to this ProfileManager.


Methods
-------


CreateProfile(createSpec):
   Create a profile from the specified CreateSpec.


  Privilege:
               Profile.Create



  Args:
    createSpec (`vim.profile.Profile.CreateSpec`_):
       Specification for the profile being created. Usually a derived class CreateSpec can be used to create the Profile.




  Returns:
    `vim.profile.Profile`_:
         Profile created from the specified createSpec.

  Raises:

    `vim.fault.DuplicateName`_: 
       If a profile with the specified name already exists.

    `vim.fault.InvalidProfileReferenceHost`_: 
       if the specified reference host is incompatible or no reference host has been specifed.


QueryPolicyMetadata(policyName, profile):
   Get the Metadata information for the policyNames. PolicyNames are available with the defaultProfile obtained by invoking the method createDefaultProfile.


  Privilege:
               System.View



  Args:
    policyName (`str`_, optional):
       Retrieve metadata for the specified policyNames. If policyName is not specified, metadata for all policies will be returned.


    profile (`vim.profile.Profile`_, optional, since `vSphere API 5.0`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    [`vim.profile.PolicyMetadata`_]:
         The metadata information for the policy.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       If policyName is invalid.

    `vim.fault.InvalidProfileReferenceHost`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


FindAssociatedProfile(entity):
   Get the profile(s) to which this entity is associated. The list of profiles will only include profiles known to this profileManager.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity`_):
       Entity for which profile is being looked up.




  Returns:
    [`vim.profile.Profile`_]:
         


