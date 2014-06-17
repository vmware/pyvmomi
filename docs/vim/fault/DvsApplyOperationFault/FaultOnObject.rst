.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizedMethodFault: ../../../vmodl/LocalizedMethodFault.rst


vim.fault.DvsApplyOperationFault.FaultOnObject
==============================================
  The fault occured during an apply operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    objectId (`str`_):

       The object identifier. It should be UUID for vSphere Distributed Switches, keys for vNetwork distributed portgroups and ports.
    type (`str`_):

       The Type of the objects.
    fault (`vmodl.LocalizedMethodFault`_):

       The fault that occured.
