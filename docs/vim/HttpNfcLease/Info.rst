
vim.HttpNfcLease.Info
=====================
  This class holds information about the lease, such as the entity covered by the lease, and HTTP URLs for up/downloading file backings.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    lease (`vim.HttpNfcLease <vim/HttpNfcLease.rst>`_):

       The `HttpNfcLease <vim/HttpNfcLease.rst>`_ object this information belongs to.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The `VirtualMachine <vim/VirtualMachine.rst>`_ or `VirtualApp <vim/VirtualApp.rst>`_ this lease covers.
    deviceUrl ([`vim.HttpNfcLease.DeviceUrl <vim/HttpNfcLease/DeviceUrl.rst>`_], optional):

       The deviceUrl property contains a mapping from logical device keys to URLs.
    totalDiskCapacityInKB (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total capacity in kilobytes of all disks in all Virtual Machines covered by this lease. This can be used to track progress when transferring disks.
    leaseTimeout (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of seconds before the lease times out. The client extends the lease by calling `HttpNfcLeaseProgress <vim/HttpNfcLease.rst#progress>`_ before the timeout has expired.
    hostMap ([`vim.HttpNfcLease.DatastoreLeaseInfo <vim/HttpNfcLease/DatastoreLeaseInfo.rst>`_], optional):

       Map of URLs for leased hosts for a given datastore. This is used to look up multi-POST-capable hosts for a datastore.
