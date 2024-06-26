# Changelog

## [Unreleased] - Release name - yyyy-mm-dd

## [8.0.3.0] - vSphere 8.0U3 Release - 2024-06-25

### Bindings
- Added support for vSAN Health APIs
- Updated bindings with support for the new vSphere 8.0U3 APIs. For details, refer to the [API reference guide](https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/)
- New features of vSphere 8.0U3 based on REST APIs are available via the [vSphere Automation SDK for Python](https://github.com/vmware/vsphere-automation-sdk-python)

### Type Hints
- Added type stubs for vSAN APIs
- All type stubs are refactored

### Added
- Python 3.12 compatibility ([`44d7b9f`](https://github.com/vmware/pyvmomi/commit/44d7b9f))
- Stub adapters allow the usage of an existing session ([`35f2743`](https://github.com/vmware/pyvmomi/commit/35f2743))
- Added pyVmomi version in the user-agent request header ([`5ad215f`](https://github.com/vmware/pyvmomi/commit/5ad215f))
- Added certFile and certKeyFile attributes to SoapStubAdapter ([`2bbfb62`](https://github.com/vmware/pyvmomi/commit/2bbfb62))
- Added project wide variables to hold the current pyVmomi version - version_info and version_info_str ([`5ad215f`](https://github.com/vmware/pyvmomi/commit/5ad215f))
- Added functions to VmomiSupport to list all types - ListManagedTypes(), ListDataTypes(), ListEnumTypes() ([`e43a287`](https://github.com/vmware/pyvmomi/commit/e43a287)) ([`9e303c1`](https://github.com/vmware/pyvmomi/commit/9e303c1))
- Added CHANGELOG file ([`c248b32`](https://github.com/vmware/pyvmomi/commit/c248b32))

### Changes
- Dependency on "pywin32" is removed ([`4bc1f52`](https://github.com/vmware/pyvmomi/commit/4bc1f52))
- Doc: Non-remote ManagedObject and DataObject methods are documented ([`472bdfc`](https://github.com/vmware/pyvmomi/commit/472bdfc))
- The support statement now reflects the Broadcom support policy ([`c68913e`](https://github.com/vmware/pyvmomi/commit/c68913e))
- Copyright switch from VMware to Broadcom ([`10c3732`](https://github.com/vmware/pyvmomi/commit/10c3732))

### Breaking changes
- sso.SsoAuthenticator.get_bearer_saml_assertion_gss_api() is removed ([`11dc306`](https://github.com/vmware/pyvmomi/commit/11dc306))
- SSLTunnelConnection is trimmed down to handle only tunnel connections. The code that handles remote proxy doubles the HTTPProxyConnection logic and therefore is removed. ([`44d7b9f`](https://github.com/vmware/pyvmomi/commit/44d7b9f))

### Deprecated
- 'publicVersions' and 'dottedVersions' aliases are deprecated ([`14b5ed2`](https://github.com/vmware/pyvmomi/commit/14b5ed2))
- pyVmomiSettings.py and related settings are deprecated - allowGetSet, allowCapitalizedNames, binaryIsBytearray, legacyThumbprintException
- Features.py and all pyVmomi feature states logic is deprecated
- pyVmomi.VmomiSupport.VmomiJSONEncoder is deprecated. Use pyVmomi.VmomiJSONEncoder.VmomiJSONEncoder
- pyVmomi.VmomiSupport.templateOf() is deprecated. Use pyVmomi.VmomiJSONEncoder.templateOf()
- pyVmomi.SoapAdapter.ThumbprintMismatchException is deprecated. Use pyVmomi.Security.ThumbprintMismatchException

## [8.0.2.0.1] - Maintenance Patch 1 for 8.0U2 - 2023-11-17

### Changes
- Fixed: #978 and #1053 - Fix SmartConnect()'s handling of IPv6 address with square brackets
- Added PyPI classifiers for Python 3.10 and Python 3.11. Support for both versions is verified.

## [8.0.2.0] - vSphere 8.0U2 Release - 2023-09-28

### Bindings
- Updated bindings and type hints with support for vSphere 8.0U2. Includes updates to VIM, PBM, EAM, SMS and VSLM namespaces. For details, refer "What's New in vSphere API 8.0U2?" section in the API reference guide: https://developer.vmware.com/apis/1720/vsphere
- New features of vSphere 8.0U2 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python

## [8.0.1.0.2] - Maintenance Patch 2 for 8.0U1 - 2023-07-19

### Bindings
-  Added bindings and type hints for Virtual Storage Lifecycle Management for vSphere 8.0U1 - VSLM namespace

### Changes
- Fixed: #1021 - Switch to static imports for type info modules
- Fixed: #1022 - Support proxy authentication
- Add custom HTTP headers support to connect.SmartStubAdapter()
- Missing filters are no longer treated as task failures
- Various small fixes for docstrings and linter checks

### Type Hints Fixes
- Fixed: #1026 - Use the "from Y import X as X" format to re-export submodules
- Fixed: #1030 - Use a fully qualified name when the type is from another namespace/package

### Tests
- _vcrpy_ dependency is updated to the latest version with Python 2 support
- _testtools_ dependency is removed
- Travis CI is no longer used
- Various test updates and fixes. All tests are enabled.

## [8.0.1.0.1] - Maintenance Patch 1 for 8.0U1 - 2023-05-25

### Type Hints Fixes
- Added missing VMODL1 classes to the type hints
- Enum values now match the letter case of the values from typeinfo files
- Fixed: #1115 - Syntax error in vim/__init__pyi
- Fixed: #1117 - Type stubs: Writable properties are marked as read-only
- Fixed: #1118 - Type stubs: Missing vim.fault.* and vmodl.fault.* types
- Fixed: #1119 - Type stubs: Enum fields should also accept Literal[] str type
- Fixed: #1120 - Type stubs: Exception types must inherit from (Base)Exception

## [8.0.1.0] - vSphere 8.0U1 Release - 2023-05-06

### Bindings
- Updated bindings with support for vSphere 8.0U1. Includes updates to VIM, PBM, EAM and SMS namespaces. For details, refer "What's New in vSphere API 8.0U1?" section in the API reference guide: https://developer.vmware.com/apis/1639/vsphere
- New features of vSphere 8.0U1 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python

### Changes
- Added support for type hints
- #892 - Allow passing ssl_context when login in with a token
- Fixed: #750 - Bumped vcrpy tests dependency to 2.1
- Fixed: #812 - Fix exception leaks
- Fixed: #1004 - Fix SmartConnect()'s SOAP and OAuth token login

## [8.0.0.1.2] - Maintenance Patch 2 for 8.0 - 2023-01-18

### Changes
- Fixed: #995 - 8.0.0.1 breaks Ansible vmware_content_deploy_ovf_template folder lookup
- This release restores the legacy behavior when retrieving managed properties and array of instances of ManagedObject

## [8.0.0.1.1] - Maintenance Patch 1 for 8.0 - 2022-12-16

### Changes
- Fixed: #993 - WaitForTask broken on version >8.0.0
- Fixed: #994 - Pyvomi module failing in connect method
- Replace publicVersions with ltsVersions
- Updated VIM namespace for the next vSphere 8.0 patch release

## [8.0.0.1] - vSphere 8.0 Release - 2022-11-24

### Bindings
- Updated bindings with support for vSphere 8.0. Includes updates to VIM, PBM, EAM, SMS and QUERY namespaces. For details, refer "What's New in vSphere API 8.0.0.1?" section in the API reference guide: https://developer.vmware.com/apis/1355/vsphere
- New features of vSphere 8.0 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python


### Breaking changes
- Minimum Python 2 requirement is 2.7.9
- DynamicTypeManagerHelper.py is removed
- ManagedMethodExecutorHelper.py is removed
- connect.ConnectNoSSL() and connect.SmartConnectNoSSL() are removed.
  Use connect.Connect(disableSslCertValidation=True) and connect.SmartConnect(disableSslCertValidation=True)
- VmomiSupport.UncallableManagedMethod is renamed to VmomiSupport.UnknownManagedMethod


### New modules
Security.py
A new module is added to handle thumbprint verification.
There is a predefined set of available crypto functions to verify the certificate thumbprints.
Its possible to configure during runtime which of the available crypto functions are allowed.

Feature.py
A new module related to pyVmomi development within VMware.


VmomiJSONEncoder.py
The VmomiJSONEncoder is moved into a dedicated module.


### More changes
- A new 'binaryIsBytearray' setting is added to select the base type for the binary type. By default, the binary type is 'str' for Python 2 and 'bytes' for Python 3. If binaryIsBytearray is True, the binary type for Python 2 is set to 'bytearray'. Required for VmomiJSONEncoder to work properly.
- The license note is removed from the Python files. LICENSE.txt holds the Apache 2 license note.
- pyVmomi now uses relative imports
- Dependency on "requests" is removed
- Added support for SAML token authentication
- Added timeout for HTTP requests
- Added option to set the maximum amount of time a task is allowed to run. On timeout, an exception is generated if raiseOnError is True.
- Add option to get all updates for the task.
- Add option to use a logger instead of the standard output
- Various bug fixes
- Code style improvements


### Deprecated
- connect.OpenUrlWithBasicAuth()
- connect.OpenPathWithStub()

## [7.0.3] -  Release vSphere 7.0U3 APIs. - 2021-10-14

- Added new bindings to support vSphere 7.0U3. Includes updates to VIM, PBM, EAM and SMS namespaces. For details, refer "What's New in vSphere API 7.0U3?" section in the API reference guide: https://code.vmware.com/apis/1192/vsphere
- New features of vSphere 7.0U3 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python
- Outdated samples are removed. Community samples project: https://github.com/vmware/pyvmomi-community-samples
- Bindings files are renamed to \_typeinfo\_{namespace}.py
- "stable" version alias is removed
- "public" version alias is renamed to "LTS"

## [7.0.2] -  Release vSphere 7.0U2 APIs. - 2021-04-09

- Added new bindings to support vSphere 7.0U2. Includes updates to VIM, PBM, EAM and SMS namespaces. For details, refer "What's New in vSphere API 7.0U2?" section in the API reference guide: https://code.vmware.com/apis/1131/vsphere
- New features of vSphere 7.0U2 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python
- Drop support of Python 3.3

## [7.0.1] -  Release vSphere 7.0U1 APIs. - 2020-10-30

- Added new bindings to support vSphere 7.0U1. Includes updates to VIM, PBM, and EAM namespaces. For details, refer "What's New in vSphere API 7.0U1?" section in the API reference guide: https://code.vmware.com/apis/1067/vsphere
- New features of vSphere 7.0U1 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python

## [7.0] -  vSphere 7.0 Release Support - 2020-04-14

- Added new bindings to support vSphere 7.0. For details, refer "What's New in vSphere API 7.0?" section in the API reference guide: https://code.vmware.com/apis/968/vsphere
- New features of vSphere 7.0 based on REST APIs are available via the vSphere Automation SDK for Python https://github.com/vmware/vsphere-automation-sdk-python

## [6.7.3] -  vSphere 6.7 Update 3 Release - 2019-09-05

- Publish new bindings to support vSphere 6.7 Update 3 Release - https://github.com/vmware/pyvmomi/pull/827
- Add sso.py to support get bearer/hok token from sso server - https://github.com/vmware/pyvmomi/pull/828
- pydoc support Fix - https://github.com/vmware/pyvmomi/pull/810
- httpProxy Support Fix - https://github.com/vmware/pyvmomi/pull/799
- Changes to VmomiSupport to handle API versions https://github.com/vmware/pyvmomi/pull/827
- Other changes Fix https://github.com/vmware/pyvmomi/pull/831
- Newer features are available via the new vSphere Automation SDK for Python [here](https://github.com/vmware/vsphere-automation-sdk-python)

## [6.7.1.2018.12] -  v6.7.1.2018.12 Bug Fix release - 2018-12-20

- Support JSON encoding for pyVmomi objects PR #732
- Fix vcrpy hardening in test-requirements. Support versions < 2.0
- Delete deprecated Docs folder

## [6.7.1] -  vSphere 6.7 Update1 Release - 2018-10-23

- Publish new bindings to support vSphere 6.7 Update 1 Release
- Newer features are available via the new vSphere Automation SDK for Python [here](https://github.com/vmware/vsphere-automation-sdk-python)

## [6.7.0] -  vSphere 6.7 Release Patch - 2018-09-06

- Publish new bindings to support vSphere 6.7
- Newer features are available via the new vSphere Automation SDK for Python [here](https://github.com/vmware/vsphere-automation-sdk-python)
- Fixed issues in first version of 6.7 bindings

## [6.5.0.2017.5-1] -  v6.5.0.2017.5-1 - 2017-05-24

- Remove sso.py and it's dependencies(lxml and pyOpenSSL) as they don't compatible with certain OS.

## [6.5.0.2017.5] -  v6.5.0.2017.5 - 2017-05-21

* Add sso.py to support get bearer/hok token from sso server
* Fixes #519, #448, #420, #421 Fix SoapAdapter serializer to support serializing unicode chars.
* Fix #487: Remove custom __getattr__ in _HTTPSConnection
* Add user-agent header when connecting to vsphere

## [6.5.0] -  vSphere 6.5 support - 2016-11-16

- Spec bump to support vSphere 6.5.
- Include EAM bindings to support vSphere EAM service.
- Fixed server thumbprint verification.
- Fixed sslcontext creation in sample code.
- Newer features are available via the new vSphere Automation SDK for Python [here](https://developercenter.vmware.com/web/sdk/65/vsphere-automation-python)

## [6.0.0.2016.6] -  v6.0.0.2016.6 - bug fix release - 2016-11-11

- Fixed bug in task.py https://github.com/vmware/pyvmomi/pull/395

## [6.0.0.2016.4] -  v6.0.0.2016.4 - bug fix release - 2016-04-23

- Add support for SPBM and SMS APIs.
- Python3 related bug fixes.
- Include task.py utility class.

## [6.0.0] -  v6.0.0 - 2015-12-01

- Spec bump to support vSphere 6.0 server objects and types [vSphere 6.0 U1 spec is used](http://pubs.vmware.com/Release_Notes/en/vsphere/60/vsphere-vcenter-server-60u1-release-notes.html)
- New ssl context parameter in Connect.py and SoapAdapter.py to support passing various ssl options while connecting to vSphere.
- Drop python 2.6 support.
- Critical bug fixes.

## [5.5.0.2014.1.1] -  v5.5.0.2014.1.1 - bug fix release - 2014-09-22

- Fixes bug with [Iso8601 date serialization](https://github.com/vmware/pyvmomi/issues/112) (for messages sent to the service)
- Simplifies test-requirements.txt
- Introduces support for `tox`
- Changes version number scheme
- Fixes README to be pypi compatible
- Improved sdist and bdist packaging support
- Changes to package information based on _The Python Packaging Authority_ instructions
- Fix [bug](https://github.com/vmware/pyvmomi/issues/131) that produces traceback when running tests for the first time
- Fixes [testing bug](https://github.com/vmware/pyvmomi/issues/147) present on some distributions.

NOTE: This is a re-release of 5.5.0-2014.1.1 the the version number was changed to eliminate the use of the `-` character.

## [5.5.0-2014.1] -  v5.5.0-2014.1 - 2014-08-22

- [Release Notes](https://github.com/vmware/pyvmomi/compare/v5.5.0...v5.5.0-2014.1)
- [Python 3 support](https://github.com/vmware/pyvmomi/issues/55)
- added [unit testing using fixtures](https://github.com/vmware/pyvmomi/issues/42)
- fixed  [session timeouts issue](https://github.com/vmware/pyvmomi/issues/43)
- fixed [Querying datastore cluster fails](https://github.com/vmware/pyvmomi/issues/24)
- fixed [Malformed Faults fail in non-informative ways](https://github.com/vmware/pyvmomi/issues/72)
- added [RST documentation](https://github.com/vmware/pyvmomi/pull/58)
- fixed [getheader does not always fetch cookie value](https://github.com/vmware/pyvmomi/issues/93)

## [5.5.0] -  v5.5.0 - 2014-08-30

pyVmomi as released with vSphere 5.5.0 GA

## [5.1.0] -  pyvmomi 5.1.0 - Initial open source release - 2013-12-14

Initial open source release!
