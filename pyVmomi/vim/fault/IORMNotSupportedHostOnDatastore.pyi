# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem

from pyVmomi.vim.fault import VimFault

class IORMNotSupportedHostOnDatastore(VimFault):
   datastore: Datastore
   datastoreName: str
   host: list[HostSystem] = []
