# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.fault import VmFaultToleranceIssue

class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
   class ReasonForIssue(Enum):
      haNotEnabled: ClassVar['ReasonForIssue'] = 'haNotEnabled'
      moreThanOneSecondary: ClassVar['ReasonForIssue'] = 'moreThanOneSecondary'
      recordReplayNotSupported: ClassVar['ReasonForIssue'] = 'recordReplayNotSupported'
      replayNotSupported: ClassVar['ReasonForIssue'] = 'replayNotSupported'
      templateVm: ClassVar['ReasonForIssue'] = 'templateVm'
      multipleVCPU: ClassVar['ReasonForIssue'] = 'multipleVCPU'
      hostInactive: ClassVar['ReasonForIssue'] = 'hostInactive'
      ftUnsupportedHardware: ClassVar['ReasonForIssue'] = 'ftUnsupportedHardware'
      ftUnsupportedProduct: ClassVar['ReasonForIssue'] = 'ftUnsupportedProduct'
      missingVMotionNic: ClassVar['ReasonForIssue'] = 'missingVMotionNic'
      missingFTLoggingNic: ClassVar['ReasonForIssue'] = 'missingFTLoggingNic'
      thinDisk: ClassVar['ReasonForIssue'] = 'thinDisk'
      verifySSLCertificateFlagNotSet: ClassVar['ReasonForIssue'] = 'verifySSLCertificateFlagNotSet'
      hasSnapshots: ClassVar['ReasonForIssue'] = 'hasSnapshots'
      noConfig: ClassVar['ReasonForIssue'] = 'noConfig'
      ftSecondaryVm: ClassVar['ReasonForIssue'] = 'ftSecondaryVm'
      hasLocalDisk: ClassVar['ReasonForIssue'] = 'hasLocalDisk'
      esxAgentVm: ClassVar['ReasonForIssue'] = 'esxAgentVm'
      video3dEnabled: ClassVar['ReasonForIssue'] = 'video3dEnabled'
      hasUnsupportedDisk: ClassVar['ReasonForIssue'] = 'hasUnsupportedDisk'
      insufficientBandwidth: ClassVar['ReasonForIssue'] = 'insufficientBandwidth'
      hasNestedHVConfiguration: ClassVar['ReasonForIssue'] = 'hasNestedHVConfiguration'
      hasVFlashConfiguration: ClassVar['ReasonForIssue'] = 'hasVFlashConfiguration'
      unsupportedProduct: ClassVar['ReasonForIssue'] = 'unsupportedProduct'
      cpuHvUnsupported: ClassVar['ReasonForIssue'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: ClassVar['ReasonForIssue'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: ClassVar['ReasonForIssue'] = 'cpuHvDisabled'
      hasEFIFirmware: ClassVar['ReasonForIssue'] = 'hasEFIFirmware'
      tooManyVCPUs: ClassVar['ReasonForIssue'] = 'tooManyVCPUs'
      tooMuchMemory: ClassVar['ReasonForIssue'] = 'tooMuchMemory'
      vMotionNotLicensed: ClassVar['ReasonForIssue'] = 'vMotionNotLicensed'
      ftNotLicensed: ClassVar['ReasonForIssue'] = 'ftNotLicensed'
      haAgentIssue: ClassVar['ReasonForIssue'] = 'haAgentIssue'
      unsupportedSPBM: ClassVar['ReasonForIssue'] = 'unsupportedSPBM'
      hasLinkedCloneDisk: ClassVar['ReasonForIssue'] = 'hasLinkedCloneDisk'
      unsupportedPMemHAFailOver: ClassVar['ReasonForIssue'] = 'unsupportedPMemHAFailOver'
      unsupportedEncryptedDisk: ClassVar['ReasonForIssue'] = 'unsupportedEncryptedDisk'
      ftMetroClusterNotEditable: ClassVar['ReasonForIssue'] = 'ftMetroClusterNotEditable'
      noHostGroupConfigured: ClassVar['ReasonForIssue'] = 'noHostGroupConfigured'

   reason: Optional[str] = None
   entityName: Optional[str] = None
   entity: Optional[ManagedEntity] = None
