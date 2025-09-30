# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.eam.issue.NoAgentVmDatastore import NoAgentVmDatastore

class NoCustomAgentVmDatastore(NoAgentVmDatastore):
   customAgentVmDatastore: list[Datastore] = []
   customAgentVmDatastoreName: list[str] = []
