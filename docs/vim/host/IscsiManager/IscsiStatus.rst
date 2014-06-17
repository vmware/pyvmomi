.. _faultMessage: ../../../vmodl/MethodFault.rst#faultMessage

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.host.IscsiManager.IscsiStatus
=================================
  The IscsiStatus data object describes the status of an operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_, optional):

       List of failure reason and associated remedy. An array of fault codes associated with the failure. The fault itself will provide an indication of the actual failure code and `faultMessage`_ will indicate the remedy that needs to be taken to correct the failure.
