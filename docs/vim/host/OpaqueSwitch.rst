
vim.host.OpaqueSwitch
=====================
  The OpaqueSwitch contains basic information about virtual switches that are managed by a management plane outside of vSphere.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The opaque switch key.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The opaque switch name.
    pnic ([`vim.host.PhysicalNic <vim/host/PhysicalNic.rst>`_], optional):

       The set of physical network adapters associated with this switch.
