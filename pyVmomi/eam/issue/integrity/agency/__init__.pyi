# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import pyVmomi.eam.issue



class VUMIssue(pyVmomi.eam.issue.AgencyIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Base class for all issues which occurred during EAM communication with
   vSphere Update Manager (VUM).
   """
   pass

class CannotDeleteSoftware(VUMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Cannot remove the Baseline associated with an Agency from VUM.
   
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   retries the delete operation.
   Note: In future this issue will denote also the removal of the Agency
   software (VIBs) from VUM software depot once VUM provides an API for that.
   """
   pass

class CannotStageSoftware(VUMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.The software defined by an Agency cannot be staged in VUM.
   
   The staging
   operation consists of the following steps:
   - Upload the Agency software (VIBs) to the VUM depot.
   - Create or update a VUM Baseline with the Agency software and scope.
     
   This is an active remediable issue. To remediate, vSphere ESX Agent Manager
   retries the stage operation.
   """
   pass

class VUMUnavailable(VUMIssue):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.VUM service is not available - its registered SOAP endpoint cannot be
   accessed or it is malfunctioning.
   
   This is an active and passive remediable issue. To remediate, vSphere ESX
   Agent Manager retries to access VUM service.
   """
   pass
