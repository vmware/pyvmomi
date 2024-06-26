# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import CustomizationEvent

class CustomizationFailed(CustomizationEvent):
   class ReasonCode(Enum):
      userDefinedScriptDisabled: ClassVar['ReasonCode'] = 'userDefinedScriptDisabled'
      customizationDisabled: ClassVar['ReasonCode'] = 'customizationDisabled'
      rawDataIsNotSupported: ClassVar['ReasonCode'] = 'rawDataIsNotSupported'
      wrongMetadataFormat: ClassVar['ReasonCode'] = 'wrongMetadataFormat'

   reason: Optional[str] = None
