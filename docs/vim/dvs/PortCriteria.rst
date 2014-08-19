
vim.dvs.PortCriteria
====================
  The criteria specification for selecting ports.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    connected (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set, only the connected ports are qualified.
    active (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set, only the active ports are qualified.
    uplinkPort (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If set to true, only the uplink ports are qualified. If set to false, only non-uplink ports are qualified.
    scope (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       If set, only the ports of which the scope covers the entity are qualified.
    portgroupKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The keys of the portgroup that is used for the scope of `inside <vim/dvs/PortCriteria.rst#inside>`_ . If this property is unset, it means any portgroup. If `inside <vim/dvs/PortCriteria.rst#inside>`_ is unset, this property is ignored.
    inside (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If unset, all ports in the switch are qualified. If set to true, only ports inside `portgroupKey <vim/dvs/PortCriteria.rst#portgroupKey>`_ or any portgroup, if not set, are qualified. If set to false, only ports outside `portgroupKey <vim/dvs/PortCriteria.rst#portgroupKey>`_ or any portgroup, if not set, are qualified.
    portKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       If set, only the ports of which the key is in the array are qualified.
