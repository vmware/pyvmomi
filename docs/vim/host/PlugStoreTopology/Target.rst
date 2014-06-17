.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.TargetTransport: ../../../vim/host/TargetTransport.rst


vim.host.PlugStoreTopology.Target
=================================
  This data object represents target information.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       The identifier of the target. This will be a string representing the transport information of the target.
    transport (`vim.host.TargetTransport`_, optional):

       Detailed, transport-specific information about the target of a path.
