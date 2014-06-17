.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.DistributedVirtualPortgroup: ../../vim/dvs/DistributedVirtualPortgroup.rst

.. _DistributedVirtualPortgroupPortgroupType: ../../vim/dvs/DistributedVirtualPortgroup/PortgroupType.rst


vim.dvs.DistributedVirtualPortgroupInfo
=======================================
  This class describes a DistributedVirtualPortgroup that a device backing can be attached to.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    switchName (`str`_):

       The name of the switch.
    switchUuid (`str`_):

       The UUID of the switch.
    portgroupName (`str`_):

       The name of the portgroup.
    portgroupKey (`str`_):

       The key of the portgroup.
    portgroupType (`str`_):

       The type of portgroup. See `DistributedVirtualPortgroupPortgroupType`_ 
    uplinkPortgroup (`bool`_):

       Whether this portgroup is an uplink portgroup.
    portgroup (`vim.dvs.DistributedVirtualPortgroup`_):

       The portgroup.
