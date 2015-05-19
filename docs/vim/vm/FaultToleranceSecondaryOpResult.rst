.. _task: ../../vim/cluster/AttemptedVmInfo.rst#task

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _powerOnResult: ../../vim/vm/FaultToleranceSecondaryOpResult.rst#powerOnResult

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _powerOnAttempted: ../../vim/vm/FaultToleranceSecondaryOpResult.rst#powerOnAttempted

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _EnableSecondaryVM_Task: ../../vim/VirtualMachine.rst#enableSecondary

.. _CreateSecondaryVM_Task: ../../vim/VirtualMachine.rst#createSecondary

.. _ClusterPowerOnVmResult: ../../vim/cluster/PowerOnVmResult.rst

.. _ClusterAttemptedVmInfo: ../../vim/cluster/AttemptedVmInfo.rst

.. _ClusterNotAttemptedVmInfo: ../../vim/cluster/NotAttemptedVmInfo.rst

.. _vim.cluster.PowerOnVmResult: ../../vim/cluster/PowerOnVmResult.rst


vim.vm.FaultToleranceSecondaryOpResult
======================================
  FaultToleranceSecondaryOpResult is a data object that reports on the outcome of the `CreateSecondaryVM_Task`_ or `EnableSecondaryVM_Task`_ operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    vm (`vim.VirtualMachine`_):

       The Secondary VirtualMachine
    powerOnAttempted (`bool`_):

       Whether an attempt was made to power on the secondary. If an attempt was made, `powerOnResult`_ will report the status of this attempt.
    powerOnResult (`vim.cluster.PowerOnVmResult`_, optional):

       The powerOnResult property reports the outcome of powering on the Secondary VirtualMachine if a power on was required. A power on will be attempted if the Primary Virtual Machine is powered on when the operation is performed. This object is only reported if `powerOnAttempted`_ is true. If the outcome of the power-on attempt is not successful, the returned `ClusterPowerOnVmResult`_ object will include an instance of `ClusterNotAttemptedVmInfo`_ whereas if the attempt was successful, then an instance of `ClusterAttemptedVmInfo`_ is returned. When `ClusterAttemptedVmInfo`_ is returned, its `task`_ property is only set if the cluster is a HA-only cluster.
