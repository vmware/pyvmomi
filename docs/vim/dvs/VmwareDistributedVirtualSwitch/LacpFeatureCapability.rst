.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability
============================================================
  The feature capabilities of Link Aggregation Control Protocol supported by the vSphere Distributed Switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    lacpSupported (`bool`_, optional):

       Flag to indicate whether Link Aggregation Control Protocol is supported on the vSphere Distributed Switch.
    multiLacpGroupSupported (`bool`_, optional):

       Flag to indicate whether the vSphere Distributed Switch supports more than one Link Aggregation Control Protocol group to be configured. It is suppported in vSphere Distributed Switch Version 5.5 or later.
