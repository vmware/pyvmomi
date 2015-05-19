.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.TargetTransport: ../../vim/host/TargetTransport.rst


vim.host.InternetScsiTargetTransport
====================================
  Internet SCSI transport information about a SCSI target.
:extends: vim.host.TargetTransport_

Attributes:
    iScsiName (`str`_):

       The iSCSI name of the target.
    iScsiAlias (`str`_):

       The iSCSI alias of the target.
    address ([`str`_], optional):

       The IP addresses through which the target may be reached.
