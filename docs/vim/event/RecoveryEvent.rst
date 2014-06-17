.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst


vim.event.RecoveryEvent
=======================
  This event is generated when recovery takes place on a management vmknic
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1`_

Attributes:
    hostName (`str`_):

       The host on which recovery happened
    portKey (`str`_):

       The key of the new port
    dvsUuid (`str`_, optional):

       The uuid of the DVS
    vnic (`str`_, optional):

       The virtual management NIC device where recovery was done
