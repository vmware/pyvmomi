# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.fault
import pyVmomi.vim.host
import pyVmomi.vim.profile



class ActiveDirectoryProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.ActiveDirectoryProfile` data object represents Active Directory
   configuration.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for
   access to configuration data for the Active Directory profile. Use the
   `pyVmomi.vim.profile.ApplyProfile.property` list for access to subprofiles, if any.
   """
   pass


class AnswerFile(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.host.AnswerFile` data object contains host-specific information that a host
   will use in combination with a `pyVmomi.vim.profile.host.HostProfile` for configuration.
   
   Answer files are stored on the vCenter Server, along with host profiles.
   An answer file is always associated with a particular host.
   
   To supply host-specific data:
   - Specify deferred parameters when you call the
     `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
     method. The host profile engine will verify the set of parameters for the
     additional configuration data.
   - Use the complete required input list
     (`pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.requireInput`[])
     as user input for the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
     method. When you apply the profile, the vCenter Server saves the additional configuration
     data in the `pyVmomi.vim.profile.host.AnswerFile.userInput` list.
   - Use the `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.updateAnswerFile` method. This method will update an existing answer file or create a new one.
   
   Attributes:
       userInput: List containing host-specific configuration data.
       createdTime: Time at which the answer file was created.
       modifiedTime: Time at which the answer file was last modified.
   """
   userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []
   createdTime: _datetime.datetime
   modifiedTime: _datetime.datetime


class AnswerFileStatusResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.host.AnswerFileStatusResult` data object shows the validity of the
   answer file associated with a host.
   
   Attributes:
       checkedTime: Time that the answer file status was determined.
       host: Host associated with the answer file.
       status: Status of the answer file.
           
           See `pyVmomi.vim.profile.host.ProfileManager.AnswerFileStatus` for valid values.
       error: If `status` is `invalid`, this property contains a list
           of status error objects.
   """
   class AnswerFileStatusError(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError` data object describes an answer file
      error and identifies the profile or policy option with which the error
      is associated.
      
      Attributes:
          userInputPath: Path to a profile or a policy option for host-specific data.
          errMsg: Message describing the error.
      """
      userInputPath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   checkedTime: _datetime.datetime
   host: pyVmomi.vim.HostSystem
   status: str
   error: list[AnswerFileStatusResult.AnswerFileStatusError] = []


class AuthenticationProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.AuthenticationProfile` data object represents the host configuration
   for authentication.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       activeDirectory: Subprofile representing the Active Directory configuration.
   """
   activeDirectory: _typing.Optional[ActiveDirectoryProfile] = None


class DateTimeProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.DateTimeProfile` data object represents host date and time configuration.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the date and time profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list
   for access to subprofiles, if any.
   """
   pass


class DvsVNicProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.DvsVNicProfile` data object is the base object
   for host and service console Virtual NIC subprofiles.
   
   If a profile plug-in defines additional policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the configuration data.
   
   Attributes:
       key: Linkable identifier.
       ipConfig: IP address for the Virtual NIC belonging to a distributed virtual switch.
   """
   key: str
   ipConfig: IpAddressProfile

class DvsHostVNicProfile(DvsVNicProfile):
   """
   The `pyVmomi.vim.profile.host.DvsHostVNicProfile` data object describes the IP configuration
   for a host Virtual NIC connected to a distributed virtual switch.
   
   The `pyVmomi.vim.profile.host.DvsVNicProfile.ipConfig` property contains the Virtual NIC IP address.
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   """
   pass


class DvsProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.DvsProfile` data object represents the distributed virtual switch
   to which this host is connected.
   
   If a profile plug-in defines policies or subprofiles,
   use the `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       key: Linkable identifier.
       name: Unique identifier for the distributed virtual switch.
       uplink: List of subprofiles that map physical NICs to uplink ports.
           
           Use the `pyVmomi.vim.profile.host.PnicUplinkProfile.key` property to access
           subprofiles in the list.
   """
   key: str
   name: str
   uplink: list[PnicUplinkProfile] = []

class DvsServiceConsoleVNicProfile(DvsVNicProfile):
   """
   The `pyVmomi.vim.profile.host.DvsServiceConsoleVNicProfile` data object describes the IP configuration
   for a service console Virtual NIC connected to a distributed virtual switch.
   
   The `pyVmomi.vim.profile.host.DvsVNicProfile.ipConfig` property contains the Virtual NIC IP address.
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   """
   pass


class ExecuteResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.profile.host.ExecuteResult` data object contains the results from a
   `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
   operation.
   
   Attributes:
       status: Status of the profile execution operation.
           
           The value is a string that contains
           one of the `pyVmomi.vim.profile.host.ExecuteResult.Status` enumerations.
       configSpec: Host configuration specification.
           
           This data is valid only if
           the `status` value is `success`.
           See `pyVmomi.vim.profile.host.ExecuteResult.Status`.
           
           Use this data object when you apply the configuration
           to a host. See the `configSpec` parameter to the
           `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
           method.
       inapplicablePath: List of property paths.
           
           Each path identifies a policy that does not apply
           to this host. For example, if the precheck policies for a port group are not satisfied,
           the port group will not be created when you apply the profile to the host.
           Based on this information, the client might not display that part of the profile tree.
       requireInput: List that describes the required input for host configuration and identifies
           any policy options that still require parameter data.
           
           Each entry in the list
           specifies the path to a policy and a parameter list. If the call to
           `pyVmomi.vim.profile.host.HostProfile.execute` includes deferred parameters,
           the `requireInput` entries
           (`requireInput[].``pyVmomi.vim.profile.DeferredPolicyOptionParameter.parameter`[])
           will be populated with the parameter data that was passed to the execute method.
           For policies that still require input data, the parameter list in the corresponding
           entry will be null.
           
           A vSphere client that displays a GUI can use this information to show the host-specific
           configuration policy options. The client can highlight required input fields
           and ask the user for data in increments instead of collecting all of the input at once.
           For example, in the first pass, the client collects a minimum of user input and
           sends that to the Server. The Server evaluates the profile and might decide to
           invalidate a particular part of the subtree or enable a new
           subtree in the profile. This would result in a new set of invalid paths
           (`pyVmomi.vim.profile.host.ExecuteResult.inapplicablePath`[]) and
           required input property paths
           (`pyVmomi.vim.profile.DeferredPolicyOptionParameter`.`pyVmomi.vim.profile.DeferredPolicyOptionParameter.inputPath`).
           The client can make a series of calls to the method until it achieves a success status.
           
           When `pyVmomi.vim.profile.host.HostProfile.execute` returns a success status,
           the `requireInput` list contains the complete list of parameters,
           consisting of the following data:
           - Deferred parameter values resolved through successive calls to
             `pyVmomi.vim.profile.host.HostProfile.execute`.
           - Default parameter values from the host configuration.
           - User-specified values that override the defaults.
             
           You can specify the returned `requireInput` list in the
           `userInput` parameter to the
           `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
           method. The Server will use the list to update the `pyVmomi.vim.profile.host.AnswerFile`
           associated with the host.
       error: List of errors that were encountered during execute.
           
           This field will be set if status is set to error.
   """
   class Status(pyVmomi.VmomiSupport.Enum):
      """
      Defines the result status values for a
      `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
      operation.
      
      The result data is contained in the
      `pyVmomi.vim.profile.host.ExecuteResult` data object.
      
      Attributes:
          success: Profile execution was successful.
              
              You can use the output configuration data
              to apply the profile to a host.
          needInput: Additional data is required to complete the operation.
              
              The data requirements are defined in the list of policy options for the profile
              (`pyVmomi.vim.profile.ApplyProfile`.`pyVmomi.vim.profile.ApplyProfile.policy`[]).
          error: Profile execution generated an error.
              
              See `pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.error`.
      """
      success: _typing.ClassVar['ExecuteResult.Status'] = 'success'
      needInput: _typing.ClassVar['ExecuteResult.Status'] = 'needInput'
      error: _typing.ClassVar['ExecuteResult.Status'] = 'error'

   class ExecuteError(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.profile.host.ExecuteResult.ExecuteError` data object
      describes an error encountered during host profile execution.
      
      Attributes:
          path: Path to the profile or policy with which the error is associated.
          message: Message describing the error.
      """
      path: _typing.Optional[pyVmomi.vim.profile.ProfilePropertyPath] = None
      message: pyVmomi.vmodl.LocalizableMessage

   status: str
   configSpec: _typing.Optional[pyVmomi.vim.host.ConfigSpec] = None
   inapplicablePath: list[pyVmomi.VmomiSupport.PropertyPath] = []
   requireInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []
   error: list[ExecuteResult.ExecuteError] = []


class FirewallProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.FirewallProfile` data object represents a host firewall configuration.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       ruleset: List of Rulesets that will be configured for the firewall subprofile.
           
           The rulesets can be enabled or disabled from the profile.
   """
   class RulesetProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      Attributes:
          key: Linkable identifier.
      """
      key: str

   ruleset: list[FirewallProfile.RulesetProfile] = []


class HostApplyProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.HostApplyProfile` data object provides access to subprofiles
   that contain configuration data for different host capabilities.
   
   The Profile Engine will use any configuration data that you supply
   to overwrite the host configuration. See the `pyVmomi.vim.profile.host.HostProfile.execute`
   and `pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration` methods.
   
   Attributes:
       memory: Memory configuration for the host.
           
           This may not be valid for all versions of the host.
       storage: Host storage configuration.
       network: Network configuration.
       datetime: Date and time configuration.
       firewall: Firewall configuration.
       security: Security Configuration of the host.
           
           The security subprofile can include data such as administrator passwords.
       service: Host configuration for services.
           
           Use the `pyVmomi.vim.profile.host.ServiceProfile.key` property
           to access a subprofile in the list.
       option: List of subprofiles representing advanced configuration options.
           
           Use the `pyVmomi.vim.profile.host.OptionProfile.key` property to access a subprofile
           in the list.
       userAccount: List of subprofiles for user accounts to be configured on the host.
           
           Use the `pyVmomi.vim.profile.host.UserProfile.key` property to access a subprofile
           in the list.
       usergroupAccount: List of subprofiles for user groups to be configured on the host.
           
           Use the `pyVmomi.vim.profile.host.UserGroupProfile.key` property to access a subprofile
           in the list.
       authentication: Authentication Configuration.
   """
   memory: _typing.Optional[HostMemoryProfile] = None
   storage: _typing.Optional[StorageProfile] = None
   network: _typing.Optional[NetworkProfile] = None
   datetime: _typing.Optional[DateTimeProfile] = None
   firewall: _typing.Optional[FirewallProfile] = None
   security: _typing.Optional[SecurityProfile] = None
   service: list[ServiceProfile] = []
   option: list[OptionProfile] = []
   userAccount: list[UserProfile] = []
   usergroupAccount: list[UserGroupProfile] = []
   authentication: _typing.Optional[AuthenticationProfile] = None


class HostMemoryProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.HostMemoryProfile` data object represents
   memory configuration for the host.
   
   This may not be valid all versions of the host.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the host memory profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list
   for access to subprofile configuration data, if any.
   """
   pass


class PortGroupProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   `pyVmomi.vim.profile.host.PortGroupProfile` is the base class for the different port group
   subprofile objects.
   
   Attributes:
       key: Linkable identifier.
       name: Name of the portgroup.
       vlan: VLAN identifier for the port group.
       vswitch: Virtual switch to which the port group is connected.
       networkPolicy: The network policy/policies applicable on the port group.
   """
   class VlanProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      The `pyVmomi.vim.profile.host.PortGroupProfile.VlanProfile` data object represents
      the VLAN identifier subprofile.
      
      The `pyVmomi.vim.profile.ApplyProfile.policy`
      property contains the configuration data values for the VLAN identifier.
      """
      pass

   class VirtualSwitchSelectionProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      The `pyVmomi.vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile` data object represents
      the virtual switch that is connected to a port group.
      
      The `pyVmomi.vim.profile.ApplyProfile.policy` property contains
      the configuration data values for the virtual switch.
      """
      pass

   key: str
   name: str
   vlan: PortGroupProfile.VlanProfile
   vswitch: PortGroupProfile.VirtualSwitchSelectionProfile
   networkPolicy: NetworkPolicyProfile

class HostPortGroupProfile(PortGroupProfile):
   """
   The `pyVmomi.vim.profile.host.HostPortGroupProfile` data object represents the subprofile
   for a port group that will be used by the ESX host.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       ipConfig: IP address configuration for the Host network.
   """
   ipConfig: IpAddressProfile


class HostProfile(pyVmomi.vim.profile.Profile):
   """
   A host profile describes ESX Server configuration.
   
   The `pyVmomi.vim.profile.host.HostProfile` managed object provides access to profile data and
   it defines methods to manipulate the profile.
   A host profile is a combination of subprofiles, each of which contains
   configuration data for a specific capability. Some examples of host capabilities are
   authentication, memory, networking, and security. For access to individual subprofiles,
   see the `pyVmomi.vim.profile.host.HostApplyProfile` data object
   (`pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.applyProfile`).
   
   Host profiles are part of the stateless configuration architecture.
   In the stateless environment, a Profile Engine runs on each ESX host,
   but an ESX host does not store its own configuration state. Instead,
   host configuration data is stored on vCenter Servers. Every time a host
   boots or reboots, it obtains its profile from the vCenter Server.
   - To create a base host profile use the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.ProfileManager.createProfile`
     method. To create a profile from an ESX host, specify a
     `pyVmomi.vim.profile.host.HostProfile.HostBasedConfigSpec`. To create a profile from a file,
     specify a `pyVmomi.vim.profile.host.HostProfile.SerializedHostProfileSpec`.
   - To create a subprofile for a particular host capability, use the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.createDefaultProfile`
     method. After you create the default profile you can modify it and save it in the base profile.
   - To update an existing profile, use the
     `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.update` method.
   - To apply a host profile to an ESX host, use the `pyVmomi.vim.profile.host.HostProfile.execute` method
     to generate configuration changes, then call the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
     method to apply them.
     
   Host-Specific Configuration
   
   An individual host or a set of hosts may have some configuration settings
   that are different from the settings specified in the host profile.
   For example, the IP configuration for the host's virtual network adapters
   must be unique.
   - To verify host-specific data, use the `deferredParam` parameter
     to the `pyVmomi.vim.profile.host.HostProfile.execute` method.
     The Profile Engine will determine if you have specified all of the required
     parameters for the host configuration. If additional data is required,
     call the `pyVmomi.vim.profile.host.HostProfile.execute` method again as many times as necessary
     to verify a complete set of parameters.
   - To apply host-specific data, use the `userInput` parameter to the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
     method.
     
     
   The Profile Engine saves host-specific data in an `pyVmomi.vim.profile.host.AnswerFile`
   that is stored on the vCenter Server.
   The `pyVmomi.vim.profile.host.ProfileManager` provides several methods to manipulate
   answer files.
   
   Profile Compliance
   
   You can create associations between hosts and profiles to support compliance checking.
   When you perform compliance checking, you can determine if a host configuration
   conforms to a host profile.
   - To create an association between a host and a profile, use the
     `pyVmomi.vim.profile.Profile.associateEntities` method.
     The method adds the host to the
     `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.entity`[] list.
   - To retrieve the list of profiles associated with a host, use the
     `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.ProfileManager.findAssociatedProfile`
     method.
   - To check host compliance, use the
     `pyVmomi.vim.profile.Profile.checkCompliance` method.
     If you do not specify any hosts, the method will check the compliance of all hosts
     that are associated with the profile.
     
     
   You can also use the Profile Compliance Manager to check compliance by specifying
   profiles, entities (hosts), or both. See
   `pyVmomi.vim.profile.ComplianceManager`.`pyVmomi.vim.profile.ComplianceManager.checkCompliance`.
   
   Profile Plug-Ins
   
   The vSphere architecture uses VMware profile plug-ins to define profile extensions.
   For information about using a plug-in to extend a host profile, see the VMware Technical Note
   Developing a Host Profile Extension Plug-in.
   
   For access to host configuration data that is defined by plug-ins, use the
   `pyVmomi.vim.profile.ApplyProfile`.`pyVmomi.vim.profile.ApplyProfile.policy`[] and
   `pyVmomi.vim.profile.ApplyProfile`.`pyVmomi.vim.profile.ApplyProfile.property`[] lists.
   The `pyVmomi.vim.profile.host.HostApplyProfile` and its subprofiles, which collectively
   define host configuration data, are derived from the `pyVmomi.vim.profile.ApplyProfile`.
   - Policies store ESX configuration data in `pyVmomi.vim.profile.PolicyOption` objects.
   - Profile property lists contain subprofiles defined by plug-ins. Subprofiles can be nested.
     - Subprofile lists are available as an extension to the base host profile
       (`pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.applyProfile`.`pyVmomi.vim.profile.ApplyProfile.property`[]).
     - Subprofile lists are available as extensions to the host subprofiles - for example,
       the network subprofile
       (`pyVmomi.vim.profile.host.HostApplyProfile`.`pyVmomi.vim.profile.host.HostApplyProfile.network`.`pyVmomi.vim.profile.ApplyProfile.property`[]).
       
     
   If you make changes to host profile data, later versions of profile plug-ins may not support
   the host configuration implied by the changes that you make. When a subsequent vSphere
   version becomes available, you must verify that the new version supports any previous
   configuration changes that you have made.
   """
   class ConfigInfo(pyVmomi.vim.profile.Profile.ConfigInfo):
      """
      The `pyVmomi.vim.profile.host.HostProfile.ConfigInfo` data object
      contains host profile data and information about profile compliance.
      
      Attributes:
          applyProfile: Profile data for host configuration.
          defaultComplyProfile: Default compliance profile.
              
              The ESX Server uses the `applyProfile`
              (`pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.applyProfile`)
              to generate the default compliance profile when you create a host profile.
              When the `applyProfile` is modified, the Server automatically
              updates the compliance profile to match it.
          defaultComplyLocator: List of compliance locators.
              
              Each locator specifies an association between
              the `applyProfile` and the `defaultComplyProfile`.
              The association identifies a component profile and the expression generated
              by the profile. vSphere clients can use this data to provide contextual
              information to the user.
          customComplyProfile: User defined compliance profile.
              
              Reserved for future use.
          disabledExpressionList: Disabled expressions in the default compliance profile
              (`DefaultComplyProfile`).
              
              Use this property to specify which expressions are disabled.
              All expressions are enabled by default.
          description: Localized description of the profile.
      """
      applyProfile: _typing.Optional[HostApplyProfile] = None
      defaultComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      defaultComplyLocator: list[pyVmomi.vim.profile.ComplianceLocator] = []
      customComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      disabledExpressionList: list[str] = []
      description: _typing.Optional[pyVmomi.vim.profile.Profile.Description] = None

   class ConfigSpec(pyVmomi.vim.profile.Profile.CreateSpec):
      """
      `pyVmomi.vim.profile.host.HostProfile.ConfigSpec` is the base data object
      for all `pyVmomi.vim.profile.host.HostProfile` configuration specifications.
      """
      pass

   class SerializedHostProfileSpec(pyVmomi.vim.profile.Profile.SerializedCreateSpec):
      """
      The `pyVmomi.vim.profile.host.HostProfile.SerializedHostProfileSpec` data object
      contains a string representation of a host profile.
      
      Use this object when you
      create a host profile from a file.
      
      Attributes:
          validatorHost: Host for profile validation.
              
              This can be a host on which
              the profile is intended to be used.
          validating: If \"false\", then the host profile will be saved without being validated.
              
              The default if not specified is \"true\".
              This option should be used with caution, since the resulting host profile
              will not be checked for errors.
      """
      validatorHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      validating: _typing.Optional[bool] = None

   class CompleteConfigSpec(HostProfile.ConfigSpec):
      """
      The `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec` data object
      specifies the complete configuration for a host profile.
      
      Attributes:
          applyProfile: Profile that contains configuration data for the host.
          customComplyProfile: User defined compliance profile.
              
              Reserved for future use.
          disabledExpressionListChanged: Flag indicating if this configuration specification contains changes
              in the `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.disabledExpressionList`.
              
              If False, the Profile Engine ignores the contents of the disabled expression list.
          disabledExpressionList: List of expressions to be disabled.
              
              Each entry in the list specifies
              a `pyVmomi.vim.profile.Expression`.`pyVmomi.vim.profile.Expression.id`.
              All expressions are enabled by default.
              
              If you set `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.disabledExpressionListChanged`
              to True, the Profile Engine uses the contents of this list to replace the contents
              of the `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.disabledExpressionList`.
              
              The expression list is contained in the
              `pyVmomi.vim.profile.host.HostProfile.ConfigInfo.defaultComplyProfile`.
              The Profile Engine automatically generates the default compliance profile
              when you create a host profile.
          validatorHost: Host for profile validation.
              
              This can be a host on which the profile
              is intended to be used. If you do not specify a validator host,
              the Profile Engine uses the `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.referenceHost`
              to validate the profile.
          validating: If \"false\", then the host profile will be saved without being validated.
              
              The default if not specified is \"true\".
              This option should be used with caution, since the resulting host profile
              will not be checked for errors.
          hostConfig: Host profile configuration data and compliance information.
              
              If `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.hostConfig` is set,
              then the HostApplyProfile
              `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.applyProfile` and
              ComplianceProfile
              `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.customComplyProfile`
              should not be set in CompleteConfigSpec.
      """
      applyProfile: _typing.Optional[HostApplyProfile] = None
      customComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      disabledExpressionListChanged: bool
      disabledExpressionList: list[str] = []
      validatorHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      validating: _typing.Optional[bool] = None
      hostConfig: _typing.Optional[HostProfile.ConfigInfo] = None

   class HostBasedConfigSpec(HostProfile.ConfigSpec):
      """
      The `pyVmomi.vim.profile.host.HostProfile.HostBasedConfigSpec` data object
      specifies the host from which configuration data is to be extracted
      and the profile(s) to be created or updated.
      
      Attributes:
          host: ESX host.
          useHostProfileEngine: Flag indicating if the Profile Engine should use the profile
              plug-ins present on the host to create the profile.
              
              If `true`, the host Profile Engine uses the vSphere 5.0
              (or later) profile plug-ins. The resulting profile is not compatible
              with legacy hosts (pre 5.0). If `false` or not specified,
              the Profile Engine creates a legacy host profile.
      """
      host: pyVmomi.vim.HostSystem
      useHostProfileEngine: _typing.Optional[bool] = None

   class ValidationState(pyVmomi.VmomiSupport.Enum):
      """This defines validation state values for host profile."""
      Ready: _typing.ClassVar['HostProfile.ValidationState'] = 'Ready'
      Running: _typing.ClassVar['HostProfile.ValidationState'] = 'Running'
      Failed: _typing.ClassVar['HostProfile.ValidationState'] = 'Failed'

   class ValidationFailureInfo(pyVmomi.vmodl.DynamicData):
      """
      This defines the validation result for the host profile.
      
      Attributes:
          name: The name of host profile to be validated.
          annotation: Host profile annotation at update.
          updateType: Host profile update type.
              
              See the enumerate class
              `UpdateType` above for the valid values.
          host: The host where the host profile is updated from.
          applyProfile: The host configuration after validation.
          failures: List of failures in the host profile configuration.
          faults: The `MethodFault`s happened at validation.
      """
      class UpdateType(pyVmomi.VmomiSupport.Enum):
         """
         Types of host profile update.
         
         Attributes:
             HostBased: Update host profile from host.
             Import: Import host profile.
             Edit: Edit host profile.
             Compose: Compose setting from host profile.
         """
         HostBased: _typing.ClassVar['HostProfile.ValidationFailureInfo.UpdateType'] = 'HostBased'
         Import: _typing.ClassVar['HostProfile.ValidationFailureInfo.UpdateType'] = 'Import'
         Edit: _typing.ClassVar['HostProfile.ValidationFailureInfo.UpdateType'] = 'Edit'
         Compose: _typing.ClassVar['HostProfile.ValidationFailureInfo.UpdateType'] = 'Compose'

      name: str
      annotation: str
      updateType: str
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      applyProfile: _typing.Optional[HostApplyProfile] = None
      failures: list[pyVmomi.vim.fault.ProfileUpdateFailed.UpdateFailure] = []
      faults: list[pyVmomi.vmodl.MethodFault] = []

   @property
   def validationState(self) -> _typing.Optional[str]:
      """
      State of the host profile validation operation.
      
      The values
      of the state will be one of `pyVmomi.vim.profile.host.HostProfile.ValidationState` enumerations.
      """
      ...
   @property
   def validationStateUpdateTime(self) -> _typing.Optional[_datetime.datetime]:
      """Update time of the validation operation."""
      ...
   @property
   def validationFailureInfo(self) -> _typing.Optional[HostProfile.ValidationFailureInfo]:
      """
      This object is created or updated if the `pyVmomi.vim.profile.host.HostProfile.ValidationState`
      is Failed.
      
      This object captures the most recent validation
      result for the host profile object in case of failure.
      """
      ...
   @property
   def complianceCheckTime(self) -> _typing.Optional[_datetime.datetime]:
      """
      The latest compliance check time.
      
      Since: vSphere API Release 8.0.1.0
      """
      ...
   @property
   def referenceHost(self) -> _typing.Optional[pyVmomi.vim.HostSystem]:
      """
      Reference host in use for this host profile.
      
      To set this property,
      use the `pyVmomi.vim.profile.host.HostProfile.updateReferenceHost`
      method. If you do not specify a host for validation
      (`pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec`.`pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec.validatorHost`),
      the Profile Engine uses the reference host to validate the profile.
      """
      ...

   def ResetValidationState(self) -> None:
      """
      This API will update the validationState to Ready
      from Failed, invalidate the validationFailureInfo
      and reset the validationStateUpdateTime.
      
      This API will return error if the validationState
      is Running.
      """
      ...
   def UpdateReferenceHost(self, host: _typing.Optional[pyVmomi.vim.HostSystem]) -> None:
      """
      Sets the `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.referenceHost` property.
      
      Args:
          host: Reference host to use. If unset, the `pyVmomi.vim.profile.host.HostProfile.referenceHost`
              property is cleared.
      """
      ...
   def Update(self, config: HostProfile.ConfigSpec) -> None:
      """
      Update the `HostProfile` with the specified configuration data.
      
      Args:
          config: Specification containing the new data.
      
      Raises:
          pyVmomi.vim.fault.DuplicateName: If the profile with the new name already exists.
          pyVmomi.vim.fault.ProfileUpdateFailed: if errors were encountered when updating
              the profile.
      """
      ...
   def Execute(self, host: pyVmomi.vim.HostSystem, deferredParam: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter]) -> ExecuteResult:
      """
      Run the Profile Engine to determine the list of configuration changes
      needed for the specified host.
      
      The method generates configuration changes
      based on the host profile.
      
      You can also specify deferred parameters to verify additional host-specific data.
      The Profile Engine uses the policy options
      (`pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.applyProfile`.`pyVmomi.vim.profile.ApplyProfile.policy`[])
      to determine the required parameters
      (`pyVmomi.vim.profile.PolicyOption`.`pyVmomi.vim.profile.PolicyOption.parameter`[])
      for host configuration. If you do not provide all of the required parameters,
      you must call the method again to provide the complete list to the Profile Engine.
      After successful profile execution, when you apply the profile,
      the Profile Engine will save the host-specific data in an `pyVmomi.vim.profile.host.AnswerFile`.
      
      Args:
          host: Host on which to execute the profile.
              The host does not have to be associated with the profile.
          deferredParam: Additional configuration data to be applied to the host.
              This should contain all of the host-specific data, including data from from
              previous calls to the method.
      
      Returns:
          Result of the execution. If the operation is successful
          (`pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.status``=success`),
          the result object includes a valid host configuration specification that you can pass to the
          `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
          method.
          
          If the operation is not successful, the object contains error information
          or information about additional data required for the host configuration.
          If additional data is required, the required input list
          (`pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.requireInput`[])
          contains both the `deferredParam` data and paths to missing parameters.
          After you fill in the missing parameters, pass the complete required input
          list via the `deferredParam` parameter in another call to the execute method
          to finish input verification. After successful profile execution, you can pass
          the verified required input list to the `pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
          method.
      """
      ...


class HostSpecification(pyVmomi.vmodl.DynamicData):
   """
   The host specification data are those needed at host boot time to create and
   configure virtual devices and host services.
   
   The `pyVmomi.vim.profile.host.HostSpecification` data object contains a collection of host sub
   specification data.
   For host sub specification data, see
   `pyVmomi.vim.profile.host.HostSubSpecification`
   for details.
   
   Attributes:
       createdTime: Time at which the host specification was created.
       lastModified: Time at which the host specification was last modified.
           
           If it isn't set,
           it is the same as `createdTime`.
       host: The host that the spec data belongs to.
       subSpecs: The collection of the host sub specifications.
           
           It is optional.
       changeID: The change ID for querying the host specification data updated in a
           time period.
           
           It has a format of timestamp:change_number, where
           timestamp is the decimal string of a start time, and change_number is
           the decimal string of an auto incremented variable counting from the
           start time.
   """
   createdTime: _datetime.datetime
   lastModified: _typing.Optional[_datetime.datetime] = None
   host: pyVmomi.vim.HostSystem
   subSpecs: list[HostSubSpecification] = []
   changeID: _typing.Optional[str] = None


class HostSpecificationManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.vim.profile.host.HostSpecificationManager` provides the
   functionality to update, restrieve and delete
   `pyVmomi.vim.profile.host.HostSpecification` and
   `pyVmomi.vim.profile.host.HostSubSpecification`.
   """
   def UpdateHostSpecification(self, host: pyVmomi.vim.HostSystem, hostSpec: HostSpecification) -> None:
      """
      Update the host specification with the provided copy.
      
      If there is no host specification for the host, create the host
      specification for this host in the host specification \"database\";
      otherwise, update the host specification with the provided.
      `pyVmomi.vim.profile.host.HostSpecification` object.
      On success, it will fire a `HostSpecificationChangedEvent`.
      
      Args:
          host: The host whose specification will be updated.
          hostSpec: The new host specification to be updated with.
      
      Raises:
          pyVmomi.vim.fault.HostSpecificationOperationFailed: If the method fails.
      """
      ...
   def UpdateHostSubSpecification(self, host: pyVmomi.vim.HostSystem, hostSubSpec: HostSubSpecification) -> None:
      """
      Update the host specification with the provided host sub specification.
      
      If there is no host specification for the host, create the host
      specification, which contains only the provided host sub specification,
      for this host; otherwise, add or update the host specification with the
      provided `pyVmomi.vim.profile.host.HostSubSpecification` object.
      This method provides a way to incrementally build the host specification.
      On success, it will fire a `HostSpecificationChangedEvent`.
      
      Args:
          host: The host whose specification will be updated.
          hostSubSpec: The data object for the new host sub specification.
      
      Raises:
          pyVmomi.vim.fault.HostSpecificationOperationFailed: If the method fails.
      """
      ...
   def RetrieveHostSpecification(self, host: pyVmomi.vim.HostSystem, fromHost: bool) -> HostSpecification:
      """
      Retrieve the host specification.
      
      When the parameter `fromHost`
      is `true`, the host specification is retrieved from the host;
      otherwise, it is from the host specification \"database\" for this manager.
      When retrieved from host, the copy in host specification \"database\" will
      be updated. On success, it will fire a
      `HostSpecificationChangedEvent`.
      
      Args:
          host: The specified host whose host specification will be retrieved.
          fromHost: Whether retrieve from the host.
      
      Returns:
          The host specification of the specified host.
      
      Raises:
          pyVmomi.vim.fault.HostSpecificationOperationFailed: If the method fails when retrieve
              from host.
      """
      ...
   def DeleteHostSubSpecification(self, host: pyVmomi.vim.HostSystem, subSpecName: str) -> None:
      """
      Delete the host sub specification specified by the provided `
      subSpecname` of the specified host.
      
      Args:
          host: The specified host for which the sub specification will be
              deleted.
          subSpecName: The name of the host sub specification to be deleted.
      
      Raises:
          pyVmomi.vim.fault.HostSpecificationOperationFailed: If the method fails when delete
              the sub spec.
      """
      ...
   def DeleteHostSpecification(self, host: pyVmomi.vim.HostSystem) -> None:
      """
      Delete the host specification of the specified host.
      
      Args:
          host: The specified host for which the specification will be
              deleted.
      
      Raises:
          pyVmomi.vim.fault.HostSpecificationOperationFailed: If the method fails when delete
              the spec.
      """
      ...
   def GetUpdatedHosts(self, startChangeID: _typing.Optional[str], endChangeID: _typing.Optional[str]) -> list[pyVmomi.vim.HostSystem]:
      """
      Query the hosts whose specification was updated in the specified
      time period.
      
      When the `startChangeID` isn't provided, it will
      return all the host updated before the `endChangeID`. When the
      `endChangeID` isn't provided, it will return all the hosts
      updated after `startChangeID`. If both aren't provided, all
      hosts having host spec will be returned.
      The format of the change ID is defined at
      `pyVmomi.vim.profile.host.HostSpecification.changeID`.
      
      Args:
          startChangeID: The beginning of the time period.
          endChangeID: The ending of the time period.
      
      Returns:
          The queried host list.
      """
      ...


class HostSubSpecification(pyVmomi.vmodl.DynamicData):
   """
   Host sub specification data are the data used when create a virtual
   device, and/or configure the virtual device and its related
   host services.
   
   A typical example of host sub specification data is the DVS host view
   specification, which is used when create DVS host view on an ESXi
   host and configure the virtual switch on the host.
   The introduction of this type of data is for improving the
   availability of the ESXi host management. For example, when
   the VirtualCenter server is not available, an ESXi host will
   have enough information to reconfigure DVS host view properly
   when the ESXi host is booted from stateless or stateless caching.
   Host sub specification data are data for VMware internal data
   structure used in virtual device creation and configuration.
   They are different to `pyVmomi.vim.profile.host.AnswerFile`
   which are from public knowledge domain or the public API
   of VMware ESXi host services.
   When the host sub specification data for a single feature
   are stored in multiple host sub specification data objects,
   it is the responsibility of the host specification source
   in this feature to guarantee the completeness and consistency
   of these host sub specification objects.
   
   Attributes:
       name: The full name of the host sub specification.
           
           The format of this member
           variable is:
           CompanyName_ProductName_SubSpecName.
           Thus, name conflict is avoided by containing the
           `company name`, `product name`, and ` sub
           specification name` in this full name.
       createdTime: Time at which the host sub specification was created.
       data: The host sub specification data
       binaryData: The host sub specification data in Binary for wire efficiency.
   """
   name: str
   createdTime: _datetime.datetime
   data: list[pyVmomi.VmomiSupport.byte] = []
   binaryData: _typing.Optional[pyVmomi.VmomiSupport.binary] = None


class IpAddressProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.IpAddressProfile` represents the Virtual NIC IP address.
   
   The `pyVmomi.vim.profile.ApplyProfile.policy` property contains
   the configuration data values for the IP address.
   """
   pass


class IpRouteProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.IpRouteProfile` data object represents the host IP route configuration.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       staticRoute: List of static routes to be configured.
   """
   staticRoute: list[StaticRouteProfile] = []


class NasStorageProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.NasStorageProfile` data object represents one NAS datastore configuration.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the NAS storage profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list
   for access to subprofile configuration data, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class NetStackInstanceProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.NetStackInstanceProfile` data object represents a subprofile
   for a netStackInstance.
   
   Attributes:
       key: Linkable identifier.
       dnsConfig: DnsConfig SubProfile for this instance of the stack.
       ipRouteConfig: IpRoute SubProfile for this instance of the stack.
   """
   key: str
   dnsConfig: NetworkProfile.DnsConfigProfile
   ipRouteConfig: IpRouteProfile


class NetworkPolicyProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.NetworkPolicyProfile` data object represents a
   network policy.
   
   The `pyVmomi.vim.profile.ApplyProfile.policy` property
   contains network configuration data values.
   """
   pass


class NetworkProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.NetworkProfile` data object contains a set of subprofiles for
   network configuration.
   
   Attributes:
       vswitch: List of virtual switch subprofiles.
           
           Use the `pyVmomi.vim.profile.host.VirtualSwitchProfile.key` property to access
           a subprofile in the list.
       vmPortGroup: List of port groups for use by virtual machines.
           
           Use the `pyVmomi.vim.profile.host.VmPortGroupProfile`.`pyVmomi.vim.profile.host.PortGroupProfile.key`
           property to access a port group in the list.
       hostPortGroup: List of port groups for use by the host.
           
           Use the `pyVmomi.vim.profile.host.HostPortGroupProfile`.`pyVmomi.vim.profile.host.PortGroupProfile.key` property
           to access port groups in the list.
       serviceConsolePortGroup: List of port groups for use by the service console.
           
           The Profile Engine uses this field only when applying a profile
           to a host that has a service console.
       dnsConfig: DNS (Domain Name System) configuration subprofile.
       ipRouteConfig: Subprofile that describes the IP Route
           configuration for the VMKernel gateway.
       consoleIpRouteConfig: Subprofile that describes the IP Route configuration
           for the Service Console gateway.
       pnic: List of subprofiles that represent physical NIC configuration.
           
           Use the `pyVmomi.vim.profile.host.PhysicalNicProfile.key` property to access a
           subprofile in the list.
       dvswitch: List of subprofiles for distributed virtual switches to which this host is connected.
           
           Use the `pyVmomi.vim.profile.host.DvsProfile.key` property to access a subprofile in the list.
       dvsServiceConsoleNic: List of subprofiles for service console Virtual NICs connected to a distributed virtual switch.
           
           Use the `pyVmomi.vim.profile.host.DvsServiceConsoleVNicProfile`.`pyVmomi.vim.profile.host.DvsVNicProfile.key` property
           to access a subprofile in the list.
       dvsHostNic: List of subprofiles for host Virtual NICs connected to a distributed virtual switch.
           
           Use the `pyVmomi.vim.profile.host.DvsHostVNicProfile`.`pyVmomi.vim.profile.host.DvsVNicProfile.key` property
           to access a subprofile in the list.
       nsxHostNic: List of subprofiles for host Virtual NICs connected to a NSX logic switch.
           
           Use the `pyVmomi.vim.profile.host.NsxHostVNicProfile`.`pyVmomi.vim.profile.host.NsxHostVNicProfile.key` property
           to access a subprofile in the list.
       netStackInstance: List of NetStackInstance subprofiles.
           
           Use the `pyVmomi.vim.profile.host.NetStackInstanceProfile.key` property to access
           a subprofile in the list.
       opaqueSwitch: OpaqueSwitch subprofile.
   """
   class DnsConfigProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      The `pyVmomi.vim.profile.host.NetworkProfile.DnsConfigProfile` data object represents DNS configuration
      for the host.
      
      Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for
      access to configuration data for the DNS profile. Use the
      `pyVmomi.vim.profile.ApplyProfile.property` list for access to subprofiles, if any.
      """
      pass

   vswitch: list[VirtualSwitchProfile] = []
   vmPortGroup: list[VmPortGroupProfile] = []
   hostPortGroup: list[HostPortGroupProfile] = []
   serviceConsolePortGroup: list[ServiceConsolePortGroupProfile] = []
   dnsConfig: _typing.Optional[NetworkProfile.DnsConfigProfile] = None
   ipRouteConfig: _typing.Optional[IpRouteProfile] = None
   consoleIpRouteConfig: _typing.Optional[IpRouteProfile] = None
   pnic: list[PhysicalNicProfile] = []
   dvswitch: list[DvsProfile] = []
   dvsServiceConsoleNic: list[DvsServiceConsoleVNicProfile] = []
   dvsHostNic: list[DvsHostVNicProfile] = []
   nsxHostNic: list[NsxHostVNicProfile] = []
   netStackInstance: list[NetStackInstanceProfile] = []
   opaqueSwitch: _typing.Optional[OpaqueSwitchProfile] = None


class NsxHostVNicProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.NsxHostVNicProfile` data object is the base object
   for host Virtual NIC connected to NSX logic switch subprofiles.
   
   If a profile plug-in defines additional policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the configuration data.
   
   Attributes:
       key: Linkable identifier.
       ipConfig: IP address for the Virtual NIC belonging to a logic switch.
   """
   key: str
   ipConfig: IpAddressProfile


class OpaqueSwitchProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.OpaqueSwitchProfile` data object represents opaque switch
   configuration for the host.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   """
   pass


class OptionProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.OptionProfile` data object encapsulates one advanced configuration.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the option profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list for access
   to subprofile configuration data, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class PermissionProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.PermissionProfile` data object represents the profile
   for a permission rule.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for
   access to configuration data for the permission profile. Use the
   `pyVmomi.vim.profile.ApplyProfile.property` list for access to subprofiles, if any.
   """
   key: str


class PhysicalNicProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.PhysicalNicProfile` data object represents physical NIC configuration.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the physical NIC profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list
   for access to subprofile configuration data, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class PnicUplinkProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.PnicUplinkProfile` data object specifies the mapping between
   a physical NIC and an uplink port.
   
   The `pyVmomi.vim.profile.ApplyProfile.policy` property contains
   the configuration data values.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class ProfileManager(pyVmomi.vim.profile.ProfileManager):
   """
   The `pyVmomi.vim.profile.host.ProfileManager` provides access to a list of
   `pyVmomi.vim.profile.host.HostProfile`s and it defines methods to manipulate
   profiles and `pyVmomi.vim.profile.host.AnswerFile`s.
   """
   class TaskListRequirement(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.TaskListRequirement` enum
      defines possible values for requirements when applying a `pyVmomi.vim.host.ConfigSpec`
      object returned as part of a `generateConfigTaskList`
      operation.
      
      Attributes:
          maintenanceModeRequired: The ESXi host must be in maintenance mode before the task list can be
              applied.
          rebootRequired: The ESXi host must be rebooted after the task list is applied in order
              for the new settings in the `pyVmomi.vim.host.ConfigSpec` to take
              effect on the host.
      """
      maintenanceModeRequired: _typing.ClassVar['ProfileManager.TaskListRequirement'] = 'maintenanceModeRequired'
      rebootRequired: _typing.ClassVar['ProfileManager.TaskListRequirement'] = 'rebootRequired'

   class ConfigTaskList(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.ConfigTaskList` data object
      represents a set of tasks to be performed on a host during host profile application.
      
      Attributes:
          configSpec: Set of configuration changes to be applied to the host.
          taskDescription: Description of tasks that will be performed on the host
              to carry out HostProfile application.
          taskListRequirement: A set of requirements whose actions must be fulfilled before and/or
              after the task list is applied on an ESXi host, e.g.
              
              whether the ESXi
              host must be in maintenance mode prior to applying the `configSpec`,
              or whether the host will need to be rebooted after applying the `configSpec`.
              See `pyVmomi.vim.profile.host.ProfileManager.TaskListRequirement` for
              details of supported values.
      """
      configSpec: _typing.Optional[pyVmomi.vim.host.ConfigSpec] = None
      taskDescription: list[pyVmomi.vmodl.LocalizableMessage] = []
      taskListRequirement: list[str] = []

   class AnswerFileCreateSpec(pyVmomi.vmodl.DynamicData):
      """
      Base class for host-specific answer file options.
      
      Attributes:
          validating: If \"false\", then the answer file will be saved without being validated.
              
              The default if not specified is \"true\".
              This option should be used with caution, since the resulting answer
              file will not be checked for errors.
      """
      validating: _typing.Optional[bool] = None

   class AnswerFileOptionsCreateSpec(ProfileManager.AnswerFileCreateSpec):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.AnswerFileOptionsCreateSpec`
      data object contains host-specific user input for an answer file.
      
      Attributes:
          userInput: List of parameters that contain host-specific data.
      """
      userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []

   class AnswerFileSerializedCreateSpec(ProfileManager.AnswerFileCreateSpec):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.AnswerFileSerializedCreateSpec` data object
      contains a serialized string representation of host-specific data for an answer file.
      
      Attributes:
          answerFileConfigString: Host-specific user input.
      """
      answerFileConfigString: str

   class AnswerFileStatus(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.AnswerFileStatus` enum
      defines possible values for answer file status.
      
      Attributes:
          valid: Answer file is valid.
          invalid: Answer file is not valid.
              
              The file is either missing or incomplete.
              - To produce an answer file, pass host-specific data (user input) to the
                `pyVmomi.vim.profile.host.ProfileManager`.`pyVmomi.vim.profile.host.ProfileManager.applyHostConfiguration`
                method.
              - To produce a complete answer file, call the
                `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
                method and fill in any missing parameters in the returned
                `pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.requireInput`
                list. After you execute the profile successfully, you can pass the complete required
                input list to the apply method.
          unknown: Answer file status is not known.
      """
      valid: _typing.ClassVar['ProfileManager.AnswerFileStatus'] = 'valid'
      invalid: _typing.ClassVar['ProfileManager.AnswerFileStatus'] = 'invalid'
      unknown: _typing.ClassVar['ProfileManager.AnswerFileStatus'] = 'unknown'

   class EntityCustomizations(pyVmomi.vmodl.DynamicData):
      """
      Data type used to contain a representation of host or cluster customization
      data in a `pyVmomi.vim.profile.host.ProfileManager.CustomizationData` object.
      
      Subclasses of this must be defined to provide host or cluster customization
      data in specific formats.
      """
      pass

   class StructuredCustomizations(ProfileManager.EntityCustomizations):
      """
      Implementation of `pyVmomi.vim.profile.host.ProfileManager.EntityCustomizations`
      that maps a cluster or host profile to the `pyVmomi.vim.profile.host.AnswerFile`
      object containing the host profiles customizations for that entity.
      
      This
      object will be used as elements of the
      `pyVmomi.vim.profile.host.ProfileManager.EntityCustomizations`.{vim.profile.host.ProfileManager.EntityCustomizations#entityCustomizations}
      when the `pyVmomi.vim.profile.host.ProfileManager.EntityCustomizations`.{vim.profile.host.ProfileManager.EntityCustomizations#customizationsFormat}
      value is \"structured\".
      
      Attributes:
          entity: Entity associated with the host customizations specified in the
              `customizations` `pyVmomi.vim.profile.host.AnswerFile` object.
              
              In the current release, this object will always be a host.
          customizations: Host Profile Customizations for the associated `entity`.
              
              This is the same object that would be returned by the
              `pyVmomi.vim.profile.host.ProfileManager.retrieveAnswerFile` method
      """
      entity: pyVmomi.vim.ManagedEntity
      customizations: _typing.Optional[AnswerFile] = None

   class HostToConfigSpecMap(pyVmomi.vmodl.DynamicData):
      """
      Data class for `HostSystem`-`AnswerFileCreateSpec`
      mapping.
      
      Attributes:
          host: The host
          configSpec: The corresponding `AnswerFileCreateSpec`.
      """
      host: pyVmomi.vim.HostSystem
      configSpec: ProfileManager.AnswerFileCreateSpec

   class ApplyHostConfigSpec(ExecuteResult):
      """
      The data object that contains the objects needed to remediate a host
      in host profile batch apply.
      
      Attributes:
          host: The host to be remediated.
          taskListRequirement: The task requirements from the results of
              `pyVmomi.vim.profile.host.ProfileManager.generateConfigTaskList` method
          taskDescription: Description of tasks that will be performed on the host
              to carry out HostProfile application.
          rebootStateless: For a stateless host, there are two approaches to apply a host
              profile:
              (1) Reboot the host and apply the host profile at boot time.
              
              (2) Apply the host profile directly from VC. We call this as
              regular apply.
              The variable rebootStateless allows users to choose the first
              approach from the two approaches above:
              apply host profile by rebooting this host.
          rebootHost: For regular apply, when some of the tasks requires reboot,
              that this variable is`true` indicates that the
              reboot automatically happens in the batch profile apply
              than that the user will manually reboot the system later.
              
              For stateless host, this variable takes effect only when
              the variable `rebootStateless` above is
              `false`.
          faultData: This contains the error details.
      """
      host: pyVmomi.vim.HostSystem
      taskListRequirement: list[str] = []
      taskDescription: list[pyVmomi.vmodl.LocalizableMessage] = []
      rebootStateless: _typing.Optional[bool] = None
      rebootHost: _typing.Optional[bool] = None
      faultData: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class ApplyHostConfigResult(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigResult` data object contains the remediation
      results for a host: the time that the remediation happens, the status,
      the errors, and optional compliance result after reboot.
      
      Attributes:
          startTime: Time that the host config apply starts.
          completeTime: Time that the host config apply completes.
          host: Host to be remediated.
          status: Status of the remediation.
              
              See
              `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigResult.Status`
              for valid values.
          errors: If `status` is `fail`, this property contains
              a list of status error message objects.
      """
      class Status(pyVmomi.VmomiSupport.Enum):
         """
         Attributes:
             success: Remediation succeeded.
             failed: Remediation failed.
             reboot_failed: Remediation succeeded but reboot after remediation failed.
                 
                 May treat this as a warning.
             stateless_reboot_failed: Stateless reboot for remediation failed.
             check_compliance_failed: Remediation and reboot succeeded but check compliance after reboot
                 failed.
                 
                 May treat this as a warning.
             state_not_satisfied: The required state is not satisfied so host profile apply cannot
                 be done.
             exit_maintenancemode_failed: Exit maintenance mode failed.
             canceled: The remediation was canceled.
         """
         success: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'success'
         failed: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'failed'
         reboot_failed: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'reboot_failed'
         stateless_reboot_failed: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'stateless_reboot_failed'
         check_compliance_failed: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'check_compliance_failed'
         state_not_satisfied: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'state_not_satisfied'
         exit_maintenancemode_failed: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'exit_maintenancemode_failed'
         canceled: _typing.ClassVar['ProfileManager.ApplyHostConfigResult.Status'] = 'canceled'

      startTime: _datetime.datetime
      completeTime: _datetime.datetime
      host: pyVmomi.vim.HostSystem
      status: str
      errors: list[pyVmomi.vmodl.MethodFault] = []

   class CompositionValidationResult(pyVmomi.vmodl.DynamicData):
      """
      The data class for the host profile composition validation
      results.
      
      Attributes:
          results: The array of
              `pyVmomi.vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement`
              for all the target host profiles.
          errors: The common error happened at validation.
      """
      class ResultElement(pyVmomi.vmodl.DynamicData):
         """
         The host profile composition validation result for a specific target
         host profile.
         
         Attributes:
             target: The target host profile.
             status: The composition validation status.
                 
                 See `pyVmomi.vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement.Status`
                 for details of supported values.
             errors: The composition validation errors.
             sourceDiffForToBeMerged: When a selected sub profile for composition exists in both the
                 source and target host profile, this member will contain the
                 source side difference for the selected sub profiles.
             targetDiffForToBeMerged: Similar to the member `sourceDiffForToBeMerged` above
                 but contains the target side difference.
                 
                 Comparing the same
                 configurations in these two variables will show the changes for
                 the configurations that exist in both source and target host
                 profile.
             toBeAdded: The sub profiles doesn't exist in the target and will be added to
                 the target at host profile composition.
             toBeDeleted: The sub profiles exists in the target but not in the source and will
                 be deleted from the target at host profile composition.
             toBeDisabled: The sub profiles to be disabled in the target host profiles.
             toBeEnabled: The sub profiles to be enabled in the target host profiles.
             toBeReenableCC: The sub profile to be unset ignoring compliance check
                 in the target host profile.
         """
         class Status(pyVmomi.VmomiSupport.Enum):
            """The composition validation status class."""
            success: _typing.ClassVar['ProfileManager.CompositionValidationResult.ResultElement.Status'] = 'success'
            error: _typing.ClassVar['ProfileManager.CompositionValidationResult.ResultElement.Status'] = 'error'

         target: pyVmomi.vim.profile.Profile
         status: str
         errors: list[pyVmomi.vmodl.LocalizableMessage] = []
         sourceDiffForToBeMerged: _typing.Optional[HostApplyProfile] = None
         targetDiffForToBeMerged: _typing.Optional[HostApplyProfile] = None
         toBeAdded: _typing.Optional[HostApplyProfile] = None
         toBeDeleted: _typing.Optional[HostApplyProfile] = None
         toBeDisabled: _typing.Optional[HostApplyProfile] = None
         toBeEnabled: _typing.Optional[HostApplyProfile] = None
         toBeReenableCC: _typing.Optional[HostApplyProfile] = None

      results: list[ProfileManager.CompositionValidationResult.ResultElement] = []
      errors: list[pyVmomi.vmodl.LocalizableMessage] = []

   class CompositionResult(pyVmomi.vmodl.DynamicData):
      """
      The data class for host profile composition result.
      
      Attributes:
          errors: The composition errors for all targets, for example, the source
              profile doesn't exist.
          results: The array of
              `pyVmomi.vim.profile.host.ProfileManager.CompositionResult.ResultElement`
              for all the target host profiles.
      """
      class ResultElement(pyVmomi.vmodl.DynamicData):
         """
         Composition result for a specific target host profile.
         
         Attributes:
             target: The target host profile.
             status: The composition status.
                 
                 See `pyVmomi.vim.profile.host.ProfileManager.CompositionResult.ResultElement.Status`
                 for details of supported values.
             errors: The composition errors.
         """
         class Status(pyVmomi.VmomiSupport.Enum):
            """The composition status class."""
            success: _typing.ClassVar['ProfileManager.CompositionResult.ResultElement.Status'] = 'success'
            error: _typing.ClassVar['ProfileManager.CompositionResult.ResultElement.Status'] = 'error'

         target: pyVmomi.vim.profile.Profile
         status: str
         errors: list[pyVmomi.vmodl.LocalizableMessage] = []

      errors: list[pyVmomi.vmodl.LocalizableMessage] = []
      results: list[ProfileManager.CompositionResult.ResultElement] = []

   def ApplyHostConfiguration(self, host: pyVmomi.vim.HostSystem, configSpec: pyVmomi.vim.host.ConfigSpec, userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter]) -> pyVmomi.vim.Task:
      """
      Apply the configuration to the host.
      
      If you specify any user input,
      the configuration will be saved in the `pyVmomi.vim.profile.host.AnswerFile`
      associated with the host. If there is no answer file, the Profile Engine
      will create one.
      
      Args:
          host: Host to be updated. User must have sufficient credentials and privileges
              to satisfy the contents of the `configSpec`.
          configSpec: Set of configuration changes to be applied to the host.
              The changes are returned by the
              `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
              method in the
              `pyVmomi.vim.profile.host.ExecuteResult`.`pyVmomi.vim.profile.host.ExecuteResult.configSpec`
              property.
          userInput: Additional host-specific data to be applied to the host.
              This data is the complete list of deferred parameters verified by the
              `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.execute`
              method, contained in the `pyVmomi.vim.profile.host.ExecuteResult` object
              returned by the method.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the host is not in maintenance mode and the
              configuration specification requires it.
          pyVmomi.vim.fault.HostConfigFailed: if the ESX Server cannot apply the configuration changes.
      """
      ...
   def GenerateConfigTaskList(self, configSpec: pyVmomi.vim.host.ConfigSpec, host: pyVmomi.vim.HostSystem) -> ProfileManager.ConfigTaskList:
      """
      Deprecated: As of vSphere API 6.0 use
      `pyVmomi.vim.profile.host.ProfileManager.generateTaskList`Generate a list of configuration tasks that will be performed on the
      host during HostProfile application.
      
      Args:
          configSpec: ConfigSpec which was proposed by
              `pyVmomi.vim.profile.host.HostProfile.execute` method.
          host: Host on which the HostProfile application needs to be
              carried out.
      
      Returns:
          List of Configuration tasks.
      """
      ...
   def GenerateTaskList(self, configSpec: pyVmomi.vim.host.ConfigSpec, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task:
      """
      Generate a list of configuration tasks that will be performed on the
      host during HostProfile application.
      
      This differs from the
      `pyVmomi.vim.profile.host.ProfileManager.generateConfigTaskList` method in
      that it returns a task to monitor the progress of the operation.
      
      Args:
          configSpec: ConfigSpec which was proposed by
              `pyVmomi.vim.profile.host.HostProfile.execute` method.
          host: Host on which the HostProfile application needs to be
              carried out.
      
      Returns:
          List of Configuration tasks.
      """
      ...
   def QueryProfileMetadata(self, profileName: list[type], profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> list[pyVmomi.vim.profile.ProfileMetadata]:
      """
      Retrieve the metadata for a set of profiles.
      
      Args:
          profileName: Names of the profiles for which metadata is requested.
              If not set, the method returns metadata for all the profiles.
          profile: Base profile whose context needs to be used during the operation
      
      Returns:
          List of profile metadata objects.
      """
      ...
   def QueryProfileStructure(self, profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> pyVmomi.vim.profile.ProfileStructure:
      """
      Get information about the structure of the profile.
      
      Args:
          profile: Base profile whose context needs to be used during the operation
      
      Returns:
          The profile structure.
      """
      ...
   def CreateDefaultProfile(self, profileType: type, profileTypeName: _typing.Optional[str], profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> pyVmomi.vim.profile.ApplyProfile:
      """
      Create a default subprofile of a given type (for example, a
      `pyVmomi.vim.profile.host.VirtualSwitchProfile`).
      
      After you create
      the subprofile, you can add it to a configuration specification
      and update the host profile:
      - Call the `CreateDefaultProfile` method.
      - Create a `pyVmomi.vim.profile.host.HostProfile.CompleteConfigSpec` object.
      - Copy the existing profile from the host configuration information
        (`pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.Profile.config`.`pyVmomi.vim.profile.host.HostProfile.ConfigInfo.applyProfile`) to the configuration specification.
      - Add the new subprofile to the configuration specification. For example,
        if you create a `VirtualSwitchProfile`, you would add it to the list
        of virtual switches in the network profile for the configuration specification
        (`pyVmomi.vim.profile.host.NetworkProfile`.`pyVmomi.vim.profile.host.NetworkProfile.vswitch`[]).
      - Call `pyVmomi.vim.profile.host.HostProfile`.`pyVmomi.vim.profile.host.HostProfile.update`
        to save the new subprofile.
      
      Args:
          profileType: Type of profile to create. The profile types
              are system-defined
              (`pyVmomi.vim.profile.ApplyProfile`.`pyVmomi.vim.profile.ApplyProfile.profileTypeName`).
          profileTypeName: If specified, the method returns a profile object
              containing data for the named profile. The type name does not have
              to be system-defined. A user-defined profile can include various
              dynamically-defined profiles.
          profile: Base profile used during the operation.
      
      Returns:
          Derived subprofile of type `profileType`.
      """
      ...
   def UpdateAnswerFile(self, host: pyVmomi.vim.HostSystem, configSpec: ProfileManager.AnswerFileCreateSpec) -> pyVmomi.vim.Task:
      """
      Update the `pyVmomi.vim.profile.host.AnswerFile` for the specified host.
      
      If there is no answer file associated with the host, the Profile Engine
      uses the answer file configuration specification to create a new one.
      
      Args:
          host: Host with which the answer file is associated.
          configSpec: Host-specific configuration data. If the configuration
              specification does not contain any host-specific user input
              (`configSpec`.`pyVmomi.vim.profile.host.ProfileManager.AnswerFileOptionsCreateSpec.userInput`),
              the method does not perform any operation on the answer file.
      
      Raises:
          pyVmomi.vim.fault.AnswerFileUpdateFailed: If the answer file could not be updated.
      """
      ...
   def RetrieveAnswerFile(self, host: pyVmomi.vim.HostSystem) -> _typing.Optional[AnswerFile]:
      """
      Returns the answer file associated with a particular host.
      
      Args:
          host: Host with which the answer file is associated.
      
      Returns:
          Answer file object will be returned if it exists.
      """
      ...
   def RetrieveAnswerFileForProfile(self, host: pyVmomi.vim.HostSystem, applyProfile: HostApplyProfile) -> _typing.Optional[AnswerFile]:
      """
      Returns the answer file associated with a particular host, augmented
      with whatever answer file values are required for the supplied host
      profile.
      
      Args:
          host: Host with which the answer file is associated.
          applyProfile: Profile configuration used to generate answer file
      
      Returns:
          Answer file object will be returned.
      """
      ...
   def ExportAnswerFile(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task:
      """
      Export a host's answer file into a serialized form.
      
      The method returns a string
      that contains only the list of user input options.
      See `pyVmomi.vim.profile.host.AnswerFile`.`pyVmomi.vim.profile.host.AnswerFile.userInput`.
      
      Args:
          host: Host with which the answer file is associated.
      
      Returns:
          Serialized form of the answer file.
      """
      ...
   def CheckAnswerFileStatus(self, host: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Check the validity of the answer files for the specified hosts.
      
      The Profile Engine uses the profile associated with a host to check
      the answer file.
      
      Args:
          host: Set of hosts for which the answer file status will be checked.
      
      Returns:
          Returns the resulting answer file status.
      """
      ...
   def QueryAnswerFileStatus(self, host: list[pyVmomi.vim.HostSystem]) -> list[AnswerFileStatusResult]:
      """
      Returns the status of the answer files associated with specified hosts.
      
      This method returns the most recent status determined by
      `pyVmomi.vim.profile.host.ProfileManager.checkAnswerFileStatus`.
      See `pyVmomi.vim.profile.host.ProfileManager.AnswerFileStatus` for valid values.
      
      Args:
          host: The hosts the answer file is associated with.
      
      Returns:
          List of answer file status objects.
      """
      ...
   def RetrieveHostCustomizations(self, hosts: list[pyVmomi.vim.HostSystem]) -> list[ProfileManager.StructuredCustomizations]:
      """
      This is the batch version of
      vim.profile.host.ProfileManager@retrieveAnswerFile.
      
      Returns a map that contains the hosts and their answer file data
      objects.
      
      Args:
          hosts: Hosts with which the answer files are associated.
      
      Returns:
          A map that contains the hosts and their answer files.
      """
      ...
   def RetrieveHostCustomizationsForProfile(self, hosts: list[pyVmomi.vim.HostSystem], applyProfile: HostApplyProfile) -> list[ProfileManager.StructuredCustomizations]:
      """
      This is the batch version of
      vim.profile.host.ProfileManager@retrieveAnswerFileForProfile.
      
      Returns a map that contains the hosts and their answer files associated
      with these hosts, augmented with whatever answer file values are
      required for the supplied host profile.
      
      Args:
          hosts: Hosts with which the answer files are associated.
          applyProfile: Profile configuration used to generate answer file
      
      Returns:
          A map contains the hosts and their answer files.
      """
      ...
   def GenerateHostConfigTaskSpec(self, hostsInfo: list[ProfileManager.StructuredCustomizations]) -> pyVmomi.vim.Task:
      """
      This method generates `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec` data object
      for each host which can be passed as input to
      `pyVmomi.vim.profile.host.ProfileManager.applyEntitiesConfiguration`
      to configure that host.
      
      For each host, this method goes through two stages,
      `pyVmomi.vim.profile.host.HostProfile.execute` stage
      `pyVmomi.vim.profile.host.ProfileManager.generateTaskList` stage. If the
      `pyVmomi.vim.profile.host.HostProfile.execute` stage completes
      successfully then the method invokes the
      `pyVmomi.vim.profile.host.ProfileManager.generateTaskList`
      stage to generate the list of configuration tasks that are needed
      to configure the host.
      This method will return a task to monitor the progress of the operation.
      
      Args:
          hostsInfo: List of host data for which configuration task list
              needs to be generated. The
              `pyVmomi.vim.profile.host.ProfileManager.StructuredCustomizations.customizations` value should be
              provided only if the host customization data for that host is
              invalid. If this property is not provided, the API will use the
              host customization data stored in VC and generate task list.
      
      Returns:
          A list of `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec` objects. Each
          `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec` is for each host in the provided
          hostsInfo list.
          This method is successful if the
          `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec.faultData` is not set and the
          `pyVmomi.vim.profile.host.ExecuteResult.status``=success`).
      """
      ...
   def ApplyEntitiesConfiguration(self, applyConfigSpecs: list[ProfileManager.ApplyHostConfigSpec]) -> pyVmomi.vim.Task:
      """
      The task for applying host configuration on a list of hosts.
      
      This is the
      batch version of `applyHostConfiguration`. The implementation
      of this method will:
      When a host is in a DRS cluster but doesn't satisfy the state requirement
      such as that the host is not in the required maintenance mode, this
      method uses DRS feature to put the host into maintenance mode.
      This method will apply a host profile to a stateful host or stateless
      host; or apply a host profile to a stateless host by reboot.
      After a host is reboot, a check compliance is done to update the latest
      compliance status.
      
      Args:
          applyConfigSpecs: An array of
              `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec`
              objects. Each applyConfigSpecs object contains the data objects
              required to remediate a host. The API caller should expand
              a cluster to all its hosts for the purpose of providing the
              required data object for configuration apply of each host.
      
      Returns:
          An array of
          `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigResult`
          objects. Each
          `pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigResult`
          is for each host in the provided host list.
      """
      ...
   def ValidateComposition(self, source: pyVmomi.vim.profile.Profile, targets: list[pyVmomi.vim.profile.Profile], toBeMerged: _typing.Optional[HostApplyProfile], toReplaceWith: _typing.Optional[HostApplyProfile], toBeDeleted: _typing.Optional[HostApplyProfile], enableStatusToBeCopied: _typing.Optional[HostApplyProfile], errorOnly: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Validates the proposed host profile composition.
      
      Args:
          source: The source host profile of the configurations for
              composition.
          targets: The array of target host profiles that the configurations
              composite into.
          toBeMerged: A `pyVmomi.vim.profile.host.HostApplyProfile` object
              contains the sub profiles that will be merged from the source to
              the target host profiles, and all the ancestors of these sub
              profiles. For singleton sub profile, it will be added into a
              target host profile if it doesn't exist in the target; otherwise,
              it replaces the one in the target.
              The member variable
              `pyVmomi.vim.profile.ApplyProfile.toBeMerged` of these sub profiles
              should have a value of `true`. The member variables
              `pyVmomi.vim.profile.ApplyProfile.toBeMerged`
              `pyVmomi.vim.profile.ApplyProfile.toReplaceWith`,
              `pyVmomi.vim.profile.ApplyProfile.toBeDeleted`
              of the ancestors should have a value of `false`.
          toReplaceWith: A `pyVmomi.vim.profile.host.HostApplyProfile` object
              contains the sub profiles that will be used to replace the array
              in the target host profiles, and all the ancestors of these sub
              profiles.
              Similar to above except that the member variable
              `pyVmomi.vim.profile.ApplyProfile.toReplaceWith`
              is turned on.
          toBeDeleted: A `pyVmomi.vim.profile.host.HostApplyProfile` object
              contains the sub profiles that will be deleted from the source
              and the target host profiles, and all the ancestors of
              these sub profiles.
              Similar to above except that the member variable
              `pyVmomi.vim.profile.ApplyProfile.toBeDeleted`
              is turned on.
          enableStatusToBeCopied: A `pyVmomi.vim.profile.host.HostApplyProfile`
              object contains the sub profiles that the member variable
              `pyVmomi.vim.profile.ApplyProfile.enabled` will be copied from the
              source host profile to all the target host profiles, and all the
              ancestors of these sub profiles.
              The member variable
              `pyVmomi.vim.profile.ApplyProfile.copyEnableStatus`
              of these sub profiles is turned on. The member variable
              `pyVmomi.vim.profile.ApplyProfile.copyEnableStatus` of the
              `pyVmomi.vim.profile.ApplyProfile.copyEnableStatus` of the
              ancestors should have a value of `false`.
          errorOnly: Indicates that the validation result for each target
              don't contain the source-target difference.
      """
      ...
   def CompositeProfile(self, source: pyVmomi.vim.profile.Profile, targets: list[pyVmomi.vim.profile.Profile], toBeMerged: _typing.Optional[HostApplyProfile], toBeReplacedWith: _typing.Optional[HostApplyProfile], toBeDeleted: _typing.Optional[HostApplyProfile], enableStatusToBeCopied: _typing.Optional[HostApplyProfile]) -> pyVmomi.vim.Task:
      """
      Composes (merge, replace, delete, disable)
      the selected configurations into the target host profiles.
      """
      ...


class SecurityProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.SecurityProfile` data object represents host security configuration.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       permission: Permission configuration.
   """
   permission: list[PermissionProfile] = []

class ServiceConsolePortGroupProfile(PortGroupProfile):
   """
   The `pyVmomi.vim.profile.host.ServiceConsolePortGroupProfile` data object represents
   the profile for a port group that will be used by the service console.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       ipConfig: IP address configuration for the service console network.
   """
   ipConfig: IpAddressProfile


class ServiceProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.ServiceProfile` data object controls the configuration of a service.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the service profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list for access
   to subprofiles, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class StaticRouteProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.StaticRouteProfile` data object represents a single static IP route.
   
   The `pyVmomi.vim.profile.ApplyProfile.policy` property contains
   data values for static route configuration.
   
   Attributes:
       key: Linkable identifier.
   """
   key: _typing.Optional[str] = None


class StorageProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.StorageProfile` data object represents the host storage configuration.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       nasStorage: List of NAS storage subprofiles.
           
           Use the `pyVmomi.vim.profile.host.NasStorageProfile.key` property
           to access a subprofile in the list.
   """
   nasStorage: list[NasStorageProfile] = []


class UserGroupProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.UserGroupProfile` data object represents a user group.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the user group profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list for access
   to subprofile configuration data, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class UserProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.UserProfile` data object represents a user.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for access to configuration data
   for the user profile. Use the `pyVmomi.vim.profile.ApplyProfile.property` list for access
   to subprofile configuration data, if any.
   
   Attributes:
       key: Linkable identifier.
   """
   key: str


class VirtualSwitchProfile(pyVmomi.vim.profile.ApplyProfile):
   """
   The `pyVmomi.vim.profile.host.VirtualSwitchProfile` data object represents a subprofile
   for a virtual switch.
   
   If a profile plug-in defines policies or subprofiles, use the
   `pyVmomi.vim.profile.ApplyProfile.policy` or `pyVmomi.vim.profile.ApplyProfile.property`
   list to access the additional configuration data.
   
   Attributes:
       key: Linkable identifier.
       name: Name of the standard virtual switch(VSS).
       link: Links that are connected to the virtual switch.
       numPorts: Number of ports on the virtual switch.
       networkPolicy: Network policy/policies for the virtual switch.
   """
   class LinkProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      The LinkProfile data object represents a subprofile
      for links connected to virtual switch.
      """
      pass

   class NumPortsProfile(pyVmomi.vim.profile.ApplyProfile):
      """
      The NumPortsProfile data object represents a
      subprofile for the number of ports for a
      virtual switch
      """
      pass

   key: str
   name: str
   link: VirtualSwitchProfile.LinkProfile
   numPorts: VirtualSwitchProfile.NumPortsProfile
   networkPolicy: NetworkPolicyProfile

class VmPortGroupProfile(PortGroupProfile):
   """
   The `pyVmomi.vim.profile.host.VmPortGroupProfile` data object represents the subprofile
   for a port group that will be used by virtual machines.
   
   Use the `pyVmomi.vim.profile.ApplyProfile.policy` list for
   access to configuration data for the virtual machine port group profile. Use the
   `pyVmomi.vim.profile.ApplyProfile.property` list for access to subprofiles, if any.
   
   vSphere Servers use `pyVmomi.vim.Network` managed objects to represent virtual machine port
   groups in the vSphere inventory.
   """
   pass
