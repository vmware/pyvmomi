
vim.host.ServiceConfig
======================
  DataObject representing configuration for a particular service.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    serviceId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the service to configure.
    startupPolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Startup policy which defines how the service be configured. See
