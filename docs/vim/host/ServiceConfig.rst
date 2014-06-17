.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.ServiceConfig
======================
  DataObject representing configuration for a particular service.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    serviceId (`str`_):

       Key of the service to configure.
    startupPolicy (`str`_):

       Startup policy which defines how the service be configured. See
