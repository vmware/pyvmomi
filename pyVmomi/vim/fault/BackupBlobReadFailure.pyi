# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import DvsFault

class BackupBlobReadFailure(DvsFault):
   entityName: str
   entityType: str
   fault: MethodFault
