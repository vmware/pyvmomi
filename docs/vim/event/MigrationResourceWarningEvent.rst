
vim.event.MigrationResourceWarningEvent
=======================================
  A migration warning that includes both the destination host and resource pool.
:extends: vim.event.MigrationEvent_

Attributes:
    dstPool (`vim.event.ResourcePoolEventArgument <vim/event/ResourcePoolEventArgument.rst>`_):

       The name of the destination resource pool.
    dstHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The name of the destination host.
