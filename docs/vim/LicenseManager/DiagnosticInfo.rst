
vim.LicenseManager.DiagnosticInfo
=================================
  This data object type provides summary status and diagnostic information for `LicenseManager <vim/LicenseManager.rst>`_ . Counters in this property can be reset to zero. The property specified as a discontinuity is used to determine when this last occurred.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    sourceLastChanged (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       A timestamp of when sourceAvailable last changed state, expressed in UTC.
    sourceLost (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Counter to track number of times connection to source was lost. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    sourceLatency (`float <https://docs.python.org/2/library/stdtypes.html>`_):

       Exponentially decaying average of the transaction time for license acquisition and routine communications with LicenseSource. Units: milliseconds.
    licenseRequests (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Counter to track total number of licenses requested. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    licenseRequestFailures (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Counter to track Total number of licenses requests that were not fulfilled (denied, timeout, or other). This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    licenseFeatureUnknowns (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Counter to track Total number of license features parsed from License source that are not recognized. This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
    opState (`vim.LicenseManager.LicenseState <vim/LicenseManager/LicenseState.rst>`_):

       The general state of the license subsystem.
    lastStatusUpdate (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       A timestamp of when opState was last updated.
    opFailureMessage (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A human readable reason when optState reports Fault condition.
