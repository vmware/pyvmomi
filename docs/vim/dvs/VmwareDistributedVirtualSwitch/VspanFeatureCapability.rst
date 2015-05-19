.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability
=============================================================
  Indicators of support for version-specific Distributed Port Mirroring sessions.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    mixedDestSupported (`bool`_):

       Flag to indicate whether mixed dest mirror session is supported on the vSphere Distributed Switch.
    dvportSupported (`bool`_):

       Flag to indicate whether dvport mirror session is supported on the vSphere Distributed Switch.
    remoteSourceSupported (`bool`_):

       Flag to indicate whether remote mirror source session is supported on the vSphere Distributed Switch.
    remoteDestSupported (`bool`_):

       Flag to indicate whether remote mirror destination session is supported on the vSphere Distributed Switch.
    encapRemoteSourceSupported (`bool`_):

       Flag to indicate whether encapsulated remote mirror source session is supported on the vSphere Distributed Switch.
