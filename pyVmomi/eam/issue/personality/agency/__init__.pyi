# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.eam.issue



class PMIssue(pyVmomi.eam.issue.AgencyIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Base class for all issues which occurred during EAM communication with
   Personality Manager.
   """
   pass


class CannotConfigureSolutions(PMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.EAM was unable to set its required compute resource configuration in PM.
   
   EAM configuration needs to be updated or PM needs to be repaired manually to
   allow the configuration.
   
   Attributes:
       cr: Compute resource that couldn't be configured
       solutionsToModify: Names of the solutions attempted to be modified
       solutionsToRemove: Names of the solutions attempted to be removed
   """
   cr: pyVmomi.vim.ComputeResource
   solutionsToModify: list[str] = []
   solutionsToRemove: list[str] = []

class DepotIssue(PMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Base class for all offline depot (VIB) issues while communicating with
   Personality Manager.
   
   Attributes:
       remoteDepotUrl: URL the offline bundle is configured in EAM.
   """
   remoteDepotUrl: str

class CannotUploadDepot(DepotIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The offline depot could not be uploaded in Personality Manager.
   
   Attributes:
       localDepotUrl: URL EAM hosted the offline bundle as in vCenter.
   """
   localDepotUrl: str

class InaccessibleDepot(DepotIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The offline depot was not available for download during communicating with
   Personality Manager.
   """
   pass

class InvalidDepot(DepotIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The offline depot has missing or invalid metadata to be usable by
   Personality Manager.
   """
   pass

class PMUnavailable(PMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.PM service is not available - its endpoint cannot be accessed or it is
   malfunctioning.
   
   This is an active and passive remediable issue. To remediate, vSphere ESX
   Agent Manager retries to access PM service.
   """
   pass
