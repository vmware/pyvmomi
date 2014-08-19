
vim.event.HealthStatusChangedEvent
==================================
  Event used to report change in health status of VirtualCenter components.
:extends: vim.event.Event_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    componentId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique ID of the VirtualCenter component.
    oldStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Previous health status of the component.
    newStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Current health status of the component.
    componentName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Component name.
