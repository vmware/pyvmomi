# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cns import QueryFilter

class KubernetesQueryFilter(QueryFilter):
   namespaces: list[str] = []
   podNames: list[str] = []
   pvcNames: list[str] = []
   pvNames: list[str] = []
