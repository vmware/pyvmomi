
vim.event.VmDeployFailedEvent
=============================
  This event records a failure to deploy from a template.
:extends: vim.event.VmEvent_

Attributes:
    destDatastore (`vim.event.EntityEventArgument <vim/event/EntityEventArgument.rst>`_):

       The destination datastore the template is being deployed to.
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
