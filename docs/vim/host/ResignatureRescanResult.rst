.. _vim.Datastore: ../../vim/Datastore.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.VmfsRescanResult: ../../vim/host/VmfsRescanResult.rst

.. _HostResignatureRescanResult: ../../vim/host/ResignatureRescanResult.rst

.. _ResignatureUnresolvedVmfsVolume_Task: ../../vim/host/DatastoreSystem.rst#resignatureUnresolvedVmfsVolume


vim.host.ResignatureRescanResult
================================
  The `HostResignatureRescanResult`_ data object identifies the newly created volume that is the result of a resignature operation. This data object is contained in the task object returned by the `ResignatureUnresolvedVmfsVolume_Task`_ method.When a client calls the resignature method, the Server resignatures the volume, rescans the specified list of hosts, and auto-mounts the volume on the other hosts that share the same underlying storage LUNs.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    rescan (`vim.host.VmfsRescanResult`_, optional):

       List of VMFS Rescan operation results.
    result (`vim.Datastore`_):

       When an UnresolvedVmfsVolume has been resignatured, we want to return the newly created VMFS Datastore.
