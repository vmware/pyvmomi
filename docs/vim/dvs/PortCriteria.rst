.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _inside: ../../vim/dvs/PortCriteria.rst#inside

.. _portgroupKey: ../../vim/dvs/PortCriteria.rst#portgroupKey

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.dvs.PortCriteria
====================
  The criteria specification for selecting ports.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    connected (`bool`_, optional):

       If set, only the connected ports are qualified.
    active (`bool`_, optional):

       If set, only the active ports are qualified.
    uplinkPort (`bool`_, optional):

       If set to true, only the uplink ports are qualified. If set to false, only non-uplink ports are qualified.
    scope (`vim.ManagedEntity`_, optional):

       If set, only the ports of which the scope covers the entity are qualified.
    portgroupKey (`str`_, optional):

       The keys of the portgroup that is used for the scope of `inside`_ . If this property is unset, it means any portgroup. If `inside`_ is unset, this property is ignored.
    inside (`bool`_, optional):

       If unset, all ports in the switch are qualified. If set to true, only ports inside `portgroupKey`_ or any portgroup, if not set, are qualified. If set to false, only ports outside `portgroupKey`_ or any portgroup, if not set, are qualified.
    portKey (`str`_, optional):

       If set, only the ports of which the key is in the array are qualified.
