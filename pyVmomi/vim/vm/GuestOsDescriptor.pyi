# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import CpuIdInfo

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import IntOption

class GuestOsDescriptor(DynamicData):
   class GuestOsFamily(Enum):
      windowsGuest: ClassVar['GuestOsFamily'] = 'windowsGuest'
      linuxGuest: ClassVar['GuestOsFamily'] = 'linuxGuest'
      netwareGuest: ClassVar['GuestOsFamily'] = 'netwareGuest'
      solarisGuest: ClassVar['GuestOsFamily'] = 'solarisGuest'
      darwinGuestFamily: ClassVar['GuestOsFamily'] = 'darwinGuestFamily'
      otherGuestFamily: ClassVar['GuestOsFamily'] = 'otherGuestFamily'

   class GuestOsIdentifier(Enum):
      dosGuest: ClassVar['GuestOsIdentifier'] = 'dosGuest'
      win31Guest: ClassVar['GuestOsIdentifier'] = 'win31Guest'
      win95Guest: ClassVar['GuestOsIdentifier'] = 'win95Guest'
      win98Guest: ClassVar['GuestOsIdentifier'] = 'win98Guest'
      winMeGuest: ClassVar['GuestOsIdentifier'] = 'winMeGuest'
      winNTGuest: ClassVar['GuestOsIdentifier'] = 'winNTGuest'
      win2000ProGuest: ClassVar['GuestOsIdentifier'] = 'win2000ProGuest'
      win2000ServGuest: ClassVar['GuestOsIdentifier'] = 'win2000ServGuest'
      win2000AdvServGuest: ClassVar['GuestOsIdentifier'] = 'win2000AdvServGuest'
      winXPHomeGuest: ClassVar['GuestOsIdentifier'] = 'winXPHomeGuest'
      winXPProGuest: ClassVar['GuestOsIdentifier'] = 'winXPProGuest'
      winXPPro64Guest: ClassVar['GuestOsIdentifier'] = 'winXPPro64Guest'
      winNetWebGuest: ClassVar['GuestOsIdentifier'] = 'winNetWebGuest'
      winNetStandardGuest: ClassVar['GuestOsIdentifier'] = 'winNetStandardGuest'
      winNetEnterpriseGuest: ClassVar['GuestOsIdentifier'] = 'winNetEnterpriseGuest'
      winNetDatacenterGuest: ClassVar['GuestOsIdentifier'] = 'winNetDatacenterGuest'
      winNetBusinessGuest: ClassVar['GuestOsIdentifier'] = 'winNetBusinessGuest'
      winNetStandard64Guest: ClassVar['GuestOsIdentifier'] = 'winNetStandard64Guest'
      winNetEnterprise64Guest: ClassVar['GuestOsIdentifier'] = 'winNetEnterprise64Guest'
      winLonghornGuest: ClassVar['GuestOsIdentifier'] = 'winLonghornGuest'
      winLonghorn64Guest: ClassVar['GuestOsIdentifier'] = 'winLonghorn64Guest'
      winNetDatacenter64Guest: ClassVar['GuestOsIdentifier'] = 'winNetDatacenter64Guest'
      winVistaGuest: ClassVar['GuestOsIdentifier'] = 'winVistaGuest'
      winVista64Guest: ClassVar['GuestOsIdentifier'] = 'winVista64Guest'
      windows7Guest: ClassVar['GuestOsIdentifier'] = 'windows7Guest'
      windows7_64Guest: ClassVar['GuestOsIdentifier'] = 'windows7_64Guest'
      windows7Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows7Server64Guest'
      windows8Guest: ClassVar['GuestOsIdentifier'] = 'windows8Guest'
      windows8_64Guest: ClassVar['GuestOsIdentifier'] = 'windows8_64Guest'
      windows8Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows8Server64Guest'
      windows9Guest: ClassVar['GuestOsIdentifier'] = 'windows9Guest'
      windows9_64Guest: ClassVar['GuestOsIdentifier'] = 'windows9_64Guest'
      windows9Server64Guest: ClassVar['GuestOsIdentifier'] = 'windows9Server64Guest'
      windows11_64Guest: ClassVar['GuestOsIdentifier'] = 'windows11_64Guest'
      windows12_64Guest: ClassVar['GuestOsIdentifier'] = 'windows12_64Guest'
      windowsHyperVGuest: ClassVar['GuestOsIdentifier'] = 'windowsHyperVGuest'
      windows2019srv_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2019srv_64Guest'
      windows2019srvNext_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2019srvNext_64Guest'
      windows2022srvNext_64Guest: ClassVar['GuestOsIdentifier'] = 'windows2022srvNext_64Guest'
      freebsdGuest: ClassVar['GuestOsIdentifier'] = 'freebsdGuest'
      freebsd64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd64Guest'
      freebsd11Guest: ClassVar['GuestOsIdentifier'] = 'freebsd11Guest'
      freebsd11_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd11_64Guest'
      freebsd12Guest: ClassVar['GuestOsIdentifier'] = 'freebsd12Guest'
      freebsd12_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd12_64Guest'
      freebsd13Guest: ClassVar['GuestOsIdentifier'] = 'freebsd13Guest'
      freebsd13_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd13_64Guest'
      freebsd14Guest: ClassVar['GuestOsIdentifier'] = 'freebsd14Guest'
      freebsd14_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd14_64Guest'
      freebsd15Guest: ClassVar['GuestOsIdentifier'] = 'freebsd15Guest'
      freebsd15_64Guest: ClassVar['GuestOsIdentifier'] = 'freebsd15_64Guest'
      redhatGuest: ClassVar['GuestOsIdentifier'] = 'redhatGuest'
      rhel2Guest: ClassVar['GuestOsIdentifier'] = 'rhel2Guest'
      rhel3Guest: ClassVar['GuestOsIdentifier'] = 'rhel3Guest'
      rhel3_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel3_64Guest'
      rhel4Guest: ClassVar['GuestOsIdentifier'] = 'rhel4Guest'
      rhel4_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel4_64Guest'
      rhel5Guest: ClassVar['GuestOsIdentifier'] = 'rhel5Guest'
      rhel5_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel5_64Guest'
      rhel6Guest: ClassVar['GuestOsIdentifier'] = 'rhel6Guest'
      rhel6_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel6_64Guest'
      rhel7Guest: ClassVar['GuestOsIdentifier'] = 'rhel7Guest'
      rhel7_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel7_64Guest'
      rhel8_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel8_64Guest'
      rhel9_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel9_64Guest'
      rhel10_64Guest: ClassVar['GuestOsIdentifier'] = 'rhel10_64Guest'
      centosGuest: ClassVar['GuestOsIdentifier'] = 'centosGuest'
      centos64Guest: ClassVar['GuestOsIdentifier'] = 'centos64Guest'
      centos6Guest: ClassVar['GuestOsIdentifier'] = 'centos6Guest'
      centos6_64Guest: ClassVar['GuestOsIdentifier'] = 'centos6_64Guest'
      centos7Guest: ClassVar['GuestOsIdentifier'] = 'centos7Guest'
      centos7_64Guest: ClassVar['GuestOsIdentifier'] = 'centos7_64Guest'
      centos8_64Guest: ClassVar['GuestOsIdentifier'] = 'centos8_64Guest'
      centos9_64Guest: ClassVar['GuestOsIdentifier'] = 'centos9_64Guest'
      oracleLinuxGuest: ClassVar['GuestOsIdentifier'] = 'oracleLinuxGuest'
      oracleLinux64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux64Guest'
      oracleLinux6Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux6Guest'
      oracleLinux6_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux6_64Guest'
      oracleLinux7Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux7Guest'
      oracleLinux7_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux7_64Guest'
      oracleLinux8_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux8_64Guest'
      oracleLinux9_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux9_64Guest'
      oracleLinux10_64Guest: ClassVar['GuestOsIdentifier'] = 'oracleLinux10_64Guest'
      suseGuest: ClassVar['GuestOsIdentifier'] = 'suseGuest'
      suse64Guest: ClassVar['GuestOsIdentifier'] = 'suse64Guest'
      slesGuest: ClassVar['GuestOsIdentifier'] = 'slesGuest'
      sles64Guest: ClassVar['GuestOsIdentifier'] = 'sles64Guest'
      sles10Guest: ClassVar['GuestOsIdentifier'] = 'sles10Guest'
      sles10_64Guest: ClassVar['GuestOsIdentifier'] = 'sles10_64Guest'
      sles11Guest: ClassVar['GuestOsIdentifier'] = 'sles11Guest'
      sles11_64Guest: ClassVar['GuestOsIdentifier'] = 'sles11_64Guest'
      sles12Guest: ClassVar['GuestOsIdentifier'] = 'sles12Guest'
      sles12_64Guest: ClassVar['GuestOsIdentifier'] = 'sles12_64Guest'
      sles15_64Guest: ClassVar['GuestOsIdentifier'] = 'sles15_64Guest'
      sles16_64Guest: ClassVar['GuestOsIdentifier'] = 'sles16_64Guest'
      nld9Guest: ClassVar['GuestOsIdentifier'] = 'nld9Guest'
      oesGuest: ClassVar['GuestOsIdentifier'] = 'oesGuest'
      sjdsGuest: ClassVar['GuestOsIdentifier'] = 'sjdsGuest'
      mandrakeGuest: ClassVar['GuestOsIdentifier'] = 'mandrakeGuest'
      mandrivaGuest: ClassVar['GuestOsIdentifier'] = 'mandrivaGuest'
      mandriva64Guest: ClassVar['GuestOsIdentifier'] = 'mandriva64Guest'
      turboLinuxGuest: ClassVar['GuestOsIdentifier'] = 'turboLinuxGuest'
      turboLinux64Guest: ClassVar['GuestOsIdentifier'] = 'turboLinux64Guest'
      ubuntuGuest: ClassVar['GuestOsIdentifier'] = 'ubuntuGuest'
      ubuntu64Guest: ClassVar['GuestOsIdentifier'] = 'ubuntu64Guest'
      debian4Guest: ClassVar['GuestOsIdentifier'] = 'debian4Guest'
      debian4_64Guest: ClassVar['GuestOsIdentifier'] = 'debian4_64Guest'
      debian5Guest: ClassVar['GuestOsIdentifier'] = 'debian5Guest'
      debian5_64Guest: ClassVar['GuestOsIdentifier'] = 'debian5_64Guest'
      debian6Guest: ClassVar['GuestOsIdentifier'] = 'debian6Guest'
      debian6_64Guest: ClassVar['GuestOsIdentifier'] = 'debian6_64Guest'
      debian7Guest: ClassVar['GuestOsIdentifier'] = 'debian7Guest'
      debian7_64Guest: ClassVar['GuestOsIdentifier'] = 'debian7_64Guest'
      debian8Guest: ClassVar['GuestOsIdentifier'] = 'debian8Guest'
      debian8_64Guest: ClassVar['GuestOsIdentifier'] = 'debian8_64Guest'
      debian9Guest: ClassVar['GuestOsIdentifier'] = 'debian9Guest'
      debian9_64Guest: ClassVar['GuestOsIdentifier'] = 'debian9_64Guest'
      debian10Guest: ClassVar['GuestOsIdentifier'] = 'debian10Guest'
      debian10_64Guest: ClassVar['GuestOsIdentifier'] = 'debian10_64Guest'
      debian11Guest: ClassVar['GuestOsIdentifier'] = 'debian11Guest'
      debian11_64Guest: ClassVar['GuestOsIdentifier'] = 'debian11_64Guest'
      debian12Guest: ClassVar['GuestOsIdentifier'] = 'debian12Guest'
      debian12_64Guest: ClassVar['GuestOsIdentifier'] = 'debian12_64Guest'
      debian13Guest: ClassVar['GuestOsIdentifier'] = 'debian13Guest'
      debian13_64Guest: ClassVar['GuestOsIdentifier'] = 'debian13_64Guest'
      asianux3Guest: ClassVar['GuestOsIdentifier'] = 'asianux3Guest'
      asianux3_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux3_64Guest'
      asianux4Guest: ClassVar['GuestOsIdentifier'] = 'asianux4Guest'
      asianux4_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux4_64Guest'
      asianux5_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux5_64Guest'
      asianux7_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux7_64Guest'
      asianux8_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux8_64Guest'
      asianux9_64Guest: ClassVar['GuestOsIdentifier'] = 'asianux9_64Guest'
      opensuseGuest: ClassVar['GuestOsIdentifier'] = 'opensuseGuest'
      opensuse64Guest: ClassVar['GuestOsIdentifier'] = 'opensuse64Guest'
      fedoraGuest: ClassVar['GuestOsIdentifier'] = 'fedoraGuest'
      fedora64Guest: ClassVar['GuestOsIdentifier'] = 'fedora64Guest'
      coreos64Guest: ClassVar['GuestOsIdentifier'] = 'coreos64Guest'
      vmwarePhoton64Guest: ClassVar['GuestOsIdentifier'] = 'vmwarePhoton64Guest'
      other24xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other24xLinuxGuest'
      other26xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other26xLinuxGuest'
      otherLinuxGuest: ClassVar['GuestOsIdentifier'] = 'otherLinuxGuest'
      other3xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other3xLinuxGuest'
      other4xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other4xLinuxGuest'
      other5xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other5xLinuxGuest'
      other6xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other6xLinuxGuest'
      other7xLinuxGuest: ClassVar['GuestOsIdentifier'] = 'other7xLinuxGuest'
      genericLinuxGuest: ClassVar['GuestOsIdentifier'] = 'genericLinuxGuest'
      other24xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other24xLinux64Guest'
      other26xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other26xLinux64Guest'
      other3xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other3xLinux64Guest'
      other4xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other4xLinux64Guest'
      other5xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other5xLinux64Guest'
      other6xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other6xLinux64Guest'
      other7xLinux64Guest: ClassVar['GuestOsIdentifier'] = 'other7xLinux64Guest'
      otherLinux64Guest: ClassVar['GuestOsIdentifier'] = 'otherLinux64Guest'
      solaris6Guest: ClassVar['GuestOsIdentifier'] = 'solaris6Guest'
      solaris7Guest: ClassVar['GuestOsIdentifier'] = 'solaris7Guest'
      solaris8Guest: ClassVar['GuestOsIdentifier'] = 'solaris8Guest'
      solaris9Guest: ClassVar['GuestOsIdentifier'] = 'solaris9Guest'
      solaris10Guest: ClassVar['GuestOsIdentifier'] = 'solaris10Guest'
      solaris10_64Guest: ClassVar['GuestOsIdentifier'] = 'solaris10_64Guest'
      solaris11_64Guest: ClassVar['GuestOsIdentifier'] = 'solaris11_64Guest'
      os2Guest: ClassVar['GuestOsIdentifier'] = 'os2Guest'
      eComStationGuest: ClassVar['GuestOsIdentifier'] = 'eComStationGuest'
      eComStation2Guest: ClassVar['GuestOsIdentifier'] = 'eComStation2Guest'
      netware4Guest: ClassVar['GuestOsIdentifier'] = 'netware4Guest'
      netware5Guest: ClassVar['GuestOsIdentifier'] = 'netware5Guest'
      netware6Guest: ClassVar['GuestOsIdentifier'] = 'netware6Guest'
      openServer5Guest: ClassVar['GuestOsIdentifier'] = 'openServer5Guest'
      openServer6Guest: ClassVar['GuestOsIdentifier'] = 'openServer6Guest'
      unixWare7Guest: ClassVar['GuestOsIdentifier'] = 'unixWare7Guest'
      darwinGuest: ClassVar['GuestOsIdentifier'] = 'darwinGuest'
      darwin64Guest: ClassVar['GuestOsIdentifier'] = 'darwin64Guest'
      darwin10Guest: ClassVar['GuestOsIdentifier'] = 'darwin10Guest'
      darwin10_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin10_64Guest'
      darwin11Guest: ClassVar['GuestOsIdentifier'] = 'darwin11Guest'
      darwin11_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin11_64Guest'
      darwin12_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin12_64Guest'
      darwin13_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin13_64Guest'
      darwin14_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin14_64Guest'
      darwin15_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin15_64Guest'
      darwin16_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin16_64Guest'
      darwin17_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin17_64Guest'
      darwin18_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin18_64Guest'
      darwin19_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin19_64Guest'
      darwin20_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin20_64Guest'
      darwin21_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin21_64Guest'
      darwin22_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin22_64Guest'
      darwin23_64Guest: ClassVar['GuestOsIdentifier'] = 'darwin23_64Guest'
      vmkernelGuest: ClassVar['GuestOsIdentifier'] = 'vmkernelGuest'
      vmkernel5Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel5Guest'
      vmkernel6Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel6Guest'
      vmkernel65Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel65Guest'
      vmkernel7Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel7Guest'
      vmkernel8Guest: ClassVar['GuestOsIdentifier'] = 'vmkernel8Guest'
      amazonlinux2_64Guest: ClassVar['GuestOsIdentifier'] = 'amazonlinux2_64Guest'
      amazonlinux3_64Guest: ClassVar['GuestOsIdentifier'] = 'amazonlinux3_64Guest'
      crxPod1Guest: ClassVar['GuestOsIdentifier'] = 'crxPod1Guest'
      crxSys1Guest: ClassVar['GuestOsIdentifier'] = 'crxSys1Guest'
      rockylinux_64Guest: ClassVar['GuestOsIdentifier'] = 'rockylinux_64Guest'
      almalinux_64Guest: ClassVar['GuestOsIdentifier'] = 'almalinux_64Guest'
      otherGuest: ClassVar['GuestOsIdentifier'] = 'otherGuest'
      otherGuest64: ClassVar['GuestOsIdentifier'] = 'otherGuest64'

   class FirmwareType(Enum):
      bios: ClassVar['FirmwareType'] = 'bios'
      efi: ClassVar['FirmwareType'] = 'efi'
      csm: ClassVar['FirmwareType'] = 'csm'

   class SupportLevel(Enum):
      experimental: ClassVar['SupportLevel'] = 'experimental'
      legacy: ClassVar['SupportLevel'] = 'legacy'
      terminated: ClassVar['SupportLevel'] = 'terminated'
      supported: ClassVar['SupportLevel'] = 'supported'
      unsupported: ClassVar['SupportLevel'] = 'unsupported'
      deprecated: ClassVar['SupportLevel'] = 'deprecated'
      techPreview: ClassVar['SupportLevel'] = 'techPreview'

   id: str
   family: str
   fullName: str
   supportedMaxCPUs: int
   numSupportedPhysicalSockets: int
   numSupportedCoresPerSocket: int
   supportedMinMemMB: int
   supportedMaxMemMB: int
   recommendedMemMB: int
   recommendedColorDepth: int
   supportedDiskControllerList: list[type] = []
   recommendedSCSIController: Optional[type] = None
   recommendedDiskController: type
   supportedNumDisks: int
   recommendedDiskSizeMB: int
   recommendedCdromController: type
   supportedEthernetCard: list[type] = []
   recommendedEthernetCard: Optional[type] = None
   supportsSlaveDisk: Optional[bool] = None
   cpuFeatureMask: list[CpuIdInfo] = []
   smcRequired: bool
   supportsWakeOnLan: bool
   supportsVMI: bool
   supportsMemoryHotAdd: bool
   supportsCpuHotAdd: bool
   supportsCpuHotRemove: bool
   supportedFirmware: list[str] = []
   recommendedFirmware: str
   supportedUSBControllerList: list[type] = []
   recommendedUSBController: Optional[type] = None
   supports3D: bool
   recommended3D: bool
   smcRecommended: bool
   ich7mRecommended: bool
   usbRecommended: bool
   supportLevel: str
   supportedForCreate: bool
   vRAMSizeInKB: IntOption
   numSupportedFloppyDevices: int
   wakeOnLanEthernetCard: list[type] = []
   supportsPvscsiControllerForBoot: bool
   diskUuidEnabled: bool
   supportsHotPlugPCI: bool
   supportsSecureBoot: Optional[bool] = None
   defaultSecureBoot: Optional[bool] = None
   persistentMemorySupported: Optional[bool] = None
   supportedMinPersistentMemoryMB: Optional[long] = None
   supportedMaxPersistentMemoryMB: Optional[long] = None
   recommendedPersistentMemoryMB: Optional[long] = None
   persistentMemoryHotAddSupported: Optional[bool] = None
   persistentMemoryHotRemoveSupported: Optional[bool] = None
   persistentMemoryColdGrowthSupported: Optional[bool] = None
   persistentMemoryColdGrowthGranularityMB: Optional[long] = None
   persistentMemoryHotGrowthSupported: Optional[bool] = None
   persistentMemoryHotGrowthGranularityMB: Optional[long] = None
   numRecommendedPhysicalSockets: Optional[int] = None
   numRecommendedCoresPerSocket: Optional[int] = None
   vvtdSupported: Optional[BoolOption] = None
   vbsSupported: Optional[BoolOption] = None
   vsgxSupported: Optional[BoolOption] = None
   vsgxRemoteAttestationSupported: Optional[bool] = None
   supportsTPM20: Optional[bool] = None
   recommendedTPM20: Optional[bool] = None
   vwdtSupported: Optional[bool] = None
