
vim.LicenseManager.LicenseUsageInfo
===================================
  Contains source information, licensed features, and usage.
:extends: vmodl.DynamicData_

Attributes:
    source (`vim.LicenseManager.LicenseSource <vim/LicenseManager/LicenseSource.rst>`_):

       The source from which licensing data is acquired.See `LicenseSource <vim/LicenseManager/LicenseSource.rst>`_ 
    sourceAvailable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Returns whether or not the source is currently available.See `sourceAvailable <vim/LicenseManager.rst#sourceAvailable>`_ 
    reservationInfo ([`vim.LicenseManager.ReservationInfo <vim/LicenseManager/ReservationInfo.rst>`_], optional):

       A list of feature reservations.
    featureInfo ([`vim.LicenseManager.FeatureInfo <vim/LicenseManager/FeatureInfo.rst>`_], optional):

       Includes all the features that are referenced in the reservation array.
