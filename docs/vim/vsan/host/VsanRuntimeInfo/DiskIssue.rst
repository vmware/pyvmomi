.. _str: https://docs.python.org/2/library/stdtypes.html

.. _uuid: ../../../../vim/host/ScsiLun.rst#uuid

.. _vSphere API 5.5: ../../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.vsan.host.VsanRuntimeInfo.DiskIssue
=======================================
  Data structure of reporting a disk issue.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    diskId (`str`_):

       Disk uuid,See `uuid`_ 
    issue (`str`_):

       Type of issueSee DiskIssueType
