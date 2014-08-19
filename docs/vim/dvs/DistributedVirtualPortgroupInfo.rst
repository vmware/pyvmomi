
vim.dvs.DistributedVirtualPortgroupInfo
=======================================
  This class describes a DistributedVirtualPortgroup that a device backing can be attached to.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    switchName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the switch.
    switchUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The UUID of the switch.
    portgroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the portgroup.
    portgroupKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The key of the portgroup.
    portgroupType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of portgroup. See `DistributedVirtualPortgroupPortgroupType <vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst>`_ 
    uplinkPortgroup (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether this portgroup is an uplink portgroup.
    portgroup (`vim.dvs.DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_):

       The portgroup.
