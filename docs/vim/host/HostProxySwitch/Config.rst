.. _str: https://docs.python.org/2/library/stdtypes.html

.. _edit: ../../../vim/host/ConfigChange/Operation.rst#edit

.. _remove: ../../../vim/host/ConfigChange/Operation.rst#remove

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.host.HostProxySwitch.Specification: ../../../vim/host/HostProxySwitch/Specification.rst


vim.host.HostProxySwitch.Config
===============================
  This data object type describes the HostProxySwitch configuration containing both the configurable properties on a HostProxySwitch and identification information.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    changeOperation (`str`_, optional):

       This property indicates the change operation to apply on this configuration specification. Valid values are:
        * 
        * `edit`_
        * 
        * 
        * `remove`_
        * See `HostConfigChangeOperation`_ 
    uuid (`str`_):

       The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
    spec (`vim.host.HostProxySwitch.Specification`_, optional):

       The specification of the HostProxySwitch.
