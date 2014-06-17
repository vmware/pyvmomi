.. _str: https://docs.python.org/2/library/stdtypes.html

.. _float: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _LicenseManager: ../../vim/LicenseManager.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager.LicenseState: ../../vim/LicenseManager/LicenseState.rst


vim.LicenseManager.DiagnosticInfo
=================================
  This data object type provides summary status and diagnostic information for `LicenseManager`_ . Counters in this property can be reset to zero. The property specified as a discontinuity is used to determine when this last occurred.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    sourceLastChanged (`datetime`_):

       A timestamp of when sourceAvailable last changed state, expressed in UTC.
    sourceLost (`str`_):

       Counter to track number of times connection to source was lost. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    sourceLatency (`float`_):

       Exponentially decaying average of the transaction time for license acquisition and routine communications with LicenseSource. Units: milliseconds.
    licenseRequests (`str`_):

       Counter to track total number of licenses requested. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    licenseRequestFailures (`str`_):

       Counter to track Total number of licenses requests that were not fulfilled (denied, timeout, or other). This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    licenseFeatureUnknowns (`str`_):

       Counter to track Total number of license features parsed from License source that are not recognized. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    opState (`vim.LicenseManager.LicenseState`_):

       The general state of the license subsystem.
    lastStatusUpdate (`datetime`_):

       A timestamp of when opState was last updated.
    opFailureMessage (`str`_):

       A human readable reason when optState reports Fault condition.
