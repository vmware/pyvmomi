.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst


vim.fault.HostAccessRestrictedToManagementServer
================================================
    :extends:

        `vmodl.fault.NotSupported`_

  Fault thrown when an attempt is made to adjust resource settings directly on a host that is being managed by VC. VC is currently the source of truth for all resource pools on the host. Examples of methods affected by this are:
   * create respool
   * update respool
   * change VM resource settings.

Attributes:

    managementServer (`str`_)




