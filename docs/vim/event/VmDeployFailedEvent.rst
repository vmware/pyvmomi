.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst

.. _vim.event.EntityEventArgument: ../../vim/event/EntityEventArgument.rst


vim.event.VmDeployFailedEvent
=============================
  This event records a failure to deploy from a template.
:extends: vim.event.VmEvent_

Attributes:
    destDatastore (`vim.event.EntityEventArgument`_):

       The destination datastore the template is being deployed to.
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
