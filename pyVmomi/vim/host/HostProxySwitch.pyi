# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import HostMember

from pyVmomi.vim.host import PhysicalNic

class HostProxySwitch(DynamicData):
   class Specification(DynamicData):
      backing: Optional[HostMember.Backing] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      uuid: str
      spec: Optional[Specification] = None

   class HostLagConfig(DynamicData):
      lagKey: str
      lagName: Optional[str] = None
      uplinkPort: list[KeyValue] = []

   class EnsInfo(DynamicData):
      opsVersion: long
      numPSOps: long
      numLcoreOps: long
      errorStatus: long
      lcoreStatus: long

   dvsUuid: str
   dvsName: str
   key: str
   numPorts: int
   configNumPorts: Optional[int] = None
   numPortsAvailable: int
   uplinkPort: list[KeyValue] = []
   mtu: Optional[int] = None
   pnic: list[PhysicalNic] = []
   spec: Specification
   hostLag: list[HostLagConfig] = []
   networkReservationSupported: Optional[bool] = None
   nsxtEnabled: Optional[bool] = None
   ensEnabled: Optional[bool] = None
   ensInterruptEnabled: Optional[bool] = None
   transportZones: list[HostMember.TransportZoneInfo] = []
   nsxUsedUplinkPort: list[str] = []
   nsxtStatus: Optional[str] = None
   nsxtStatusDetail: Optional[str] = None
   ensInfo: Optional[EnsInfo] = None
   networkOffloadingEnabled: Optional[bool] = None
   hostUplinkState: list[HostMember.HostUplinkState] = []
