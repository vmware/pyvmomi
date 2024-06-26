# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class NatService(DynamicData):
   class PortForwardSpecification(DynamicData):
      type: str
      name: str
      hostPort: int
      guestPort: int
      guestIpAddress: str

   class NameServiceSpec(DynamicData):
      dnsAutoDetect: bool
      dnsPolicy: str
      dnsRetries: int
      dnsTimeout: int
      dnsNameServer: list[str] = []
      nbdsTimeout: int
      nbnsRetries: int
      nbnsTimeout: int

   class Specification(DynamicData):
      virtualSwitch: str
      activeFtp: bool
      allowAnyOui: bool
      configPort: bool
      ipGatewayAddress: str
      udpTimeout: int
      portForward: list[PortForwardSpecification] = []
      nameService: Optional[NameServiceSpec] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification
