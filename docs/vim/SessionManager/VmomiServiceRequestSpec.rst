
vim.SessionManager.VmomiServiceRequestSpec
==========================================
  This data object type describes a request to invoke a specific method in a VMOMI service. It currenly only supports {link vim.SessionManager#cloneSession} method. The GenericServiceTicket.id returned from `AcquireGenericServiceTicket <vim/SessionManager.rst#acquireGenericServiceTicket>`_ for this request can be use for `CloneSession <vim/SessionManager.rst#cloneSession>`_ to clone a session
:extends: vim.SessionManager.ServiceRequestSpec_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    method (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the method identified by this request spec
