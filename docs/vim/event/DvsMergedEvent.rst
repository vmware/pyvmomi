.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.event.DvsEventArgument: ../../vim/event/DvsEventArgument.rst


vim.event.DvsMergedEvent
========================
  Two distributed virtual switches was merged.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    sourceDvs (`vim.event.DvsEventArgument`_):

       The source DVS.
    destinationDvs (`vim.event.DvsEventArgument`_):

       The destination DVS.
