.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HbrCreateInstance_Task: ../../vim/HbrManager.rst#createInstance

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _HbrStartOfflineInstance_Task: ../../vim/HbrManager.rst#startOfflineInstance

.. _vim.HbrManager.ReplicationVmInfo.ProgressInfo: ../../vim/HbrManager/ReplicationVmInfo/ProgressInfo.rst


vim.HbrManager.ReplicationVmInfo
================================
  This data object represents the essential information about the state of a given replicated `VirtualMachine`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    state (`str`_):

       A string representing the current State of the virtual machine.
    progressInfo (`vim.HbrManager.ReplicationVmInfo.ProgressInfo`_, optional):

       Progress stats for the current operation. Never present if the state is not "syncing" or "active". If not present while in one of these states, the host is still gathering initial operation statistics (progress can be assumed to be 0).
    imageId (`str`_, optional):

       An optional imageId that identifies the instance being created, this is the imagId string that is passed to `HbrCreateInstance_Task`_ or `HbrStartOfflineInstance_Task`_ 
    lastError (`vmodl.LocalizedMethodFault`_, optional):

       A MethodFault representing the last replication specific error that the `VirtualMachine`_ encountered during a create instance operation. The successful creation of an instance will clear any error.
