.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.vApp.ProductInfo: ../../vim/vApp/ProductInfo.rst

.. _vim.ResourcePool.Summary: ../../vim/ResourcePool/Summary.rst

.. _vim.VirtualApp.VAppState: ../../vim/VirtualApp/VAppState.rst


vim.VirtualApp.Summary
======================
  This data object type encapsulates a typical set of resource pool information that is useful for list views and summary pages.
:extends: vim.ResourcePool.Summary_
:since: `vSphere API 4.0`_

Attributes:
    product (`vim.vApp.ProductInfo`_, optional):

       Product information. References to properties in the URLs are expanded.
    vAppState (`vim.VirtualApp.VAppState`_, optional):

       Whether the vApp is running
    suspended (`bool`_, optional):

       Whether a vApp is suspended, in the process of being suspended, or in the process of being resumed. A stopped vApp is marked as suspended under the following conditions:
        * All child virtual machines are either suspended or powered-off.
        * There is at least one suspended virtual machine for which the stop action is not "suspend".If the vAppState property is "stopped", the value is set to true if the vApp is suspended (according the the above definition).If the vAppState property is "stopping" or "starting" and the suspend flag is set to true, then the vApp is either in the process of being suspended or resumed from a suspended state, respectively.If the vAppState property is "started", then the suspend flag is set to false.
    installBootRequired (`bool`_, optional):

       Whether one or more VMs in this vApp require a reboot to finish installation.
    instanceUuid (`str`_, optional):

       vCenter-specific UUID of the vApp
