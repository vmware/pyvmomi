.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DVPortgroupEvent: ../../vim/event/DVPortgroupEvent.rst

.. _vim.dvs.DistributedVirtualPortgroup.ConfigSpec: ../../vim/dvs/DistributedVirtualPortgroup/ConfigSpec.rst


vim.event.DVPortgroupReconfiguredEvent
======================================
  Two distributed virtual portgroup was reconfigured.
:extends: vim.event.DVPortgroupEvent_
:since: `vSphere API 4.0`_

Attributes:
    configSpec (`vim.dvs.DistributedVirtualPortgroup.ConfigSpec`_):

       The reconfiguration spec.
