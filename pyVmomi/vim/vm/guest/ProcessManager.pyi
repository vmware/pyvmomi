# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.guest import GuestAuthentication

class ProcessManager(ManagedObject):
   class ProgramSpec(DynamicData):
      programPath: str
      arguments: str
      workingDirectory: Optional[str] = None
      envVariables: list[str] = []

   class WindowsProgramSpec(ProgramSpec):
      startMinimized: bool

   class ProcessInfo(DynamicData):
      name: str
      pid: long
      owner: str
      cmdLine: str
      startTime: datetime
      endTime: Optional[datetime] = None
      exitCode: Optional[int] = None

   def StartProgram(self, vm: VirtualMachine, auth: GuestAuthentication, spec: ProgramSpec) -> long: ...
   def ListProcesses(self, vm: VirtualMachine, auth: GuestAuthentication, pids: list[long]) -> list[ProcessInfo]: ...
   def TerminateProcess(self, vm: VirtualMachine, auth: GuestAuthentication, pid: long) -> NoReturn: ...
   def ReadEnvironmentVariable(self, vm: VirtualMachine, auth: GuestAuthentication, names: list[str]) -> list[str]: ...
