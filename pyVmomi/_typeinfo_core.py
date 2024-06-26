# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from .VmomiSupport import CreateDataType, CreateManagedType
from .VmomiSupport import CreateEnumType
from .VmomiSupport import AddVersion, AddVersionParent
from .VmomiSupport import AddBreakingChangesInfo
from .VmomiSupport import F_LINK, F_LINKABLE
from .VmomiSupport import F_OPTIONAL, F_SECRET

AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")

from .VmomiSupport import newestVersions
newestVersions.Add("vmodl.version.version2")

from .VmomiSupport import ltsVersions
ltsVersions.Add("vmodl.version.version2")

from .VmomiSupport import oldestVersions
oldestVersions.Add("vmodl.version.version0")

CreateDataType("vmodl.DynamicArray", "DynamicArray", "vmodl.DataObject", "vmodl.version.version0", [("dynamicType", "string", "vmodl.version.version0", F_OPTIONAL), ("val", "anyType[]", "vmodl.version.version0", 0)])
CreateDataType("vmodl.DynamicData", "DynamicData", "vmodl.DataObject", "vmodl.version.version0", [("dynamicType", "string", "vmodl.version.version0", F_OPTIONAL), ("dynamicProperty", "vmodl.DynamicProperty[]", "vmodl.version.version0", F_OPTIONAL)])
CreateDataType("vmodl.DynamicProperty", "DynamicProperty", "vmodl.DataObject", "vmodl.version.version0", [("name", "vmodl.PropertyPath", "vmodl.version.version0", 0), ("val", "anyType", "vmodl.version.version0", 0)])
CreateDataType("vmodl.KeyAnyValue", "KeyAnyValue", "vmodl.DynamicData", "vmodl.version.version1", [("key", "string", "vmodl.version.version1", 0), ("value", "anyType", "vmodl.version.version1", 0)])
CreateDataType("vmodl.LocalizableMessage", "LocalizableMessage", "vmodl.DynamicData", "vmodl.version.version1", [("key", "string", "vmodl.version.version1", 0), ("arg", "vmodl.KeyAnyValue[]", "vmodl.version.version1", F_OPTIONAL), ("message", "string", "vmodl.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.fault.HostCommunication", "HostCommunication", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.HostNotConnected", "HostNotConnected", "vmodl.fault.HostCommunication", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.HostNotReachable", "HostNotReachable", "vmodl.fault.HostCommunication", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.InvalidArgument", "InvalidArgument", "vmodl.RuntimeFault", "vmodl.version.version0", [("invalidProperty", "vmodl.PropertyPath", "vmodl.version.version0", F_OPTIONAL)])
CreateDataType("vmodl.fault.InvalidRequest", "InvalidRequest", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.InvalidType", "InvalidType", "vmodl.fault.InvalidRequest", "vmodl.version.version0", [("argument", "vmodl.PropertyPath", "vmodl.version.version0", F_OPTIONAL)])
CreateDataType("vmodl.fault.ManagedObjectNotFound", "ManagedObjectNotFound", "vmodl.RuntimeFault", "vmodl.version.version0", [("obj", "vmodl.ManagedObject", "vmodl.version.version0", 0)])
CreateDataType("vmodl.fault.MethodNotFound", "MethodNotFound", "vmodl.fault.InvalidRequest", "vmodl.version.version0", [("receiver", "vmodl.ManagedObject", "vmodl.version.version0", 0), ("method", "string", "vmodl.version.version0", 0)])
CreateDataType("vmodl.fault.NotEnoughLicenses", "NotEnoughLicenses", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.NotImplemented", "NotImplemented", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.NotSupported", "NotSupported", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.RequestCanceled", "RequestCanceled", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.SecurityError", "SecurityError", "vmodl.RuntimeFault", "vmodl.version.version0", None)
CreateDataType("vmodl.fault.SystemError", "SystemError", "vmodl.RuntimeFault", "vmodl.version.version0", [("reason", "string", "vmodl.version.version0", 0)])
CreateDataType("vmodl.fault.UnexpectedFault", "UnexpectedFault", "vmodl.RuntimeFault", "vmodl.version.version0", [("faultName", "vmodl.TypeName", "vmodl.version.version0", 0), ("fault", "vmodl.MethodFault", "vmodl.version.version0", F_OPTIONAL)])
