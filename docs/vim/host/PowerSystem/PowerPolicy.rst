
vim.host.PowerSystem.PowerPolicy
================================
  Power Management Policy data object. Used to retrieve and specify current host power management policy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Power Policy Key. Internally generated key which uniquely identifies power management policy on a host.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Power Policy Name.
    shortName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Power Policy Short Name. This is not localizable property which can be used to identify specific power managing policies like "custom" power policy. Custom power policy has short name set to "custom".
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Power Policy Description.
