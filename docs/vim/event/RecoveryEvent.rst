
vim.event.RecoveryEvent
=======================
  This event is generated when recovery takes place on a management vmknic
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The host on which recovery happened
    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The key of the new port
    dvsUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The uuid of the DVS
    vnic (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The virtual management NIC device where recovery was done
