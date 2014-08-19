
vim.LicenseManager.FeatureInfo
==============================
  A single feature that can be licensed. This information is immutable.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique identifier for license as defined in License source data. Max length of this string is 64 characters of ASCII/ISO Latin-1 character set.
    featureName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The display string for the feature name.
    featureDescription (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A human readable description of what function this feature enables.
    state (`vim.LicenseManager.FeatureInfo.State <vim/LicenseManager/FeatureInfo/State.rst>`_, optional):

       Describes the state of the feature based on the current edition license. This property is unset for an edition license.
    costUnit (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Each license has a cost associated with it and the value of costUnit specifies the applicable unit.See `LicenseFeatureInfoUnit <vim/LicenseManager/FeatureInfo/CostUnit.rst>`_ 
    sourceRestriction (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Describe any restriction on the source of a license for this feature.See `LicenseFeatureInfoSourceRestriction <vim/LicenseManager/FeatureInfo/SourceRestriction.rst>`_ 
    dependentKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Report List of feature keys used by this edition.
    edition (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether the feature is an edition.
    expiresOn (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Date representing the expiration date
