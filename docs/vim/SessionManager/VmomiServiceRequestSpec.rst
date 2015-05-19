.. _str: https://docs.python.org/2/library/stdtypes.html

.. _CloneSession: ../../vim/SessionManager.rst#cloneSession

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _AcquireGenericServiceTicket: ../../vim/SessionManager.rst#acquireGenericServiceTicket

.. _vim.SessionManager.ServiceRequestSpec: ../../vim/SessionManager/ServiceRequestSpec.rst


vim.SessionManager.VmomiServiceRequestSpec
==========================================
  This data object type describes a request to invoke a specific method in a VMOMI service. It currenly only supports {link vim.SessionManager#cloneSession} method. The GenericServiceTicket.id returned from `AcquireGenericServiceTicket`_ for this request can be use for `CloneSession`_ to clone a session
:extends: vim.SessionManager.ServiceRequestSpec_
:since: `vSphere API 5.1`_

Attributes:
    method (`str`_):

       Name of the method identified by this request spec
