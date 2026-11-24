# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.eam.issue



class PMIssue(pyVmomi.eam.issue.AgentIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Base class for all issues which occurred during EAM communication with
   Personality Manager.
   """
   pass

class AwaitingPMRemediation(PMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The agent workflow is blocked until its' required solutions are re-mediated
   externally in Personality Manager.
   
   This issue is only passively remediable. The desired state has to be applied
   in PM by an user.
   """
   pass

class BlockedByAgencyOperation(PMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The agent workflow is blocked by a failed agency operation with
   Personality Manager.
   
   This issue is only passively remediable. The agency's PM related issue has to
   be resolved.
   """
   pass
