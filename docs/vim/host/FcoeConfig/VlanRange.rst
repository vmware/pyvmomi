
vim.host.FcoeConfig.VlanRange
=============================
  Used to represent inclusive intervals of VLAN IDs. Valid VLAN IDs fall within the range [0,4094], and the low value of a VlanRange must be less than or equal to the high value.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vlanLow (`int <https://docs.python.org/2/library/stdtypes.html>`_):

    vlanHigh (`int <https://docs.python.org/2/library/stdtypes.html>`_):

