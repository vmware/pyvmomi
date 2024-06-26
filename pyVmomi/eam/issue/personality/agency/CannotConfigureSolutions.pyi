# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ComputeResource

from pyVmomi.eam.issue.personality.agency import PMIssue

class CannotConfigureSolutions(PMIssue):
   cr: ComputeResource
   solutionsToModify: list[str] = []
   solutionsToRemove: list[str] = []
