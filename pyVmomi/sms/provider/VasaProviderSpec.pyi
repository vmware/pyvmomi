# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.sms.provider.ProviderSpec import ProviderSpec

class VasaProviderSpec(ProviderSpec):
   username: str
   password: str
   url: str
   certificate: Optional[str] = None
