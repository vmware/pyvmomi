# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class AuthenticationRequired(pyVmomi.vmodl.RuntimeFault):
   """
   The `pyVmomi.vmodl.fault.AuthenticationRequired` fault indicates that the client must
   authenticate or re-authenticate to access the requested resource.
   
   This fault is thrown when:
   - No authentication credentials are provided in the request
   - The provided access token is invalid, expired, or revoked
   - The authentication scheme used is not supported
   - The request has malformed authentication parameters
     
   When this fault occurs, clients should examine the `pyVmomi.vmodl.fault.AuthenticationRequired.authenticate`
   challenges to determine the appropriate authentication method and
   parameters. The VI/JSON infrastructure automatically converts this fault
   into standard HTTP authentication responses with appropriate status codes
   (400, 401, 403) and WWW-Authenticate headers based on the challenge details.
   
   For OAuth 2.0 Bearer token authentication, clients may need to:
   - Obtain a new access token if the current one is expired
   - Register full user claims with vCenter
   - Discover authentication endpoint from OpenID Connect Configuration
   
   Attributes:
       authenticate: Applicable to the request authentication schemes and their requirements.
   """
   class AuthenticationScheme(pyVmomi.VmomiSupport.Enum):
      """
      Possible authentication schemes.
      
      Attributes:
          Basic: Authentication scheme which transmits credentials as
              user-id/password pairs, encoded using Base64.
              
              See RFC 7617 for details.
          Bearer: Authentication scheme which transmits opaque access token string.
              
              See RFC 6750 for details.
      """
      Basic: _typing.ClassVar['AuthenticationRequired.AuthenticationScheme'] = 'Basic'
      Bearer: _typing.ClassVar['AuthenticationRequired.AuthenticationScheme'] = 'Bearer'

   class ErrorType(pyVmomi.VmomiSupport.Enum):
      """
      Possible reasons why an access request is declined.
      
      Attributes:
          invalid_request: The request is missing a required parameter, includes an unsupported
              parameter or parameter value, repeats the same parameter, uses more
              than one method for including an access token, or is otherwise
              malformed.
          invalid_token: The access token is invalid, expired, revoked or is invalid for
              other reasons.
              
              The client may request a new access token and
              retry the request.
          insufficient_scope: The request requires higher privileges than provided by the access
              token.
          registration_required: vCenter requires registration of the full user claims to enable the
              provided access token use in vCenter.
              
              The client application should
              obtain the full claims token from the authorization server on the
              \"ovl\" field specified URI and register the full claims token with
              vCenter. After registration, the client application should retry
              the request.
      """
      invalid_request: _typing.ClassVar['AuthenticationRequired.ErrorType'] = 'invalid_request'
      invalid_token: _typing.ClassVar['AuthenticationRequired.ErrorType'] = 'invalid_token'
      insufficient_scope: _typing.ClassVar['AuthenticationRequired.ErrorType'] = 'insufficient_scope'
      registration_required: _typing.ClassVar['AuthenticationRequired.ErrorType'] = 'registration_required'

   class Challenge(pyVmomi.vmodl.DynamicData):
      """
      Authentication challenge comprised of authentication scheme and
      requirements.
      
      The authentication challenge descries a procedure and
      parameters the client application can use to successfully authorize
      access.
      
      Attributes:
          scheme: Authentication scheme described in the challenge.
              
              The field possible
              values are described by `pyVmomi.vmodl.fault.AuthenticationRequired.AuthenticationScheme` enum.
          realm: Defines the protection space of the scheme.
              
              The protection space
              determines the domain over which credentials might be automatically
              applied. If a prior request has been authorized the application may
              reuse the same credentials for all other requests within the same
              protection space for a period of time determined by the
              authentication scheme, parameters or application preferences.
          error: The reason why the access request was declined.
              
              The field
              possible values are described by `pyVmomi.vmodl.fault.AuthenticationRequired.ErrorType` enum.
          errorDescription: Provides developers human-readable explanation that is not meant to
              be displayed to end-users.
          ovl: Full claims token URI.
              
              An application uses this value to obtain
              Full Claims Token that is then registered with vCenter to enable
              the provided access token use in vCenter.
          oidcConfigUrl: OpenID Connect Configuration URI.
              
              An application uses this value to
              obtain OpenID Connect Configuration.
      """
      scheme: str
      realm: _typing.Optional[str] = None
      error: _typing.Optional[str] = None
      errorDescription: _typing.Optional[str] = None
      ovl: _typing.Optional[str] = None
      oidcConfigUrl: _typing.Optional[str] = None

   authenticate: list[AuthenticationRequired.Challenge] = []


class HostCommunication(pyVmomi.vmodl.RuntimeFault):
   """
   A HostCommunication fault is thrown if an error happened
   while communicating to a host.
   
   This would typically be
   due to network connections or server failures.
   """
   pass

class HostNotConnected(HostCommunication):
   """
   A HostNotConnected fault is thrown if a method needs
   to communicate with a host that has been disconnected in
   VirtualCenter.
   """
   pass

class HostNotReachable(HostCommunication):
   """
   A HostNotReachable fault is thrown if the server was unable
   to communicate with the host
   """
   pass


class InvalidArgument(pyVmomi.vmodl.RuntimeFault):
   """
   An InvalidArgument exception is thrown if the
   set of arguments passed to the function is not
   specified correctly.
   
   Attributes:
       invalidProperty: Optional name of the invalid property.
   """
   invalidProperty: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None


class InvalidRequest(pyVmomi.vmodl.RuntimeFault):
   """
   An InvalidRequest fault is thrown in response to a malformed
   request to the server that fails in the transport layer, e.g.,
   the SOAP XML request was invalid.
   
   Sub-types of this fault,
   provides more specific transport errors, such as a using a
   reference to an unknown managed object type or method.
   """
   pass


class InvalidToken(pyVmomi.vmodl.RuntimeFault):
   """
   Thrown when the API request is associated with an access token
   that the server does not accept.
   
   The token might be malformed,
   with an invalid signature or content, expired validity, etc.
   """
   pass


class InvalidType(InvalidRequest):
   """
   InvalidType is thrown when a managed object request refers to
   an unexpected or unknown type.
   
   Attributes:
       argument: Name of the argument that was malformed.
   """
   argument: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None


class ManagedObjectNotFound(pyVmomi.vmodl.RuntimeFault):
   """
   A ManagedObjectNotFound exception is thrown when a request refers to
   a managed object that no longer exists or has never existed.
   
   Attributes:
       obj: The managed object reference that generated the error.
   """
   obj: pyVmomi.VmomiSupport.ManagedObject


class MethodNotFound(InvalidRequest):
   """
   MethodNotFound is thrown to indicate that a method called on a managed
   object does not exist.
   
   Attributes:
       receiver: The receiver of the call
       method: The method called.
   """
   receiver: pyVmomi.VmomiSupport.ManagedObject
   method: str


class NotEnoughLicenses(pyVmomi.vmodl.RuntimeFault):
   """
   A NotEnoughLicensesFault occurs when an operation
   fails because there are not enough licenses installed.
   """
   pass


class NotImplemented(pyVmomi.vmodl.RuntimeFault):
   """
   NotImplemented exception is thrown if the method is not
   yet implemented.
   """
   pass


class NotSupported(pyVmomi.vmodl.RuntimeFault):
   """
   Thrown if the method is not supported on the
   server.
   
   Not all methods are supported on all servers
   (for example, an ESX Server host supports less functionality than
   a VirtualCenter server). A feature might also be disabled
   due to missing liceneses.
   """
   pass


class RequestCanceled(pyVmomi.vmodl.RuntimeFault):
   """A RequestCanceled fault is thrown if the user canceled the task."""
   pass


class SecurityError(pyVmomi.vmodl.RuntimeFault):
   """Thrown when the client is not allowed access to the property or method."""
   pass


class SessionNotFound(pyVmomi.vmodl.RuntimeFault):
   """TODO"""
   pass


class SystemError(pyVmomi.vmodl.RuntimeFault):
   """
   Exception type for reporting a low-level operating system
   error.
   
   Attributes:
       reason: A message to indicate detailed information about the error.
           
           This property is not internationalization friendly and
           normally reported by the underlying operating system.
   """
   reason: str


class UnexpectedFault(pyVmomi.vmodl.RuntimeFault):
   """
   An UnexpectedFault may be thrown when a newer version of the server
   reports a error that a cannot be converted to a fault that a client
   that is using an older version of the API would expect.
   
   Attributes:
       faultName: Name of the unexpected fault.
       fault: The unexpected fault if the server can send it in a form that the client
           will be able to de-serialize.
   """
   faultName: type
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
