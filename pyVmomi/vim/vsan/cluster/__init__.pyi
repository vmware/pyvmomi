# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.vim.vsan


class ComplianceResourceCheckStatusType:
   """
   Defines the type of status for the Compliance Resource Check Query.
   
   The status is one of the four inProgress/aborted/completed/uninitialized.
   """
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.vsan.cluster.ConfigInfo` data object contains configuration
   data for the VSAN service in a cluster.
   
   This data object is used both for
   specifying cluster-wide settings when updating the VSAN service, and as an
   output datatype when retrieving current cluster-wide VSAN service settings.
   
   See Also: `pyVmomi.vim.ComputeResource.reconfigureEx`
   
   Attributes:
       enabled: Whether the VSAN service is enabled for the cluster.
       defaultConfig: Default VSAN settings to use for hosts admitted to the cluster when the
           VSAN service is enabled.
           
           If omitted, values will default as though the
           fields in the `pyVmomi.vim.vsan.cluster.ConfigInfo.HostDefaultInfo` have been omitted.
       vsanEsaEnabled: Whether the vSAN ESA is enabled for vSAN cluster.
           
           This can only be
           enabled when vSAN is enabled on the cluster.
           
           Since: vSphere API Release 8.0.0.1
       vsanCyberRecoveryEnabled: Whether vSAN Cyber Recovery is enabled.
           
           Cyber Recovery has not been configured and is disabled when it is omitted.
           
           Since: vSphere API Release 9.1.0.0
   """
   class HostDefaultInfo(pyVmomi.vmodl.DynamicData):
      """
      Default VSAN service configuration to be used for hosts admitted
      to the cluster.
      
      See Also: `pyVmomi.vim.vsan.cluster.ConfigInfo.defaultConfig`
      
      Attributes:
          uuid: VSAN service cluster UUID, in the string form
              \"nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn\", where n are hexadecimal
              digits.
              
              When enabling the VSAN service on the cluster, this value shall
              not be specified by the user; a suitable UUID will be generated
              by the platform.
              While the VSAN service is enabled, this is a read-only value.
          autoClaimStorage: Whether the VSAN service is configured to automatically claim local
              storage on VSAN-enabled hosts in the cluster.
              
              If omitted while enabling the VSAN service, this value will default
              to `true`.
              Changing this value to `false` shall not affect any
              existing disk mappings in use by hosts currently participating in
              the VSAN service.
              Changing this value to `true` will result in local disks
              being automatically claimed for use by the VSAN service, for hosts
              currently participating in the VSAN service.
          checksumEnabled: Whether the VSAN service is configured to enforce checksum protection.
              
              If omitted while enabling the VSAN service, this value will default
              to `false`.
              Change this value to `false` shall not affect any existing
              disk status.
              Changing this value to `true` shall do disk enforcement
              check that all VSAN disks are checksum enabled.
      """
      uuid: _typing.Optional[str] = None
      autoClaimStorage: _typing.Optional[bool] = None
      checksumEnabled: _typing.Optional[bool] = None

   enabled: _typing.Optional[bool] = None
   defaultConfig: _typing.Optional[ConfigInfo.HostDefaultInfo] = None
   vsanEsaEnabled: _typing.Optional[bool] = None
   vsanCyberRecoveryEnabled: _typing.Optional[bool] = None


class CoreConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   vSAN first-class settings which should be configured together with
   vSAN enablement.
   
   Since: vSphere API Release 9.0.0.0
   """
   vsanMaxEnabled: _typing.Optional[bool] = None


class CoreConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   vSAN first-class settings which should be configured together with
   vSAN enablement.
   
   Since: vSphere API Release 9.0.0.0
   """
   vsanMaxEnabled: _typing.Optional[bool] = None


class VbossClusterConfig(pyVmomi.vim.vsan.VbossConfig):
   """
   Defines the cluster side configuration properties
   of vSAN vBoss service.
   
   It inherits all common properties from
   `pyVmomi.vim.vsan.VbossConfig`.
   """
   pass

class VsanManagedStorageType:
   """vSAN managed storage types."""
   pass
