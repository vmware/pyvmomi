
vim.host.HostProxySwitch.Config
===============================
  This data object type describes the HostProxySwitch configuration containing both the configurable properties on a HostProxySwitch and identification information.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       This property indicates the change operation to apply on this configuration specification. Valid values are:
        * 
        * `edit <vim/host/ConfigChange/Operation.rst#edit>`_
        * 
        * 
        * `remove <vim/host/ConfigChange/Operation.rst#remove>`_
        * See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
    spec (`vim.host.HostProxySwitch.Specification <vim/host/HostProxySwitch/Specification.rst>`_, optional):

       The specification of the HostProxySwitch.
