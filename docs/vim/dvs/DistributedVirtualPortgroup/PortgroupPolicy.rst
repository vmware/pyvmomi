
vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy
===================================================
  The DistributedVirtualPortgroup policies. This field is not applicable when queried directly against an ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    blockOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the `blocked <vim/dvs/DistributedVirtualPort/Setting.rst#blocked>`_ setting of an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    shapingOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the `inShapingPolicy <vim/dvs/DistributedVirtualPort/Setting.rst#inShapingPolicy>`_ or `outShapingPolicy <vim/dvs/DistributedVirtualPort/Setting.rst#outShapingPolicy>`_ settings of an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    vendorConfigOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow the `vendorSpecificConfig <vim/dvs/DistributedVirtualPort/Setting.rst#vendorSpecificConfig>`_ setting of an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    livePortMovingAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Allow a live port to be moved in and out of the portgroup.
    portConfigResetAtDisconnect (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       If true, reset the port network setting back to the portgroup setting (thus removing the per-port setting) when the port is disconnected from the connectee.
    networkResourcePoolOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Allow the setting of `networkResourcePoolKey <vim/dvs/DistributedVirtualPort/Setting.rst#networkResourcePoolKey>`_ of an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
    trafficFilterOverrideAllowed (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Allow the setting of `filterPolicy <vim/dvs/DistributedVirtualPort/Setting.rst#filterPolicy>`_ , for an individual port to override the setting in `defaultPortConfig <vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig>`_ of a portgroup.
