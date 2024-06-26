# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.eam import Agent

from pyVmomi.vim import HostSystem

from pyVmomi.eam.issue import AgencyIssue

class AgentIssue(AgencyIssue):
   agent: Agent
   agentName: str
   host: HostSystem
   hostName: str
