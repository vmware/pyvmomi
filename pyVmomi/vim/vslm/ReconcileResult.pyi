# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

class ReconcileResult(DynamicData):
   class InvalidDiskPath(DynamicData):
      path: str
      reason: str

   class ReconcileDetail(DynamicData):
      hostName: Optional[str] = None
      reconcileReportPath: Optional[str] = None
      isReconciled: Optional[bool] = None
      isDeepScanned: Optional[bool] = None
      numberOfReconcileIssues: Optional[int] = None
      numberOfFcdsBeforeReconcile: Optional[int] = None
      numberOfFcdsAfterReconcile: Optional[int] = None
      invalidDiskPaths: list[InvalidDiskPath] = []

   reconcileDetails: list[ReconcileDetail] = []
