.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _blocked: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#blocked

.. _filterPolicy: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#filterPolicy

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _inShapingPolicy: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#inShapingPolicy

.. _outShapingPolicy: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#outShapingPolicy

.. _defaultPortConfig: ../../../vim/dvs/DistributedVirtualPortgroup/ConfigInfo.rst#defaultPortConfig

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vendorSpecificConfig: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#vendorSpecificConfig

.. _networkResourcePoolKey: ../../../vim/dvs/DistributedVirtualPort/Setting.rst#networkResourcePoolKey


vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy
===================================================
  The DistributedVirtualPortgroup policies. This field is not applicable when queried directly against an ESX host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    blockOverrideAllowed (`bool`_):

       Allow the `blocked`_ setting of an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    shapingOverrideAllowed (`bool`_):

       Allow the `inShapingPolicy`_ or `outShapingPolicy`_ settings of an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    vendorConfigOverrideAllowed (`bool`_):

       Allow the `vendorSpecificConfig`_ setting of an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    livePortMovingAllowed (`bool`_):

       Allow a live port to be moved in and out of the portgroup.
    portConfigResetAtDisconnect (`bool`_):

       If true, reset the port network setting back to the portgroup setting (thus removing the per-port setting) when the port is disconnected from the connectee.
    networkResourcePoolOverrideAllowed (`bool`_, optional):

       Allow the setting of `networkResourcePoolKey`_ of an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
    trafficFilterOverrideAllowed (`bool`_, optional):

       Allow the setting of `filterPolicy`_ , for an individual port to override the setting in `defaultPortConfig`_ of a portgroup.
