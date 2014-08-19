
vim.host.InternetScsiTargetTransport
====================================
  Internet SCSI transport information about a SCSI target.
:extends: vim.host.TargetTransport_

Attributes:
    iScsiName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The iSCSI name of the target.
    iScsiAlias (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The iSCSI alias of the target.
    address ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The IP addresses through which the target may be reached.
