# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanFileServicePreflightCheckResult(DynamicData):
   ovfInstalled: Optional[str] = None
   fsvmVersion: Optional[str] = None
   lastUpgradeDate: Optional[datetime] = None
   ovfMixedModeIssue: Optional[str] = None
   hostVersion: Optional[str] = None
   mixedModeIssue: Optional[str] = None
   networkPartitionIssue: Optional[str] = None
   vsanDatastoreIssue: Optional[str] = None
   domainConfigIssue: Optional[str] = None
   fileServiceVersion: Optional[str] = None
   dvsConfigIssue: Optional[str] = None
   domainConfigWarning: Optional[str] = None
   ntpConfigWarning: Optional[str] = None
