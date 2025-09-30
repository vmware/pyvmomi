# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

class VsanVsanPcapResult(DynamicData):
   calltime: float
   vmknic: str
   tcpdumpFilter: str
   snaplen: int
   pkts: list[str] = []
   pcap: Optional[str] = None
   error: Optional[MethodFault] = None
   hostname: Optional[str] = None
