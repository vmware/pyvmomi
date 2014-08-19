
vim.HttpNfcLease.DatastoreLeaseInfo
===================================
  For a given datastore, represented by datastoreKey, contains a list of leased multi-POST-capable hosts connected to it.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    datastoreKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Datastore key.
    hosts ([`vim.HttpNfcLease.HostInfo <vim/HttpNfcLease/HostInfo.rst>`_]):

       List of hosts connected to this datastore and covered by this lease. The hosts in this list are multi-POST-capable, and any one of them can be used to transfer disks on this datastore.
