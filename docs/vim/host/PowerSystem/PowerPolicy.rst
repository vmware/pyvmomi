.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.PowerSystem.PowerPolicy
================================
  Power Management Policy data object. Used to retrieve and specify current host power management policy.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    key (`int`_):

       Power Policy Key. Internally generated key which uniquely identifies power management policy on a host.
    name (`str`_):

       Power Policy Name.
    shortName (`str`_):

       Power Policy Short Name. This is not localizable property which can be used to identify specific power managing policies like "custom" power policy. Custom power policy has short name set to "custom".
    description (`str`_):

       Power Policy Description.
