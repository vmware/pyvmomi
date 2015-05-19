.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _config: ../../../vim/profile/Profile.rst#config

.. _vim.Task: ../../../vim/Task.rst

.. _parameter: ../../../vim/profile/PolicyOption.rst#parameter

.. _AnswerFile: ../../../vim/profile/host/AnswerFile.rst

.. _HostProfile: ../../../vim/profile/host/HostProfile.rst

.. _applyProfile: ../../../vim/profile/host/HostProfile/ConfigInfo.rst#applyProfile

.. _PolicyOption: ../../../vim/profile/PolicyOption.rst

.. _referenceHost: ../../../vim/profile/host/HostProfile.rst#referenceHost

.. _validatorHost: ../../../vim/profile/host/HostProfile/CompleteConfigSpec.rst#validatorHost

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.Profile: ../../../vim/profile/Profile.rst

.. _UpdateReferenceHost: ../../../vim/profile/host/HostProfile.rst#updateReferenceHost

.. _vim.fault.DuplicateName: ../../../vim/fault/DuplicateName.rst

.. _HostProfileCompleteConfigSpec: ../../../vim/profile/host/HostProfile/CompleteConfigSpec.rst

.. _vim.fault.ProfileUpdateFailed: ../../../vim/fault/ProfileUpdateFailed.rst

.. _vim.profile.host.ExecuteResult: ../../../vim/profile/host/ExecuteResult.rst

.. _vim.profile.host.HostProfile.ConfigSpec: ../../../vim/profile/host/HostProfile/ConfigSpec.rst

.. _vim.profile.DeferredPolicyOptionParameter: ../../../vim/profile/DeferredPolicyOptionParameter.rst


vim.profile.host.HostProfile
============================
  A host profile describes ESX Server configuration. The `HostProfile`_ managed object provides access to profile data and it defines methods to manipulate the profile. A host profile is a combination of subprofiles, each of which contains configuration data for a specific capability. Some examples of host capabilities are authentication, memory, networking, and security. For access to individual subprofiles, see the `HostApplyProfile`_ data object ( `HostProfile`_ . `config`_ . `applyProfile`_ ).Host profiles are part of the stateless configuration architecture. In the stateless environment, a Profile Engine runs on each ESX host, but an ESX host does not store its own configuration state. Instead, host configuration data is stored on vCenter Servers. Every time a host boots or reboots, it obtains its profile from the vCenter Server.
   * To create a base host profile use the
   * `HostProfileManager`_
   * .
   * `CreateProfile`_
   * method. To create a profile from an ESX host, specify a
   * `HostProfileHostBasedConfigSpec`_
   * . To create a profile from a file, specify a
   * `HostProfileSerializedHostProfileSpec`_
   * .
   * 
   * To create a subprofile for a particular host capability, use the
   * `HostProfileManager`_
   * .
   * `CreateDefaultProfile`_
   * method. After you create the default profile you can modify it and save it in the base profile.
   * 
   * To update an existing profile, use the
   * `HostProfile`_
   * .
   * `UpdateHostProfile`_
   * method.
   * 
   * To apply a host profile to an ESX host, use the
   * `ExecuteHostProfile`_
   * method to generate configuration changes, then call the
   * `HostProfileManager`_
   * .
   * `ApplyHostConfig_Task`_
   * method to apply them.Host-Specific ConfigurationAn individual host or a set of hosts may have some configuration settings that are different from the settings specified in the host profile. For example, the IP configuration for the host's virtual network adapters must be unique.
   * To verify host-specific data, use the
   * deferredParam
   * parameter to the
   * `ExecuteHostProfile`_
   * method. The Profile Engine will determine if you have specified all of the required parameters for the host configuration. If additional data is required, call the
   * `ExecuteHostProfile`_
   * method again as many times as necessary to verify a complete set of parameters.
   * 
   * To apply host-specific data, use the
   * userInput
   * parameter to the
   * `HostProfileManager`_
   * .
   * `ApplyHostConfig_Task`_
   * method.
   * The Profile Engine saves host-specific data in an `AnswerFile`_ that is stored on the vCenter Server. The `HostProfileManager`_ provides several methods to manipulate answer files.Profile ComplianceYou can create associations between hosts and profiles to support compliance checking. When you perform compliance checking, you can determine if a host configuration conforms to a host profile.
   * To create an association between a host and a profile, use the
   * `AssociateProfile`_
   * method. The method adds the host to the
   * `HostProfile`_
   * .
   * `entity`_
   * [] list.
   * To retrieve the list of profiles associated with a host, use the
   * `HostProfileManager`_
   * .
   * `FindAssociatedProfile`_
   * method.
   * To check host compliance, use the
   * `CheckProfileCompliance_Task`_
   * method. If you do not specify any hosts, the method will check the compliance of all hosts that are associated with the profile.You can also use the Profile Compliance Manager to check compliance by specifying profiles, entities (hosts), or both. See `ProfileComplianceManager`_ . `CheckCompliance_Task`_ .Profile Plug-InsThe vSphere architecture uses VMware profile plug-ins to define profile extensions. For information about using a plug-in to extend a host profile, see the VMware Technical NoteDeveloping a Host Profile Extension Plug-in.For access to host configuration data that is defined by plug-ins, use the `ApplyProfile`_ . `policy`_ [] and `ApplyProfile`_ . `property`_ [] lists. The `HostApplyProfile`_ and its subprofiles, which collectively define host configuration data, are derived from the `ApplyProfile`_ .
   * Policies store ESX configuration data in
   * `PolicyOption`_
   * objects.
   * Profile property lists contain subprofiles defined by plug-ins. Subprofiles can be nested.
   * 
   * Subprofile lists are available as an extension to the base host profile (
   * `HostProfile`_
   * .
   * `config`_
   * .
   * `applyProfile`_
   * .
   * `property`_
   * []).
   * Subprofile lists are available as extensions to the host subprofiles - for example, the network subprofile (
   * `HostApplyProfile`_
   * .
   * `network`_
   * .
   * `property`_
   * []).If you make changes to host profile data, later versions of profile plug-ins may not support the host configuration implied by the changes that you make. When a subsequent vSphere version becomes available, you must verify that the new version supports any previous configuration changes that you have made.


:extends: vim.profile.Profile_
:since: `vSphere API 4.0`_


Attributes
----------
    referenceHost (`vim.HostSystem`_):
       Reference host in use for this host profile. To set this property, use the `UpdateReferenceHost`_ method. If you do not specify a host for validation ( `HostProfileCompleteConfigSpec`_ . `validatorHost`_ ), the Profile Engine uses the reference host to validate the profile.


Methods
-------


UpdateReferenceHost(host):
   Sets the `HostProfile`_ . `referenceHost`_ property.


  Privilege:
               Profile.Edit



  Args:
    host (`vim.HostSystem`_, optional):
       Reference host to use. If unset, the `referenceHost`_ property is cleared.




  Returns:
    None
         


UpdateHostProfile(config):
   Update theHostProfilewith the specified configuration data.


  Privilege:
               Profile.Edit



  Args:
    config (`vim.profile.host.HostProfile.ConfigSpec`_):
       Specification containing the new data.




  Returns:
    None
         

  Raises:

    `vim.fault.DuplicateName`_: 
       If the profile with the new name already exists.

    `vim.fault.ProfileUpdateFailed`_: 
       if errors were encountered when updating the profile.


ExecuteHostProfile(host, deferredParam):
   Run the Profile Engine to determine the list of configuration changes needed for the specified host. The method generates configuration changes based on the host profile.You can also specify deferred parameters to verify additional host-specific data. The Profile Engine uses the policy options ( `HostProfile`_ . `config`_ . `applyProfile`_ . `policy`_ []) to determine the required parameters ( `PolicyOption`_ . `parameter`_ []) for host configuration. If you do not provide all of the required parameters, you must call the method again to provide the complete list to the Profile Engine. After successful profile execution, when you apply the profile, the Profile Engine will save the host-specific data in an `AnswerFile`_ .


  Privilege:
               System.View



  Args:
    host (`vim.HostSystem`_):
       Host on which to execute the profile. The host does not have to be associated with the profile.


    deferredParam (`vim.profile.DeferredPolicyOptionParameter`_, optional):
       Additional configuration data to be applied to the host. This should contain all of the host-specific data, including data from from previous calls to the method.




  Returns:
    `vim.profile.host.ExecuteResult`_:
         Result of the execution. If the operation is successful ( `ProfileExecuteResult`_ . `status`_ =success), the result object includes a valid host configuration specification that you can pass to the `HostProfileManager`_ . `ApplyHostConfig_Task`_ method.If the operation is not successful, the object contains error information or information about additional data required for the host configuration. If additional data is required, the required input list ( `ProfileExecuteResult`_ . `requireInput`_ []) contains both thedeferredParamdata and paths to missing parameters. After you fill in the missing parameters, pass the complete required input list via thedeferredParamparameter in another call to the execute method to finish input verification. After successful profile execution, you can pass the verified required input list to the `ApplyHostConfig_Task`_ method.


