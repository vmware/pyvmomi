# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import binary

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualTPM(VirtualDevice):
   endorsementKeyCertificateSigningRequest: list[binary] = []
   endorsementKeyCertificate: list[binary] = []
