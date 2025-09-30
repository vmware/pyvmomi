# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.ChoiceOption import ChoiceOption

from pyVmomi.vim.vm.Message import Message

class QuestionInfo(DynamicData):
   id: str
   text: str
   choice: ChoiceOption
   message: list[Message] = []
