
vim.host.LowLevelProvisioningManager.VmRecoveryInfo
===================================================
  Virtual machine information that can be used for recovery, for example, to decide whether to register a virtual machine with a server if the virtual machine is currently unregistered. This data object does not contain a complete virtual machine configuration, but a subset of information available from `VirtualMachineConfigInfo <vim/vm/ConfigInfo.rst>`_ , all of which are available via virtual machine configuration files.The documentation for each property in this data object describes the property in `VirtualMachineConfigInfo <vim/vm/ConfigInfo.rst>`_ that contains the same information if available.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The hardware version of this virtual machine. Same as `version <vim/vm/ConfigInfo.rst#version>`_ .
    biosUUID (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       128-bit SMBIOS UUID of this virtual machine. Same as `uuid <vim/vm/ConfigInfo.rst#uuid>`_ .
    instanceUUID (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       VirtualCenter-specific 128-bit UUID of this virtual machine. Same as `instanceUuid <vim/vm/ConfigInfo.rst#instanceUuid>`_ .
    ftInfo (`vim.vm.FaultToleranceConfigInfo <vim/vm/FaultToleranceConfigInfo.rst>`_, optional):

       Fault Tolerance settings for this virtual machine. Same as `ftInfo <vim/vm/ConfigInfo.rst#ftInfo>`_ . Unset if non FT.
