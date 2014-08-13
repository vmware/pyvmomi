.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.MultipathStateInfo.Path: ../../vim/host/MultipathStateInfo/Path.rst


vim.host.MultipathStateInfo
===========================
  This data object type describes the state of storage paths on the host. All storage paths on the host are enumerated in this data object.The reason all path state information is encapsulated in this data object is because the path may actively change. This data object ensures that a request to gather path state changes only needs to fetch this data object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    path ([`vim.host.MultipathStateInfo.Path`_], optional):

       List of paths on the system and their path states.
