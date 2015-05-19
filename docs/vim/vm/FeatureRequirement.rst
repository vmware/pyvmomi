.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.FeatureRequirement
=========================
  Feature requirement contains a key, featureName and an opaque value
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    key (`str`_):

       Accessor name to the feature requirement test
    featureName (`str`_):

       Name of the feature. Identical to the key.
    value (`str`_):

       Opaque value for the feature operation. Operation is contained in the value.
