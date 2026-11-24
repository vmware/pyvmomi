# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim.profile



class ClusterProfile(pyVmomi.vim.profile.Profile):
   class ConfigInfo(pyVmomi.vim.profile.Profile.ConfigInfo):
      """
      Attributes:
          complyProfile: Compliance profile for the cluster
      """
      complyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None

   class CreateSpec(pyVmomi.vim.profile.Profile.CreateSpec):
      """Base class for Cluster CreateSpecs"""
      pass

   class ConfigSpec(ClusterProfile.CreateSpec):
      """
      DataObject which is a baseclass for other configuration
      specifications.
      """
      pass

   class CompleteConfigSpec(ClusterProfile.ConfigSpec):
      """
      DataObject completely specifying the configuration of
      the profile.
      
      Attributes:
          complyProfile: User defined compliance profile for the cluster.
              
              If unset, clear the complyProfile.
      """
      complyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None

   class ServiceType(pyVmomi.VmomiSupport.Enum):
      """
      Type of services for which Profile can be requested for
      
      Attributes:
          DRS: Distributed Resource Scheduling
          HA: High Availability
          DPM: Distributed Power Management
          FT: Fault tolerance
      """
      DRS: _typing.ClassVar['ClusterProfile.ServiceType'] = 'DRS'
      HA: _typing.ClassVar['ClusterProfile.ServiceType'] = 'HA'
      DPM: _typing.ClassVar['ClusterProfile.ServiceType'] = 'DPM'
      FT: _typing.ClassVar['ClusterProfile.ServiceType'] = 'FT'

   class ConfigServiceCreateSpec(ClusterProfile.ConfigSpec):
      """
      DataObject which allows reconfiguration of a profile
      based on services that will be available on the cluster.
      
      Attributes:
          serviceType: Type of the service for which the ClusterProfile is being requested.
              
              If more than one service is specified, the created ClusterProfile
              will cater for all the services.
              Possible values are specified by
              `pyVmomi.vim.profile.cluster.ClusterProfile.ServiceType`.
              If unset, clear the compliance expressions on the profile.
      """
      serviceType: list[str] = []

   def Update(self, config: ClusterProfile.ConfigSpec) -> None:
      """
      Update the ClusterProfile with the specified config.
      
      Args:
          config: Specification which describes the changes.
      
      Raises:
          pyVmomi.vim.fault.DuplicateName: If the profile with the new name already exists.
      """
      ...


class ProfileManager(pyVmomi.vim.profile.ProfileManager):
   pass
