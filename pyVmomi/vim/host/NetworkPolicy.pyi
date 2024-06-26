# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import NetOffloadCapabilities

class NetworkPolicy(DynamicData):
   class SecurityPolicy(DynamicData):
      allowPromiscuous: Optional[bool] = None
      macChanges: Optional[bool] = None
      forgedTransmits: Optional[bool] = None

   class TrafficShapingPolicy(DynamicData):
      enabled: Optional[bool] = None
      averageBandwidth: Optional[long] = None
      peakBandwidth: Optional[long] = None
      burstSize: Optional[long] = None

   class NicFailureCriteria(DynamicData):
      checkSpeed: Optional[str] = None
      speed: Optional[int] = None
      checkDuplex: Optional[bool] = None
      fullDuplex: Optional[bool] = None
      checkErrorPercent: Optional[bool] = None
      percentage: Optional[int] = None
      checkBeacon: Optional[bool] = None

   class NicOrderPolicy(DynamicData):
      activeNic: list[str] = []
      standbyNic: list[str] = []

   class NicTeamingPolicy(DynamicData):
      policy: Optional[str] = None
      reversePolicy: Optional[bool] = None
      notifySwitches: Optional[bool] = None
      rollingOrder: Optional[bool] = None
      failureCriteria: Optional[NicFailureCriteria] = None
      nicOrder: Optional[NicOrderPolicy] = None

   security: Optional[SecurityPolicy] = None
   nicTeaming: Optional[NicTeamingPolicy] = None
   offloadPolicy: Optional[NetOffloadCapabilities] = None
   shapingPolicy: Optional[TrafficShapingPolicy] = None
