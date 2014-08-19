
vim.vsan.host.VsanRuntimeInfo.DiskIssue
=======================================
  Data structure of reporting a disk issue.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    diskId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Disk uuid,See `uuid <vim/host/ScsiLun.rst#uuid>`_ 
    issue (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of issueSee DiskIssueType
