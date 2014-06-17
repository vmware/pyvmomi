.. _vim.LicenseManager.ReservationInfo: ../../../vim/LicenseManager/ReservationInfo.rst

.. _vim.LicenseManager.ReservationInfo.State: ../../../vim/LicenseManager/ReservationInfo/State.rst

vim.LicenseManager.ReservationInfo.State
========================================
  Describes the reservation state of a license.
  :contained by: `vim.LicenseManager.ReservationInfo`_

  :type: `vim.LicenseManager.ReservationInfo.State`_

  :name: licensed

values:
--------

unlicensedUse
   The LicenseManager failed to acquire a license but the implementation policy allows us to use the licensed feature anyway. This is possible, for example, when a license server becomes unavailable after a license had been successfully reserved from it.

notUsed
   This license is currently unused by the system, or the feature does not apply. For example, a DRS license appears as NotUsed if the host is not part of a DRS-enabled cluster.

noLicense
   This indicates that the license has expired or the system attempted to acquire the license but was not successful in reserving it.

licensed
   The required number of licenses have been acquired from the license source.
