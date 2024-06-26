# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

class CertificateManager(ManagedObject):
   def RefreshCACertificatesAndCRLs(self, host: list[HostSystem]) -> Task: ...
   def RefreshCertificates(self, host: list[HostSystem]) -> Task: ...
   def RevokeCertificates(self, host: list[HostSystem]) -> Task: ...
