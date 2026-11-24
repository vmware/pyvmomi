# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.eam
import pyVmomi.vim
import pyVmomi.vmodl



class EamRuntimeFault(pyVmomi.vmodl.RuntimeFault):
   """The common base type for all vSphere ESX Agent Manager runtime exceptions."""
   pass

class EamAppFault(EamRuntimeFault):
   """
   Application related error
   As opposed to system errors, application ones are always function of the
   input and the current state.
   
   They occur always upon same conditions. In most
   of the cases they are recoverable, i.e. the client can determine what is
   wrong and know how to recover.
   NOTE: Since there is not yet need to distinguish among specific error
   sub-types then we define a common type. Tomorrow, if necessary, we can add an
   additional level of detailed exception types and make this one abstract.
   """
   pass


class CertificateNotTrustedFault(EamAppFault):
   """
   An CertificateNotTrusted fault is thrown when an Agency's configuration
   contains OVF package URL or VIB URL for that vSphere ESX Agent Manager is not
   able to make successful SSL trust verification of the server's certificate.
   
   Reasons for this might be that the certificate provided via the API
   `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust` and `pyVmomi.eam.Agent.ConfigInfo.vibSslTrust`
   or via the script /usr/lib/vmware-eam/bin/eam-utility.py
   - is invalid.
   - does not match the server's certificate.
     
   If there is no provided certificate, the fault is thrown when the server's
   certificate is not trusted by the system or is invalid - @see
   `pyVmomi.eam.Agent.ConfigInfo.ovfSslTrust` and
   `pyVmomi.eam.Agent.ConfigInfo.vibSslTrust`.
   To enable Agency creation 1) provide a valid certificate used by the
   server hosting the `pyVmomi.eam.Agent.ConfigInfo.ovfPackageUrl` or
   `pyVmomi.eam.Agent.ConfigInfo.vibUrl` or 2) ensure the server's certificate is
   signed by a CA trusted by the system. Then retry the operation, vSphere
   ESX Agent Manager will retry the SSL trust verification and proceed with
   reaching the desired state.
   
   Attributes:
       url: The URL that failed the SSL trust verification.
   
   Since: vEAM API 8.2
   """
   url: _typing.Optional[str] = None


class DisabledClusterFault(EamAppFault):
   """
   Thrown when trying to modify state over disabled clusters.
   
   Attributes:
       disabledComputeResource: The MoRefs of the disabled compute resources.
   
   Since: vEAM API 7.6
   """
   disabledComputeResource: list[pyVmomi.vim.ComputeResource] = []


class EamFault(pyVmomi.vmodl.MethodFault):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.The common base type for all vSphere ESX Agent Manager exceptions.
   
   TODO migrate to EamRuntimeFault
   """
   pass

class EamIOFault(EamRuntimeFault):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.IO error
   NOTE: Since this type is a first of system-type errors we do not introduce a
   common base type for them.
   
   Once add a second system type exception though, it
   should be introduced.
   """
   pass

class EamServiceNotInitialized(EamRuntimeFault):
   """
   Thrown when calling vSphere ESX Agent Manager when it is not fully
   initialized.
   """
   pass

class EamSystemFault(EamRuntimeFault):
   """System fault."""
   pass


class InvalidAgencyScope(EamFault):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An `InvalidAgencyScope` fault is thrown when the scope in an
   `pyVmomi.eam.Agency.ConfigInfo` is invalid.
   
   See Also: `pyVmomi.eam.Agency.ConfigInfo`
   
   Attributes:
       unknownComputeResource: The MoRefs of the unknown compute resources.
   """
   unknownComputeResource: list[pyVmomi.vim.ComputeResource] = []


class InvalidAgentConfiguration(EamFault):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An `InvalidAgentConfiguration` fault is thrown when the agent
   configuration of an agency configuration is empty or invalid.
   
   See Also: `pyVmomi.eam.Agency.ConfigInfo`
   
   Attributes:
       invalidAgentConfiguration: An optional invalid agent configuration.
       invalidField: The invalid field.
   """
   invalidAgentConfiguration: _typing.Optional[pyVmomi.eam.Agent.ConfigInfo] = None
   invalidField: _typing.Optional[str] = None

class InvalidLogin(EamRuntimeFault):
   """Thrown when a user cannot be authenticated."""
   pass

class InvalidState(EamAppFault):
   """Thrown when a user is not allowed to execute an operation."""
   pass


class InvalidUrl(EamFault):
   """
   Deprecated: as of vSphere 9.0. Please refer to vLCM APIs.An `InvalidUrl` fault is thrown when an `pyVmomi.eam.Agency`'s configuration scope
   is updated and the OVF package URL or VIB URL cannot be downloaded.
   
   See Also: `pyVmomi.eam.Agency.ConfigInfo`
   
   Attributes:
       url: The invalid URL.
       malformedUrl: True if the URL has an invalid format; otherwise, false.
       unknownHost: True if the host cannot be reached; otherwise, false.
       connectionRefused: True if the connection to the host was refused; otherwise, false.
       responseCode: The HTTP response code returned by the server.
           
           Only set if `malformedUrl` is false.
   """
   url: str
   malformedUrl: bool
   unknownHost: bool
   connectionRefused: bool
   responseCode: _typing.Optional[int] = None

class InvalidVibPackage(EamRuntimeFault):
   """Deprecated: as of vSphere 9.0. Please refer to vLCM Image APIs.Indicates for an invalid or unknown Vib package structure and/or format."""
   pass

class NoConnectionToVCenter(EamRuntimeFault):
   """Thrown when calling vSphere ESX Agent Manager when it is not connected to the vCenter server."""
   pass

class NotAuthorized(EamRuntimeFault):
   """Thrown when an a user cannot be authorized."""
   pass
