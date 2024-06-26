# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class AboutInfo(DynamicData):
   name: str
   fullName: str
   vendor: str
   version: str
   patchLevel: Optional[str] = None
   build: str
   localeVersion: Optional[str] = None
   localeBuild: Optional[str] = None
   osType: str
   productLineId: str
   apiType: str
   apiVersion: str
   instanceUuid: Optional[str] = None
   licenseProductName: Optional[str] = None
   licenseProductVersion: Optional[str] = None
