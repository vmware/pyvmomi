# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.encryption.CryptoKeyId import CryptoKeyId

from pyVmomi.vim.fault.InvalidState import InvalidState

class EncryptionKeyRequired(InvalidState):
   requiredKey: list[CryptoKeyId] = []
