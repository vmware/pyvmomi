.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.SelectionSet: ../../vim/SelectionSet.rst


vim.dvs.DistributedVirtualPortgroupSelection
============================================
  Class to specify selection criteria of list of vNetwork Distributed Portgroups.
:extends: vim.SelectionSet_
:since: `vSphere API 5.0`_

Attributes:
    dvsUuid (`str`_):

       vSphere Distributed Switch uuid
    portgroupKey (`str`_):

       List of vNetwork Distributed Portgroup keys
