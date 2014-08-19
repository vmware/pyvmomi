
vim.vm.FeatureRequirement
=========================
  Feature requirement contains a key, featureName and an opaque value
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Accessor name to the feature requirement test
    featureName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the feature. Identical to the key.
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Opaque value for the feature operation. Operation is contained in the value.
