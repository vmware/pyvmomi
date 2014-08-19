
vim.LicenseManager.AvailabilityInfo
===================================
  Describes how many licenses of a particular feature is provided by the licensing source.
:extends: vmodl.DynamicData_

Attributes:
    feature (`vim.LicenseManager.FeatureInfo <vim/LicenseManager/FeatureInfo.rst>`_):

       Describes the feature.
    total (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Total number of licenses for this given type that are installed on the source.
    available (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The number of licenses that have not yet been reserved on the source.
