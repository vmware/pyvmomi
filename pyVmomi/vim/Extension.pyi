# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import Description
from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.ext import ExtendedProductInfo
from pyVmomi.vim.ext import ManagedEntityInfo
from pyVmomi.vim.ext import SolutionManagerInfo

class Extension(DynamicData):
   class ServerInfo(DynamicData):
      url: str
      description: Description
      company: str
      type: str
      adminEmail: list[str] = []
      serverThumbprint: Optional[str] = None
      serverCertificate: Optional[str] = None

   class ClientInfo(DynamicData):
      version: str
      description: Description
      company: str
      type: str
      url: str

   class TaskTypeInfo(DynamicData):
      taskID: str

   class EventTypeInfo(DynamicData):
      eventID: str
      eventTypeSchema: Optional[str] = None

   class FaultTypeInfo(DynamicData):
      faultID: str

   class PrivilegeInfo(DynamicData):
      privID: str
      privGroupName: str

   class ResourceInfo(DynamicData):
      locale: str
      module: str
      data: list[KeyValue] = []

   class HealthInfo(DynamicData):
      url: str

   class OvfConsumerInfo(DynamicData):
      callbackUrl: str
      sectionType: list[str] = []

   description: Description
   key: str
   company: Optional[str] = None
   type: Optional[str] = None
   version: str
   subjectName: Optional[str] = None
   server: list[ServerInfo] = []
   client: list[ClientInfo] = []
   taskList: list[TaskTypeInfo] = []
   eventList: list[EventTypeInfo] = []
   faultList: list[FaultTypeInfo] = []
   privilegeList: list[PrivilegeInfo] = []
   resourceList: list[ResourceInfo] = []
   lastHeartbeatTime: datetime
   healthInfo: Optional[HealthInfo] = None
   ovfConsumerInfo: Optional[OvfConsumerInfo] = None
   extendedProductInfo: Optional[ExtendedProductInfo] = None
   managedEntityInfo: list[ManagedEntityInfo] = []
   shownInSolutionManager: Optional[bool] = None
   solutionManagerInfo: Optional[SolutionManagerInfo] = None
