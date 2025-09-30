# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault.DvsFault import DvsFault

class DvsNotAuthorized(DvsFault):
   sessionExtensionKey: Optional[str] = None
   dvsExtensionKey: Optional[str] = None
