
vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec
======================================================
  This class is used to specify ProductSpec for the DVS. The two properties are strictly mutually exclusive. If both properties are set, then an InvalidArgument fault would be thrown.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    newSwitchProductSpec (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):

       The ProductSpec for new DVS
    distributedVirtualSwitch (`vim.DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_, optional):

       Get ProductSpec from the existing DVS
