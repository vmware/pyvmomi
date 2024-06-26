# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.host import DiagnosticPartition
from pyVmomi.vim.host import ScsiDisk

class DiagnosticSystem(ManagedObject):
   @property
   def activePartition(self) -> Optional[DiagnosticPartition]: ...

   def QueryAvailablePartition(self) -> list[DiagnosticPartition]: ...
   def SelectActivePartition(self, partition: Optional[ScsiDisk.Partition]) -> NoReturn: ...
   def QueryPartitionCreateOptions(self, storageType: str, diagnosticType: str) -> list[DiagnosticPartition.CreateOption]: ...
   def QueryPartitionCreateDesc(self, diskUuid: str, diagnosticType: str) -> DiagnosticPartition.CreateDescription: ...
   def CreateDiagnosticPartition(self, spec: DiagnosticPartition.CreateSpec) -> NoReturn: ...
