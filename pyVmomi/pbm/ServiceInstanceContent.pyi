# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm.AboutInfo import AboutInfo

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.auth.SessionManager import SessionManager

from pyVmomi.pbm.capability.CapabilityMetadataManager import CapabilityMetadataManager

from pyVmomi.pbm.compliance.ComplianceManager import ComplianceManager

from pyVmomi.pbm.placement.PlacementSolver import PlacementSolver

from pyVmomi.pbm.profile.ProfileManager import ProfileManager

from pyVmomi.pbm.replication.ReplicationManager import ReplicationManager

class ServiceInstanceContent(DynamicData):
   aboutInfo: AboutInfo
   sessionManager: SessionManager
   capabilityMetadataManager: CapabilityMetadataManager
   profileManager: ProfileManager
   complianceManager: ComplianceManager
   placementSolver: PlacementSolver
   replicationManager: Optional[ReplicationManager] = None
