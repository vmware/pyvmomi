# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FileSystemVolume

class NasVolume(FileSystemVolume):
   class UserInfo(DynamicData):
      user: str

   class SecurityType(Enum):
      AUTH_SYS: ClassVar['SecurityType'] = 'AUTH_SYS'
      SEC_KRB5: ClassVar['SecurityType'] = 'SEC_KRB5'
      SEC_KRB5I: ClassVar['SecurityType'] = 'SEC_KRB5I'
      SEC_KRB5P: ClassVar['SecurityType'] = 'SEC_KRB5P'

   class Specification(DynamicData):
      remoteHost: str
      remotePath: str
      localPath: str
      accessMode: str
      type: Optional[str] = None
      userName: Optional[str] = None
      password: Optional[str] = None
      remoteHostNames: list[str] = []
      securityType: Optional[str] = None
      vmknicToBind: Optional[str] = None
      vmknicBound: Optional[bool] = None
      connections: Optional[int] = None

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      spec: Optional[Specification] = None

   remoteHost: str
   remotePath: str
   userName: Optional[str] = None
   remoteHostNames: list[str] = []
   securityType: Optional[str] = None
   protocolEndpoint: Optional[bool] = None
