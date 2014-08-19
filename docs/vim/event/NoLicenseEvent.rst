
vim.event.NoLicenseEvent
========================
  These are events reported by License Manager.A NoLicenseEvent is reported if the required licenses could not be reserved. Each feature that is not fully licensed is reported.
:extends: vim.event.LicenseEvent_

Attributes:
    feature (`vim.LicenseManager.FeatureInfo <vim/LicenseManager/FeatureInfo.rst>`_):

