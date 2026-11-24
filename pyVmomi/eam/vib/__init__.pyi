# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.vmodl



class VibInfo(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.A data entity providing information about a VIB.
   
   This abstraction contains only those of the VIB attributes which convey
   important information for the client to identify, preview and select VIBs.
   """
   class SoftwareTags(pyVmomi.vmodl.DynamicData):
      """A data entity providing information about software tags of a VIB"""
      tags: list[str] = []

   id: str
   name: str
   version: str
   vendor: str
   summary: str
   softwareTags: _typing.Optional[VibInfo.SoftwareTags] = None
   releaseDate: _datetime.datetime
