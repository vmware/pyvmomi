.. _str: https://docs.python.org/2/library/stdtypes.html

.. _config: ../../../vim/profile/Profile.rst#config

.. _vswitch: ../../../vim/profile/host/NetworkProfile.rst#vswitch

.. _vim.Task: ../../../vim/Task.rst

.. _userInput: ../../../vim/profile/host/AnswerFile.rst#userInput

.. _AnswerFile: ../../../vim/profile/host/AnswerFile.rst

.. _HostProfile: ../../../vim/profile/host/HostProfile.rst

.. _applyProfile: ../../../vim/profile/host/HostProfile/ConfigInfo.rst#applyProfile

.. _NetworkProfile: ../../../vim/profile/host/NetworkProfile.rst

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _UpdateHostProfile: ../../../vim/profile/host/HostProfile.rst#update

.. _vim.host.ConfigSpec: ../../../vim/host/ConfigSpec.rst

.. _vim.profile.Profile: ../../../vim/profile/Profile.rst

.. _VirtualSwitchProfile: ../../../vim/profile/host/VirtualSwitchProfile.rst

.. _GenerateConfigTaskList: ../../../vim/profile/host/ProfileManager.rst#generateConfigTaskList

.. _vim.fault.InvalidState: ../../../vim/fault/InvalidState.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.ProfileManager: ../../../vim/profile/ProfileManager.rst

.. _vim.fault.HostConfigFailed: ../../../vim/fault/HostConfigFailed.rst

.. _CheckAnswerFileStatus_Task: ../../../vim/profile/host/ProfileManager.rst#checkAnswerFileStatus

.. _vim.profile.ProfileMetadata: ../../../vim/profile/ProfileMetadata.rst

.. _vmodl.fault.InvalidArgument: ../../../vmodl/fault/InvalidArgument.rst

.. _vim.profile.host.AnswerFile: ../../../vim/profile/host/AnswerFile.rst

.. _vim.profile.ProfileStructure: ../../../vim/profile/ProfileStructure.rst

.. _HostProfileCompleteConfigSpec: ../../../vim/profile/host/HostProfile/CompleteConfigSpec.rst

.. _vim.fault.AnswerFileUpdateFailed: ../../../vim/fault/AnswerFileUpdateFailed.rst

.. _vim.profile.host.HostApplyProfile: ../../../vim/profile/host/HostApplyProfile.rst

.. _HostProfileManagerAnswerFileStatus: ../../../vim/profile/host/ProfileManager/AnswerFileStatus.rst

.. _vim.fault.InvalidProfileReferenceHost: ../../../vim/fault/InvalidProfileReferenceHost.rst

.. _vim.profile.host.AnswerFileStatusResult: ../../../vim/profile/host/AnswerFileStatusResult.rst

.. _vim.profile.DeferredPolicyOptionParameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst

.. _vim.profile.host.ProfileManager.ConfigTaskList: ../../../vim/profile/host/ProfileManager/ConfigTaskList.rst

.. _vim.profile.host.ProfileManager.AnswerFileCreateSpec: ../../../vim/profile/host/ProfileManager/AnswerFileCreateSpec.rst


vim.profile.host.ProfileManager
===============================
  The `HostProfileManager`_ provides access to a list of `HostProfile`_ s and it defines methods to manipulate profiles and `AnswerFile`_ s.


:extends: vim.profile.ProfileManager_
:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


ApplyHostConfig(host, configSpec, userInput):
   Apply the configuration to the host. If you specify any user input, the configuration will be saved in the `AnswerFile`_ associated with the host. If there is no answer file, the Profile Engine will create one.


  Privilege:
               dynamic



  Args:
    host (`vim.HostSystem`_):
       Host to be updated. User must have sufficient credentials and privileges to satisfy the contents of theconfigSpec.


    configSpec (`vim.host.ConfigSpec`_):
       Set of configuration changes to be applied to the host. The changes are returned by the `HostProfile`_ . `ExecuteHostProfile`_ method in the `ProfileExecuteResult`_ . `configSpec`_ property.


    userInput (`vim.profile.DeferredPolicyOptionParameter`_, optional, since `vSphere API 5.0`_ ):
       Additional host-specific data to be applied to the host. This data is the complete list of deferred parameters verified by the `HostProfile`_ . `ExecuteHostProfile`_ method, contained in the `ProfileExecuteResult`_ object returned by the method.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       if the host is not in maintenance mode and the configuration specification requires it.

    `vim.fault.HostConfigFailed`_:
       if the ESX Server cannot apply the configuration changes.


GenerateConfigTaskList(configSpec, host):
   Generate a list of configuration tasks that will be performed on the host during HostProfile application.


  Privilege:
               System.View



  Args:
    configSpec (`vim.host.ConfigSpec`_):
       ConfigSpec which was proposed by `ExecuteHostProfile`_ method.


    host (`vim.HostSystem`_):
       Host on which the HostProfile application needs to be carried out.




  Returns:
    `vim.profile.host.ProfileManager.ConfigTaskList`_:
         List of Configuration tasks.


GenerateHostProfileTaskList(configSpec, host):
   Generate a list of configuration tasks that will be performed on the host during HostProfile application. This differs from the `GenerateConfigTaskList`_ method in that it returns a task to monitor the progress of the operation.
  since: `vSphere API 5.5`_


  Privilege:
               System.View



  Args:
    configSpec (`vim.host.ConfigSpec`_):
       ConfigSpec which was proposed by `ExecuteHostProfile`_ method.


    host (`vim.HostSystem`_):
       Host on which the HostProfile application needs to be carried out.




  Returns:
     `vim.Task`_:
         List of Configuration tasks.


QueryHostProfileMetadata(profileName, profile):
   Retrieve the metadata for a set of profiles.


  Privilege:
               System.View



  Args:
    profileName (`str`_, optional):
       Names of the profiles for which metadata is requested. If not set, the method returns metadata for all the profiles.


    profile (`vim.profile.Profile`_, optional, since `vSphere API 5.0`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    [`vim.profile.ProfileMetadata`_]:
         List of profile metadata objects.

  Raises:

    `vmodl.fault.InvalidArgument`_:
       If profileName parameter is invalid.

    `vim.fault.InvalidProfileReferenceHost`_:
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


QueryProfileStructure(profile):
   Get information about the structure of the profile.
  since: `vSphere API 5.0`_


  Privilege:
               System.View



  Args:
    profile (`vim.profile.Profile`_, optional, since `vSphere API 5.0`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    `vim.profile.ProfileStructure`_:
         The profile structure.

  Raises:

    `vim.fault.InvalidProfileReferenceHost`_:
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


CreateDefaultProfile(profileType, profileTypeName, profile):
   Create a default subprofile of a given type (for example, a `VirtualSwitchProfile`_ ). After you create the subprofile, you can add it to a configuration specification and update the host profile:
    * Call the
    * CreateDefaultProfile
    * method.
    * Create a
    * `HostProfileCompleteConfigSpec`_
    * object.
    * Copy the existing profile from the host configuration information (
    * `HostProfile`_
    * .
    * `config`_
    * .
    * `applyProfile`_
    * ) to the configuration specification.
    * Add the new subprofile to the configuration specification. For example, if you create a
    * VirtualSwitchProfile
    * , you would add it to the list of virtual switches in the network profile for the configuration specification (
    * `NetworkProfile`_
    * .
    * `vswitch`_
    * []).
    * Call
    * `HostProfile`_
    * .
    * `UpdateHostProfile`_
    * to save the new subprofile.


  Privilege:
               System.View



  Args:
    profileType (`str`_):
       Type of profile to create. The profile types are system-defined ( `ApplyProfile`_ . `profileTypeName`_ ).


    profileTypeName (`str`_, optional, since `vSphere API 5.0`_ ):
       If specified, the method returns a profile object containing data for the named profile. The type name does not have to be system-defined. A user-defined profile can include various dynamically-defined profiles.


    profile (`vim.profile.Profile`_, optional, since `vSphere API 5.0`_ ):
       Base profile used during the operation.




  Returns:
    `vim.profile.ApplyProfile`_:
         Derived subprofile of typeprofileType.

  Raises:

    `vmodl.fault.InvalidArgument`_:
       If either the profileType or profileTypeName is incorrect.

    `vim.fault.InvalidProfileReferenceHost`_:
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


UpdateAnswerFile(host, configSpec):
   Update the `AnswerFile`_ for the specified host. If there is no answer file associated with the host, the Profile Engine uses the answer file configuration specification to create a new one.
  since: `vSphere API 5.0`_


  Privilege:
               Profile.Edit



  Args:
    host (`vim.HostSystem`_):
       Host with which the answer file is associated.


    configSpec (`vim.profile.host.ProfileManager.AnswerFileCreateSpec`_):
       Host-specific configuration data. If the configuration specification does not contain any host-specific user input (configSpec. `userInput`_ ), the method does not perform any operation on the answer file.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.AnswerFileUpdateFailed`_:
       If the answer file could not be updated.

    `vmodl.fault.InvalidArgument`_:
       If the input parameters are incorrect.


RetrieveAnswerFile(host):
   Returns the answer file associated with a particular host.
  since: `vSphere API 5.0`_


  Privilege:



  Args:
    host (`vim.HostSystem`_):
       Host with which the answer file is associated.




  Returns:
    `vim.profile.host.AnswerFile`_:
         Answer file object will be returned if it exists.


RetrieveAnswerFileForProfile(host, applyProfile):
   Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile.
  since: `vSphere API 5.1`_


  Privilege:



  Args:
    host (`vim.HostSystem`_):
       Host with which the answer file is associated.


    applyProfile (`vim.profile.host.HostApplyProfile`_):
       Profile configuration used to generate answer file




  Returns:
    `vim.profile.host.AnswerFile`_:
         Answer file object will be returned.


ExportAnswerFile(host):
   Export a host's answer file into a serialized form. The method returns a string that contains only the list of user input options. See `AnswerFile`_ . `userInput`_ .
  since: `vSphere API 5.0`_


  Privilege:
               Profile.Export



  Args:
    host (`vim.HostSystem`_):
       Host with which the answer file is associated.




  Returns:
     `vim.Task`_:
         Serialized form of the answer file.


CheckAnswerFileStatus(host):
   Check the validity of the answer files for the specified hosts. The Profile Engine uses the profile associated with a host to check the answer file.
  since: `vSphere API 5.0`_


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem`_):
       Set of hosts for which the answer file status will be checked.




  Returns:
     `vim.Task`_:
         Returns the resulting answer file status.

  Raises:

    `vim.fault.InvalidProfileReferenceHost`_:
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


QueryAnswerFileStatus(host):
   Returns the status of the answer files associated with specified hosts. This method returns the most recent status determined by `CheckAnswerFileStatus_Task`_ . See `HostProfileManagerAnswerFileStatus`_ for valid values.
  since: `vSphere API 5.0`_


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem`_):
       The hosts the answer file is associated with.




  Returns:
    [`vim.profile.host.AnswerFileStatusResult`_]:
         List of answer file status objects.
