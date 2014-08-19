
vim.event.DVPortgroupReconfiguredEvent
======================================
  Two distributed virtual portgroup was reconfigured.
:extends: vim.event.DVPortgroupEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    configSpec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec <vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst>`_):

       The reconfiguration spec.
