.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _LicenseSource: ../../vim/LicenseManager/LicenseSource.rst

.. _sourceAvailable: ../../vim/LicenseManager.rst#sourceAvailable

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager.FeatureInfo: ../../vim/LicenseManager/FeatureInfo.rst

.. _vim.LicenseManager.LicenseSource: ../../vim/LicenseManager/LicenseSource.rst

.. _vim.LicenseManager.ReservationInfo: ../../vim/LicenseManager/ReservationInfo.rst


vim.LicenseManager.LicenseUsageInfo
===================================
  Contains source information, licensed features, and usage.
:extends: vmodl.DynamicData_

Attributes:
    source (`vim.LicenseManager.LicenseSource`_):

       The source from which licensing data is acquired.See `LicenseSource`_ 
    sourceAvailable (`bool`_):

       Returns whether or not the source is currently available.See `sourceAvailable`_ 
    reservationInfo (`vim.LicenseManager.ReservationInfo`_, optional):

       A list of feature reservations.
    featureInfo (`vim.LicenseManager.FeatureInfo`_, optional):

       Includes all the features that are referenced in the reservation array.
