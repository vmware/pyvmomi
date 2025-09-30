# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam.Agent import Agent

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.eam.issue.AgencyIssue import AgencyIssue

class AgentIssue(AgencyIssue):
   agent: Agent
   cluster: Optional[ComputeResource] = None
