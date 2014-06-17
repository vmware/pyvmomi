.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.dvs.ProductSpec: ../../vim/dvs/ProductSpec.rst


vim.event.DvsUpgradeAvailableEvent
==================================
  An upgrade for the distributed virtual switch is available.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    productInfo (`vim.dvs.ProductSpec`_):

       The product info of the upgrade.
