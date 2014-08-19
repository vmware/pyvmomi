
vim.fault.DvsApplyOperationFault.FaultOnObject
==============================================
  The fault occured during an apply operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    objectId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The object identifier. It should be UUID for vSphere Distributed Switches, keys for vNetwork distributed portgroups and ports.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The Type of the objects.
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The fault that occured.
