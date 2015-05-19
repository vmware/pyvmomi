.. _str: https://docs.python.org/2/library/stdtypes.html

.. _uuid: ../../../vim/vm/ConfigInfo.rst#uuid

.. _ftInfo: ../../../vim/vm/ConfigInfo.rst#ftInfo

.. _version: ../../../vim/vm/ConfigInfo.rst#version

.. _instanceUuid: ../../../vim/vm/ConfigInfo.rst#instanceUuid

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _VirtualMachineConfigInfo: ../../../vim/vm/ConfigInfo.rst

.. _vim.vm.FaultToleranceConfigInfo: ../../../vim/vm/FaultToleranceConfigInfo.rst


vim.host.LowLevelProvisioningManager.VmRecoveryInfo
===================================================
  Virtual machine information that can be used for recovery, for example, to decide whether to register a virtual machine with a server if the virtual machine is currently unregistered. This data object does not contain a complete virtual machine configuration, but a subset of information available from `VirtualMachineConfigInfo`_ , all of which are available via virtual machine configuration files.The documentation for each property in this data object describes the property in `VirtualMachineConfigInfo`_ that contains the same information if available.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    version (`str`_):

       The hardware version of this virtual machine. Same as `version`_ .
    biosUUID (`str`_):

       128-bit SMBIOS UUID of this virtual machine. Same as `uuid`_ .
    instanceUUID (`str`_):

       VirtualCenter-specific 128-bit UUID of this virtual machine. Same as `instanceUuid`_ .
    ftInfo (`vim.vm.FaultToleranceConfigInfo`_, optional):

       Fault Tolerance settings for this virtual machine. Same as `ftInfo`_ . Unset if non FT.
