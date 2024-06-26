# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import KeyValue

from pyVmomi.vim.fault import GatewayToHostConnectFault

class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
   verificationToken: str
   propertiesToVerify: list[KeyValue] = []
