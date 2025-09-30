# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns.QueryFilter import QueryFilter

class KubernetesQueryFilter(QueryFilter):
   namespaces: list[str] = []
   podNames: list[str] = []
   pvcNames: list[str] = []
   pvNames: list[str] = []
