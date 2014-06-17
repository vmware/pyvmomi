.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager.FeatureInfo: ../../vim/LicenseManager/FeatureInfo.rst


vim.LicenseManager.AvailabilityInfo
===================================
  Describes how many licenses of a particular feature is provided by the licensing source.
:extends: vmodl.DynamicData_

Attributes:
    feature (`vim.LicenseManager.FeatureInfo`_):

       Describes the feature.
    total (`int`_):

       Total number of licenses for this given type that are installed on the source.
    available (`int`_):

       The number of licenses that have not yet been reserved on the source.
