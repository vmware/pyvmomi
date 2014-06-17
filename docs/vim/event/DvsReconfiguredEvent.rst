.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.DistributedVirtualSwitch.ConfigSpec: ../../vim/DistributedVirtualSwitch/ConfigSpec.rst


vim.event.DvsReconfiguredEvent
==============================
  A distributed virtual switch was reconfigured.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    configSpec (`vim.DistributedVirtualSwitch.ConfigSpec`_):

       The reconfiguration spec.
