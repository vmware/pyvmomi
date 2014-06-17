.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.cluster.SlotPolicy: ../../vim/cluster/SlotPolicy.rst


vim.cluster.FixedSizeSlotPolicy
===============================
  This policy allows setting a fixed slot size
:extends: vim.cluster.SlotPolicy_
:since: `vSphere API 5.1`_

Attributes:
    cpu (`int`_):

       The cpu component of the slot size (in MHz)
    memory (`int`_):

       The memory component of the slot size (in megabytes)
