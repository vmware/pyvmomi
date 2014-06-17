.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.cluster.NotAttemptedVmInfo
==============================
  This data class reports one virtual machine powerOn failure.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    vm (`vim.VirtualMachine`_):

       The virtual machine that can not be powered on.
    fault (`vmodl.LocalizedMethodFault`_):

       The exception returned.
