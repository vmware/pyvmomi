
vim.vm.FaultToleranceSecondaryOpResult
======================================
  FaultToleranceSecondaryOpResult is a data object that reports on the outcome of the `CreateSecondaryVM_Task <vim/VirtualMachine.rst#createSecondary>`_ or `EnableSecondaryVM_Task <vim/VirtualMachine.rst#enableSecondary>`_ operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       The Secondary VirtualMachine
    powerOnAttempted (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether an attempt was made to power on the secondary. If an attempt was made, `powerOnResult <vim/vm/FaultToleranceSecondaryOpResult.rst#powerOnResult>`_ will report the status of this attempt.
    powerOnResult (`vim.cluster.PowerOnVmResult <vim/cluster/PowerOnVmResult.rst>`_, optional):

       The powerOnResult property reports the outcome of powering on the Secondary VirtualMachine if a power on was required. A power on will be attempted if the Primary Virtual Machine is powered on when the operation is performed. This object is only reported if `powerOnAttempted <vim/vm/FaultToleranceSecondaryOpResult.rst#powerOnAttempted>`_ is true. If the outcome of the power-on attempt is not successful, the returned `ClusterPowerOnVmResult <vim/cluster/PowerOnVmResult.rst>`_ object will include an instance of `ClusterNotAttemptedVmInfo <vim/cluster/NotAttemptedVmInfo.rst>`_ whereas if the attempt was successful, then an instance of `ClusterAttemptedVmInfo <vim/cluster/AttemptedVmInfo.rst>`_ is returned. When `ClusterAttemptedVmInfo <vim/cluster/AttemptedVmInfo.rst>`_ is returned, its `task <vim/cluster/AttemptedVmInfo.rst#task>`_ property is only set if the cluster is a HA-only cluster.
