
vim.event.DatastoreFileCopiedEvent
==================================
  This event records copy of a file or directory.
:extends: vim.event.DatastoreFileEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    sourceDatastore (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_):

       Source datastore.
    sourceFile (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Datastore path of the source file or directory.
