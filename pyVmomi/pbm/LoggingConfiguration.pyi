# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class LoggingConfiguration(DynamicData):
   class Component(Enum):
      pbm: ClassVar['Component'] = 'pbm'
      vslm: ClassVar['Component'] = 'vslm'
      sms: ClassVar['Component'] = 'sms'
      spbm: ClassVar['Component'] = 'spbm'
      sps: ClassVar['Component'] = 'sps'
      httpclient_header: ClassVar['Component'] = 'httpclient_header'
      httpclient_content: ClassVar['Component'] = 'httpclient_content'
      vmomi: ClassVar['Component'] = 'vmomi'

   class LogLevel(Enum):
      INFO: ClassVar['LogLevel'] = 'INFO'
      DEBUG: ClassVar['LogLevel'] = 'DEBUG'
      TRACE: ClassVar['LogLevel'] = 'TRACE'

   component: str
   logLevel: str
