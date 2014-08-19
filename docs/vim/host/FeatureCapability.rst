
vim.host.FeatureCapability
==========================
  A feature that the host is able to provide at a particular value.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Accessor name to the feature capability.
    featureName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the feature. Identical to the key.
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Opaque value that the feature is capable at.
