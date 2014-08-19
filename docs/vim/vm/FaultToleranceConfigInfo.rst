
vim.vm.FaultToleranceConfigInfo
===============================
  FaultToleranceConfigInfo is a data object type containing Fault Tolerance settings for this virtual machine. role, instanceUuids and configPaths contain information about the whole fault tolerance group.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    role (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The index of the current VM in instanceUuids array starting from 1, so 1 means that it is the primary VM.
    instanceUuids ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The instanceUuid of all the VMs in this fault tolerance group. The first element is the instanceUuid of the primary VM.
    configPaths ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The configuration file path for all the VMs in this fault tolerance group.
