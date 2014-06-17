.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DatastoreFileEvent: ../../vim/event/DatastoreFileEvent.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst


vim.event.DatastoreFileMovedEvent
=================================
  This event records move of a file or directory.
:extends: vim.event.DatastoreFileEvent_
:since: `vSphere API 4.0`_

Attributes:
    sourceDatastore (`vim.event.DatastoreEventArgument`_):

       Source datastore.
    sourceFile (`str`_):

       Datastore path of the source file or directory.
