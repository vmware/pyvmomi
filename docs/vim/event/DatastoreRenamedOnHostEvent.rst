.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst


vim.event.DatastoreRenamedOnHostEvent
=====================================
  This event records when a datastore is added to VirtualCenter and is renamed by VirtualCenter because this datastore already exists in VirtualCenter with a different name, or because the name conflicts with another datastore in VirtualCenter.
:extends: vim.event.HostEvent_

Attributes:
    oldName (`str`_):

       The old datastore name.
    newName (`str`_):

       The new datastore name.
