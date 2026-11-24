# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.vmodl



class VibInfo(pyVmomi.vmodl.DynamicData):
   class SoftwareTags(pyVmomi.vmodl.DynamicData):
      tags: list[str] = []

   id: str
   name: str
   version: str
   vendor: str
   summary: str
   softwareTags: _typing.Optional[SoftwareTags] = None
   releaseDate: _datetime.datetime
