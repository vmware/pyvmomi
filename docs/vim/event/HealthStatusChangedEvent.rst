.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.Event: ../../vim/event/Event.rst


vim.event.HealthStatusChangedEvent
==================================
  Event used to report change in health status of VirtualCenter components.
:extends: vim.event.Event_
:since: `vSphere API 4.0`_

Attributes:
    componentId (`str`_):

       Unique ID of the VirtualCenter component.
    oldStatus (`str`_):

       Previous health status of the component.
    newStatus (`str`_):

       Current health status of the component.
    componentName (`str`_):

       Component name.
