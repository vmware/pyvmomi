# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vim.event import ProfileEvent

class ProfileReferenceHostChangedEvent(ProfileEvent):
   referenceHost: Optional[HostSystem] = None
   referenceHostName: Optional[str] = None
   prevReferenceHostName: Optional[str] = None
