# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class PlacementResult(DynamicData):
   datastore: Datastore
   placementFaults: list[MethodFault] = []
