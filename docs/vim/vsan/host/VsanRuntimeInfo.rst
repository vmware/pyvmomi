
vim.vsan.host.VsanRuntimeInfo
=============================
  This data object contains VSAN cluster runtime information from the perspective of the host in question. This data object is used to represent read-only state whose values may change during operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    membershipList ([`vim.vsan.host.MembershipInfo <vim/vsan/host/MembershipInfo.rst>`_], optional):

       This property reports host membership information.
    diskIssues ([`vim.vsan.host.VsanRuntimeInfo.DiskIssue <vim/vsan/host/VsanRuntimeInfo/DiskIssue.rst>`_], optional):

       List of disk issues detected on this host.To retrieve more information on the issues, use `QueryDisksForVsan <vim/host/VsanSystem.rst#queryDisksForVsan>`_ .
    accessGenNo (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Generation number tracking object accessibility.
