
vim.host.VmfsRescanResult
=========================
  When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API, we resignature and auto-mount on the other hosts which share the same underlying storage luns. As part of the operation, we rescan host. This data object describes the outcome of rescan operation on a host
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       Host name on which rescan was performed
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       'fault' would be set if the operation was not successful
