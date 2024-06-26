# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.host import DirectoryStoreInfo

class ActiveDirectoryInfo(DirectoryStoreInfo):
   class DomainMembershipStatus(Enum):
      unknown: ClassVar['DomainMembershipStatus'] = 'unknown'
      ok: ClassVar['DomainMembershipStatus'] = 'ok'
      noServers: ClassVar['DomainMembershipStatus'] = 'noServers'
      clientTrustBroken: ClassVar['DomainMembershipStatus'] = 'clientTrustBroken'
      serverTrustBroken: ClassVar['DomainMembershipStatus'] = 'serverTrustBroken'
      inconsistentTrust: ClassVar['DomainMembershipStatus'] = 'inconsistentTrust'
      otherProblem: ClassVar['DomainMembershipStatus'] = 'otherProblem'

   joinedDomain: Optional[str] = None
   trustedDomain: list[str] = []
   domainMembershipStatus: Optional[str] = None
   smartCardAuthenticationEnabled: Optional[bool] = None
