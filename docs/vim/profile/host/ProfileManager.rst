
vim.profile.host.ProfileManager
===============================
  The `HostProfileManager <vim/profile/host/ProfileManager.rst>`_ provides access to a list of `HostProfile <vim/profile/host/HostProfile.rst>`_ s and it defines methods to manipulate profiles and `AnswerFile <vim/profile/host/AnswerFile.rst>`_ s.


:extends: vim.profile.ProfileManager_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------


Methods
-------


ApplyHostConfig(host, configSpec, userInput):
   Apply the configuration to the host. If you specify any user input, the configuration will be saved in the `AnswerFile <vim/profile/host/AnswerFile.rst>`_ associated with the host. If there is no answer file, the Profile Engine will create one.


  Privilege:
               dynamic



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host to be updated. User must have sufficient credentials and privileges to satisfy the contents of theconfigSpec.


    configSpec (`vim.host.ConfigSpec <vim/host/ConfigSpec.rst>`_):
       Set of configuration changes to be applied to the host. The changes are returned by the `HostProfile <vim/profile/host/HostProfile.rst>`_ . `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ method in the `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ . `configSpec <vim/profile/host/ExecuteResult.rst#configSpec>`_ property.


    userInput (`vim.profile.DeferredPolicyOptionParameter <vim/profile/DeferredPolicyOptionParameter.rst>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Additional host-specific data to be applied to the host. This data is the complete list of deferred parameters verified by the `HostProfile <vim/profile/host/HostProfile.rst>`_ . `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ method, contained in the `ProfileExecuteResult <vim/profile/host/ExecuteResult.rst>`_ object returned by the method.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the host is not in maintenance mode and the configuration specification requires it.

    `vim.fault.HostConfigFailed <vim/fault/HostConfigFailed.rst>`_: 
       if the ESX Server cannot apply the configuration changes.


GenerateConfigTaskList(configSpec, host):
   Generate a list of configuration tasks that will be performed on the host during HostProfile application.


  Privilege:
               System.View



  Args:
    configSpec (`vim.host.ConfigSpec <vim/host/ConfigSpec.rst>`_):
       ConfigSpec which was proposed by `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ method.


    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host on which the HostProfile application needs to be carried out.




  Returns:
    `vim.profile.host.ProfileManager.ConfigTaskList <vim/profile/host/ProfileManager/ConfigTaskList.rst>`_:
         List of Configuration tasks.


GenerateHostProfileTaskList(configSpec, host):
   Generate a list of configuration tasks that will be performed on the host during HostProfile application. This differs from the `GenerateConfigTaskList <vim/profile/host/ProfileManager.rst#generateConfigTaskList>`_ method in that it returns a task to monitor the progress of the operation.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               System.View



  Args:
    configSpec (`vim.host.ConfigSpec <vim/host/ConfigSpec.rst>`_):
       ConfigSpec which was proposed by `ExecuteHostProfile <vim/profile/host/HostProfile.rst#execute>`_ method.


    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host on which the HostProfile application needs to be carried out.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         List of Configuration tasks.


QueryHostProfileMetadata(profileName, profile):
   Retrieve the metadata for a set of profiles.


  Privilege:
               System.View



  Args:
    profileName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Names of the profiles for which metadata is requested. If not set, the method returns metadata for all the profiles.


    profile (`vim.profile.Profile <vim/profile/Profile.rst>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    [`vim.profile.ProfileMetadata <vim/profile/ProfileMetadata.rst>`_]:
         List of profile metadata objects.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If profileName parameter is invalid.

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


QueryProfileStructure(profile):
   Get information about the structure of the profile.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    profile (`vim.profile.Profile <vim/profile/Profile.rst>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Base profile whose context needs to be used during the operation




  Returns:
    `vim.profile.ProfileStructure <vim/profile/ProfileStructure.rst>`_:
         The profile structure.

  Raises:

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


CreateDefaultProfile(profileType, profileTypeName, profile):
   Create a default subprofile of a given type (for example, a `VirtualSwitchProfile <vim/profile/host/VirtualSwitchProfile.rst>`_ ). After you create the subprofile, you can add it to a configuration specification and update the host profile:
    * Call the
    * CreateDefaultProfile
    * method.
    * Create a
    * `HostProfileCompleteConfigSpec <vim/profile/host/HostProfile/CompleteConfigSpec.rst>`_
    * object.
    * Copy the existing profile from the host configuration information (
    * `HostProfile <vim/profile/host/HostProfile.rst>`_
    * .
    * `config <vim/profile/Profile.rst#config>`_
    * .
    * `applyProfile <vim/profile/host/HostProfile/ConfigInfo.rst#applyProfile>`_
    * ) to the configuration specification.
    * Add the new subprofile to the configuration specification. For example, if you create a
    * VirtualSwitchProfile
    * , you would add it to the list of virtual switches in the network profile for the configuration specification (
    * `NetworkProfile <vim/profile/host/NetworkProfile.rst>`_
    * .
    * `vswitch <vim/profile/host/NetworkProfile.rst#vswitch>`_
    * []).
    * Call
    * `HostProfile <vim/profile/host/HostProfile.rst>`_
    * .
    * `UpdateHostProfile <vim/profile/host/HostProfile.rst#update>`_
    * to save the new subprofile.


  Privilege:
               System.View



  Args:
    profileType (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Type of profile to create. The profile types are system-defined ( `ApplyProfile <vim/profile/ApplyProfile.rst>`_ . `profileTypeName <vim/profile/ApplyProfile.rst#profileTypeName>`_ ).


    profileTypeName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       If specified, the method returns a profile object containing data for the named profile. The type name does not have to be system-defined. A user-defined profile can include various dynamically-defined profiles.


    profile (`vim.profile.Profile <vim/profile/Profile.rst>`_, optional, since `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_ ):
       Base profile used during the operation.




  Returns:
    `vim.profile.ApplyProfile <vim/profile/ApplyProfile.rst>`_:
         Derived subprofile of typeprofileType.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If either the profileType or profileTypeName is incorrect.

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


UpdateAnswerFile(host, configSpec):
   Update the `AnswerFile <vim/profile/host/AnswerFile.rst>`_ for the specified host. If there is no answer file associated with the host, the Profile Engine uses the answer file configuration specification to create a new one.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Profile.Edit



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host with which the answer file is associated.


    configSpec (`vim.profile.host.ProfileManager.AnswerFileCreateSpec <vim/profile/host/ProfileManager/AnswerFileCreateSpec.rst>`_):
       Host-specific configuration data. If the configuration specification does not contain any host-specific user input (configSpec. `userInput <vim/profile/host/ProfileManager/AnswerFileOptionsCreateSpec.rst#userInput>`_ ), the method does not perform any operation on the answer file.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.AnswerFileUpdateFailed <vim/fault/AnswerFileUpdateFailed.rst>`_: 
       If the answer file could not be updated.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the input parameteres are incorrect.


RetrieveAnswerFile(host):
   Returns the answer file associated with a particular host.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host with which the answer file is associated.




  Returns:
    `vim.profile.host.AnswerFile <vim/profile/host/AnswerFile.rst>`_:
         Answer file object will be returned if it exists.


RetrieveAnswerFileForProfile(host, applyProfile):
   Returns the answer file associated with a particular host, augmented with whatever answer file values are required for the supplied host profile.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host with which the answer file is associated.


    applyProfile (`vim.profile.host.HostApplyProfile <vim/profile/host/HostApplyProfile.rst>`_):
       Profile configuration used to generate answer file




  Returns:
    `vim.profile.host.AnswerFile <vim/profile/host/AnswerFile.rst>`_:
         Answer file object will be returned.


ExportAnswerFile(host):
   Export a host's answer file into a serialized form. The method returns a string that contains only the list of user input options. See `AnswerFile <vim/profile/host/AnswerFile.rst>`_ . `userInput <vim/profile/host/AnswerFile.rst#userInput>`_ .
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               Profile.Export



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Host with which the answer file is associated.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         Serialized form of the answer file.


CheckAnswerFileStatus(host):
   Check the validity of the answer files for the specified hosts. The Profile Engine uses the profile associated with a host to check the answer file.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       Set of hosts for which the answer file status will be checked.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         Returns the resulting answer file status.

  Raises:

    `vim.fault.InvalidProfileReferenceHost <vim/fault/InvalidProfileReferenceHost.rst>`_: 
       if the reference host associated with the profile is incompatible or there is no reference host for the profile.


QueryAnswerFileStatus(host):
   Returns the status of the answer files associated with specified hosts. This method returns the most recent status determined by `CheckAnswerFileStatus_Task <vim/profile/host/ProfileManager.rst#checkAnswerFileStatus>`_ . See `HostProfileManagerAnswerFileStatus <vim/profile/host/ProfileManager/AnswerFileStatus.rst>`_ for valid values.
  since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):
       The hosts the answer file is associated with.




  Returns:
    [`vim.profile.host.AnswerFileStatusResult <vim/profile/host/AnswerFileStatusResult.rst>`_]:
         List of answer file status objects.


