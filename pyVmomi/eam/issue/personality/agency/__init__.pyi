# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.eam.issue



class CannotConfigureSolutions(PMIssue):
   cr: pyVmomi.vim.ComputeResource
   solutionsToModify: list[str] = []
   solutionsToRemove: list[str] = []

class CannotUploadDepot(DepotIssue):
   localDepotUrl: str

class DepotIssue(PMIssue):
   remoteDepotUrl: str

class InaccessibleDepot(DepotIssue):
   pass

class InvalidDepot(DepotIssue):
   pass


class PMIssue(pyVmomi.eam.issue.AgencyIssue):
   pass

class PMUnavailable(PMIssue):
   pass
