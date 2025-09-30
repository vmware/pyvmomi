# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam.Agent import Agent

from pyVmomi.eam.fault.EamFault import EamFault

class InvalidAgentConfiguration(EamFault):
   invalidAgentConfiguration: Optional[Agent.ConfigInfo] = None
   invalidField: Optional[str] = None
