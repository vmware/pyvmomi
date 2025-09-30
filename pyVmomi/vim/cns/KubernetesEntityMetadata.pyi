# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns.EntityMetadata import EntityMetadata

from pyVmomi.vim.cns.KubernetesEntityReference import KubernetesEntityReference

class KubernetesEntityMetadata(EntityMetadata):
   entityType: str
   namespace: Optional[str] = None
   referredEntity: list[KubernetesEntityReference] = []
