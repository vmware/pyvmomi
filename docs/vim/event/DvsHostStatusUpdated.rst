
vim.event.DvsHostStatusUpdated
==============================
  A host has it's status or statusDetail updated.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    hostMember (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The host.
    oldStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Host's old status.
    newStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Host's new status.
    oldStatusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Comments regarding host's old status.
    newStatusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Comments regarding host's new status.
