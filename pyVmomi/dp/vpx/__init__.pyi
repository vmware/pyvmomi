# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import capability as capability
from . import dr as dr


class DiskAlreadyClaimedReason:
   """
   Enumeration of reason codes representing why backend needs to report
   the disk being claimed already.
   """
   pass

class InvalidProtectionReason:
   """Enumeration of reason codes representing the invalid data protection states."""
   pass

class MigrationType:
   """
   Indicates the type of migration that is in progress for a
   `pyVmomi.dp.vpx.ProtectedEntity`.
   """
   pass

class ProtectionStatusType:
   """Indicates the protection status for the `pyVmomi.dp.vpx.ProtectedEntity`."""
   pass

class ProtectionSupportType:
   """Indicates if the cluster supports vSphere Data Protection."""
   pass

class SnapshotType:
   """Indicates the type of snapshot taken on a given protected entity."""
   pass

class SyncType:
   """Indicates the type of sync operation to perform on a given protected entity."""
   pass

class VSphereDataProtectionCapabilities:
   """
   Enumeration of vSphere Data Protection capabilities (features).
   
   Since: 8.0.0.4
   """
   pass

class VSphereDataProtectionCapabilities90U1:
   """
   vSphere Data Protection capabilities (features) introduced in 9.0U1 release.
   
   Some of the capabilities will be enabled in 9.0U1 release, while others will
   be enabled in a subsequent release. For those capabilities that will be
   enabled in 9.0U1 releases, the required minimal ESX vmodl api version is
   '9.1.0.0'.
   """
   pass

class VssBackupContext:
   """
   Indicates the backup context to be used for a VSS snapshot.
   
   Applicable only
   for windows VMs. Refer to `VSS_SNAPSHOT_CONTEXT` enumeration on MSDN.
   """
   pass

class VssBackupType:
   """
   Indicates the backup type for a VSS snapshot.
   
   Applicable only for windows
   VMs. Refer to `VSS_BACKUP_TYPE` enumeration on MSDN.
   """
   pass
