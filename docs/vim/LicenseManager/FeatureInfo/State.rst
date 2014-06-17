.. _EnableFeature: ../../../vim/LicenseManager/FeatureInfo.rst#enable

.. _DisableFeature: ../../../vim/LicenseManager/FeatureInfo.rst#disable

.. _vim.LicenseManager.FeatureInfo: ../../../vim/LicenseManager/FeatureInfo.rst

.. _vim.LicenseManager.FeatureInfo.State: ../../../vim/LicenseManager/FeatureInfo/State.rst

vim.LicenseManager.FeatureInfo.State
====================================
  Describes the state of the feature.
  :contained by: `vim.LicenseManager.FeatureInfo`_

  :type: `vim.LicenseManager.FeatureInfo.State`_

  :name: optional

values:
--------

disabled
   The current edition license does not allow this additional feature.

optional
   The current edition license allows this additional feature. The `EnableFeature`_ and `DisableFeature`_ methods can be used to enable or disable this feature.

enabled
   The current edition license has implicitly enabled this additional feature.
