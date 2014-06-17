.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DatastoreEvent: ../../vim/event/DatastoreEvent.rst


vim.event.DatastoreFileEvent
============================
  Base class for events related to datastore file and directory operations.Propertydatastoreinherited from DatastoreEvent refers to the destination datastore in case there is more than datastore involved in the operation.
:extends: vim.event.DatastoreEvent_
:since: `vSphere API 4.0`_

Attributes:
    targetFile (`str`_):

       Datastore path of the target file or directory.
