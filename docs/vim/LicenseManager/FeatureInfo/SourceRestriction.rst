.. _vim.LicenseManager.FeatureInfo: ../../../vim/LicenseManager/FeatureInfo.rst

.. _vim.LicenseManager.FeatureInfo.SourceRestriction: ../../../vim/LicenseManager/FeatureInfo/SourceRestriction.rst

vim.LicenseManager.FeatureInfo.SourceRestriction
================================================
  Some licenses may only be allowed to load from a specified source. This enum indicates what restrictions exist for this license if any.
  :contained by: `vim.LicenseManager.FeatureInfo`_

  :type: `vim.LicenseManager.FeatureInfo.SourceRestriction`_

  :name: file

values:
--------

served
   The feature's license can only be served.

unrestricted
   The feature does not have a source restriction.

file
   The feature's license can only come from a file.
