# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl



class BrokenDiskChainIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered a disk chain that could not be processed.
   
   This suggests that a parent object in a snapshot chain was unable to be
   opened either due to being removed, CID mismatch or some other error.
   
   Attributes:
       uuids: Object UUIDs of broken diskchain objects
   """
   uuids: list[str] = []


class DisallowDataMovementIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Disk format conversion process needs to move the data but
   `pyVmomi.vim.cluster.VsanDiskFormatConversionSpec.allowDataMovement`
   is set to false.
   """
   pass


class DisallowEvacuateDataIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Disk format conversion does not allow evacuating data from hosts in
   maintenance mode.
   
   The hosts must exit maintenance mode.
   
   Attributes:
       hosts: Hosts to which this issue applies.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []


class DiskUnhealthIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered at least one unhealthy disk used by vSAN.
   
   Attributes:
       uuids: UUIDs of unhealthy vSAN disks.
   """
   uuids: list[str] = []


class HigherObjectsPresentDuringDowngradeIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered higher version objects preventing a downgrade.
   
   Attributes:
       uuids: Object UUIDs of higher version objects.
   """
   uuids: list[str] = []


class HostPropertyRetrieveIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered at least one host cannot be communicated.
   
   Attributes:
       hosts: Hosts this issue applies to.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []


class HostWithHybridDiskgroupIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered at least one host has hybrid diskgroup,
   which cannot support space efficiency.
   
   Attributes:
       hosts: Hosts this issue applies to.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []


class HostsCompressionOnlyNotSupported(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check detects some host(s) without compression-only capability
   while compression-only is being enabled.
   
   Attributes:
       hosts: Hosts which do not have compression-only capability.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []


class MixedEsxVersionInClientIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered unsupported ESXi mix mode.
   
   Attributes:
       clusterName: Client cluster to which this issue applies.
   """
   clusterName: str


class MixedEsxVersionIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """Preflight check encountered unsupported ESXi mix mode."""
   pass


class ObjectInaccessibleIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered inaccessible objects, which
   cannot be evacuated during rolling process.
   
   Attributes:
       uuids: Object UUIDs of inaccessible objects.
   """
   uuids: list[str] = []


class ObjectPolicyIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered objects with unsupported policy by
   goal vSAN disk format.
   
   Attributes:
       uuids: Object UUIDs of objects with unsupported policy.
   """
   uuids: list[str] = []


class RemoteClusterNotCompatible(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check detects issue with computed format version
   and it's compatibility with all the client clusters.
   
   Attributes:
       compatibilityInfo: An array of key-value pair.
           
           This array contains the
           names of client and server clusters. Minimum and
           maximum supported format version for the client
           cluster and server cluster's format version.
           Key-value pairs:
           - \"clientClusterName\": Name of the cluster mounting the server
             cluster
           - \"serverClusterName\": Name of the cluster being mounted
           - \"clientVfvMin\": Minimum supported client's target version
           - \"clientVfvMax\": Maximum supported client's target version
           - \"serverVFV\": Supported target version for server cluster
   """
   compatibilityInfo: list[pyVmomi.vmodl.KeyAnyValue] = []


class UnknownScanIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Preflight check encountered an object(s) that could not be processed.
   
   The object appeared to have a descriptor file that existed, but could not be
   understood for some reason.
   
   Attributes:
       uuids: Object UUIDs of unscanable objects
   """
   uuids: list[str] = []


class UnsupportedHighDiskVersionIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   """
   Detected that hosts may have higher disk version which is not supported
   by vCenter.
   
   Attributes:
       hosts: Hosts having this issue.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []
