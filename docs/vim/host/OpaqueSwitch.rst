.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.PhysicalNic: ../../vim/host/PhysicalNic.rst


vim.host.OpaqueSwitch
=====================
  The OpaqueSwitch contains basic information about virtual switches that are managed by a management plane outside of vSphere.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_):

       The opaque switch key.
    name (`str`_, optional):

       The opaque switch name.
    pnic (`vim.host.PhysicalNic`_, optional):

       The set of physical network adapters associated with this switch.
