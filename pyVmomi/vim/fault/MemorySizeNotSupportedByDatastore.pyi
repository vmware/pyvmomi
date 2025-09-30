# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.fault.VirtualHardwareCompatibilityIssue import VirtualHardwareCompatibilityIssue

class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
   datastore: Datastore
   memorySizeMB: int
   maxMemorySizeMB: int
