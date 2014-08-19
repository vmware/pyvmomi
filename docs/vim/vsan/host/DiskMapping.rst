
vim.vsan.host.DiskMapping
=========================
  A `VsanHostDiskMapping <vim/vsan/host/DiskMapping.rst>`_ is a set of one SSD `HostScsiDisk <vim/host/ScsiDisk.rst>`_ backed by a set of one or more non-SSD `HostScsiDisk <vim/host/ScsiDisk.rst>`_ . The maximum allowed `VsanHostDiskMapping <vim/vsan/host/DiskMapping.rst>`_ for a host is 5. A maximum set of 6 non-SSDs `HostScsiDisk <vim/host/ScsiDisk.rst>`_ can be added to the one SSD `HostScsiDisk <vim/host/ScsiDisk.rst>`_ .See `VsanHostConfigInfoStorageInfo <vim/vsan/host/ConfigInfo/StorageInfo.rst>`_ See vim.host.VsanSystem#initializeDisks(DiskMapping[])
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    ssd (`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_):

       SSD ScsiDisk.
    nonSsd ([`vim.host.ScsiDisk <vim/host/ScsiDisk.rst>`_]):

       Set of non-SSD backing ScsiDisk.
