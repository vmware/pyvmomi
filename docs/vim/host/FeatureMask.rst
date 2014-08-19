
vim.host.FeatureMask
====================
  A mask that is applied to a host feature capability.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Accessor name to the feature mask.
    featureName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the feature Identical to the key.
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Opaque value to change the host feature capability to. Masking operation is contained in the value.
