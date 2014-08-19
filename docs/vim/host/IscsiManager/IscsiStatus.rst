
vim.host.IscsiManager.IscsiStatus
=================================
  The IscsiStatus data object describes the status of an operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    reason ([`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_], optional):

       List of failure reason and associated remedy. An array of fault codes associated with the failure. The fault itself will provide an indication of the actual failure code and `faultMessage <vmodl/MethodFault.rst#faultMessage>`_ will indicate the remedy that needs to be taken to correct the failure.
