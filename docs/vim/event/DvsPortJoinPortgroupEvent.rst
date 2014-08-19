
vim.event.DvsPortJoinPortgroupEvent
===================================
  A port was moved into the distributed virtual portgroup.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The port key.
    portgroupKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The portgroup key.
    portgroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The portgroup name.
