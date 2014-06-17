.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _DistributedVirtualSwitchManagerHostContainer: ../../../vim/dvs/DistributedVirtualSwitchManager/HostContainer.rst


vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec
=========================================================
  Base class for filters to check host compatibility.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    inclusive (`bool`_):

       If this flag is true, then the filter returns the hosts in the `DistributedVirtualSwitchManagerHostContainer`_ that satisfy the criteria specified by this filter, otherwise it returns hosts that don't meet the criteria.
