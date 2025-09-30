# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vim.fault.VimFault import VimFault

from pyVmomi.vim.profile.ProfilePropertyPath import ProfilePropertyPath

class ProfileUpdateFailed(VimFault):
   class UpdateFailure(DynamicData):
      profilePath: ProfilePropertyPath
      errMsg: LocalizableMessage

   failure: list[UpdateFailure] = []
   warnings: list[UpdateFailure] = []
