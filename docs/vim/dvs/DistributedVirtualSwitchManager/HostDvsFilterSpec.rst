
vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec
=========================================================
  Base class for filters to check host compatibility.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    inclusive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       If this flag is true, then the filter returns the hosts in the `DistributedVirtualSwitchManagerHostContainer <vim/dvs/DistributedVirtualSwitchManager/HostContainer.rst>`_ that satisfy the criteria specified by this filter, otherwise it returns hosts that don't meet the criteria.
