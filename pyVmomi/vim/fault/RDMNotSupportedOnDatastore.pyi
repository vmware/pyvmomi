# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.fault.VmConfigFault import VmConfigFault

class RDMNotSupportedOnDatastore(VmConfigFault):
   device: str
   datastore: Datastore
   datastoreName: str
