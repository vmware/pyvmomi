.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.DvsHostStatusUpdated
==============================
  A host has it's status or statusDetail updated.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.1`_

Attributes:
    hostMember (`vim.event.HostEventArgument`_):

       The host.
    oldStatus (`str`_, optional):

       Host's old status.
    newStatus (`str`_, optional):

       Host's new status.
    oldStatusDetail (`str`_, optional):

       Comments regarding host's old status.
    newStatusDetail (`str`_, optional):

       Comments regarding host's new status.
