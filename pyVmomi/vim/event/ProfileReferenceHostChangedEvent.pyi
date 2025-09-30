# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.event.ProfileEvent import ProfileEvent

class ProfileReferenceHostChangedEvent(ProfileEvent):
   referenceHost: Optional[HostSystem] = None
   referenceHostName: Optional[str] = None
   prevReferenceHostName: Optional[str] = None
