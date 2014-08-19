
vim.vm.ReplicationConfigSpec.DiskSettings
=========================================
  The ReplicationConfigSpec.DiskSettings object type encapsulates the replication properties of a replicated disk of a replicated virtual machine.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The disk's device key in the VM's configuration. Used to uniquely identify the disk to be configured for replication in the primary VM.
    diskReplicationId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       An opaque identifier that uniquely identifies a replicated disk between primary and secondary sites.
