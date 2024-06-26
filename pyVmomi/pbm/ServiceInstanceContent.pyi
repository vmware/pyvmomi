# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm import AboutInfo

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.auth import SessionManager

from pyVmomi.pbm.capability import CapabilityMetadataManager

from pyVmomi.pbm.compliance import ComplianceManager

from pyVmomi.pbm.placement import PlacementSolver

from pyVmomi.pbm.profile import ProfileManager

from pyVmomi.pbm.replication import ReplicationManager

class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   capabilityMetadataManager: CapabilityMetadataManager
   profileManager: ProfileManager
   complianceManager: ComplianceManager
   placementSolver: PlacementSolver
   replicationManager: Optional[ReplicationManager] = None
