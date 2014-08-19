
vim.HbrManager.ReplicationVmInfo
================================
  This data object represents the essential information about the state of a given replicated `VirtualMachine <vim/VirtualMachine.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A string representing the current State of the virtual machine.
    progressInfo (`vim.HbrManager.ReplicationVmInfo.ProgressInfo <vim/HbrManager/ReplicationVmInfo/ProgressInfo.rst>`_, optional):

       Progress stats for the current operation. Never present if the state is not "syncing" or "active". If not present while in one of these states, the host is still gathering initial operation statistics (progress can be assumed to be 0).
    imageId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       An optional imageId that identifies the instance being created, this is the imagId string that is passed to `HbrCreateInstance_Task <vim/HbrManager.rst#createInstance>`_ or `HbrStartOfflineInstance_Task <vim/HbrManager.rst#startOfflineInstance>`_ 
    lastError (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       A MethodFault representing the last replication specific error that the `VirtualMachine <vim/VirtualMachine.rst>`_ encountered during a create instance operation. The successful creation of an instance will clear any error.
