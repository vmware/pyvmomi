.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VirtualApp: ../../vim/VirtualApp.rst

.. _HttpNfcLease: ../../vim/HttpNfcLease.rst

.. _VirtualMachine: ../../vim/VirtualMachine.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.HttpNfcLease: ../../vim/HttpNfcLease.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HttpNfcLeaseProgress: ../../vim/HttpNfcLease.rst#progress

.. _vim.HttpNfcLease.DeviceUrl: ../../vim/HttpNfcLease/DeviceUrl.rst

.. _vim.HttpNfcLease.DatastoreLeaseInfo: ../../vim/HttpNfcLease/DatastoreLeaseInfo.rst


vim.HttpNfcLease.Info
=====================
  This class holds information about the lease, such as the entity covered by the lease, and HTTP URLs for up/downloading file backings.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    lease (`vim.HttpNfcLease`_):

       The `HttpNfcLease`_ object this information belongs to.
    entity (`vim.ManagedEntity`_):

       The `VirtualMachine`_ or `VirtualApp`_ this lease covers.
    deviceUrl ([`vim.HttpNfcLease.DeviceUrl`_], optional):

       The deviceUrl property contains a mapping from logical device keys to URLs.
    totalDiskCapacityInKB (`long`_):

       Total capacity in kilobytes of all disks in all Virtual Machines covered by this lease. This can be used to track progress when transferring disks.
    leaseTimeout (`int`_):

       Number of seconds before the lease times out. The client extends the lease by calling `HttpNfcLeaseProgress`_ before the timeout has expired.
    hostMap ([`vim.HttpNfcLease.DatastoreLeaseInfo`_], optional):

       Map of URLs for leased hosts for a given datastore. This is used to look up multi-POST-capable hosts for a datastore.
