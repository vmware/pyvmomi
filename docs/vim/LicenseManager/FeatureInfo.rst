.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _LicenseFeatureInfoUnit: ../../vim/LicenseManager/FeatureInfo/CostUnit.rst

.. _LicenseFeatureInfoSourceRestriction: ../../vim/LicenseManager/FeatureInfo/SourceRestriction.rst

.. _vim.LicenseManager.FeatureInfo.State: ../../vim/LicenseManager/FeatureInfo/State.rst


vim.LicenseManager.FeatureInfo
==============================
  A single feature that can be licensed. This information is immutable.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       Unique identifier for license as defined in License source data. Max length of this string is 64 characters of ASCII/ISO Latin-1 character set.
    featureName (`str`_):

       The display string for the feature name.
    featureDescription (`str`_, optional):

       A human readable description of what function this feature enables.
    state (`vim.LicenseManager.FeatureInfo.State`_, optional):

       Describes the state of the feature based on the current edition license. This property is unset for an edition license.
    costUnit (`str`_):

       Each license has a cost associated with it and the value of costUnit specifies the applicable unit.See `LicenseFeatureInfoUnit`_ 
    sourceRestriction (`str`_, optional):

       Describe any restriction on the source of a license for this feature.See `LicenseFeatureInfoSourceRestriction`_ 
    dependentKey ([`str`_], optional):

       Report List of feature keys used by this edition.
    edition (`bool`_, optional):

       Flag to indicate whether the feature is an edition.
    expiresOn (`datetime`_, optional):

       Date representing the expiration date
