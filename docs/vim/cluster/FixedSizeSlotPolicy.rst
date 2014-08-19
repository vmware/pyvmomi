
vim.cluster.FixedSizeSlotPolicy
===============================
  This policy allows setting a fixed slot size
:extends: vim.cluster.SlotPolicy_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    cpu (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The cpu component of the slot size (in MHz)
    memory (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The memory component of the slot size (in megabytes)
