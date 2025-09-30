# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

from pyVmomi.vmodl.fault.NotEnoughLicenses import NotEnoughLicenses

class LicenseDowngradeDisallowed(NotEnoughLicenses):
   edition: str
   entityId: str
   features: list[KeyAnyValue] = []
