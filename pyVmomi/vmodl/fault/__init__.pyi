# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class AuthenticationRequired(pyVmomi.vmodl.RuntimeFault):
   class AuthenticationScheme(pyVmomi.VmomiSupport.Enum):
      Basic: _typing.ClassVar['AuthenticationScheme'] = 'Basic'
      Bearer: _typing.ClassVar['AuthenticationScheme'] = 'Bearer'

   class ErrorType(pyVmomi.VmomiSupport.Enum):
      invalid_request: _typing.ClassVar['ErrorType'] = 'invalid_request'
      invalid_token: _typing.ClassVar['ErrorType'] = 'invalid_token'
      insufficient_scope: _typing.ClassVar['ErrorType'] = 'insufficient_scope'
      registration_required: _typing.ClassVar['ErrorType'] = 'registration_required'

   class Challenge(pyVmomi.vmodl.DynamicData):
      scheme: str
      realm: _typing.Optional[str] = None
      error: _typing.Optional[str] = None
      errorDescription: _typing.Optional[str] = None
      ovl: _typing.Optional[str] = None
      oidcConfigUrl: _typing.Optional[str] = None

   authenticate: list[Challenge] = []


class HostCommunication(pyVmomi.vmodl.RuntimeFault):
   pass

class HostNotConnected(HostCommunication):
   pass

class HostNotReachable(HostCommunication):
   pass


class InvalidArgument(pyVmomi.vmodl.RuntimeFault):
   invalidProperty: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None


class InvalidRequest(pyVmomi.vmodl.RuntimeFault):
   pass


class InvalidToken(pyVmomi.vmodl.RuntimeFault):
   pass


class InvalidType(InvalidRequest):
   argument: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None


class ManagedObjectNotFound(pyVmomi.vmodl.RuntimeFault):
   obj: pyVmomi.VmomiSupport.ManagedObject


class MethodNotFound(InvalidRequest):
   receiver: pyVmomi.VmomiSupport.ManagedObject
   method: str


class NotEnoughLicenses(pyVmomi.vmodl.RuntimeFault):
   pass


class NotImplemented(pyVmomi.vmodl.RuntimeFault):
   pass


class NotSupported(pyVmomi.vmodl.RuntimeFault):
   pass


class RequestCanceled(pyVmomi.vmodl.RuntimeFault):
   pass


class SecurityError(pyVmomi.vmodl.RuntimeFault):
   pass


class SessionNotFound(pyVmomi.vmodl.RuntimeFault):
   pass


class SystemError(pyVmomi.vmodl.RuntimeFault):
   reason: str


class UnexpectedFault(pyVmomi.vmodl.RuntimeFault):
   faultName: type
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
