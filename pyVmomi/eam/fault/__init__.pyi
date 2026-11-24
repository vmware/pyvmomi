# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl



class CertificateNotTrustedFault(EamAppFault):
   url: _typing.Optional[str] = None


class DisabledClusterFault(EamAppFault):
   disabledComputeResource: list[pyVmomi.vim.ComputeResource] = []

class EamAppFault(EamRuntimeFault):
   pass


class EamFault(pyVmomi.vmodl.MethodFault):
   pass

class EamIOFault(EamRuntimeFault):
   pass


class EamRuntimeFault(pyVmomi.vmodl.RuntimeFault):
   pass

class EamServiceNotInitialized(EamRuntimeFault):
   pass

class EamSystemFault(EamRuntimeFault):
   pass


class InvalidAgencyScope(EamFault):
   unknownComputeResource: list[pyVmomi.vim.ComputeResource] = []


class InvalidAgentConfiguration(EamFault):
   invalidAgentConfiguration: _typing.Optional[pyVmomi.eam.Agent.ConfigInfo] = None
   invalidField: _typing.Optional[str] = None

class InvalidLogin(EamRuntimeFault):
   pass

class InvalidState(EamAppFault):
   pass


class InvalidUrl(EamFault):
   url: str
   malformedUrl: bool
   unknownHost: bool
   connectionRefused: bool
   responseCode: _typing.Optional[int] = None

class InvalidVibPackage(EamRuntimeFault):
   pass

class NoConnectionToVCenter(EamRuntimeFault):
   pass

class NotAuthorized(EamRuntimeFault):
   pass
