.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _AcquireGenericServiceTicket: ../../vim/SessionManager.rst#acquireGenericServiceTicket


vim.SessionManager.ServiceRequestSpec
=====================================
  This data object type describes a request to a service. It is used as argument to `AcquireGenericServiceTicket`_ . This is the base class for more specific service request specifications. E.g. for HTTP services the derived class will provide a URL property.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
