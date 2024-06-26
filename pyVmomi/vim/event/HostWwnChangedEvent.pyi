# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.event import HostEvent

class HostWwnChangedEvent(HostEvent):
   oldNodeWwns: list[long] = []
   oldPortWwns: list[long] = []
   newNodeWwns: list[long] = []
   newPortWwns: list[long] = []
